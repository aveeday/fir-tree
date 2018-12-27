# https://gloss.ua/citynews/120111-Gde-v-Kieve-mozhno-budet-kupit-elku-spisok-adresov
# https://kyivcity.gov.ua/news/iz_15_grudnya_na_190_lokatsiyakh_mista_rozpochnetsya_prodazh_yalinok_iz_chipami_individualnimi_nomerami_ta_shtrikh-kodami_perelik_adres.html
# a=[]; $("[width|='321']").each(function(i,v) { if (i>0) { a.push({"addr": v.innerText}) } }); copy(a);

import requests
import json

errors = []

def getLatLon(addr):
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'address': addr, 'key':'AIzaSyCQcbKltB_-oSCwLj7zhKulNTCnjNNGZFY'}
    r = requests.get(url, params=params)
    results = r.json()['results']
    location = results[0]['geometry']['location']
    return location

def addLocation(item):
    try:
        item["location"] = getLatLon(item["addr"])
    except IndexError:
        errors.append(item)
    return item

with open('addrs.json') as f:
    data = json.load(f)

output = map(addLocation, data)

with open('data.json', 'w') as outfile:
    json.dump(output, outfile)

with open('errors.json', 'w') as outfile:
    json.dump(errors, outfile)
