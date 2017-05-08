import urllib
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location, for example "Ann Arbor, MI:')
    # address = "Ann Arbor, MI"

    if len(address) < 1: break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})

    print('Retrieving', url)

    uh = urllib.urlopen(url)

    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

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
    print '+++Pretty Print: +++'
    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
