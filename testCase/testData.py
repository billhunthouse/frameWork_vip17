import requests
from requests.auth import HTTPBasicAuth
import json

url = 'https://api.privy.id/Privypassv2/userdemoverificationsync.json'
authValue = {"username":"welab","password":"r[BcgS4Uyk5[K3&"}
value = {
 "trId": "368",
 "nik": "3174051810760002",
 "name": "EKO NURMANSJAH JAYASUDIRJA",
 "dob": "18-10-1976",
 "pob": "JAKARTA"
}

re = requests.post(url,json=value,auth=(authValue['username'],authValue['password']))
js = re.json()
print(js)