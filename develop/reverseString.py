
import urllib.request,json
country_api="https://free.currencyconverterapi.com/api/v5/countries"

with urllib.request.urlopen(country_api) as country:
    data=json.loads(country.read().decode())
    for k,v in data.items():
        for k1,v1 in v.items():
            alpha3=v1['alpha3']
            currencyId=v1["currencyId"]
            currencyName=v1["currencyName"]
            currencySymbol=v1["currencySymbol"]
            id=v1[ "id"]
            name=v1["name"]

            print(alpha3,currencyId,currencyName,currencySymbol,id,name)
