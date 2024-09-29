import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "helloworld/tim")
print(response.json())

data = [{"likes": 78, "name": "Tim", "views": 100000},
        {"likes": 5000, "name": "Joe", "views": 800000},
        {"likes": 100, "name": "Pia", "views": 600000}]

for i in range(len(data)):
    video_response = requests.put(BASE + "video/" + str(i), json=data[i])
    print(video_response.json())

input()
video_response = requests.get(BASE + "video/6")
print(video_response.json())