from clearscreen import clearscreen
from Discovery.discovery_page import discovery_page

def menu():
    print ("WELCOME TO DNAC OTOBOT\n\n")
    print ("1.Discovery\n")

def main_page():
    clearscreen()
    while True:
        menu()
        try:
            select = int(input("Select:"))
            if select == 1:
                clearscreen()
                discovery_page()
            elif select == 10:
                break
            else:
                pass
        except:
            print ("Please input number only")   
    
### MAIN ###    
main_page()







        



