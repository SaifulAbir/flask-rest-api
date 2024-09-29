import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "helloworld/tim")
print(response.json())

video_response = requests.put(BASE + "video/1", {"likes": 10})
print(video_response.json())