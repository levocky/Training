import urllib
import xml.etree.ElementTree as ET

# Test data link
link1 ='http://python-data.dr-chuck.net/comments_42.xml'
# Actual data link
link2 = 'http://python-data.dr-chuck.net/comments_361387.xml'


#address = raw_input('Enter location: ')

url = link2

#url = address

if len(url) > 0 : 

    print 'Retrieving', url
    uh = urllib.urlopen(url)

    data = uh.read()
    print 'Retrieved',len(data),'characters'

    tree = ET.fromstring(data)
    results = tree.findall('comments/comment')

    print "Count: ", len(results)

    sumnum = 0
    for i in results:
        print i.find('name').text, i.find('count').text
        sumnum += int(float(i.find('count').text))
    print "Sum: ", sumnum


## -- USING //COUNT    
##    counts = tree.findall('.//count')
##    print "Counts = " , len(counts)

##    print list(counts)
   
##    numsum = sum(list(counts))
##    print numsum
##                 
    




