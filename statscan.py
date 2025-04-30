"""
This module queries the StatsCan API to retrieve monthly prices of food

"""

import requests
import xmltodict


query = "spaghetti bolognese"
api_url = 'https://www150.statcan.gc.ca/t1/wds/sdmx/statcan/rest/structure/Data_Structure_18100245'


response = requests.get(api_url)
if response.status_code == requests.codes.ok:
    temp = xmltodict.parse(response.text)['mes:Structure']['mes:Structures']
    print(temp['str:Dataflows']['str:Dataflow']['str:Structure']['Ref'].keys())
    print(temp['str:Codelists']['str:Codelist'])
else:
    print("Error:", response.status_code, response.text)
    
    

    
