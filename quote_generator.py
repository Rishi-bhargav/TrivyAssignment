import random

def generate_quote():
    quotes = [
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "The way to get started is to quit talking and begin doing. - Walt Disney",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
        "If life were predictable it would cease to be life, and be without flavor. - Eleanor Roosevelt",
        "Life is what happens when you're busy making other plans. - John Lennon"
    ]
    return random.choice(quotes)

print("Random Quote Generator")
print("Here's your random quote:")
print(generate_quote())