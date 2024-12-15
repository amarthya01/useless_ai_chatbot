import random

# List of silly responses
responses = [
    "I'm thinking... still thinking... never mind.",
    "It’s top secret. So secret, I don’t even know.",
    "My circuits suggest yes. Or no. Probably.",
    "Try turning around three times and asking again.",
    "Error 404: Answer not found.",
    "Ask yourself: is the question really worth it?",
    "The universe says, 'Nah, not today.'",
    "I'm not lazy; I just prefer not to answer.",
]

sarcastic_responses = [
    "Oh, sure. That’s a totally reasonable question.",
    "Why don’t you Google it?",
    "Wow, so original. Never heard that one before.",
]

positive_responses = [
    "You’re doing great! Keep asking questions!",
    "I’m here for you, even if I don’t know the answer.",
    "That’s a wonderful question!",
]

def get_response(mode='random'):
    if mode == 'sarcastic':
        return random.choice(sarcastic_responses)
    elif mode == 'positive':
        return random.choice(positive_responses)
    else:
        return random.choice(responses)

# Function to get a random response
def get_response():
    return random.choice(responses)
