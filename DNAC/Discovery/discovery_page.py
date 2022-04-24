from prettytable import PrettyTable
from Discovery.discovery_class import discovery_dna

def discovery_page():
    while True:
        print ("WELCOME TO DNAC OTOBOT\n\n1.Show Discovery Status\n2.Run Discovery\n3.Add/Remove  Discovery\n4.CLI Info\n5.SNMPv2 Read Community Info\n6.SNMPv2 Write Community Info\n7.SNMPv3 Info\n8.HTTP READ Info\n9.HTTP WRITE Info\n10.Exit")
        try:
            select = int(input("Select:"))
            if select == 1:
                table = PrettyTable(["Name", "IP Address Range", "Preferred Mgmt Method","Discovery Status","Discovery Condition","Id"])
                for item in discovery_dna().discovery_lists()['response']:
                    table.add_row([item['name'], item['ipAddressList'],item['preferredMgmtIPMethod'],item['discoveryStatus'],item['discoveryCondition'],item['id']])
                print (table)
            elif select == 2:
                discovery_dna().findIdDiscovery()
                table = PrettyTable(["Name", "IP Address Range", "Preferred Mgmt Method","Discovery Status","Discovery Condition","Id"])
                for item in discovery_dna().discovery_lists()['response']:
                    table.add_row([item['name'], item['ipAddressList'],item['preferredMgmtIPMethod'],item['discoveryStatus'],item['discoveryCondition'],item['id']])
                print (table)
            elif select == 3:
                discovery_dna().AddNewDiscovery()
                table = PrettyTable(["Name", "IP Address Range", "Preferred Mgmt Method","Discovery Status","Id"])
                for item in discovery_dna().discovery_lists()['response']:
                    table.add_row([item['name'], item['ipAddressList'],item['preferredMgmtIPMethod'],item['discoveryStatus'],item['id']])
                print (table)
            elif select == 4:
                items = discovery_dna().GetGlobalCredentials(select)
                table = PrettyTable(["Name","Username","Id","Comments"])
                y=0
                for item in items:
                    table.add_row([items[y]['description'],items[y]['username'],items[y]['id'],items[y]['comments']])
                    y+=1
                print (table)
            elif select == 5:
                items = discovery_dna().GetGlobalCredentials(select)
                table = PrettyTable(["SNMPv2 Read Name","Read CommunityName","Id","Comments"])
                y=0
                for item in items:
                    table.add_row([items[y]['description'],items[y]['readCommunity'],items[y]['id'],items[y]['comments']])
                    y+=1
                print (table)
            elif select == 6:
                items = discovery_dna().GetGlobalCredentials(select)
                table = PrettyTable(["SNMPv2 Write Name","Write CommunityName","Id","Comments"])
                y=0
                for item in items:
                    table.add_row([items[y]['description'],items[y]['writeCommunity'],items[y]['id'],items[y]['comments']])
                    y+=1
                print (table)
            elif select == 7:
                items = discovery_dna().GetGlobalCredentials(select)
                table = PrettyTable(["SNMPv3 Name","privacy Type","snmpMode","Authentication Type","Id","comments"])
                y=0
                for item in items:
                    table.add_row([items[y]['description'],items[y]['privacyType'],items[y]['snmpMode'],items[y]['authType'],items[y]['id'],items[y]['comments']])
                    y+=1
                print (table)
            elif select == 8:
                items = discovery_dna().GetGlobalCredentials(select)
                table = PrettyTable(["HTTP Read Name","Username","Port","Id","Comments"])
                y=0
                for item in items:
                    table.add_row([items[y]['description'],items[y]['username'],items[y]['port'],items[y]['id'],items[y]['comments']])
                    y+=1
                print(table)
            elif select == 9:
                items = discovery_dna().GetGlobalCredentials(select)
                table = PrettyTable(["HTTP Write Name","Username","Port","Id","Comments"])
                y=0
                for item in items:
                    table.add_row([items[y]['description'],items[y]['username'],items[y]['port'],items[y]['id'],items[y]['comments']])
                    y+=1
                print (table)
            elif select == 10:
                break
            else:
                pass
        except:
            print ("Please input number only")