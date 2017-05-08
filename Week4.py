
import sys

if sys.version_info[0] == 3:
    #print ('Version is ' , sys.version_info[0])
    import urllib.request as urllib
else:
    import urlib


##fhand = urllib.urlopen('http://www.dr-chuck.com/page1.htm')
##print (fhand.read().decode('utf-8'))
##for line in fhand:
##    print(line.decode('utf-8').strip())
    
#import urllib
from BeautifulSoup import *
#from bs4 import BeautifulSoup


#url = 'http://aotscbus.ims.att.com:8080/Agent/index.htm'
#url = 'http://www.sme.sk'
url = 'http://www.dr-chuck.com/page1.htm'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')

tags = soup('a')

for tag in tags:
    print (tag.get('href',None))

