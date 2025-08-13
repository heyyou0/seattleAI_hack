import os
import json
import requests
import time
from openai import OpenAI

# Try OpenAI first, then fallback to Hugging Face
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
HF_API_KEY = os.environ.get("HF_API_KEY")

if OPENAI_API_KEY:
    openai_client = OpenAI(api_key=OPENAI_API_KEY)
else:
    openai_client = None

# Using Hugging Face Inference API as backup
HF_API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
HF_HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

def query_huggingface(payload):
    """Query Hugging Face Inference API"""
    try:
        response = requests.post(HF_API_URL, headers=HF_HEADERS, json=payload, timeout=30)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"HF API Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"HF API Request Error: {str(e)}")
        return None

def generate_tarot_reading(question, selected_cards, reading_type):
    """
    Generate a personalized tarot reading using OpenAI, Hugging Face, or fallback to a structured reading.
    """
    try:
        # Prepare card information for the reading
        cards_info = []
        for card in selected_cards:
            card_info = f"{card['name']}: {card['description']} Keywords: {', '.join(card['keywords'])}"
            cards_info.append(card_info)
        
        cards_text = "\n".join(cards_info)
        
        # Create the context based on reading type
        reading_context = {
            "1-card": "This is a single card reading focused on providing direct insight and guidance.",
            "3-card": "This is a three-card reading representing Past, Present, and Future influences.",
            "celtic-cross": "This is a Celtic Cross reading, a comprehensive 10-card spread that provides deep insight into the situation."
        }
        
        context = reading_context.get(reading_type, reading_context["1-card"])
        
        # Try OpenAI first if available
        if openai_client:
            try:
                response = openai_client.chat.completions.create(
                    model="gpt-4o",  # the newest OpenAI model is "gpt-4o" which was released May 13, 2024. do not change this unless explicitly requested by the user
                    messages=[
                        {"role": "system", "content": "You are a wise, mystical tarot reader with deep knowledge of card meanings and symbolism. Provide insightful, spiritual readings that connect the card meanings to the user's question."},
                        {"role": "user", "content": f"Question: '{question}'\n\nCards drawn:\n{cards_text}\n\n{context}\n\nProvide a mystical, insightful tarot reading that interprets these cards in relation to the question:"}
                    ],
                    max_tokens=400,
                    temperature=0.8
                )
                return response.choices[0].message.content.strip()
            except Exception as e:
                print(f"OpenAI API Error: {str(e)}")
        
        # Try Hugging Face as backup
        if HF_API_KEY:
            prompt = f"You are a wise tarot reader. For the question '{question}', interpret these cards:\n{cards_text}\n\n{context}\n\nProvide an insightful, mystical reading:"
            payload = {
                "inputs": prompt,
                "parameters": {
                    "max_new_tokens": 300,
                    "temperature": 0.8,
                    "do_sample": True,
                    "return_full_text": False
                }
            }
            hf_response = query_huggingface(payload)
            print(f"HF Response: {hf_response}")  # Debug output
            
            # If Hugging Face works, use its response
            if hf_response and isinstance(hf_response, list) and len(hf_response) > 0:
                generated_text = hf_response[0].get("generated_text", "").strip()
                if generated_text and len(generated_text) > 50:  # Only return if substantial content
                    return generated_text
        
        # Fallback: Generate a structured reading based on card meanings
        return generate_structured_reading(question, selected_cards, reading_type)
        
    except Exception as e:
        print(f"Error in generate_tarot_reading: {str(e)}")
        return generate_structured_reading(question, selected_cards, reading_type)

def generate_structured_reading(question, selected_cards, reading_type):
    """
    Generate a structured tarot reading based on card meanings when AI is unavailable
    """
    try:
        reading_parts = []
        
        # Add greeting
        reading_parts.append(f"🔮 **Your {reading_type.replace('-', ' ').title()} Reading**\n")
        reading_parts.append(f"**Your Question:** {question}\n")
        
        # Interpret each card
        for i, card in enumerate(selected_cards):
            if reading_type == "3-card":
                positions = ["Past", "Present", "Future"]
                position = positions[i] if i < len(positions) else f"Card {i+1}"
            elif reading_type == "celtic-cross":
                positions = ["Present Situation", "Challenge/Cross", "Distant Past", "Recent Past", 
                           "Possible Outcome", "Near Future", "Your Approach", "External Influences", 
                           "Hopes and Fears", "Final Outcome"]
                position = positions[i] if i < len(positions) else f"Card {i+1}"
            else:
                position = "Your Card"
            
            reading_parts.append(f"**{position}: {card['name']}**")
            reading_parts.append(f"{card['description']}")
            
            # Add relevant meaning based on context
            if card['meanings']['upright']:
                reading_parts.append(f"*Key meanings:* {', '.join(card['meanings']['upright'])}")
            
            reading_parts.append("")
        
        # Add guidance section
        reading_parts.append("**✨ Guidance and Reflection:**")
        
        # Generate contextual guidance based on the cards
        if len(selected_cards) == 1:
            card = selected_cards[0]
            guidance = f"The {card['name']} appears in response to your question about {question.lower()}. "
            guidance += f"This card suggests focusing on {', '.join(card['keywords'][:2])}. "
            guidance += "Consider how these themes relate to your current situation and what steps you might take to align with this energy."
        
        elif len(selected_cards) == 3:
            guidance = "Your three-card spread reveals a journey through time. "
            guidance += f"The past influence of {selected_cards[0]['name']} has shaped your current situation represented by {selected_cards[1]['name']}. "
            guidance += f"Moving forward, {selected_cards[2]['name']} suggests the energy and opportunities available to you. "
            guidance += "Reflect on how these connected themes can guide your decision-making."
        
        else:
            card_names = [card['name'] for card in selected_cards[:3]]
            guidance = f"The cards {', '.join(card_names)} and others in your spread create a rich tapestry of insight. "
            guidance += "Each card contributes to the overall message about your question. "
            guidance += "Look for patterns and connections between the card meanings to understand the deeper guidance being offered."
        
        reading_parts.append(guidance)
        reading_parts.append("\n*Trust in the wisdom of the cards and your own intuition.*")
        
        return "\n".join(reading_parts)
        
    except Exception as e:
        return f"The cosmic energies are shifting... Please try your reading again. The cards are eager to share their wisdom with you."
