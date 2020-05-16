import time
import datetime
import requests
import json

# Default Info
_START_DATE = 1577836800000000000
_END_DATE = 1585699200000000000
_CURR_DATE = datetime.date.today().strftime("%d/%m/%Y")
_CURR_TIME_NS = time.time_ns()
_DATA_SOURCE_ID = "derived:com.google.calories.expended:com.google.android.gms:merge_calories_expended"
_DATASET_ID = f"{_START_DATE}-{_END_DATE}"
_TOKEN = "ya29.a0Ae4lvC34Tel0ez6li8trnLxnYbTpvKg-5hQd8Z-XSc-wkzPQmf6WVVeS6gLntO5lThHJQmnp7seoYIUalOfLClljw6Nh" \
         "-c4FMo4IQRu4CzQ2YotlRUtXBVPkXorTYLBUpg66xooJsfxgK2lrsiQqMjxKSQbongcigng "

def google_request(access_token=_TOKEN, dataSourceId=_DATA_SOURCE_ID, datasetId=_DATASET_ID):
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
