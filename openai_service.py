import os
import json
from openai import OpenAI

# the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
# do not change this unless explicitly requested by the user
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "default_key")
openai = OpenAI(api_key=OPENAI_API_KEY)

def generate_tarot_reading(question, selected_cards, reading_type):
    """
    Generate a personalized tarot reading using OpenAI based on the user's question and selected cards.
    """
    try:
        # Prepare card information for the prompt
        cards_info = []
        for card in selected_cards:
            card_info = f"- {card['name']}: {card['description']} Keywords: {', '.join(card['keywords'])}"
            cards_info.append(card_info)
        
        cards_text = "\n".join(cards_info)
        
        # Create the prompt based on reading type
        reading_context = {
            "1-card": "This is a single card reading focused on providing direct insight and guidance.",
            "3-card": "This is a three-card reading representing Past, Present, and Future influences.",
            "celtic-cross": "This is a Celtic Cross reading, a comprehensive 10-card spread that provides deep insight into the situation."
        }
        
        context = reading_context.get(reading_type, reading_context["1-card"])
        
        prompt = f"""You are a wise and intuitive tarot reader with deep knowledge of tarot symbolism and meanings. 
        
User's Question: "{question}"

Reading Type: {reading_type.upper()}
{context}

Selected Cards:
{cards_text}

Please provide a personalized, insightful tarot reading that:
1. Addresses the user's specific question directly
2. Interprets each card in relation to their question and situation
3. Explains how the cards work together to tell a story
4. Offers practical guidance and actionable insights
5. Maintains a mystical yet supportive tone
6. Is approximately 300-500 words

Structure your response with clear sections and provide meaningful interpretations that connect the card meanings to the user's life situation."""

        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are an experienced tarot reader who provides insightful, personalized readings that combine traditional tarot meanings with intuitive guidance. Your readings are mystical yet grounded, offering both spiritual insight and practical wisdom."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=800,
            temperature=0.7
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        raise Exception(f"Failed to generate tarot reading: {str(e)}")
