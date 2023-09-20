import requests

url = 'http://httpbin.org/anything'
# localserver = 'http://127.0.0.1:8000/productapp/'
localserver = 'http://127.0.0.1:8000/deco/'

# status_Code = requests.get(url,json={"name":"Home"})
# print(status_Code.text)
# print(status_Code.json())
# print(status_Code.headers)
# print(status_Code.text)
# print(requests.api)
# print(requests.head)
# print(requests.Request)
# print(requests.session())
# response = requests.get(localserver, params={"abe": 1}, json={"message": 'Hello World'})
# print(response.json())
# print(response.text)
# print(response.json()['Json'])
# db model
# -------------------------------
# response = requests.get(localserver)
# print(response.text)
# print(response.headers)
# print(response.content)
# print(response.json())

res = requests.get(localserver)
print(res.json()['Hello'])
