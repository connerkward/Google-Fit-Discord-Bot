import time
import datetime
import requests
import json

# Default Info
# Date Range of Results
_START_DATE = 1577836800000000000
_END_DATE = 1585699200000000000
# Current Date
_CURR_DATE = datetime.date.today().strftime("%d/%m/%Y")
_CURR_TIME_NS = time.time_ns()
# Google Data
_DATA_SOURCE_ID = "derived:com.google.calories.expended:com.google.android.gms:merge_calories_expended"
_DATASET_ID = f"{_START_DATE}-{_END_DATE}"
# Google Access Token
_TOKEN = "ya29.a0Ae4lvC34Tel0ez6li8trnLxnYbTpvKg-5hQd8Z-XSc-wkzPQmf6WVVeS6gLntO5lThHJQmnp7seoYIUalOfLClljw6Nh" \
         "-c4FMo4IQRu4CzQ2YotlRUtXBVPkXorTYLBUpg66xooJsfxgK2lrsiQqMjxKSQbongcigng"

def google_request(access_token=_TOKEN, dataSourceId=_DATA_SOURCE_ID, datasetId=_DATASET_ID):
    """
    Google Request for certain Data Source over time
    :param access_token: From Google Oath2
    :param dataSourceId: Location and Name of 
    :param datasetId: in form f"{_START_DATE}-{_END_DATE}"
    :return: (not currently working sends form of list)
    """
    url = f'https://www.googleapis.com/fitness/v1/users/me/dataSources/{dataSourceId}/datasets/{datasetId}'
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {access_token}"}
    result = requests.get(url, headers=headers)

    print(result.url)
    db = json.loads(result.text)
    print(json.dumps(json.loads(result.text), indent=2))

    with open("date.txt", "w") as f:
        json.dump(json.dumps(json.loads(result.text), indent=1), f)
    above_1k = list()
    for i in range(0, len(db["point"])):
        if db["point"][i]["value"][0]["fpVal"] > 1000:
            above_1k.append(db["point"][i]["value"][0]["fpVal"])
    print(int(sum(above_1k)))

    return above_1k
