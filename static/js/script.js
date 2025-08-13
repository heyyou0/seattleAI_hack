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
        
        // Create fan container
        const fanContainer = document.createElement('div');
        fanContainer.className = 'card-fan-container';
        
        // Generate 78 cards (full tarot deck) in fan layout
        for (let i = 0; i < 78; i++) {
            const cardElement = this.createCardElement(i);
            this.positionCardInFan(cardElement, i, 78);
            fanContainer.appendChild(cardElement);
        }
        
        cardGrid.appendChild(fanContainer);
    }
    
    positionCardInFan(cardElement, index, totalCards) {
        // Calculate fan spread angle (adjust for visual appeal)
        const maxAngle = 90; // Total spread angle in degrees
        const angleStep = maxAngle / (totalCards - 1);
        const angle = (index * angleStep) - (maxAngle / 2);
        
        // Calculate position in fan
        const radius = 250; // Distance from center
        const x = Math.sin(angle * Math.PI / 180) * radius;
        const y = Math.cos(angle * Math.PI / 180) * radius * 0.3; // Flatten the arc
        
        // Apply transform with rotation and position
        cardElement.style.transform = `
            translate(${x}px, ${y}px) 
            rotate(${angle}deg)
        `;
        cardElement.style.zIndex = totalCards - Math.abs(index - totalCards/2);
    }
    
    createCardElement(cardId) {
        const cardDiv = document.createElement('div');
        cardDiv.className = 'tarot-card';
        cardDiv.dataset.cardId = cardId;
        
        cardDiv.innerHTML = `
            <div class="card-face card-back">
                <svg width="100%" height="100%" viewBox="0 0 80 120" fill="none">
                    <rect width="80" height="120" rx="12" fill="#2D1B69" stroke="#8B5A2B" stroke-width="2"/>
                    <circle cx="40" cy="30" r="10" fill="#C9A96E"/>
                    <path d="M30 60 L50 60 M30 70 L50 70 M30 80 L50 80" stroke="#C9A96E" stroke-width="2"/>
                    <circle cx="40" cy="100" r="10" fill="#C9A96E"/>
                </svg>
            </div>
            <div class="card-face card-front">
                <div class="card-image-placeholder" id="card-image-${cardId}">
                    ✦
                </div>
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
        
        // Animate card coming down from fan
        setTimeout(() => {
            this.animateCardSelection(cardElement, this.selectedCards.length - 1);
        }, 100);
        
        // Load card data and update front face
        this.loadCardData(cardId);
    }
    
    animateCardSelection(cardElement, selectionIndex) {
        // Calculate position for selected cards at bottom of screen
        const screenWidth = window.innerWidth;
        const cardWidth = 120;
        const spacing = 140;
        const startX = (screenWidth / 2) - ((this.requiredCards - 1) * spacing / 2);
        const targetX = startX + (selectionIndex * spacing) - (screenWidth / 2);
        const targetY = 200; // Distance from original position
        
        cardElement.style.transform = `
            translate(${targetX}px, ${targetY}px) 
            rotate(0deg) 
            scale(1.2)
        `;
        cardElement.style.zIndex = 1000 + selectionIndex;
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
                
                // Try to load actual card image
                const imageElement = document.getElementById(`card-image-${cardId}`);
                const imagePath = `/static/images/${cardData.image}`;
                
                // Create img element to test if image exists
                const img = new Image();
                img.onload = () => {
                    imageElement.innerHTML = `<img src="${imagePath}" alt="${cardData.name}">`;
                };
                img.onerror = () => {
                    // Keep placeholder if image doesn't exist
                    imageElement.innerHTML = `<div style="font-size: 1.5rem;">✦</div><div style="font-size: 0.6rem;">${cardData.name}</div>`;
                };
                img.src = imagePath;
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
        // Hide card selection and show reading
        document.getElementById('card-selection-section').classList.add('d-none');
        document.getElementById('reading-section').classList.remove('d-none');
        
        // Display selected cards with flipping animation
        const cardsDisplay = document.getElementById('selected-cards-display');
        cardsDisplay.innerHTML = '';
        
        // Create cards first (face down)
        const cardElements = [];
        cards.forEach((card, index) => {
            const cardDiv = document.createElement('div');
            cardDiv.className = 'selected-card';
            cardDiv.style.opacity = '0';
            cardDiv.style.transform = 'translateY(20px)';
            
            cardDiv.innerHTML = `
                <div class="tarot-card" style="width: 120px; height: 180px; position: relative;">
                    <div class="card-face card-back" style="transform: rotateY(0deg);">
                        <svg width="100%" height="100%" viewBox="0 0 80 120" fill="none">
                            <rect width="80" height="120" rx="12" fill="#2D1B69" stroke="#8B5A2B" stroke-width="2"/>
                            <circle cx="40" cy="30" r="10" fill="#C9A96E"/>
                            <path d="M30 60 L50 60 M30 70 L50 70 M30 80 L50 80" stroke="#C9A96E" stroke-width="2"/>
                            <circle cx="40" cy="100" r="10" fill="#C9A96E"/>
                        </svg>
                    </div>
                    <div class="card-face card-front" style="transform: rotateY(180deg);">
                        <div class="card-image-container" style="
                            width: 90%;
                            height: 70%;
                            background: linear-gradient(145deg, #F5F1FF, #E6D7FF);
                            border: 2px solid #C9A96E;
                            border-radius: 8px;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            color: #2D1B69;
                            font-family: 'Cinzel', serif;
                            font-size: 0.8rem;
                            text-align: center;
                            margin-bottom: 5px;
                            position: relative;
                            overflow: hidden;
                        ">
                            ${this.getCardImageOrPlaceholder(card)}
                        </div>
                    </div>
                </div>
                <h6 style="margin-top: 10px; color: var(--golden-glow);">${card.name}</h6>
            `;
            
            cardsDisplay.appendChild(cardDiv);
            cardElements.push(cardDiv);
        });
        
        // Animate cards appearing and then flipping one by one
        this.animateCardFlipSequence(cardElements, () => {
            // Display AI reading after all cards are flipped
            document.getElementById('ai-reading').innerHTML = `
                <div style="white-space: pre-line;">${reading}</div>
            `;
        });
        
        // Smooth scroll to reading
        document.getElementById('reading-section').scrollIntoView({
            behavior: 'smooth'
        });
    }
    
    getCardImageOrPlaceholder(card) {
        // Try to get actual card image path
        const imagePath = `/static/images/${card.image}`;
        return `<img src="${imagePath}" alt="${card.name}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 6px;" 
                     onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                <div style="display: none; width: 100%; height: 100%; align-items: center; justify-content: center; flex-direction: column;">
                    <div style="font-size: 2rem; margin-bottom: 5px;">✦</div>
                    <div style="font-size: 0.6rem; text-align: center;">${card.name}</div>
                </div>`;
    }
    
    animateCardFlipSequence(cardElements, callback) {
        // First, make cards appear
        cardElements.forEach((cardElement, index) => {
            setTimeout(() => {
                cardElement.style.transition = 'all 0.6s ease';
                cardElement.style.opacity = '1';
                cardElement.style.transform = 'translateY(0)';
            }, index * 200);
        });
        
        // Then flip cards one by one
        setTimeout(() => {
            cardElements.forEach((cardElement, index) => {
                setTimeout(() => {
                    const tarotCard = cardElement.querySelector('.tarot-card');
                    tarotCard.classList.add('flipped');
                    tarotCard.style.transform = 'rotateY(180deg)';
                    
                    // Call callback after last card is flipped
                    if (index === cardElements.length - 1) {
                        setTimeout(callback, 600);
                    }
                }, index * 800);
            });
        }, cardElements.length * 200 + 500);
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
