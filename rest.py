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

# レスポンスを表示する
print(response.status_code)
print(response.text)
