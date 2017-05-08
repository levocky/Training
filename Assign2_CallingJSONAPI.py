import urllib
import json


serviceurl ='http://python-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location:')
    
    if len(address) < 1: break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})

    print('Retrieving', url)

    uh = urllib.urlopen(url)

    data = uh.read().decode()
    
    print 'Retrieved', len(data), 'characters'

    # Test if loaded propeerly 
    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue


    # PRINT
    #print '+++Pretty Print: +++'
    #print(json.dumps(js, indent=4))

    placeid = js["results"][0]["place_id"]
    print 'Place id ', placeid

    


