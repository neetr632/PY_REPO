from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext

# Define the command handler for the /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! I am your friendly bot.')

# Define the message handler
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi')

def main() -> None:
    # Replace 'YOUR_BOT_TOKEN' with the actual token of your bot
    updater = Updater("6952409274:AAEI3166vQKM_V3--3_JU5tXV1mqkSNUf-c")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the command handler for the /start command
    dp.add_handler(CommandHandler("start", start))

    # Register the message handler
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop it
    updater.idle()

if __name__ == '__main__':
    main()
