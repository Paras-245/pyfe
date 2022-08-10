import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    sum = 0
    url = address
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')

    tree = ET.fromstring(data)
    counts = tree.findall('.//count')
    for count in counts:
        sum += int(count.text)
    print(sum)






