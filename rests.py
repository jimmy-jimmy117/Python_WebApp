import requests
import json

# 送信するデータを定義する
data = {
    "name": "dummy",
    "age": 21,
    "friends": ["dummy1", "dummy2", "dummy3"],
    "is_man": False,
}

# POSTリクエストを送信する
url = "http://127.0.0.1:5000/try_rest"
headers = {"Content-Type": "application/json"}

response = requests.post(url, headers=headers, data=json.dumps(data))

# レスポンスのJSONデータを取得し、"friends"をループで出力する
if response.status_code == 200:
    response_json = response.json()
    if "friends" in response_json["response_json"]:
        print("Friends:")
        for friend in response_json["response_json"]["friends"]:
            print(friend)
    else:
        print("No friends data in the response.")
else:
    print(f"Error: {response.status_code}, {response.text}")
