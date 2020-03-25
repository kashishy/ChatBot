# Create templates
bot_template = "BOT : {0}"
user_template = "USER : {0}"
from Chapter_1 import ChitChat


# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = ChitChat.respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))

# Send a message to the bot
send_message("hello")