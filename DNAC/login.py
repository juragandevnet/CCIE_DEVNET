import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import Timeout

class logindna(object):
    def __init__ (self):
        self.DNA_IP    = '10.66.49.201'
        self.username   = 'administrator'
        self.password   = 'C1scoalTEC@'
    def get_token(self):
        try:
            self.response = requests.request('POST','https://'+self.DNA_IP+'/dna/system/api/v1/auth/token',auth=HTTPBasicAuth(username=self.username,password=self.password),verify=False, timeout=3)
            return self.response.json()['Token']
        except Timeout:
            return "Check your Connection DNAC, Make sure you are able to access DNAC"

        
      
        