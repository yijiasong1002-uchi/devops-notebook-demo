import requests

url = "https://5e6e-128-135-204-91.ngrok-free.app/"

res = requests.get(url)
print("Response from server:", res.json())