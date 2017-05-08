import urllib
import json


adr = input('Enter url:')

# test data
#adr = " http://python-data.dr-chuck.net/comments_42.json"
# Actual data
#adr = "http://python-data.dr-chuck.net/comments_361391.json"

uh = urllib.urlopen(adr)
info = uh.read()

info = json.loads(str(info))

print 'Count:', len(info['comments'])

sumnum = 0
for item in info['comments']:
    print 'Name:', item['name'], ', Count:', item['count']
    sumnum +=  int(float(item['count']))

print 'Sum:', sumnum
