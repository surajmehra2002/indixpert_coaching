

import requests

# response = requests.get("https://www.academy.indixpert.com/")
r = requests.get('https://httpbin.org/get')
print(r.headers['Content-Type'])
# print(response.text)
# print(response.ok)
# print(response.json)
# print(response.reason)
# print(type(response))

# webpage = response.content
# print(webpage)
# print(type(webpage))

# print(f"Error: {response.status_code}")




# r = requests.post('https://httpbin.org/post', data={'key':'value'})
# print(r.json()['form'])



# r = requests.head('https://httpbin.org/get')
# print(type(r.headers.get('Content-Length')))



# from requests import get
# url = 'https://httpbin.org/get'
# response = get(url)
# print(response.json()['url'])