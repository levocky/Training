import urllib
from BeautifulSoup import *
import re

#url ='http://python-data.dr-chuck.net/known_by_Asa.html'
url = 'http://skcbcdb01.emea.att.com/timetrack/?menu=group_view_teams&id=747'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('link')
for tag in tags:
    print tag.get('href', None)
