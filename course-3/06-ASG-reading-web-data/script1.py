import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
print(type(fhand))
for line in fhand:
    print(line.decode().strip())