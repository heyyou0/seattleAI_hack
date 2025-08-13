import os
import logging
from flask import Flask, render_template, request, jsonify
from tarot_data import TAROT_DECK
from openai_service import generate_tarot_reading

# Set up logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "mystic_tarot_secret_key")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_reading', methods=['POST'])
def get_reading():
    try:
        data = request.get_json()
        question = data.get('question', '')
        selected_cards = data.get('selected_cards', [])
        reading_type = data.get('reading_type', '1-card')
        
        if not selected_cards:
            return jsonify({'error': 'No cards selected'}), 400
        
        # Get card details
        cards_details = []
        for card_id in selected_cards:
            if 0 <= card_id < len(TAROT_DECK):
                cards_details.append(TAROT_DECK[card_id])
        
        if not cards_details:
            return jsonify({'error': 'Invalid card selection'}), 400
        
        # Generate AI reading
        reading = generate_tarot_reading(question, cards_details, reading_type)
        
        return jsonify({
            'success': True,
            'reading': reading,
            'cards': cards_details
        })
        
    except Exception as e:
        logging.error(f"Error generating reading: {str(e)}")
        return jsonify({'error': 'Failed to generate reading. Please try again.'}), 500

@app.route('/get_card/<int:card_id>')
def get_card(card_id):
    if 0 <= card_id < len(TAROT_DECK):
        return jsonify(TAROT_DECK[card_id])
    return jsonify({'error': 'Card not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
