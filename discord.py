import requests
import json

def send(data, webhook_url):
    """
    Used to send data to a discord webhook url
    :param data: dictionary of REST JSON. Key "contents" for message text
    :param webhook_url: url of discord webhook
    :return: None
    """
    dis_data = data
    url = webhook_url
    headers = {"Content-Type": "application/json"}
    discord_request = requests.post(url, data=json.dumps(dis_data), headers=headers)

    try:
        discord_request.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
       print("Payload delivered successfully, code {}.".format(discord_request.status_code))
