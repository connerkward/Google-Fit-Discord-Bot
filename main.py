from http import client
import time
import datetime
import requests
import json

this_year_start_date = 1577836800000000000
winter_end_date = 1585699200000000000

curr_date = datetime.date.today().strftime("%d/%m/%Y")
curr_time_ns = time.time_ns()

print("curr", time.time_ns())
print(curr_date)
print(time.mktime(datetime.datetime.strptime(curr_date, "%d/%m/%Y").timetuple()))

dataSourceId = "derived:com.google.calories.expended:com.google.android.gms:merge_calories_expended"

datasetId = f"{this_year_start_date}-{winter_end_date}"

url = f'https://www.googleapis.com/fitness/v1/users/me/dataSources/{dataSourceId}/datasets/{datasetId}'



access_token = "ya29.a0Ae4lvC34Tel0ez6li8trnLxnYbTpvKg-5hQd8Z-XSc-wkzPQmf6WVVeS6gLntO5lThHJQmnp7seoYIUalOfLClljw6Nh-c4FMo4IQRu4CzQ2YotlRUtXBVPkXorTYLBUpg66xooJsfxgK2lrsiQqMjxKSQbongcigng"
headers = {"Content-Type": "application/json", "Authorization": f"Bearer {access_token}"}
result = requests.get(url, headers=headers)


print(result.url)
db = json.loads(result.text)
print (json.dumps(json.loads(result.text), indent=2))

with open("date.txt", "w") as f:
    json.dump(json.dumps(json.loads(result.text), indent=1), f)

above_1k = list()
for i in range(0, len(db["point"])):
    if db["point"][i]["value"][0]["fpVal"] > 1000:
        above_1k.append(db["point"][i]["value"][0]["fpVal"])
print(int(sum(above_1k)))

