import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "helloworld/tim")
print(response.json())

video_response = requests.put(BASE + "video/1", json={"likes": 10, "name": "Tim", "views": 100000})
print(video_response.json())

input()

video_response = requests.get(BASE + "video/1")
print(video_response.json())