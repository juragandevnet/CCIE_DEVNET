import requests
import urllib3
from requests.auth import HTTPBasicAuth
from login import logindna
urllib3.disable_warnings()

login = logindna()
token = login.get_token()
class SDAFabric_DNA(object):
    def __init__ (self):
        self.DNA_IP = login.DNA_IP
        self.headers = {'X-Auth-Token': token, 'Content-Type': 'application/json', 'Accept': 'application/json'}
    def GetFabricInfo(self): 
        self.query_string_params = {'fabricName': 'SDA_Fabric'}
        self.response = requests.request('GET','https://'+self.DNA_IP+'/dna/intent/api/v1/business/sda/fabric', headers = self.headers,params=self.query_string_params, verify=False)
        return self.response.json()
    def GetDeviceFabricInfo(self): 
        #self.query_string_params = {''}
        self.response = requests.request('GET','https://'+self.DNA_IP+'/dna/intent/api/v1/business/sda/device', headers = self.headers, verify=False)
        return self.response.json()
    def fabric_count(self):
        self.response = requests.request('GET','https://'+self.DNA_IP+'/dna/intent/api/v1/business/sda/fabric/count', headers = self.headers,verify=False)
        return self.response.json()
    def fabric_site(self):
        self.query_string_params= {'id': ''}
        self.response = requests.request('GET','https://'+self.DNA_IP+'/dna/intent/api/v1/business/sda/fabric-site', headers = self.headers,params=self.query_string_params,verify=False)
        return self.response.json()['response']

 