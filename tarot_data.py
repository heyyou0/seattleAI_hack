# Complete 78-card Tarot deck data
TAROT_DECK = [
    # Major Arcana (0-21)
    {
        "id": 0,
        "name": "The Fool",
        "element": "Air",
        "keywords": ["new beginnings", "innocence", "adventure", "potential"],
        "meanings": {
            "upright": ["New beginnings", "Innocence", "Free spirit", "Adventure"],
            "reversed": ["Recklessness", "Risk-taking", "Foolishness", "Lack of direction"]
        },
        "description": "The Fool represents new beginnings, having faith in the future, being inexperienced, not knowing what to expect, having beginner's luck, improvisation and believing in the universe.",
        "image": "the_fool.svg"
    },
    {
        "id": 1,
        "name": "The Magician",
        "element": "Air",
        "keywords": ["manifestation", "power", "skill", "concentration"],
        "meanings": {
            "upright": ["Manifestation", "Resourcefulness", "Power", "Inspired action"],
            "reversed": ["Manipulation", "Poor planning", "Untapped talents", "Confusion"]
        },
        "description": "The Magician represents manifestation, resourcefulness, power, and inspired action. He has the ability to turn ideas into reality.",
        "image": "the_magician.svg"
    },
    {
        "id": 2,
        "name": "The High Priestess",
        "element": "Water",
        "keywords": ["intuition", "sacred knowledge", "divine feminine", "subconscious"],
        "meanings": {
            "upright": ["Intuition", "Sacred knowledge", "Divine feminine", "Subconscious mind"],
            "reversed": ["Secrets", "Disconnected from intuition", "Withdrawal", "Silence"]
        },
        "description": "The High Priestess represents intuition, sacred knowledge, divine feminine, and the subconscious mind.",
        "image": "the_high_priestess.jpg"
    },
    {
        "id": 3,
        "name": "The Empress",
        "element": "Earth",
        "keywords": ["femininity", "beauty", "nature", "abundance"],
        "meanings": {
            "upright": ["Femininity", "Beauty", "Nature", "Abundance"],
            "reversed": ["Creative block", "Dependence on others", "Infertility", "Lack of growth"]
        },
        "description": "The Empress represents femininity, beauty, nature, and abundance. She is the mother figure of the tarot.",
        "image": "the_empress.jpg"
    },
    {
        "id": 4,
        "name": "The Emperor",
        "element": "Fire",
        "keywords": ["authority", "structure", "control", "fatherly figure"],
        "meanings": {
            "upright": ["Authority", "Structure", "Control", "Fatherly figure"],
            "reversed": ["Tyranny", "Rigidity", "Coldness", "Abuse of power"]
        },
        "description": "The Emperor represents authority, structure, control, and fatherly figure. He is the father figure of the tarot.",
        "image": "the_emperor.jpg"
    },
    {
        "id": 5,
        "name": "The Hierophant",
        "element": "Earth",
        "keywords": ["spiritual wisdom", "religious beliefs", "conformity", "tradition"],
        "meanings": {
            "upright": ["Spiritual wisdom", "Religious beliefs", "Conformity", "Tradition"],
            "reversed": ["Personal beliefs", "Freedom", "Challenging the status quo", "Rebellion"]
        },
        "description": "The Hierophant represents spiritual wisdom, religious beliefs, conformity, and tradition.",
        "image": "the_hierophant.jpg"
    },
    {
        "id": 6,
        "name": "The Lovers",
        "element": "Air",
        "keywords": ["love", "harmony", "relationships", "values alignment"],
        "meanings": {
            "upright": ["Love", "Harmony", "Relationships", "Values alignment"],
            "reversed": ["Disharmony", "Imbalance", "Misalignment of values", "Broken relationship"]
        },
        "description": "The Lovers represents love, harmony, relationships, and values alignment.",
        "image": "the_lovers.jpg"
    },
    {
        "id": 7,
        "name": "The Chariot",
        "element": "Water",
        "keywords": ["control", "willpower", "success", "determination"],
        "meanings": {
            "upright": ["Control", "Willpower", "Success", "Determination"],
            "reversed": ["Lack of control", "Lack of direction", "Aggression", "Powerlessness"]
        },
        "description": "The Chariot represents control, willpower, success, and determination.",
        "image": "the_chariot.jpg"
    },
    {
        "id": 8,
        "name": "Strength",
        "element": "Fire",
        "keywords": ["strength", "courage", "persuasion", "influence"],
        "meanings": {
            "upright": ["Strength", "Courage", "Persuasion", "Influence"],
            "reversed": ["Self doubt", "Low energy", "Raw emotion", "Weakness"]
        },
        "description": "Strength represents inner strength, courage, persuasion, and influence.",
        "image": "strength.jpg"
    },
    {
        "id": 9,
        "name": "The Hermit",
        "element": "Earth",
        "keywords": ["soul searching", "introspection", "inner guidance", "solitude"],
        "meanings": {
            "upright": ["Soul searching", "Introspection", "Inner guidance", "Solitude"],
            "reversed": ["Isolation", "Loneliness", "Withdrawal", "Paranoia"]
        },
        "description": "The Hermit represents soul searching, introspection, inner guidance, and solitude.",
        "image": "the_hermit.jpg"
    },
    {
        "id": 10,
        "name": "Wheel of Fortune",
        "element": "Fire",
        "keywords": ["good luck", "karma", "life cycles", "destiny"],
        "meanings": {
            "upright": ["Good luck", "Karma", "Life cycles", "Destiny"],
            "reversed": ["Bad luck", "Lack of control", "Clinging to control", "Bad luck"]
        },
        "description": "The Wheel of Fortune represents good luck, karma, life cycles, and destiny.",
        "image": "wheel_of_fortune.jpg"
    },
    {
        "id": 11,
        "name": "Justice",
        "element": "Air",
        "keywords": ["justice", "fairness", "truth", "cause and effect"],
        "meanings": {
            "upright": ["Justice", "Fairness", "Truth", "Cause and effect"],
            "reversed": ["Unfairness", "Lack of accountability", "Dishonesty", "Bias"]
        },
        "description": "Justice represents justice, fairness, truth, and cause and effect.",
        "image": "justice.jpg"
    },
    {
        "id": 12,
        "name": "The Hanged Man",
        "element": "Water",
        "keywords": ["suspension", "restriction", "letting go", "sacrifice"],
        "meanings": {
            "upright": ["Suspension", "Restriction", "Letting go", "Sacrifice"],
            "reversed": ["Delays", "Resistance", "Stalling", "Indecision"]
        },
        "description": "The Hanged Man represents suspension, restriction, letting go, and sacrifice.",
        "image": "the_hanged_man.jpg"
    },
    {
        "id": 13,
        "name": "Death",
        "element": "Water",
        "keywords": ["endings", "beginnings", "change", "transformation"],
        "meanings": {
            "upright": ["Endings", "Beginnings", "Change", "Transformation"],
            "reversed": ["Resistance to change", "Personal transformation", "Inner purging", "Stagnation"]
        },
        "description": "Death represents endings, beginnings, change, and transformation. It rarely means literal death.",
        "image": "death.jpg"
    },
    {
        "id": 14,
        "name": "Temperance",
        "element": "Fire",
        "keywords": ["balance", "moderation", "patience", "purpose"],
        "meanings": {
            "upright": ["Balance", "Moderation", "Patience", "Purpose"],
            "reversed": ["Imbalance", "Excess", "Self-healing", "Re-alignment"]
        },
        "description": "Temperance represents balance, moderation, patience, and purpose.",
        "image": "temperance.jpg"
    },
    {
        "id": 15,
        "name": "The Devil",
        "element": "Earth",
        "keywords": ["bondage", "addiction", "sexuality", "materialism"],
        "meanings": {
            "upright": ["Bondage", "Addiction", "Sexuality", "Materialism"],
            "reversed": ["Releasing limiting beliefs", "Exploring dark thoughts", "Detachment", "Breaking free"]
        },
        "description": "The Devil represents bondage, addiction, sexuality, and materialism.",
        "image": "the_devil.jpg"
    },
    {
        "id": 16,
        "name": "The Tower",
        "element": "Fire",
        "keywords": ["sudden change", "upheaval", "chaos", "revelation"],
        "meanings": {
            "upright": ["Sudden change", "Upheaval", "Chaos", "Revelation"],
            "reversed": ["Personal transformation", "Fear of change", "Avoiding disaster", "Delayed transformation"]
        },
        "description": "The Tower represents sudden change, upheaval, chaos, and revelation.",
        "image": "the_tower.jpg"
    },
    {
        "id": 17,
        "name": "The Star",
        "element": "Air",
        "keywords": ["hope", "faith", "purpose", "renewal"],
        "meanings": {
            "upright": ["Hope", "Faith", "Purpose", "Renewal"],
            "reversed": ["Lack of faith", "Despair", "Self-trust", "Disconnection"]
        },
        "description": "The Star represents hope, faith, purpose, and renewal.",
        "image": "the_star.jpg"
    },
    {
        "id": 18,
        "name": "The Moon",
        "element": "Water",
        "keywords": ["illusion", "fear", "anxiety", "subconscious"],
        "meanings": {
            "upright": ["Illusion", "Fear", "Anxiety", "Subconscious"],
            "reversed": ["Release of fear", "Repressed emotion", "Inner confusion", "Unveiled secrets"]
        },
        "description": "The Moon represents illusion, fear, anxiety, and subconscious.",
        "image": "the_moon.jpg"
    },
    {
        "id": 19,
        "name": "The Sun",
        "element": "Fire",
        "keywords": ["positivity", "fun", "warmth", "success"],
        "meanings": {
            "upright": ["Positivity", "Fun", "Warmth", "Success"],
            "reversed": ["Inner child", "Feeling down", "Overly optimistic", "Lack of success"]
        },
        "description": "The Sun represents positivity, fun, warmth, and success.",
        "image": "the_sun.jpg"
    },
    {
        "id": 20,
        "name": "Judgement",
        "element": "Fire",
        "keywords": ["judgement", "rebirth", "inner calling", "absolution"],
        "meanings": {
            "upright": ["Judgement", "Rebirth", "Inner calling", "Absolution"],
            "reversed": ["Self-doubt", "Inner critic", "Ignoring the call", "Lack of self awareness"]
        },
        "description": "Judgement represents judgement, rebirth, inner calling, and absolution.",
        "image": "judgement.jpg"
    },
    {
        "id": 21,
        "name": "The World",
        "element": "Earth",
        "keywords": ["completion", "integration", "accomplishment", "travel"],
        "meanings": {
            "upright": ["Completion", "Integration", "Accomplishment", "Travel"],
            "reversed": ["Seeking personal closure", "Shortcut", "Delays", "Lack of achievement"]
        },
        "description": "The World represents completion, integration, accomplishment, and travel.",
        "image": "the_world.jpg"
    },
    
    # Wands Suit (22-35)
    {
        "id": 22,
        "name": "Ace of Wands",
        "element": "Fire",
        "keywords": ["inspiration", "new opportunities", "growth", "potential"],
        "meanings": {
            "upright": ["Inspiration", "New opportunities", "Growth", "Potential"],
            "reversed": ["An emerging idea", "Lack of direction", "Distractions", "Delays"]
        },
        "description": "The Ace of Wands represents inspiration, new opportunities, growth, and potential.",
        "image": "ace_of_wands.jpg"
    },
    {
        "id": 23,
        "name": "Two of Wands",
        "element": "Fire",
        "keywords": ["future planning", "making decisions", "leaving comfort zone", "personal goals"],
        "meanings": {
            "upright": ["Future planning", "Making decisions", "Leaving comfort zone", "Personal goals"],
            "reversed": ["Personal goals", "Inner alignment", "Fear of unknown", "Lack of planning"]
        },
        "description": "The Two of Wands represents future planning, making decisions, leaving comfort zone, and personal goals.",
        "image": "two_of_wands.jpg"
    },
    {
        "id": 24,
        "name": "Three of Wands",
        "element": "Fire",
        "keywords": ["expansion", "foresight", "overseas opportunities", "leadership"],
        "meanings": {
            "upright": ["Expansion", "Foresight", "Overseas opportunities", "Leadership"],
            "reversed": ["Playing small", "Lack of foresight", "Unexpected delays", "Lack of preparation"]
        },
        "description": "The Three of Wands represents expansion, foresight, overseas opportunities, and leadership.",
        "image": "three_of_wands.jpg"
    },
    {
        "id": 25,
        "name": "Four of Wands",
        "element": "Fire",
        "keywords": ["celebration", "joy", "harmony", "relaxation"],
        "meanings": {
            "upright": ["Celebration", "Joy", "Harmony", "Relaxation"],
            "reversed": ["Personal celebration", "Inner harmony", "Conflict with others", "Transition"]
        },
        "description": "The Four of Wands represents celebration, joy, harmony, and relaxation.",
        "image": "four_of_wands.jpg"
    },
    {
        "id": 26,
        "name": "Five of Wands",
        "element": "Fire",
        "keywords": ["conflict", "disagreements", "competition", "tension"],
        "meanings": {
            "upright": ["Conflict", "Disagreements", "Competition", "Tension"],
            "reversed": ["Inner conflict", "Conflict avoidance", "Tension release", "Avoiding conflict"]
        },
        "description": "The Five of Wands represents conflict, disagreements, competition, and tension.",
        "image": "five_of_wands.jpg"
    },
    {
        "id": 27,
        "name": "Six of Wands",
        "element": "Fire",
        "keywords": ["success", "public recognition", "progress", "self-confidence"],
        "meanings": {
            "upright": ["Success", "Public recognition", "Progress", "Self-confidence"],
            "reversed": ["Private achievement", "Personal definition of success", "Fall from grace", "Lack of recognition"]
        },
        "description": "The Six of Wands represents success, public recognition, progress, and self-confidence.",
        "image": "six_of_wands.jpg"
    },
    {
        "id": 28,
        "name": "Seven of Wands",
        "element": "Fire",
        "keywords": ["challenge", "competition", "protection", "perseverance"],
        "meanings": {
            "upright": ["Challenge", "Competition", "Protection", "Perseverance"],
            "reversed": ["Exhaustion", "Give up", "Burnt out", "Paranoia"]
        },
        "description": "The Seven of Wands represents challenge, competition, protection, and perseverance.",
        "image": "seven_of_wands.jpg"
    },
    {
        "id": 29,
        "name": "Eight of Wands",
        "element": "Fire",
        "keywords": ["movement", "fast paced change", "action", "alignment"],
        "meanings": {
            "upright": ["Movement", "Fast paced change", "Action", "Alignment"],
            "reversed": ["Delays", "Frustration", "Resisting change", "Internal alignment"]
        },
        "description": "The Eight of Wands represents movement, fast paced change, action, and alignment.",
        "image": "eight_of_wands.jpg"
    },
    {
        "id": 30,
        "name": "Nine of Wands",
        "element": "Fire",
        "keywords": ["resilience", "courage", "persistence", "test of faith"],
        "meanings": {
            "upright": ["Resilience", "Courage", "Persistence", "Test of faith"],
            "reversed": ["Inner resources", "Struggle", "Overwhelm", "Defensive"]
        },
        "description": "The Nine of Wands represents resilience, courage, persistence, and test of faith.",
        "image": "nine_of_wands.jpg"
    },
    {
        "id": 31,
        "name": "Ten of Wands",
        "element": "Fire",
        "keywords": ["burden", "extra responsibility", "hard work", "completion"],
        "meanings": {
            "upright": ["Burden", "Extra responsibility", "Hard work", "Completion"],
            "reversed": ["Doing it all", "Carrying the burden", "Delegation", "Release"]
        },
        "description": "The Ten of Wands represents burden, extra responsibility, hard work, and completion.",
        "image": "ten_of_wands.jpg"
    },
    {
        "id": 32,
        "name": "Page of Wands",
        "element": "Fire",
        "keywords": ["inspiration", "ideas", "discovery", "limitless potential"],
        "meanings": {
            "upright": ["Inspiration", "Ideas", "Discovery", "Limitless potential"],
            "reversed": ["Newly formed ideas", "Redirecting energy", "Self-limiting beliefs", "Lack of direction"]
        },
        "description": "The Page of Wands represents inspiration, ideas, discovery, and limitless potential.",
        "image": "page_of_wands.jpg"
    },
    {
        "id": 33,
        "name": "Knight of Wands",
        "element": "Fire",
        "keywords": ["energy", "passion", "inspired action", "adventure"],
        "meanings": {
            "upright": ["Energy", "Passion", "Inspired action", "Adventure"],
            "reversed": ["Passion project", "Haste", "Scattered energy", "Delays"]
        },
        "description": "The Knight of Wands represents energy, passion, inspired action, and adventure.",
        "image": "knight_of_wands.jpg"
    },
    {
        "id": 34,
        "name": "Queen of Wands",
        "element": "Fire",
        "keywords": ["courage", "confidence", "independence", "social butterfly"],
        "meanings": {
            "upright": ["Courage", "Confidence", "Independence", "Social butterfly"],
            "reversed": ["Self-respect", "Self-confidence", "Introverted", "Re-establish sense of self"]
        },
        "description": "The Queen of Wands represents courage, confidence, independence, and social butterfly.",
        "image": "queen_of_wands.jpg"
    },
    {
        "id": 35,
        "name": "King of Wands",
        "element": "Fire",
        "keywords": ["natural leader", "vision", "entrepreneur", "honour"],
        "meanings": {
            "upright": ["Natural leader", "Vision", "Entrepreneur", "Honour"],
            "reversed": ["Impulsiveness", "Haste", "Ruthless", "High expectations"]
        },
        "description": "The King of Wands represents natural leader, vision, entrepreneur, and honour.",
        "image": "king_of_wands.jpg"
    },
    
    # Cups Suit (36-49)
    {
        "id": 36,
        "name": "Ace of Cups",
        "element": "Water",
        "keywords": ["love", "new relationships", "compassion", "creativity"],
        "meanings": {
            "upright": ["Love", "New relationships", "Compassion", "Creativity"],
            "reversed": ["Self-love", "Intuition", "Repressed emotions", "Emptiness"]
        },
        "description": "The Ace of Cups represents love, new relationships, compassion, and creativity.",
        "image": "ace_of_cups.jpg"
    },
    {
        "id": 37,
        "name": "Two of Cups",
        "element": "Water",
        "keywords": ["unified love", "partnership", "mutual attraction", "relationships"],
        "meanings": {
            "upright": ["Unified love", "Partnership", "Mutual attraction", "Relationships"],
            "reversed": ["Self-love", "Break-ups", "Disharmony", "Distrust"]
        },
        "description": "The Two of Cups represents unified love, partnership, mutual attraction, and relationships.",
        "image": "two_of_cups.jpg"
    },
    {
        "id": 38,
        "name": "Three of Cups",
        "element": "Water",
        "keywords": ["celebration", "friendship", "creativity", "collaborations"],
        "meanings": {
            "upright": ["Celebration", "Friendship", "Creativity", "Collaborations"],
            "reversed": ["Independence", "Social gatherings", "Three's a crowd", "Gossip"]
        },
        "description": "The Three of Cups represents celebration, friendship, creativity, and collaborations.",
        "image": "three_of_cups.jpg"
    },
    {
        "id": 39,
        "name": "Four of Cups",
        "element": "Water",
        "keywords": ["meditation", "contemplation", "apathy", "reevaluation"],
        "meanings": {
            "upright": ["Meditation", "Contemplation", "Apathy", "Reevaluation"],
            "reversed": ["Retreat", "Withdrawal", "Checking in", "Stillness"]
        },
        "description": "The Four of Cups represents meditation, contemplation, apathy, and reevaluation.",
        "image": "four_of_cups.jpg"
    },
    {
        "id": 40,
        "name": "Five of Cups",
        "element": "Water",
        "keywords": ["regret", "failure", "disappointment", "pessimism"],
        "meanings": {
            "upright": ["Regret", "Failure", "Disappointment", "Pessimism"],
            "reversed": ["Personal setbacks", "Self-forgiveness", "Moving on", "Acceptance"]
        },
        "description": "The Five of Cups represents regret, failure, disappointment, and pessimism.",
        "image": "five_of_cups.jpg"
    },
    {
        "id": 41,
        "name": "Six of Cups",
        "element": "Water",
        "keywords": ["revisiting the past", "childhood memories", "innocence", "joy"],
        "meanings": {
            "upright": ["Revisiting the past", "Childhood memories", "Innocence", "Joy"],
            "reversed": ["Living in the past", "Forgiveness", "Lacking playfulness", "Maturity"]
        },
        "description": "The Six of Cups represents revisiting the past, childhood memories, innocence, and joy.",
        "image": "six_of_cups.jpg"
    },
    {
        "id": 42,
        "name": "Seven of Cups",
        "element": "Water",
        "keywords": ["opportunities", "choices", "wishful thinking", "illusion"],
        "meanings": {
            "upright": ["Opportunities", "Choices", "Wishful thinking", "Illusion"],
            "reversed": ["Alignment", "Personal values", "Overwhelmed by choices", "Lack of purpose"]
        },
        "description": "The Seven of Cups represents opportunities, choices, wishful thinking, and illusion.",
        "image": "seven_of_cups.jpg"
    },
    {
        "id": 43,
        "name": "Eight of Cups",
        "element": "Water",
        "keywords": ["disappointment", "abandonment", "withdrawal", "escapism"],
        "meanings": {
            "upright": ["Disappointment", "Abandonment", "Withdrawal", "Escapism"],
            "reversed": ["Trying one more time", "Indecision", "Aimless drifting", "Walking away"]
        },
        "description": "The Eight of Cups represents disappointment, abandonment, withdrawal, and escapism.",
        "image": "eight_of_cups.jpg"
    },
    {
        "id": 44,
        "name": "Nine of Cups",
        "element": "Water",
        "keywords": ["contentment", "satisfaction", "gratitude", "wish come true"],
        "meanings": {
            "upright": ["Contentment", "Satisfaction", "Gratitude", "Wish come true"],
            "reversed": ["Inner happiness", "Materialism", "Dissatisfaction", "Indulgence"]
        },
        "description": "The Nine of Cups represents contentment, satisfaction, gratitude, and wish come true.",
        "image": "nine_of_cups.jpg"
    },
    {
        "id": 45,
        "name": "Ten of Cups",
        "element": "Water",
        "keywords": ["divine love", "blissful relationships", "harmony", "alignment"],
        "meanings": {
            "upright": ["Divine love", "Blissful relationships", "Harmony", "Alignment"],
            "reversed": ["Disconnection", "Misaligned values", "Struggling relationships", "Disharmony"]
        },
        "description": "The Ten of Cups represents divine love, blissful relationships, harmony, and alignment.",
        "image": "ten_of_cups.jpg"
    },
    {
        "id": 46,
        "name": "Page of Cups",
        "element": "Water",
        "keywords": ["creative opportunities", "intuitive messages", "curiosity", "possibility"],
        "meanings": {
            "upright": ["Creative opportunities", "Intuitive messages", "Curiosity", "Possibility"],
            "reversed": ["New ideas", "Doubting intuition", "Creative blocks", "Emotional immaturity"]
        },
        "description": "The Page of Cups represents creative opportunities, intuitive messages, curiosity, and possibility.",
        "image": "page_of_cups.jpg"
    },
    {
        "id": 47,
        "name": "Knight of Cups",
        "element": "Water",
        "keywords": ["creativity", "romance", "charm", "imagination"],
        "meanings": {
            "upright": ["Creativity", "Romance", "Charm", "Imagination"],
            "reversed": ["Overactive imagination", "Unrealistic", "Jealousy", "Moodiness"]
        },
        "description": "The Knight of Cups represents creativity, romance, charm, and imagination.",
        "image": "knight_of_cups.jpg"
    },
    {
        "id": 48,
        "name": "Queen of Cups",
        "element": "Water",
        "keywords": ["compassionate", "caring", "emotionally stable", "intuitive"],
        "meanings": {
            "upright": ["Compassionate", "Caring", "Emotionally stable", "Intuitive"],
            "reversed": ["Inner compassion", "Self-care", "Co-dependency", "Emotional instability"]
        },
        "description": "The Queen of Cups represents compassionate, caring, emotionally stable, and intuitive.",
        "image": "queen_of_cups.jpg"
    },
    {
        "id": 49,
        "name": "King of Cups",
        "element": "Water",
        "keywords": ["emotionally balanced", "compassionate leader", "diplomacy", "balance"],
        "meanings": {
            "upright": ["Emotionally balanced", "Compassionate leader", "Diplomacy", "Balance"],
            "reversed": ["Self-compassion", "Inner feelings", "Moodiness", "Emotional manipulation"]
        },
        "description": "The King of Cups represents emotionally balanced, compassionate leader, diplomacy, and balance.",
        "image": "king_of_cups.jpg"
    },
    
    # Swords Suit (50-63)
    {
        "id": 50,
        "name": "Ace of Swords",
        "element": "Air",
        "keywords": ["new ideas", "mental clarity", "breakthrough", "communication"],
        "meanings": {
            "upright": ["New ideas", "Mental clarity", "Breakthrough", "Communication"],
            "reversed": ["Inner clarity", "Re-thinking an idea", "Clouded judgement", "Confusion"]
        },
        "description": "The Ace of Swords represents new ideas, mental clarity, breakthrough, and communication.",
        "image": "ace_of_swords.jpg"
    },
    {
        "id": 51,
        "name": "Two of Swords",
        "element": "Air",
        "keywords": ["difficult decisions", "weighing up options", "an impasse", "avoidance"],
        "meanings": {
            "upright": ["Difficult decisions", "Weighing up options", "An impasse", "Avoidance"],
            "reversed": ["Indecision", "Confusion", "Information overload", "Overwhelming choices"]
        },
        "description": "The Two of Swords represents difficult decisions, weighing up options, an impasse, and avoidance.",
        "image": "two_of_swords.jpg"
    },
    {
        "id": 52,
        "name": "Three of Swords",
        "element": "Air",
        "keywords": ["heartbreak", "emotional pain", "sorrow", "grief"],
        "meanings": {
            "upright": ["Heartbreak", "Emotional pain", "Sorrow", "Grief"],
            "reversed": ["Negative self-talk", "Releasing pain", "Optimism", "Forgiveness"]
        },
        "description": "The Three of Swords represents heartbreak, emotional pain, sorrow, and grief.",
        "image": "three_of_swords.jpg"
    },
    {
        "id": 53,
        "name": "Four of Swords",
        "element": "Air",
        "keywords": ["rest", "relaxation", "meditation", "contemplation"],
        "meanings": {
            "upright": ["Rest", "Relaxation", "Meditation", "Contemplation"],
            "reversed": ["Exhaustion", "Burn-out", "Deep contemplation", "Stagnation"]
        },
        "description": "The Four of Swords represents rest, relaxation, meditation, and contemplation.",
        "image": "four_of_swords.jpg"
    },
    {
        "id": 54,
        "name": "Five of Swords",
        "element": "Air",
        "keywords": ["conflict", "disagreements", "competition", "defeat"],
        "meanings": {
            "upright": ["Conflict", "Disagreements", "Competition", "Defeat"],
            "reversed": ["Reconciliation", "Making amends", "Past resentment", "Revenge"]
        },
        "description": "The Five of Swords represents conflict, disagreements, competition, and defeat.",
        "image": "five_of_swords.jpg"
    },
    {
        "id": 55,
        "name": "Six of Swords",
        "element": "Air",
        "keywords": ["transition", "change", "rite of passage", "releasing baggage"],
        "meanings": {
            "upright": ["Transition", "Change", "Rite of passage", "Releasing baggage"],
            "reversed": ["Personal transition", "Resistance to change", "Unfinished business", "Seeking closure"]
        },
        "description": "The Six of Swords represents transition, change, rite of passage, and releasing baggage.",
        "image": "six_of_swords.jpg"
    },
    {
        "id": 56,
        "name": "Seven of Swords",
        "element": "Air",
        "keywords": ["betrayal", "deception", "getting away with something", "acting strategically"],
        "meanings": {
            "upright": ["Betrayal", "Deception", "Getting away with something", "Acting strategically"],
            "reversed": ["Imposter syndrome", "Self-deceit", "Keeping secrets", "Getting away with it"]
        },
        "description": "The Seven of Swords represents betrayal, deception, getting away with something, and acting strategically.",
        "image": "seven_of_swords.jpg"
    },
    {
        "id": 57,
        "name": "Eight of Swords",
        "element": "Air",
        "keywords": ["negative thoughts", "self-imposed restriction", "imprisonment", "victim mentality"],
        "meanings": {
            "upright": ["Negative thoughts", "Self-imposed restriction", "Imprisonment", "Victim mentality"],
            "reversed": ["Self-limiting beliefs", "Inner critic", "Releasing negative thoughts", "Open to new perspectives"]
        },
        "description": "The Eight of Swords represents negative thoughts, self-imposed restriction, imprisonment, and victim mentality.",
        "image": "eight_of_swords.jpg"
    },
    {
        "id": 58,
        "name": "Nine of Swords",
        "element": "Air",
        "keywords": ["anxiety", "worry", "fear", "depression"],
        "meanings": {
            "upright": ["Anxiety", "Worry", "Fear", "Depression"],
            "reversed": ["Inner turmoil", "Deep-seated fears", "Secrets", "Releasing worry"]
        },
        "description": "The Nine of Swords represents anxiety, worry, fear, and depression.",
        "image": "nine_of_swords.jpg"
    },
    {
        "id": 59,
        "name": "Ten of Swords",
        "element": "Air",
        "keywords": ["painful endings", "deep wounds", "betrayal", "loss"],
        "meanings": {
            "upright": ["Painful endings", "Deep wounds", "Betrayal", "Loss"],
            "reversed": ["Recovery", "Regeneration", "Resisting an inevitable end", "Surviving disaster"]
        },
        "description": "The Ten of Swords represents painful endings, deep wounds, betrayal, and loss.",
        "image": "ten_of_swords.jpg"
    },
    {
        "id": 60,
        "name": "Page of Swords",
        "element": "Air",
        "keywords": ["new ideas", "curiosity", "thirst for knowledge", "new ways of communicating"],
        "meanings": {
            "upright": ["New ideas", "Curiosity", "Thirst for knowledge", "New ways of communicating"],
            "reversed": ["Self-expression", "All talk and no action", "Lack of planning", "Haste"]
        },
        "description": "The Page of Swords represents new ideas, curiosity, thirst for knowledge, and new ways of communicating.",
        "image": "page_of_swords.jpg"
    },
    {
        "id": 61,
        "name": "Knight of Swords",
        "element": "Air",
        "keywords": ["ambitious", "action-oriented", "driven to succeed", "fast-thinking"],
        "meanings": {
            "upright": ["Ambitious", "Action-oriented", "Driven to succeed", "Fast-thinking"],
            "reversed": ["Restless", "Unfocused", "Impulsive", "Burn-out"]
        },
        "description": "The Knight of Swords represents ambitious, action-oriented, driven to succeed, and fast-thinking.",
        "image": "knight_of_swords.jpg"
    },
    {
        "id": 62,
        "name": "Queen of Swords",
        "element": "Air",
        "keywords": ["independent", "unbiased judgement", "clear boundaries", "direct communication"],
        "meanings": {
            "upright": ["Independent", "Unbiased judgement", "Clear boundaries", "Direct communication"],
            "reversed": ["Overly-emotional", "Easily influenced", "Bitchy", "Cold-hearted"]
        },
        "description": "The Queen of Swords represents independent, unbiased judgement, clear boundaries, and direct communication.",
        "image": "queen_of_swords.jpg"
    },
    {
        "id": 63,
        "name": "King of Swords",
        "element": "Air",
        "keywords": ["mental clarity", "intellectual power", "authority", "truth"],
        "meanings": {
            "upright": ["Mental clarity", "Intellectual power", "Authority", "Truth"],
            "reversed": ["Quiet power", "Inner truth", "Misuse of power", "Manipulation"]
        },
        "description": "The King of Swords represents mental clarity, intellectual power, authority, and truth.",
        "image": "king_of_swords.jpg"
    },
    
    # Pentacles Suit (64-77)
    {
        "id": 64,
        "name": "Ace of Pentacles",
        "element": "Earth",
        "keywords": ["a new financial or career opportunity", "manifestation", "abundance"],
        "meanings": {
            "upright": ["A new financial or career opportunity", "Manifestation", "Abundance"],
            "reversed": ["Lost opportunity", "Lack of planning and foresight", "Bad investment"]
        },
        "description": "The Ace of Pentacles represents a new financial or career opportunity, manifestation, and abundance.",
        "image": "ace_of_pentacles.jpg"
    },
    {
        "id": 65,
        "name": "Two of Pentacles",
        "element": "Earth",
        "keywords": ["multiple priorities", "time management", "prioritisation", "adaptability"],
        "meanings": {
            "upright": ["Multiple priorities", "Time management", "Prioritisation", "Adaptability"],
            "reversed": ["Over-committed", "Disorganisation", "Reprioritisation", "Overwhelm"]
        },
        "description": "The Two of Pentacles represents multiple priorities, time management, prioritisation, and adaptability.",
        "image": "two_of_pentacles.jpg"
    },
    {
        "id": 66,
        "name": "Three of Pentacles",
        "element": "Earth",
        "keywords": ["teamwork", "collaboration", "learning", "implementation"],
        "meanings": {
            "upright": ["Teamwork", "Collaboration", "Learning", "Implementation"],
            "reversed": ["Disharmony", "Misaligned goals", "Lack of teamwork", "Apathy"]
        },
        "description": "The Three of Pentacles represents teamwork, collaboration, learning, and implementation.",
        "image": "three_of_pentacles.jpg"
    },
    {
        "id": 67,
        "name": "Four of Pentacles",
        "element": "Earth",
        "keywords": ["saving money", "security", "conservatism", "scarcity"],
        "meanings": {
            "upright": ["Saving money", "Security", "Conservatism", "Scarcity"],
            "reversed": ["Over-spending", "Greed", "Self-protection", "Financial insecurity"]
        },
        "description": "The Four of Pentacles represents saving money, security, conservatism, and scarcity.",
        "image": "four_of_pentacles.jpg"
    },
    {
        "id": 68,
        "name": "Five of Pentacles",
        "element": "Earth",
        "keywords": ["financial loss", "poverty", "lack mindset", "isolation"],
        "meanings": {
            "upright": ["Financial loss", "Poverty", "Lack mindset", "Isolation"],
            "reversed": ["Recovery from financial loss", "Spiritual poverty", "Inner resources", "Positive change"]
        },
        "description": "The Five of Pentacles represents financial loss, poverty, lack mindset, and isolation.",
        "image": "five_of_pentacles.jpg"
    },
    {
        "id": 69,
        "name": "Six of Pentacles",
        "element": "Earth",
        "keywords": ["giving", "receiving", "sharing wealth", "generosity"],
        "meanings": {
            "upright": ["Giving", "Receiving", "Sharing wealth", "Generosity"],
            "reversed": ["Self-care", "Unpaid debts", "One-sided charity", "Power dynamics"]
        },
        "description": "The Six of Pentacles represents giving, receiving, sharing wealth, and generosity.",
        "image": "six_of_pentacles.jpg"
    },
    {
        "id": 70,
        "name": "Seven of Pentacles",
        "element": "Earth",
        "keywords": ["long-term view", "sustainable results", "perseverance", "investment"],
        "meanings": {
            "upright": ["Long-term view", "Sustainable results", "Perseverance", "Investment"],
            "reversed": ["Lack of long-term vision", "Limited success or reward", "Impatience", "Lack of reward"]
        },
        "description": "The Seven of Pentacles represents long-term view, sustainable results, perseverance, and investment.",
        "image": "seven_of_pentacles.jpg"
    },
    {
        "id": 71,
        "name": "Eight of Pentacles",
        "element": "Earth",
        "keywords": ["apprenticeship", "repetitive tasks", "mastery", "skill development"],
        "meanings": {
            "upright": ["Apprenticeship", "Repetitive tasks", "Mastery", "Skill development"],
            "reversed": ["Self-development", "Perfectionism", "Misdirected activity", "Lack of quality"]
        },
        "description": "The Eight of Pentacles represents apprenticeship, repetitive tasks, mastery, and skill development.",
        "image": "eight_of_pentacles.jpg"
    },
    {
        "id": 72,
        "name": "Nine of Pentacles",
        "element": "Earth",
        "keywords": ["abundance", "luxury", "self-sufficiency", "financial independence"],
        "meanings": {
            "upright": ["Abundance", "Luxury", "Self-sufficiency", "Financial independence"],
            "reversed": ["Self-worth", "Over-investment in work", "Hustling", "Material instability"]
        },
        "description": "The Nine of Pentacles represents abundance, luxury, self-sufficiency, and financial independence.",
        "image": "nine_of_pentacles.jpg"
    },
    {
        "id": 73,
        "name": "Ten of Pentacles",
        "element": "Earth",
        "keywords": ["wealth", "financial security", "family", "long-term success"],
        "meanings": {
            "upright": ["Wealth", "Financial security", "Family", "Long-term success"],
            "reversed": ["The dark side of wealth", "Financial failure or loss", "Lack of family support", "Fleeting success"]
        },
        "description": "The Ten of Pentacles represents wealth, financial security, family, and long-term success.",
        "image": "ten_of_pentacles.jpg"
    },
    {
        "id": 74,
        "name": "Page of Pentacles",
        "element": "Earth",
        "keywords": ["manifestation", "financial opportunity", "skill development", "ambition"],
        "meanings": {
            "upright": ["Manifestation", "Financial opportunity", "Skill development", "Ambition"],
            "reversed": ["Lack of progress", "Procrastination", "Learn from failure", "Impatience"]
        },
        "description": "The Page of Pentacles represents manifestation, financial opportunity, skill development, and ambition.",
        "image": "page_of_pentacles.jpg"
    },
    {
        "id": 75,
        "name": "Knight of Pentacles",
        "element": "Earth",
        "keywords": ["hard work", "productivity", "routine", "conservatism"],
        "meanings": {
            "upright": ["Hard work", "Productivity", "Routine", "Conservatism"],
            "reversed": ["Self-discipline", "Boredom", "Feeling 'stuck'", "Perfectionism"]
        },
        "description": "The Knight of Pentacles represents hard work, productivity, routine, and conservatism.",
        "image": "knight_of_pentacles.jpg"
    },
    {
        "id": 76,
        "name": "Queen of Pentacles",
        "element": "Earth",
        "keywords": ["nurturing", "practical", "providing financially", "a working parent"],
        "meanings": {
            "upright": ["Nurturing", "Practical", "Providing financially", "A working parent"],
            "reversed": ["Financial independence", "Self-care", "Work-home conflict", "Smothering"]
        },
        "description": "The Queen of Pentacles represents nurturing, practical, providing financially, and a working parent.",
        "image": "queen_of_pentacles.jpg"
    },
    {
        "id": 77,
        "name": "King of Pentacles",
        "element": "Earth",
        "keywords": ["financial success", "business leader", "security", "discipline"],
        "meanings": {
            "upright": ["Financial success", "Business leader", "Security", "Discipline"],
            "reversed": ["Financially inept", "Obsessed with wealth and status", "Bad business decisions", "Corruption"]
        },
        "description": "The King of Pentacles represents financial success, business leader, security, and discipline.",
        "image": "king_of_pentacles.jpg"
    }
]
