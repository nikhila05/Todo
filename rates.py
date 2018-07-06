import requests
a = requests.get('https://ratesapi.io/api/latest')
print (a.text)
