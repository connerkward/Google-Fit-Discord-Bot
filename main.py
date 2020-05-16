import discord
import google

# Get Token From token.txt
with open("token.txt") as t:
    for line in t:
        TEMP_TOKEN = line

# Request Response from Google (Check google.py for more specific variables and data sources)
g_response = google.google_request(access_token=TEMP_TOKEN)

# Send to Discord
web_hook = "https://discordapp.com/api/webhooks/708841556571848725/zJoGnm5jKbS6y6WRf5xCUKB4fIo7v0L2VBzemRa6pGkoeBYwzLgd9IhQ75cUeqGkLC6q"
data = {"content":f"{str(g_response)}"}
discord.discord_send(data=data, webhook_url=web_hook)




