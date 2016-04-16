import requests



r = requests.post('http://localhost:8889/image', files={'capture.jpg': open('/Users/kirk/Documents/GoPiGo/GoKirkGo/capture.jpg', 'rb')})