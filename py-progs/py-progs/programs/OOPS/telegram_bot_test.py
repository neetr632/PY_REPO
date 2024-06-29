import telepot
from telepot.loop import MessageLoop
import instaloader

# Telegram bot token
TOKEN = '7082815494:AAGM2pzdNdf0N0zHDxT3uH9Ijwqi_3NoCak'

# Create Instaloader instance
L = instaloader.Instaloader()

# Function to handle incoming messages
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Received command: %s' % command)

    if command.startswith('/download_profile'):
        try:
            # Get the username from the command
            username = command.split(' ')[1]
            
            # Download the profile
            profile = instaloader.Profile.from_username(L.context, username)
            L.download_profile(profile.username, profile_pic=True)
            
            # Send a success message
            bot.sendMessage(chat_id, 'Profile downloaded successfully!')
        except IndexError:
            bot.sendMessage(chat_id, 'Please provide a username after the command.')
        except Exception as e:
            bot.sendMessage(chat_id, 'An error occurred: %s' % str(e))

# Create Telegram bot
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print('Bot is listening...')

# Keep the program running
while True:
    pass
