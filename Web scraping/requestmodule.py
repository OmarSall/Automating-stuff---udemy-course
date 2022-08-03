import requests

res = requests.get('http://automatetheboringstuff.com/')

res.status_code

print(res.text[:500])

playFile = open('RomeoAndJuliet.txt', 'wb')

for chunk in res.iter_content(100000):
    playFile.write(chunk)