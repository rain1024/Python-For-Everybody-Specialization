import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'comments' not in js:
    print('==== Failure To Retrieve ====')
    print(data)

comments = js['comments']
total_sum = 0
count = 0
for item in comments:
    total_sum += int(item['count'])
    count += 1

print('Count:', count)
print('Sum:', total_sum)