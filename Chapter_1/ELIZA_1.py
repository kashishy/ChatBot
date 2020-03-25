import random

# Create templates
bot_template = "BOT : {0}"
user_template = "USER : {0}"

responses = {
    "question": [
        "you tell me!",
        "I don't know :"
    ],
    "statement": [
        "how long have you felt this way?",
        "tell me more!",
        "oh wow!",
        "can you back that up?"
    ],
    "default": [
        "default message"
    ]
}
def respond(message):
    # Check for a question mark
    if message.endswith("?"):
        # Return a random question
        return random.choice(responses["question"])
    # Return a random statement
    return random.choice(responses["statement"])

def send_message(message):
    print(user_template.format(message))
    response = respond(message)
    print(bot_template.format(response))

# Send messages ending in a question mark
send_message("what's today's weather?")
send_message("what's today's weather?")

# Send messages which don't end with a question mark
send_message("I love building chatbots")
send_message("I love building chatbots")
