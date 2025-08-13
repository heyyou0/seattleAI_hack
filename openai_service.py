import os
import json
import requests
import time

# Using Hugging Face Inference API for free AI-powered tarot readings
# Using a more suitable model for text generation
HF_API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
HF_HEADERS = {
    "Authorization": f"Bearer {os.environ.get('HF_API_KEY', '')}",
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
    Generate a personalized tarot reading using Hugging Face models or fallback to a structured reading.
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
        
        # Try Hugging Face first, but if it fails, provide a structured reading
        hf_response = None
        if HF_HEADERS["Authorization"] != "Bearer ":
            prompt = f"As a tarot reader, interpret these cards for the question '{question}': {cards_text}. {context}"
            payload = {
                "inputs": prompt,
                "parameters": {
                    "max_new_tokens": 400,
                    "temperature": 0.7,
                    "return_full_text": False
                }
            }
            hf_response = query_huggingface(payload)
        
        # If Hugging Face works, use its response
        if hf_response and isinstance(hf_response, list) and len(hf_response) > 0:
            return hf_response[0].get("generated_text", "").strip()
        
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
