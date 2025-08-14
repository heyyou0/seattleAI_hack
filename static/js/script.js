// Mystic Tarot Application JavaScript

class TarotApp {
    constructor() {
        this.selectedCards = [];
        this.readingType = '1-card';
        this.requiredCards = 1;
        this.isSelectionComplete = false;
        // New property to hold the shuffled order of cards
        this.cardOrder = [];

        this.init();
    }

    init() {
        // Shuffle the deck of cards before generating the grid
        this.shuffleDeck();
        this.bindEvents();
        this.setupReadingTypeSelection();
        this.generateCardGrid();
    }

    // New method to shuffle the deck
    shuffleDeck() {
        // Create an array of card IDs from 0 to 77
        const deck = Array.from({ length: 78 }, (_, i) => i);

        // Fisher-Yates (Knuth) shuffle algorithm
        for (let i = deck.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [deck[i], deck[j]] = [deck[j], deck[i]]; // Swap elements
        }
        this.cardOrder = deck;
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

        // Event listener for the dismiss button on the error alert
        const errorAlert = document.getElementById('error-alert');
        if (errorAlert) {
            const closeButton = errorAlert.querySelector('.btn-close');
            if (closeButton) {
                closeButton.addEventListener('click', () => {
                    errorAlert.classList.add('d-none');
                });
            }
        }
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

        const fanContainer = document.createElement('div');
        fanContainer.className = 'card-fan-container';

        // Use the shuffled cardOrder to generate the cards
        this.cardOrder.forEach((cardId, index) => {
            const cardElement = this.createCardElement(cardId);
            this.positionCardInFan(cardElement, index, this.cardOrder.length);
            fanContainer.appendChild(cardElement);
        });

        cardGrid.appendChild(fanContainer);
    }

    positionCardInFan(cardElement, index, totalCards) {
        const maxAngle = 160; 
        const radius = 320;
        const k = 0.45;

        // Increase the fan width factor to make cards more spread out
        const spreadFactor = 1.3; // 1.0 = original, increase for wider gaps

        // Normalize index to [-1, 1]
        const t = totalCards === 1 ? 0 : (index / (totalCards - 1)) * 2 - 1;

        // Compute X with spread factor
        const fanWidth = radius * 2 * spreadFactor;
        const x = t * (fanWidth / 2);

        // U-curve for Y
        const y = -Math.pow(t, 2) * radius * k + radius * k * 0.2;

        // Rotation tangent along fan curve
        const deg = (index * maxAngle) / (totalCards - 1) - maxAngle / 2;
        const rad = deg * Math.PI / 180;
        const rotRad = Math.atan2(-k * Math.sin(rad), Math.cos(rad));
        const rotDeg = rotRad * 180 / Math.PI;

        cardElement.style.transform = `translate(${x}px, ${y}px) rotate(${rotDeg}deg)`;

        // Layering
        const center = (totalCards - 1) / 2;
        cardElement.style.zIndex = String(Math.floor(totalCards - Math.abs(index - center)));
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
        // Calculate position for selected cards at bottom center
        const cardWidth = 120;
        const spacing = 130;
        const totalWidth = (this.requiredCards - 1) * spacing;
        const startX = -totalWidth / 2;
        const targetX = startX + (selectionIndex * spacing);
        const targetY = 180; // Distance below the fan

        // Remove rotation and keep cards straight when selected
        cardElement.style.transform = `
            translate(${targetX}px, ${targetY}px) 
            rotate(0deg) 
            scale(1.3)
        `;
        cardElement.style.zIndex = 2000 + selectionIndex;
        cardElement.style.transition = 'all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
    }

    deselectCard(cardId, cardElement) {
        const index = this.selectedCards.indexOf(cardId);
        if (index > -1) {
            this.selectedCards.splice(index, 1);
            cardElement.classList.remove('selected');

            // Find the original index of the card in the shuffled deck to restore its position
            const originalIndex = this.cardOrder.indexOf(cardId);
            const totalCards = 78;
            this.positionCardInFan(cardElement, originalIndex, totalCards);
            cardElement.style.transition = 'all 0.6s ease';

            // Re-animate remaining selected cards
            this.selectedCards.forEach((selectedCardId, newIndex) => {
                const selectedElement = document.querySelector(`[data-card-id="${selectedCardId}"]`);
                if (selectedElement) {
                    setTimeout(() => {
                        this.animateCardSelection(selectedElement, newIndex);
                    }, 100);
                }
            });
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
        const errorAlert = document.getElementById('error-alert');

        if (!question) {
            // Show the Bootstrap error alert
            errorAlert.classList.add('show');
            errorAlert.classList.remove('d-none');
            return;
        }

        // Hide the error alert if it was showing
        errorAlert.classList.remove('show');
        errorAlert.classList.add('d-none');

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
            // An alert is still good here for a double-check
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
            const msgBox = document.createElement('div');
            msgBox.className = 'message-box';
            msgBox.textContent = 'Error generating reading: ' + error.message;
            document.body.appendChild(msgBox);
            setTimeout(() => msgBox.remove(), 3000);
        } finally {
            // Hide loading overlay
            document.getElementById('loading-overlay').classList.add('d-none');
        }
    }

