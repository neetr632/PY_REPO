import webbrowser

# Open the Google homepage in a new tab in Google Chrome and hide it
webbrowser.open("https://www.google.com/", new=1)

# Wait for 1 second
import time
time.sleep(10)

# Raise the web browser window
webbrowser.get("https://www.google.com/").activate()
