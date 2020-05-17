import time
import datetime
import requests
import json

# Default Info
# Default Date Range of Results
_CURR_DATE = datetime.datetime.today()
_CURR_DAY_START = _CURR_DATE.replace(hour=0, minute=0, second=0, microsecond=0)
_CURR_DAY_END = _CURR_DAY_START + datetime.timedelta(1)
_CURR_DAY_START_NS = int(_CURR_DAY_START.timestamp()) * 1000000000
_CURR_DAY_END_NS = int(_CURR_DAY_END.timestamp()) * 1000000000
# Default Google Data Location
_DATA_SOURCE_ID = "derived:com.google.calories.expended:com.google.android.gms:merge_calories_expended"


def request(access_token, dataSourceId=_DATA_SOURCE_ID, start=_CURR_DAY_START_NS,end=_CURR_DAY_END_NS,sources=False):
    """
    Google Request for certain Data Source over time
    :param access_token: From Google Oath2
    :param dataSourceId: Location and Name of
    :param datasetId: in form f"{_START_DATE}-{_END_DATE}"
    :return: Float of estimated calories burned, working for input activities, unclear about step generated
    """
    # Format date range string
    datasetId = f"{start}-{end}"
    print(datasetId)
    url = f'https://www.googleapis.com/fitness/v1/users/me/dataSources/{dataSourceId}/datasets/{datasetId}'
    if sources:
        url = "https://www.googleapis.com/fitness/v1/users/me/dataSources"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {access_token}"}
    result = requests.get(url, headers=headers)

    print(result.url)
    db = json.loads(result.text)
    print(json.dumps(json.loads(result.text), indent=2))

    #with open("date.txt", "w") as f:
    #    json.dump(json.dumps(json.loads(result.text), indent=1), f)
    #print(db)
    above_1k = list()
    for i in range(0, len(db["point"])):
        #print(int(db["point"][i]["startTimeNanos"])/1000000000)
        this = int(db["point"][i]["startTimeNanos"])/1000000000
        #if this in range(int(int(start)/1000000000), int(int(end)/1000000000)) and int(db["point"][i]["value"][0]["fpVal"]) > 50:
            #print(this)
        above_1k.append(db["point"][i]["value"][0]["fpVal"])
            #print(above_1k)
    print(int(sum(above_1k)))
    return sum(above_1k)
