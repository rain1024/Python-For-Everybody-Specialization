import urllib.request, urllib.parse, urllib.error

url = "https://www.google.com/robots.txt"

fhand = urllib.request.urlopen(url)
for line in fhand:
    print(line.decode().strip())