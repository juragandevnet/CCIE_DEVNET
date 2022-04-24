import requests
from login import logindna
import urllib3
from requests.auth import HTTPBasicAuth
urllib3.disable_warnings()

login = logindna()
token = login.get_token()
class devices_dna(object):
    def __init__ (self):
        self.DNA_IP = login.DNA_IP
        self.device_ip = '192.168.99.1'
        self.headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}
    def info(self):
        self.response = requests.request('GET','https://'+ self.DNA_IP +'/dna/intent/api/v1/network-device/ip-address/{}'.format(self.device_ip),headers=self.headers,verify=False)
        return self.response.json()['response']
    def count(self):
        self.response = requests.request('GET','https://'+ self.DNA_IP +'/dna/intent/api/v1/network-device/count', headers = self.headers, verify=False)
        return self.response.json()['response']
    def GetModuleInfoById(self):
        self.response = requests.request('GET','https://'+ self.DNA_IP +'/dna/intent/api/v1/network-device/module?id=30180634-6ea6-40f5-a354-c1980239a422', headers = self.headers, verify=False)
        return self.response.json()['response']
    def GetDeviceList(self):
        self.response = requests.request('GET','https://'+ self.DNA_IP +'/dna/intent/api/v1/network-device/', headers = self.headers, verify=False)
        return self.response.json()['response']
    def DeleteDeviceId(self):
        self.id = input ("Which id you want to remove: ")
        self.response = requests.request('DELETE','https://'+ self.DNA_IP +'/dna/intent/api/v1/network-device/'+ self.id +'?isForceDelete=TRUE', headers = self.headers, verify=False)
        print(self.response.text.encode('utf8'))

  
        
