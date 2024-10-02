import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Your bot token
BOT_TOKEN = '7331405735:AAEsxpin1pSEeIqXNCFxOH5f3MF2VpLru2I'

# Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

# Handle /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Welcome message
    welcome_message = """Welcome to SKID 🐹
You are now the director of a crypto exchange. Which one? You choose. Tap the screen, collect coins, pump up your passive income, and develop your own income strategy. We’ll definitely appreciate your efforts once the token is listed (dates coming soon). Don't forget about your friends — bring them to the game and get even more coins together!"""

    # Create inline keyboard with two buttons: one for playing the game and one for subscribing
    markup = InlineKeyboardMarkup()

    # Play button
    web_app_url = "https://66fc60a893a391d089a2c19b--golden-cuchufli-362b4a.netlify.app/"
    play_button = InlineKeyboardButton("Play", web_app=WebAppInfo(url=web_app_url))
    
    # Subscribe button
    subscribe_button = InlineKeyboardButton("Subscribe to the Channel", url="https://t.me/successkidofficialsol")
    
    # Add both buttons to the markup
    markup.add(play_button)
    markup.add(subscribe_button)

    # Send the message with the buttons
    bot.send_message(message.chat.id, welcome_message, reply_markup=markup)

# Start the bot
bot.polling()
