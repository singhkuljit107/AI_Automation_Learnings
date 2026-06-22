# Refreshing the requests library
import requests

# request get() method
r = requests.get('https://api.github.com/events')

# request post() method
r = requests.post('https://httpbin.org/post', data={'name': 'kuljit singh'})
data = r.json()
# print(data['form'])

# request delete() method

r = requests.delete('https://httpbin.org/delete')
# print(r.status_code)

# Passing Parameters In URLs
payload = {'Role': 'batsman', 'Order': 'opener'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)
