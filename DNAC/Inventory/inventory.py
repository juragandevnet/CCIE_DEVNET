import requests
import urllib3
from requests.auth import HTTPBasicAuth
from login import logindna
urllib3.disable_warnings()

login = logindna()
token = login.get_token()
class inventory_dna(object):
    def __init__ (self):
        self.DNA_IP = login.DNA_IP
        self.headers = {'X-Auth-Token': token, 'Content-Type': 'application/json', 'Accept': 'application/json'}
    def inventory_lists(self):
        self.response = requests.get('https://'+ self.DNA_IP +'/dna/intent/api/v1/network-device', headers = self.headers, verify=False)
        return self.response.json()['response']
    def inventory_remove(self):
        self.query_string_params = {'isForceDelete': 'true'}
        self.response = requests.request('DELETE', 'https://'+ self.DNA_IP +'/dna/intent/api/v1/network-device/2d8f8c10-f195-46bb-b00d-074482a02928',
        headers=self.headers,params=self.query_string_params ,verify=False)
        print (self.response.text.encode('utf8'))
