import os
import json
import time
import requests

# Initialize OpenAI client
try:
    from openai import OpenAI
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    openai_client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None
except ImportError:
    openai_client = None

# Hugging Face API setup
HF_API_KEY = os.environ.get("HF_API_KEY") or os.environ.get("HF_TOKEN")
HF_TOKEN = HF_API_KEY
HF_MODEL = "HuggingFaceH4/zephyr-7b-beta"
HF_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL}"
HF_HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}


def hf_generate(prompt, max_tries=6):
    """Hugging Face Inference API call with retry logic."""
    if not HF_TOKEN:
        print("HF_TOKEN is not set. API call will fail.")
        return None

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 300,
            "temperature": 0.8,
            "do_sample": True,
            "return_full_text": False
        }
    }
    backoff = 2
    for i in range(max_tries):
        try:
            print(f"Attempting to call HF API (try {i+1})...")
            r = requests.post(HF_URL, headers=HF_HEADERS, json=payload, timeout=60)
        except Exception as e:
            if i == max_tries - 1:
                print(f"Failed to connect to HF API after {max_tries} tries: {e}")
                raise
            print(f"Connection error: {e}. Retrying in {backoff} seconds.")
            time.sleep(backoff)
            backoff *= 1.5
            continue

        # Handle different status codes
        if r.status_code == 503:
            try:
                eta = r.json().get("estimated_time", 6)
            except Exception:
                eta = 6
            print(f"Model is loading (503). Retrying in {min(eta, 10)} seconds.")
            time.sleep(min(eta, 10))
            continue

        if r.status_code == 200:
            try:
                data = r.json()
                print("HF API call successful.")
            except Exception:
                print("HF API returned non-JSON response. Returning raw text.")
                return r.text.strip()

            if isinstance(data, list) and data:
                gt = data[0].get("generated_text") or data[0].get("summary_text")
                if gt:
                    return gt.strip()

            if isinstance(data, dict):
                gt = data.get("generated_text") or data.get("text")
                if gt:
                    return gt.strip()

            print(f"HF API returned valid JSON but no text content: {json.dumps(data)}")
            return None

        if r.status_code in (404, 429, 500):
            if i == max_tries - 1:
                print(f"HF error {r.status_code}: {r.text[:200]}")
                return None
            print(f"HF API returned {r.status_code}. Retrying in {backoff} seconds.")
            time.sleep(backoff)
            backoff *= 1.5
            continue

        print(f"HF API returned unexpected status code {r.status_code}: {r.text[:200]}")
        return None

    print("HF: Model not available, please try again later.")
    return None


def generate_structured_reading(question, selected_cards, reading_type):
    """Generate a structured reading based on card meanings when AI services are unavailable."""
    reading_parts = [
        f"🔮 **Mystical Tarot Reading**\n",
        f"**Your Question:** {question or 'General guidance'}\n",
        f"**Reading Type:** {reading_type.title()} Card Reading\n"
    ]
    
    if reading_type == "3-card":
        positions = ["Past", "Present", "Future"]
        for i, card in enumerate(selected_cards[:3]):
            card_name = card.get('name', 'Unknown')
            card_description = card.get('description', '')
            keywords = ', '.join(card.get('keywords', []))
            
            part = (
                f"\n**{positions[i]}: {card_name}**\n"
                f"The {card_name} represents {card_description}.\n"
                f"Key themes: {keywords}\n"
                f"This card suggests: {card_description.split(', ')[0] if card_description else 'No specific suggestions'}"
            )
            reading_parts.append(part)
    else:
        for card in selected_cards:
            card_name = card.get('name', 'Unknown')
            card_description = card.get('description', '')
            keywords = ', '.join(card.get('keywords', []))
            
            part = (
                f"\n**{card_name}**\n"
                f"The {card_name} represents {card_description}.\n"
                f"Key themes: {keywords}\n"
                f"This card suggests: {card_description.split(', ')[0] if card_description else 'No specific suggestions'}"
            )
            reading_parts.append(part)
    
    reading_parts.append(
        "\n✨ The cards have spoken. Trust your intuition as you move forward on your path."
    )
    
    return "\n".join(reading_parts)


def generate_tarot_reading(question, selected_cards, reading_type):
    """
    Generate a personalized tarot reading using OpenAI, Hugging Face, or fallback to structured reading.
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
                if response.choices[0].message.content:
                    return response.choices[0].message.content.strip()
            except Exception as e:
                print(f"OpenAI API Error: {str(e)}")
        
        # Try Hugging Face as backup
        if HF_API_KEY:
            prompt = f"You are a wise tarot reader. For the question '{question}', interpret these cards:\n{cards_text}\n\n{context}\n\nProvide an insightful, mystical reading:"
            hf_response = hf_generate(prompt)
            print(f"HF Response: {hf_response}")  # Debug output
            
            # If Hugging Face works, use its response
            if hf_response and len(hf_response) > 50:
                return hf_response
        
        # Fallback: Generate a structured reading based on card meanings
        return generate_structured_reading(question, selected_cards, reading_type)
        
    except Exception as e:
        print(f"Error in generate_tarot_reading: {str(e)}")
        return generate_structured_reading(question, selected_cards, reading_type)