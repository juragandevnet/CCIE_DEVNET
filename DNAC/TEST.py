#import getpass
#import json
#import pandas as pd
#import math
#import requests
#from discovery import discovery_dna
#from prettytable import PrettyTable
#discovery = discovery_dna()


#discovery.TEST()
#discovery.GenerateDiscoveryReport()

#if discovery.GetNetworkDevicesInfo(2786)[0]['hostname'] in response:
 #   print("Modol")
#else:
 #   print("Apaan Lw")
#print (discovery.GetNetworkDevicesInfo(2786)[0]['hostname'])

#print (json.dumps(discovery.GetNetworkDevicesInfo(2786),indent=2))

#discovery.GenerateDiscoveryReport()


#print (discovery.discovery_lists()['response'][0]['globalCredentialIdList'][0])
#print (discovery.GetGlobalCredentials(8)[0]['id'])



#print (json.dumps(discovery.discovery_lists(),indent=2))
#print (json.dumps(discovery.GetGlobalCredentials(8),indent=2))



'''reader = pd.read_excel(r'C:/Users/'+ getpass.getuser() +'/Desktop/AUTOBOTS/NewDiscovery.xlsx')

i=0
for item in reader['netconfPort']:
    text = reader['netconfPort'][i]
    if math.isnan(text):
        print ("Kosong")
    else:
        print ("Ada")
    i+=1


theglobal =  { "Global": 
       text
}
cisco = theglobal
themodol = json.dumps(cisco)
ciscoodoy = json.loads(themodol)
print (ciscoodoy)
'''

from typing import ItemsView
from Discovery.discovery_page import *
from Discovery.discovery_class import *
from network_settings import *
from login import logindna
import requests
import xlsxwriter

token = logindna().get_token()
DNA_IP = logindna().DNA_IP
headers = {
    'X-Auth-Token': token,
    'Content-Type': 'application/json',
    'Accpet': 'application/json'
}

#print(logindna().get_token())
#print(discovery_page())

#print(discovery_dna().AddNewDiscovery())

print(discovery_dna().CreateForm())





'''
TEST = ["1","2","3"]
x = "".join(TEST)
print(x)
'''



#print(r'C:\\Users\\hawijaya\\OneDrive - Cisco\\DATA\\02.Python Lab\\0.github\\CCIE_DEVNET\\DNAC\\Discovery\\Discovery_report.xlsx')


'''
httpread_data = []
for HttpReadCredential in NetworkSettings_DNA().DeviceCredential_Lists()['http_read']:
    httpread_data.append(HttpReadCredential['username'])

print(httpread_data)
'''

id = 296

response = requests.request('GET','https://'+ DNA_IP +f'/dna/intent/api/v1/discovery/{id}/network-device/1/10', headers = headers,verify=False)
networkdevice = response.json()

response = requests.request('GET','https://'+ DNA_IP +'/dna/intent/api/v1/device-credential/', headers = headers,verify=False)
device = response.json()

response = requests.request('GET','https://'+ DNA_IP +'/dna/intent/api/v1/discovery/', headers = headers,verify=False)
discovery = response.json()

'''
for discovery_item in discovery['response']:
    response = requests.request('GET','https://'+ DNA_IP +f"/dna/intent/api/v1/discovery/{discovery_item['id']}/network-device/1/100", headers = headers,verify=False)
    networkdevice = response.json()
    hostname = []
    for networkdevice_item in networkdevice['response']:
        if 'hostname' in networkdevice_item:
            hostname.append(networkdevice_item['hostname'])
    print(hostname)
'''


'''
for discovery_item in discovery['response']:
    x=0
    test = []
    for globalCredentialIdList in discovery_item['globalCredentialIdList']:
        for device_item in device['snmp_v2_read']:
            if globalCredentialIdList == device_item['id']:
                #print("KETEMU", discovery_item['id'],test)
                test.append(device_item['description'])
                print(test)  
    x+=1
'''      