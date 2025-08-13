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
    """
    Query Hugging Face Inference API with retry logic
    """
    try:
        response = requests.post(HF_API_URL, headers=HF_HEADERS, json=payload, timeout=60)
        print(f"HF API Status: {response.status_code}")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"HF API Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"HF API Request Error: {str(e)}")
        return None

def generate_structured_reading(question, selected_cards, reading_type):
    """
    Generate a structured tarot reading based on card meanings when AI APIs are unavailable
    """
    try:
        reading_parts = []
        
        # Reading introduction based on type
        intro_messages = {
            "1-card": f"For your question '{question}', the cards reveal:",
            "3-card": f"Your three-card reading for '{question}' shows the past, present, and future influences:",
            "celtic-cross": f"The Celtic Cross spread for your question '{question}' provides deep insights:"
        }
        
        reading_parts.append(intro_messages.get(reading_type, intro_messages["1-card"]))
        reading_parts.append("")
        
        # Process each card
        for i, card in enumerate(selected_cards):
            card_name = card.get("name", "Unknown Card")
            keywords = card.get("keywords", [])
            meanings = card.get("meanings", {})
            description = card.get("description", "")
            
            # Position context for different reading types
            if reading_type == "3-card":
                positions = ["Past", "Present", "Future"]
                position = positions[i] if i < len(positions) else f"Card {i+1}"
            elif reading_type == "celtic-cross":
                positions = ["Present", "Challenge", "Past", "Future", "Crown", "Foundation", 
                           "Your Approach", "External Influences", "Hopes/Fears", "Outcome"]
                position = positions[i] if i < len(positions) else f"Position {i+1}"
            else:
                position = "Your Card"
            
            # Build card interpretation
            card_text = f"**{position}: {card_name}**"
            reading_parts.append(card_text)
            
            if description:
                reading_parts.append(description)
            
            if keywords:
                reading_parts.append(f"Key themes: {', '.join(keywords[:4])}")
            
            # Add upright meanings if available
            upright = meanings.get("upright", [])
            if upright:
                reading_parts.append(f"This card suggests: {', '.join(upright[:3])}")
            
            reading_parts.append("")
        
        # Closing message
        reading_parts.append("✨ The cards have spoken. Trust your intuition as you move forward on your path.")
        
        return "\n".join(reading_parts)
        
    except Exception as e:
        print(f"Error in generate_structured_reading: {str(e)}")
        return "The cosmic energies are shifting... Please try your reading again. The cards are eager to share their wisdom with you."

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