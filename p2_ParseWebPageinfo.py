# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *
# for regexp use
import re


url = raw_input('Enter - ')
#url = 'http://python-data.dr-chuck.net/comments_42.html'
#url ='http://python-data.dr-chuck.net/comments_361390.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags for span
tags = soup('span')
numsum = 0
numcount = 0
for tag in tags:
    # Look at the parts of a tag and extract number
    
    num = re.findall('[0-9.]+',str(tag))
    numsum += int(num[0])
    numcount += 1
    #print 'TAG:',tag, ' ', int(num[0]), 'Sum:', numsum, 'Count:', numcount
print 'Count ', numcount
print 'Sum ', numsum
    
    
    

   




    ##fhand = urllib.urlopen('http://www.dr-chuck.com/page1.htm')
##print (fhand.read().decode('utf-8'))
##for line in fhand:
##    print(line.decode('utf-8').strip())
    
#import urllib
#from BeautifulSoup import *
#from bs4 import BeautifulSoup


#url = 'http://aotscbus.ims.att.com:8080/Agent/index.htm'
#url = 'http://www.sme.sk'
#url = 'http://www.dr-chuck.com/page1.htm'
