import requests

import json
  
# Opening JSON file
f = open('./credentials.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
print(data)
  
# api-endpointhttp://192.168.1.505000/api/printer?history=true&limit=2?
URL = "http://"+data["URL"]+":"+data["port"]+"/api/printer?history=true&limit=2"
PARAMS={
    "host": data["URL"],
    "X-Api-Key":data["key"]
}


r = requests.get(url = URL, headers=PARAMS)
  
# extracting data in json format
loaded = r.json()
print("====-=-=")
print(r)
print("====")
print(loaded)
# Closing file
f.close()