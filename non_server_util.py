import discord
import google
import datetime

"""
DEPRECATED, only for testing
"""

# Get Token From token.txt
with open("token.txt") as t:
    for line in t:
        TEMP_TOKEN = line

_CURR_DATE = datetime.datetime.today()
_CURR_DAY_START = _CURR_DATE.replace(hour=0, minute=0, second=0, microsecond=0) - datetime.timedelta(137)
_CURR_DAY_END = _CURR_DAY_START + datetime.timedelta(1)
print(_CURR_DAY_START)
print(_CURR_DAY_END)
_CURR_DAY_START_NS = int(_CURR_DAY_START.timestamp()) * 1000000000
_CURR_DAY_END_NS = int(_CURR_DAY_END.timestamp()) * 1000000000

#sourceid = "derived:com.google.calories.expended:com.google.android.gms:merge_calories_expended"
#sourceid ='derived:com.google.calories.expended:com.google.android.gms:from_activities'
sourceid = 'derived:com.google.calories.expended:com.google.android.gms:platform_calories_expended'

# Request Response from Google (Check google.py for more specific variables and data sources) # defaults to current day
g_response = google.request(access_token=TEMP_TOKEN, dataSourceId=sourceid, start=_CURR_DAY_START_NS, end=_CURR_DAY_END_NS)
print("cals:", int(g_response))
# Send to Discord
web_hook = "https://discordapp.com/api/webhooks/708841556571848725/zJoGnm5jKbS6y6WRf5xCUKB4fIo7v0L2VBzemRa6pGkoeBYwzLgd9IhQ75cUeqGkLC6q"
user = "Someone"
data = {"content":f"{user} has burnt {str(int(g_response))} calories today!"}
discord.send(data=data, webhook_url=web_hook)




