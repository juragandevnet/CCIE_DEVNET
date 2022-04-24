def Hostname(line):
    if 'hostname' in line:
        line = line.strip('\n')
        line = line.strip('hostname')
    else:
        line = "NOT FOUND"
    return line
def PID(line):
    if "NAME: \"Chassis 1 WS-C6513-E\", DESCR: \"Chassis 1 Cisco Systems, Inc. Catalyst 6500 13-slot Chassis System\"" in line:
        return "WS-C6513"
        #print("WS-C6513")
    elif "NAME: \"Chassis 1 WS-C6509-E\", DESCR: \"Chassis 1 Cisco Systems, Inc. Catalyst 6500 9-slot Chassis System\"" in line:
        return "WS-C6509-E"
        #print("WS-C6509-E")
    elif 'NAME: "Switch System", DESCR: "Cisco Systems, Inc. WS-C4507R+E 7 slot switch "' in line:
        return "WS-C4507R+E"
        #print("WS-C4507R+E")
    elif ("NAME: \"Switch 1\", DESCR: \"WS-C3850-24T-S\"" and "NAME: \"Switch 2\", DESCR: \"WS-C3850-24T-S\"") in line:
        return "WS-C3850-24TS-S"
        #print("WS-C3850-24TS-S")
    elif "NAME: \"Switch 1\", DESCR: \"WS-C3850-24T-E\"" and "NAME: \"Switch 2\", DESCR: \"WS-C3850-24T-E\"" in line:
        return "WS-C3850-24T-E"
        #print("WS-C3850-24T-E")
    elif "NAME: \"Switch 1\", DESCR: \"WS-C3850-24P-E\"" and "NAME: \"Switch 2\", DESCR: \"WS-C3850-24P-E\"" in line:
        return "WS-C3850-24P-E"
        #print("WS-C3850-24P-E")
    else:
        return "NOT FOUND"
def JoinCPU(cpu):
    cpu = ' '.join([str(elem) for elem in cpu])
    return cpu
def CPU(line):
    if "Core 0" in line:
        line = line.split(';')
        sec = line[0].strip("Core 0: CPU utilization for five seconds: ")
        ten = line[1].strip(" one minute: ")
        five = line[2].strip(" five minutes: ")
        cpu = sec + " " + ten + " "+ five
    elif "Core 1" in line:
        line = line.split(';')
        sec = line[0].strip("Core 1: CPU utilization for five seconds: ")
        ten = line[1].strip(" one minute: ")
        five = line[2].strip(" five minutes: ")
        cpu = sec + " " + ten + " "+ five
    elif "Core 2" in line:
        line = line.split(';')
        sec = line[0].strip("Core 2: CPU utilization for five seconds: ")
        ten = line[1].strip(" one minute: ")
        five = line[2].strip(" five minutes: ")
        cpu = sec + " " + ten + " "+ five
    elif "Core 3" in line:
        line = line.split(';')
        sec = line[0].strip("Core 3: CPU utilization for five seconds: ")
        ten = line[1].strip(" one minute: ")
        five = line[2].strip(" five minutes: ")
        cpu = sec + " " + ten + " "+ five
    elif "CPU utilization for five seconds: " in line:
        line = line.split(';')
        sec = line[0].strip("CPU utilization for five seconds: ")
        ten = line[1].strip(" one minute: ")
        five = line[2].strip(" five minutes: ")
        cpu = sec + " " + ten + " "+ five
    else:
        cpu = "NOT FOUND"
    return cpu




'''
    
    elif "Core 3: CPU utilization for five seconds: " in line:
        line = line.split(';')
        sec = line[0].strip("Core 3: CPU utilization for five seconds: ")
        ten = line[1].strip(" one minute: ")
        five = line[2].strip(" five minutes: ")
        cpu = sec + " " + ten + " "+ five   
    else:
        cpu = "NOT FOUND"
'''
            

