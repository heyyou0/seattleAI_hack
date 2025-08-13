// Mystic Tarot Application JavaScript

class TarotApp {
    constructor() {
        this.selectedCards = [];
        this.readingType = '1-card';
        this.requiredCards = 1;
        this.isSelectionComplete = false;
        
        this.init();
    }
    
    init() {
        this.bindEvents();
        this.setupReadingTypeSelection();
        this.generateCardGrid();
    }
    
    bindEvents() {
        // Begin reading button
        document.getElementById('begin-reading-btn').addEventListener('click', () => {
            this.startCardSelection();
        });
        
        // Reveal reading button
        document.getElementById('reveal-reading-btn').addEventListener('click', () => {
            this.generateReading();
        });
        
        // New reading button
        document.getElementById('new-reading-btn').addEventListener('click', () => {
            this.resetApplication();
        });
        
        // Reading type selection
        document.querySelectorAll('input[name="reading-type"]').forEach(radio => {
            radio.addEventListener('change', (e) => {
                this.handleReadingTypeChange(e.target.value);
            });
        });
    }
    
    setupReadingTypeSelection() {
        document.querySelectorAll('.reading-type-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove active class from all buttons
                document.querySelectorAll('.reading-type-btn').forEach(b => 
                    b.classList.remove('active')
                );
                
                // Add active class to clicked button
                btn.classList.add('active');
                
                // Update the corresponding radio button
                const radioId = btn.getAttribute('for');
                document.getElementById(radioId).checked = true;
                
                // Update reading type
                const value = document.getElementById(radioId).value;
                this.handleReadingTypeChange(value);
            });
        });
    }
    
    handleReadingTypeChange(value) {
        this.readingType = value;
        
        // Update required cards count
        switch(value) {
            case '1-card':
                this.requiredCards = 1;
                break;
            case '3-card':
                this.requiredCards = 3;
                break;
            case 'celtic-cross':
                this.requiredCards = 10;
                break;
        }
        
        // Update UI
        this.updateSelectionInstruction();
        this.updateSelectionCounter();
    }
    
    updateSelectionInstruction() {
        const instruction = document.getElementById('selection-instruction');
        let text = '';
        
        switch(this.readingType) {
            case '1-card':
                text = 'Select 1 card from the deck below for quick insight';
                break;
            case '3-card':
                text = 'Select 3 cards from the deck below for Past, Present, and Future guidance';
                break;
            case 'celtic-cross':
                text = 'Select 10 cards from the deck below for a comprehensive Celtic Cross reading';
                break;
        }
        
        instruction.textContent = text;
    }
    
    updateSelectionCounter() {
        document.getElementById('selected-count').textContent = this.selectedCards.length;
        document.getElementById('required-count').textContent = this.requiredCards;
    }
    
    generateCardGrid() {
        const cardGrid = document.getElementById('card-grid');
        cardGrid.innerHTML = '';
        
        // Generate 78 cards (full tarot deck)
        for (let i = 0; i < 78; i++) {
            const cardElement = this.createCardElement(i);
            cardGrid.appendChild(cardElement);
        }
    }
    
    createCardElement(cardId) {
        const cardDiv = document.createElement('div');
        cardDiv.className = 'tarot-card';
        cardDiv.dataset.cardId = cardId;
        
        cardDiv.innerHTML = `
            <div class="card-face card-back">
                <svg width="60" height="80" viewBox="0 0 60 80" fill="none">
                    <rect width="60" height="80" rx="8" fill="#2D1B69" stroke="#8B5A2B" stroke-width="2"/>
                    <circle cx="30" cy="25" r="8" fill="#C9A96E"/>
                    <path d="M22 40 L38 40 M22 45 L38 45 M22 50 L38 50" stroke="#C9A96E" stroke-width="2"/>
                    <circle cx="30" cy="60" r="8" fill="#C9A96E"/>
                </svg>
            </div>
            <div class="card-face card-front">
                <h6 id="card-name-${cardId}">Loading...</h6>
            </div>
        `;
        
        cardDiv.addEventListener('click', () => {
            this.handleCardSelection(cardId, cardDiv);
        });
        
        return cardDiv;
    }
    
    handleCardSelection(cardId, cardElement) {
        if (this.isSelectionComplete) return;
        
        if (cardElement.classList.contains('selected')) {
            // Deselect card
            this.deselectCard(cardId, cardElement);
        } else {
            // Select card
            this.selectCard(cardId, cardElement);
        }
        
        this.updateSelectionCounter();
        this.checkSelectionComplete();
    }
    
    selectCard(cardId, cardElement) {
        if (this.selectedCards.length >= this.requiredCards) {
            return; // Can't select more cards
        }
        
        this.selectedCards.push(cardId);
        cardElement.classList.add('selected');
        
        // Load card data and update front face
        this.loadCardData(cardId);
    }
    
    deselectCard(cardId, cardElement) {
        const index = this.selectedCards.indexOf(cardId);
        if (index > -1) {
            this.selectedCards.splice(index, 1);
            cardElement.classList.remove('selected');
        }
    }
    
    async loadCardData(cardId) {
        try {
            const response = await fetch(`/get_card/${cardId}`);
            const cardData = await response.json();
            
            if (cardData && cardData.name) {
                document.getElementById(`card-name-${cardId}`).textContent = cardData.name;
            }
        } catch (error) {
            console.error('Error loading card data:', error);
            document.getElementById(`card-name-${cardId}`).textContent = 'Card ' + (cardId + 1);
        }
    }
    
    checkSelectionComplete() {
        const revealBtn = document.getElementById('reveal-reading-btn');
        
        if (this.selectedCards.length === this.requiredCards) {
            this.isSelectionComplete = true;
            revealBtn.classList.remove('d-none');
            revealBtn.classList.add('mystical-glow');
            
            // Disable further selection
            document.querySelectorAll('.tarot-card:not(.selected)').forEach(card => {
                card.style.opacity = '0.5';
                card.style.cursor = 'not-allowed';
            });
        } else {
            this.isSelectionComplete = false;
            revealBtn.classList.add('d-none');
            revealBtn.classList.remove('mystical-glow');
            
            // Re-enable selection
            document.querySelectorAll('.tarot-card').forEach(card => {
                card.style.opacity = '1';
                card.style.cursor = 'pointer';
            });
        }
    }
    
    startCardSelection() {
        const question = document.getElementById('user-question').value.trim();
        
        if (!question) {
            alert('Please enter your question before beginning the reading.');
            return;
        }
        
        // Hide question section and show card selection
        document.getElementById('question-section').classList.add('d-none');
        document.getElementById('card-selection-section').classList.remove('d-none');
        
        // Smooth scroll to card selection
        document.getElementById('card-selection-section').scrollIntoView({
            behavior: 'smooth'
        });
    }
    
    async generateReading() {
        const question = document.getElementById('user-question').value.trim();
        
        if (!question || this.selectedCards.length === 0) {
            alert('Please enter a question and select cards.');
            return;
        }
        
        // Show loading overlay
        document.getElementById('loading-overlay').classList.remove('d-none');
        
        try {
            const response = await fetch('/get_reading', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    question: question,
                    selected_cards: this.selectedCards,
                    reading_type: this.readingType
                })
            });
            
            const data = await response.json();
            
            if (data.success) {
                this.displayReading(data.reading, data.cards);
            } else {
                throw new Error(data.error || 'Failed to generate reading');
            }
        } catch (error) {
            console.error('Error generating reading:', error);
            alert('Error generating reading: ' + error.message);
        } finally {
            // Hide loading overlay
            document.getElementById('loading-overlay').classList.add('d-none');
        }
    }
    
    displayReading(reading, cards) {
        // Display selected cards
        const cardsDisplay = document.getElementById('selected-cards-display');
        cardsDisplay.innerHTML = '';
        
        cards.forEach((card, index) => {
            const cardDiv = document.createElement('div');
            cardDiv.className = 'selected-card card-reveal-animation';
            cardDiv.style.animationDelay = `${index * 0.2}s`;
            
            cardDiv.innerHTML = `
                <div class="card-image-placeholder" style="
                    width: 100%;
                    height: 150px;
                    background: linear-gradient(145deg, #2D1B69, #1a0d4a);
                    border: 2px solid #C9A96E;
                    border-radius: 8px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: #C9A96E;
                    font-family: 'Playfair Display', serif;
                    font-size: 0.9rem;
                    text-align: center;
                    padding: 10px;
                ">
                    ${card.name}
                </div>
                <h6>${card.name}</h6>
            `;
            
            cardsDisplay.appendChild(cardDiv);
        });
        
        // Display AI reading
        document.getElementById('ai-reading').innerHTML = `
            <div style="white-space: pre-line;">${reading}</div>
        `;
        
        // Hide card selection and show reading
        document.getElementById('card-selection-section').classList.add('d-none');
        document.getElementById('reading-section').classList.remove('d-none');
        
        // Smooth scroll to reading
        document.getElementById('reading-section').scrollIntoView({
            behavior: 'smooth'
        });
    }
    
    resetApplication() {
        // Reset all state
        this.selectedCards = [];
        this.readingType = '1-card';
        this.requiredCards = 1;
        this.isSelectionComplete = false;
        
        // Reset UI
        document.getElementById('user-question').value = '';
        document.getElementById('one-card').checked = true;
        document.querySelectorAll('.reading-type-btn').forEach(btn => 
            btn.classList.remove('active')
        );
        document.querySelector('label[for="one-card"]').classList.add('active');
        
        // Reset card grid
        document.querySelectorAll('.tarot-card').forEach(card => {
            card.classList.remove('selected');
            card.style.opacity = '1';
            card.style.cursor = 'pointer';
        });
        
        // Show question section, hide others
        document.getElementById('question-section').classList.remove('d-none');
        document.getElementById('card-selection-section').classList.add('d-none');
        document.getElementById('reading-section').classList.add('d-none');
        document.getElementById('reveal-reading-btn').classList.add('d-none');
        
        // Update counters
        this.updateSelectionInstruction();
        this.updateSelectionCounter();
        
        // Scroll to top
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new TarotApp();
});
