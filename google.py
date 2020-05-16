import time
import datetime
import requests
import json

start_date = 1577836800000000000
end_date = 1585699200000000000
curr_date = datetime.date.today().strftime("%d/%m/%Y")
curr_time_ns = time.time_ns()

start_date = "asd"
end_date = "asd"
dsi = "derived:com.google.calories.expended:com.google.android.gms:merge_calories_expended"
dsid = f"{start_date}-{end_date}"
act = "ya29.a0Ae4lvC34Tel0ez6li8trnLxnYbTpvKg-5hQd8Z-XSc-wkzPQmf6WVVeS6gLntO5lThHJQmnp7seoYIUalOfLClljw6Nh-c4FMo4IQRu4CzQ2YotlRUtXBVPkXorTYLBUpg66xooJsfxgK2lrsiQqMjxKSQbongcigng"

def google_request(access_token=act, dataSourceId=dsi, datasetId=dsid):
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