    displayReading(reading, cards) {
        // Hide card selection and show reading
        document.getElementById('card-selection-section').classList.add('d-none');
        document.getElementById('reading-section').classList.remove('d-none');

        const cardsDisplay = document.getElementById('selected-cards-display');
        cardsDisplay.innerHTML = '';

        const cardElements = [];

        cards.forEach((card, index) => {
            const cardDiv = document.createElement('div');
            cardDiv.className = 'selected-card';
            cardDiv.style.opacity = '0';
            cardDiv.style.transform = 'translateY(20px)';

            // Each tarot-card has back visible first, front hidden
            cardDiv.innerHTML = `
                <div class="tarot-card" style="
                    width: 120px;
                    height: 180px;
                    position: relative;
                    transform: rotateY(0deg); /* start face-down */
                    transform-style: preserve-3d;
                    transition: transform 0.8s ease-in-out;
                ">
                    <div class="card-face card-back" style="
                        backface-visibility: hidden;
                        width: 100%;
                        height: 100%;
                        position: absolute;
                        top: 0; left: 0;
                    ">
                        <svg width="100%" height="100%" viewBox="0 0 80 120" fill="none">
                            <rect width="80" height="120" rx="12" fill="#2D1B69" stroke="#8B5A2B" stroke-width="2"/>
                            <circle cx="40" cy="30" r="10" fill="#C9A96E"/>
                            <path d="M30 60 L50 60 M30 70 L50 70 M30 80 L50 80" stroke="#C9A96E" stroke-width="2"/>
                            <circle cx="40" cy="100" r="10" fill="#C9A96E"/>
                        </svg>
                    </div>
                    <div class="card-face card-front" style="
                        backface-visibility: hidden;
                        transform: rotateY(180deg);
                        width: 100%;
                        height: 100%;
                        position: absolute;
                        top: 0; left: 0;
                    ">
                        ${this.getCardImageOrPlaceholder(card)}
                    </div>
                </div>
                <h6 style="margin-top: 10px; color: var(--golden-glow);">${card.name}</h6>
            `;

            cardsDisplay.appendChild(cardDiv);
            cardElements.push(cardDiv);
        });

        // Animate cards appearing
        cardElements.forEach((cardElement, index) => {
            setTimeout(() => {
                cardElement.style.transition = 'all 0.6s ease';
                cardElement.style.opacity = '1';
                cardElement.style.transform = 'translateY(0)';
            }, index * 200);
        });

        // Flip cards one by one after they appear
        setTimeout(() => {
            cardElements.forEach((cardElement, index) => {
                setTimeout(() => {
                    const tarotCard = cardElement.querySelector('.tarot-card');
                    tarotCard.style.transform = 'rotateY(180deg)'; // flip face-up
                }, index * 800);
            });
        }, cardElements.length * 200 + 500);

        // Display AI reading after all cards flipped
        setTimeout(() => {
            document.getElementById('ai-reading').innerHTML = `<div style="white-space: pre-line;">${reading}</div>`;
        }, cardElements.length * 1000);
    }


    getCardImageOrPlaceholder(card) {
        // Try to get actual card image path
        const imagePath = `/static/images/${card.image}`;
        return `<img src="${imagePath}" alt="${card.name}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 8px; position: absolute; top: 0; left: 0;" 
                    onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                <div style="display: none; width: 100%; height: 100%; align-items: center; justify-content: center; flex-direction: column; background: linear-gradient(145deg, #2D1B69, #1a0d4a); border-radius: 8px; position: absolute; top: 0; left: 0;">
                    <div style="font-size: 2rem; margin-bottom: 5px; color: #C9A96E;">✦</div>
                    <div style="font-size: 0.6rem; text-align: center; color: #C9A96E; padding: 5px;">${card.name}</div>
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

        // Shuffle the deck for a new reading
        this.shuffleDeck();

        // Reset UI
        document.getElementById('user-question').value = '';
        document.getElementById('one-card').checked = true;
        document.querySelectorAll('.reading-type-btn').forEach(btn => 
            btn.classList.remove('active')
        );
        document.querySelector('label[for="one-card"]').classList.add('active');

        // Hide the error alert
        const errorAlert = document.getElementById('error-alert');
        if (errorAlert) {
            errorAlert.classList.add('d-none');
            errorAlert.classList.remove('show');
        }

        // Reset card grid and regenerate to fix positioning bug
        document.querySelectorAll('.tarot-card').forEach(card => {
            card.classList.remove('selected');
            card.style.opacity = '1';
            card.style.cursor = 'pointer';
            card.style.transform = ''; // Reset transform
            card.style.zIndex = ''; // Reset z-index
        });

        // Clear the previous reading results
        const aiReadingDiv = document.getElementById('ai-reading');
        if (aiReadingDiv) {
            aiReadingDiv.innerHTML = '';
        }
        const selectedCardsDisplayDiv = document.getElementById('selected-cards-display');
        if (selectedCardsDisplayDiv) {
            selectedCardsDisplayDiv.innerHTML = '';
        }

        // Regenerate the card grid to reset all positions
        this.generateCardGrid();

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