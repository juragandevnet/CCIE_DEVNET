import sys
sys.path.append('../DNAC')
import math
import requests
import json
import urllib3
import xlsxwriter
from login import logindna
from network_settings import NetworkSettings_DNA
from prettytable import PrettyTable
from functions import ExcelWriter
urllib3.disable_warnings()

class discovery_dna(object):
    def __init__(self):
        self.token = logindna().get_token()
        self.DNA_IP = logindna().DNA_IP
        self.headers = {
                            'X-Auth-Token': self.token,
                            'Content-Type': 'application/json',
                            'Accpet': 'application/json'
        }
    def discovery_table(self):
        self.table = PrettyTable(["Name", "IP Address Range", "Preferred Mgmt Method","Discovery Status","Discovery Condition","Id"])
        for self.item in self.discovery_lists()['response']:
            self.table.add_row([self.item['name'], self.item['ipAddressList'], self.item['preferredMgmtIPMethod'], self.item['discoveryStatus'], self.item['discoveryCondition'], self.item['id']])
        print(self.table)
    def discovery_lists(self):
        self.response = requests.request('GET','https://'+ self.DNA_IP +'/dna/intent/api/v1/discovery/', headers = self.headers, verify=False)
        return self.response.json()
    def findIdDiscovery(self):
        self.loop_FID = True
        try:
            self.name = input("Input Discovery Name to run discovery: ")
            self.response = requests.request('GET','https://'+ self.DNA_IP +"/dna/intent/api/v1/discovery/", headers = self.headers,verify=False)
            x=0
            while self.loop_FID:
                if self.response.json()['response'][x]['name']== self.name:
                    self.ipAddressList = self.response.json()['response'][x]['ipAddressList']
                    self.id = self.response.json()['response'][x]['id']
                    self.RunDiscovery(self.id,self.ipAddressList)
                    self.loop_FID=False
                    break
                elif self.name == "ALL":
                    for self.elements in self.response.json()['response']:
                        self.RunDiscovery(self.response.json()['response'][x]['id'],self.response.json()['response'][x]['ipAddressList'])
                        print ("Sukses 1")
                    self.loop_FID=False
                    break
                else:
                    pass
                x+=1
        except:
            pass
    def RunDiscovery(self,id,ipAddressList):
        self.id = id
        self.ipAddressList = ipAddressList
        self.payload = {
                    "ipAddressList": self.ipAddressList,
                    "id": self.id,
                    "discoveryCondition": "Queued",
                    "discoveryStatus": "Active"
        }
        self.response = requests.request('PUT','https://'+ self.DNA_IP +"/dna/intent/api/v1/discovery/", headers = self.headers,data=json.dumps(self.payload),verify=False)
    def findIdRemove(self):
        x=0
        self.name = input ("Input the discovery Name to remove discovery job: ")
        self.response = requests.request('GET','https://'+ self.DNA_IP +"/dna/intent/api/v1/discovery/", headers = self.headers,verify=False)
        for self.item in self.response.json()['response']:
            if self.response.json()['response'][x]['name'] == self.name:
                self.ipAddressList = self.response.json()['response'][x]['ipAddressList']
                self.id = self.response.json()['response'][x]['id']
                self.remove()
            elif self.name == "ALL":
                self.removeall()
                break
            elif self.response.json()['response']=="":
                print ("NOT FOUND")
                break
            x+=1
    def remove(self):
        self.payload = {
            "id": self.id
        }
        self.response = requests.request ('DELETE','https://'+ self.DNA_IP +'/dna/intent/api/v1/discovery/'+self.id, headers = self.headers, data = json.dumps(self.payload),verify=False)
        return self.response.json()
    def removeall(self):
        self.response = requests.request ('DELETE','https://'+ self.DNA_IP +'/dna/intent/api/v1/discovery/', headers = self.headers,verify=False)
        return self.response.json()
    def CreateForm(self):
        self.df = (
            {
                "no": [],
                "cdpLevel": [],
                "discoveryType": [],
                "enablePasswordList": [],
                "globalCredentialIdList": [],
                "httpReadCredential": [],
                "httpWriteCredential": [],
                "ipAddressList": [],
                "ipFilterList": [],
                "lldpLevel": [],
                "name": [],
                "netconfPort": [],
                "noAddNewDevice": [],
                "parentDiscoveryId": [],
                "passwordList": [],
                "preferredMgmtIPMethod": [],
                "protocolOrder": [],
                "reDiscovery": [],
                "retry": [],
                "snmpAuthPassphrase": [],
                "snmpAuthProtocol": [],
                "snmpMode": [],
                "snmpPrivPassphrase": [],
                "snmpPrivProtocol": [],
                "snmpROCommunityDesc": [],
                "snmpRWCommunityDesc": [],
                "snmpUserName": [],
                "snmpVersion": [],
                "timeout": [],
                "updateMgmtIp": [],
                "userNameList": []
            }
        )
        self.workbook = xlsxwriter.Workbook(f'{sys.path[0]}\Discovery\\NewDiscovery.xlsx')
        self.worksheet = self.workbook.add_worksheet('NewDiscovery')
        self.bold = self.workbook.add_format({'bold': True})
        num_column = 0
        for item in self.df:
            self.worksheet.write(0, num_column, item, self.bold)
            num_column+=1
        # FOR CDP LEVEL
        self.worksheet.data_validation('B2:B100',{'validate':'list','value': ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']})
        # FOR CDP TYPE
        self.worksheet.data_validation('C2:C100',{'validate':'list','value': ['CDP','Range','LLDP']})
        # FOR HTTP READ 
        httpread_data = []
        for HttpReadCredential in NetworkSettings_DNA().DeviceCredential_Lists()["http_read"]:
            httpread_data.append(HttpReadCredential['username'])
        self.worksheet.data_validation('F2:F100',{'validate':'list','value': httpread_data})
        # FOR HTTP WRITE
        httpwrite_data = []
        for HttpWriteCredential in NetworkSettings_DNA().DeviceCredential_Lists()["http_write"]:
            httpwrite_data.append(HttpWriteCredential['username'])
        self.worksheet.data_validation('G2:G100',{'validate':'list','value': httpwrite_data})
        # FOR LLDP LEVEL
        self.worksheet.data_validation('J2:J100',{'validate':'list','value': ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']})
        # FOR SNMPv2 READ
        SNMPv2_Desc = []
        for SnmpV2_ReadCredential in NetworkSettings_DNA().DeviceCredential_Lists()["snmp_v2_read"]:
            SNMPv2_Desc.append(SnmpV2_ReadCredential['description'])
        self.worksheet.data_validation('Y2:Y100',{'validate':'list','value': SNMPv2_Desc})
        # FOR SNMPv2 WRITE
        SNMPv2_DescWrite = []
        for SnmpV2_WriteCredential in NetworkSettings_DNA().DeviceCredential_Lists()["snmp_v2_write"]:
            SNMPv2_DescWrite.append(SnmpV2_WriteCredential['description'])
        self.worksheet.data_validation('Z2:Z100',{'validate':'list','value': SNMPv2_DescWrite})

        print ("Excel Form has been successfully created")
        i=0
        for Columns in self.df:
            if 'no' in Columns:
                self.worksheet.set_column(i, i , int(len(str(Columns))))
            else:
                self.worksheet.set_column(i, i , int(len(str(Columns)) + 10))
            i+=1
        self.workbook.close()
    def GenerateDiscoveryReport(self):
        ###API Call###
        self.response = requests.request('GET','https://'+ self.DNA_IP +'/dna/intent/api/v1/discovery/', headers = self.headers,verify=False)
        self.discovery = self.response.json()
        self.responsedevice = requests.request('GET','https://'+ self.DNA_IP +'/dna/intent/api/v1/device-credential/', headers = self.headers,verify=False)
        self.device = self.responsedevice.json()
        ###Define Column###
        self.df =(
            {
                'No': [],
                'Id': [],
                'Name': [],
                'DiscoveryType': [],
                'IpAddressList': [],
                'PreferredMgmtIPMethod': [],
                'CLICredentials': [],
                'Snmpv2cRead': [],
                'Snmpv2cWrite': [],
                'Snmpv3': [],
                'HttpReadCredentials' : [],
                'HttpWriteCredentials' : [],
                'CdpLevel': [],
                'LldpLevel': [],
                'ProtocolOrder': [],
                'TimeOut':[],
                'RetryCount': [],
                'DiscoveryCondition': [],
                'MgmtIpAddress': [],
                'Hostname': [],
                'Icmp': [],
                'Snmp': [],
                'Cli': [],
                'Netconf':[]
            }
        )
        self.workbook = xlsxwriter.Workbook(f'{sys.path[0]}\Discovery\Discovery_Report.xlsx')
        self.worksheet = self.workbook.add_worksheet('Discovery_Report')
        self.cell_format = self.workbook.add_format()
        self.bold = self.workbook.add_format({'bold': True})
        self.cell_format.set_text_wrap()
        ### Make Bold of Column Name###
        num_column = 0
        for item in self.df:
            self.worksheet.write(0, num_column, item, self.bold)
            num_column+=1
        ###Write Items to Excel Form###
        for row_num, self.reports in enumerate(self.discovery['response']):
            response = requests.request('GET','https://'+ self.DNA_IP +f"/dna/intent/api/v1/discovery/{self.reports['id']}/network-device/1/100", headers = self.headers,verify=False)
            networkdevice = response.json()
            self.worksheet.write(row_num+1, 0, row_num+1)
            self.worksheet.write(row_num+1, 1, self.reports['id'])
            self.worksheet.write(row_num+1, 2, self.reports['name'])
            self.worksheet.write(row_num+1, 3, self.reports['discoveryType'])
            self.worksheet.write(row_num+1, 4, self.reports['ipAddressList'])
            self.worksheet.write(row_num+1, 5, self.reports['preferredMgmtIPMethod'])
            # THIS IS FOR CLI ONLY
            self.cli = []
            for self.globalCredentialIdList in self.reports['globalCredentialIdList']:
                for self.device_item in self.device['cli']:
                    if self.globalCredentialIdList == self.device_item['id']:
                        self.cli.append(self.device_item['username'])
            self.worksheet.write(row_num+1, 6, f'{ExcelWriter(self.cli)}', self.cell_format)
            # THIS IS FOR SNMPv2 Only
            self.snmpv2 = []
            for self.globalCredentialIdList in self.reports['globalCredentialIdList']:
                for self.device_item in self.device['snmp_v2_read']:
                    if self.globalCredentialIdList == self.device_item['id']:
                        self.snmpv2.append(self.device_item['description'])
            self.worksheet.write(row_num+1, 7, f'{ExcelWriter(self.snmpv2)}', self.cell_format)
            # THIS IS FOR SNMPv2 Write Only
            self.snmpv2Write = []
            for self.globalCredentialIdList in self.reports['globalCredentialIdList']:
                for self.device_item in self.device['snmp_v2_write']:
                    if self.globalCredentialIdList == self.device_item['id']:
                        self.snmpv2Write.append(self.device_item['description'])
            self.worksheet.write(row_num+1, 8, f'{ExcelWriter(self.snmpv2Write)}', self.cell_format)
            # THIS IS FOR SNMPV3 Only
            self.snmpv3 = []
            for self.globalCredentialIdList in self.reports['globalCredentialIdList']:
                for self.device_item in self.device['snmp_v3']:
                    if self.globalCredentialIdList == self.device_item['id']:
                        self.snmpv3.append(self.device_item['description'])
            self.worksheet.write(row_num+1, 9, f'{ExcelWriter(self.snmpv3)}', self.cell_format)
            # THIS IS FOR HTTP_READ Only
            self.HttpRead = []
            for self.globalCredentialIdList in self.reports['globalCredentialIdList']:
                for self.device_item in self.device['http_read']:
                    if self.globalCredentialIdList == self.device_item['id']:
                        self.HttpRead.append(self.device_item['username'])
            self.worksheet.write(row_num+1, 10, f'{ExcelWriter(self.HttpRead)}', self.cell_format)
            # THIS IS FOR HTTP_WRITE Only
            self.HttpWrite = []
            for self.globalCredentialIdList in self.reports['globalCredentialIdList']:
                for self.device_item in self.device['http_write']:
                    if self.globalCredentialIdList == self.device_item['id']:
                        self.HttpRead.append(self.device_item['username'])
            self.worksheet.write(row_num+1, 11, f'{ExcelWriter(self.HttpRead)}', self.cell_format)
            if 'cdpLevel' in self.reports:
                self.worksheet.write(row_num+1, 12, self.reports['cdpLevel'])
            if 'lldpLevel' in self.reports:
                self.worksheet.write(row_num+1, 13, self.reports['lldpLevel'])
            self.worksheet.write(row_num+1, 14, self.reports['protocolOrder'])
            self.worksheet.write(row_num+1, 15, self.reports['timeOut'])
            self.worksheet.write(row_num+1, 16, self.reports['retryCount'])
            self.worksheet.write(row_num+1, 17, self.reports['discoveryCondition'])
            # THIS IS FOR IPMgmt Inside Discovery ID
            MgmtIP = []
            for networkdevice_item in networkdevice['response']:
                if 'managementIpAddress' in networkdevice_item:
                    MgmtIP.append(networkdevice_item['managementIpAddress'])  
            self.worksheet.write(row_num+1, 18, f'{ExcelWriter(MgmtIP)}', self.cell_format)
            # THIS IS FOR hostname inside discovery ID
            hostname = []
            for networkdevice_item in networkdevice['response']:
                if 'hostname' in networkdevice_item:
                    hostname.append(networkdevice_item['hostname'])        
            self.worksheet.write(row_num+1, 19, f'{ExcelWriter(hostname)}', self.cell_format)
            # THIS IS FOR ICMP status inside discovery ID
            IcmpStatus = []
            for networkdevice_item in networkdevice['response']:
                if 'pingStatus' in networkdevice_item:
                    IcmpStatus.append(networkdevice_item['pingStatus']) 
            self.worksheet.write(row_num+1, 20, f'{ExcelWriter(IcmpStatus)}', self.cell_format)
            # THIS IS FOR SNMP status inside discovery ID
            snmpStatus = []
            for networkdevice_item in networkdevice['response']:
                if 'snmpStatus' in networkdevice_item:
                    snmpStatus.append(networkdevice_item['snmpStatus']) 
            self.worksheet.write(row_num+1, 21, f'{ExcelWriter(snmpStatus)}', self.cell_format)
            # THIS IS FOR CLI status inside discovery ID
            cliStatus = []
            for networkdevice_item in networkdevice['response']:
                if 'cliStatus' in networkdevice_item:
                    cliStatus.append(networkdevice_item['cliStatus']) 
            self.worksheet.write(row_num+1, 22, f'{ExcelWriter(cliStatus)}', self.cell_format)
            # THIS IS FOR NETCONF status inside discovery ID
            netconfStatus = []
            for networkdevice_item in networkdevice['response']:
                if 'netconfStatus' in networkdevice_item:
                    netconfStatus.append(networkdevice_item['netconfStatus']) 
            self.worksheet.write(row_num+1, 23, f'{ExcelWriter(netconfStatus)}', self.cell_format)
        print ("Discovery Report has been created!")
        i=0
        for Columns in self.df:
            if 'No' in Columns:
                self.worksheet.set_column(i, i , int(len(str(Columns))))
            else:
                self.worksheet.set_column(i, i , int(len(str(Columns)) + 10))
            i+=1
        self.workbook.close()
    def AddNewDiscovery(self):
        while True:
            self.discovery_table()
            print ("\nWELCOME TO AUTOBOTS BY SILUMAN NETWORKS \n1.Create Discovery Form\n2.Add New Discovery Form\n3.Remove Discovery\n4.Generate Discovery Report\n5.exit")
            try:
                self.select = int(input("Select:"))
                if self.select == 1:
                    self.CreateForm()
                elif self.select == 2:
                    self.SubmitDiscoveryForm()
                elif self.select == 3:
                    self.findIdRemove()
                elif self.select == 4:
                    self.GenerateDiscoveryReport()
                elif self.select == 5:
                    break
                else:
                    pass
            except:
                print ("Please input number only")   
    def CLICredentialsPage(self):
        self.loop_CCP = True
        while self.loop_CCP:
            print("WELCOME TO AUTOBOTS BY SILUMAN NETWORKS\n1.CLI Info\n2.Create CLI Credentials Form\n3.Create Cli Credentials\n4.Update CLI Credentials\n6.Remove CLI Credentials\n7.exit")
            try:
                self.select = int(input("Select:"))
                if self.select == 1:
                    self. items = self.GetGlobalCredentials(4)
                    self.table = PrettyTable(["Name","Username","Id","Comments"])
                    y=0
                    for self.item in self.items:
                        self.table.add_row([self.items[y]['description'],self.items[y]['username'],self.items[y]['id'],self.items[y]['comments']])
                        y+=1
                    print (self.table)
                elif self.select == 7:
                    self.loop_CCP = False
                else:
                    pass
            except:
                print ("Please input number only")
    def GetNetworkDevicesInfo(self,id):
        self.id=id
        self.response = requests.request('GET','https://'+ self.DNA_IP +'/dna/intent/api/v1/discovery/'+str(self.id)+'/network-device/', headers=self.headers,verify=False)
        return self.response.json()['response']
    def SubmitDiscoveryForm(self):
        self.reader = xlsxwriter.Workbook(f'{sys.path[0]}\Discovery\\NewDiscovery.xlsx')
        self.NumberOfRows = len(self.reader.index)
        self.enablePasswordList = ""
        self.globalCredentialIdList=[]
        i=0
        while i < self.NumberOfRows:
            ### Check enablePasswordList ###
            if math.isnan(self.reader['enablePasswordList'][i]):
                self.enablePasswordList = ""
            else:
                self.enablePasswordList = self.reader['enablePasswordList'][i]
            ### Logical program for globalCredentialIdList ###
            for self.item in self.reader['globalCredentialIdList'][i]:
                self.globalCredentialIdList = self.reader['globalCredentialIdList'][i].rsplit("\n")
            ### Logical program for nteconfPort NaN ###
            for self.item in self.reader['netconfPort']:
                self.text = self.reader['netconfPort'][i]
                if math.isnan(self.text):
                    self.netconfPort = "AA"
                else:
                    self.netconfPort = self.reader['netconfPort']
            self.payload= {
                "discoveryType" : self.reader['discoveryType'][i],
                "cdpLevel": int(self.reader['cdpLevel'][i]),
                "lldpLevel": int(self.reader['lldpLevel'][i]),      
                "enablePasswordList": [self.enablePasswordList],
                "globalCredentialIdList": self.globalCredentialIdList,
                "ipAddressList" : self.reader['ipAddressList'][i],
                "name" : self.reader['name'][i],
                "preferredMgmtIPMethod": self.reader['preferredMgmtIPMethod'][i],
                "protocolOrder" : self.reader['protocolOrder'][i],
                "reDiscovery" : bool(self.reader['reDiscovery'][i]),
                "retry" : int(self.reader['retry'][i]),
                "timeout" : int(self.reader['timeout'][i]),
                "noAddNewDevice" : bool(self.reader['noAddNewDevice'][i]),
            }
            self.response = requests.request('POST','https://'+ self.DNA_IP +'/dna/intent/api/v1/discovery', headers = self.headers, data = json.dumps(self.payload),verify=False)
            self.response.json()
            print ("New Discovery Has Been Successfully Added")
            i+=1
    def GetGlobalCredentials(self,no):
        # FOR CLI ONLY
        if no == 4:
            return NetworkSettings_DNA().DeviceCredential_Lists()['cli']
        elif no == 5:
            return NetworkSettings_DNA().DeviceCredential_Lists()['snmp_v2_read']
        elif no == 6:
            return NetworkSettings_DNA().DeviceCredential_Lists()['snmp_v2_write']
        elif no == 7:
            return NetworkSettings_DNA().DeviceCredential_Lists()['snmp_v3']
        elif no == 8:
            return NetworkSettings_DNA().DeviceCredential_Lists()['http_write']
        elif no == 9:
            return NetworkSettings_DNA().DeviceCredential_Lists()['http_read']
        