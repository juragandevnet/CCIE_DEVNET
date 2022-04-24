import requests
import urllib3
from requests.auth import HTTPBasicAuth
from login import logindna
urllib3.disable_warnings()

login = logindna()
token = login.get_token()

class NetworkSettings_DNA(object):
    def __init__ (self):
        self.DNA_IP = login.DNA_IP
        self.headers = {'X-Auth-Token': token, 'Content-Type': 'application/json', 'Accept': 'application/json'}
    def Pools_Lists(self):
        self.query_string_params = {'id':'a88777c3-080d-4e2e-90c0-6cc1a60d033f'}
        self.response = requests.request('GET','https://'+ self.DNA_IP +'/dna/intent/api/v1/global-pool/', headers =self.headers,params=self.query_string_params,verify=False)
        return self.response.json()
    def DeviceCredential_Lists(self):
        self.response = requests.request('GET','https://'+ self.DNA_IP +'/dna/intent/api/v1/device-credential', headers =self.headers,verify=False)
        return self.response.json()
    def CreateDeviceCredentials(self):
        self.payload = '''{
            "settings": {
                "cliCredential": [
                    {
                        "description": "THEBOGOR",
                        "username": "THEBOGOR",
                        "password": "THEBOGOR",
                        "enablePassword": "THEBOGOR"
                    }
                ],
                "snmpV2cRead": [
                    {
                        "description": "THEBOGOR",
                        "readCommunity": "THEBOGOR"
                    }
                ],
                "snmpV2cWrite":[
                    {
                        "desripction": "THEBOGOR",
                        "writecommunity": "THEBOGOR"
                    }
                ],
                "snmpV3":[
                    {
                        "description": "THEBOGOR",
                        "username": "THEBOGOR",
                        "privacyType": "AES128",
                        "privacyPassword": "THEBOGOR",
                        "authType": "SHA"
                        "authPassword": "THEBOGOR"
                        "snmpMode": "AUTHPRIV"
                    }
                ],
                "httpsRead":[
                    {
                        "name": "THEBOGOR",
                        "username": "THEBOGOR",
                        "password": "THEBOGOR",
                        "port": 0
                    }
                ],
                "httpsWrite":[
                    {
                        "name": "THEBOGOR",
                        "username": "THEBOGOR",
                        "password": "THEBOGOR",
                        "port": 0
                    }
                ]
            }
        }'''
        self.response = requests.request('POST','https://'+ self.DNA_IP +'/dna/intent/api/v1/device-credential/', headers =self.headers, data =self.payload, verify=False)
        return self.response.json()
    def RemoveDevieCredentials(self):
        self.id = input("Which Discovery ID you want to remove: ")
        self.response = requests.request ('DELETE','https://'+ self.DNA_IP +'/dna/intent/api/v1/device-credential/'+ self.id, headers = self.headers,verify=False)
        return self.response.json()
    def RemoveAllDeviceCredentials(self):
        self.response = requests.request ('DELETE','https://'+ self.DNA_IP +'/dna/intent/api/v1/device-credential/', headers = self.headers,verify=False)
        return self.response.json()
    def UpdateDeviceCredentials(self):
        self.payload = '''{
            "settings": {
                "cliCredential": [
                    {
                        "description": "THEBOGOR",
                        "username": "THEBOGOR",
                        "password": "THEBOGOR",
                        "enablePassword": "THEBOGOR",
                        "id": "7d03121d-d9ba-451d-be61-efde140a342e"
                    }
                ]
            }
        }'''
        self.response = requests.request('PUT','https://'+ self.DNA_IP +'/dna/intent/api/v1/device-credential/', headers =self.headers, data =self.payload,verify=False)
        return self.response.json()
   