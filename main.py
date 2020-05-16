import discord

web_hook = "https://discordapp.com/api/webhooks/708841556571848725/zJoGnm5jKbS6y6WRf5xCUKB4fIo7v0L2VBzemRa6pGkoeBYwzLgd9IhQ75cUeqGkLC6q"
data = {"content":"Text"}
discord.discord_send(data=data, webhook_url=web_hook)


