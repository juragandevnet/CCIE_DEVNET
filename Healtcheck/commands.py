from ast import Break


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
    elif "NAME: \"Chassis 1 WS-C6509-E\", DESCR: \"Chassis 1 Cisco Systems, Inc. Catalyst 6500 9-slot Chassis System\"" in line:
        return "WS-C6509-E"
    elif 'NAME: "Switch System", DESCR: "Cisco Systems, Inc. WS-C4507R+E 7 slot switch "' in line:
        return "WS-C4507R+E"
    elif ("NAME: \"Switch 1\", DESCR: \"WS-C3850-24T-S\"" and "NAME: \"Switch 2\", DESCR: \"WS-C3850-24T-S\"") in line:
        return "WS-C3850-24TS-S"
    elif "NAME: \"Switch 1\", DESCR: \"WS-C3850-24T-E\"" and "NAME: \"Switch 2\", DESCR: \"WS-C3850-24T-E\"" in line:
        return "WS-C3850-24T-E"
    elif "NAME: \"Switch 1\", DESCR: \"WS-C3850-24P-E\"" and "NAME: \"Switch 2\", DESCR: \"WS-C3850-24P-E\"" in line:
        return "WS-C3850-24P-E"
    else:
        return "NOT FOUND"
def JoinCPU(raw):
    if 'FAIL' in raw:
        return 'FAIL'
    else:
        return 'PASS'

    #merge = ' '.join([str(elem) for elem in cpu])
    #for output in merge:
    #    print(output)
def CPU(line):
    cpu = ''
    if "Core 0: CPU utilization for five seconds: " in line:
        line = line.split(';')
        ten = line[1].strip(" one minute: ").replace('%','')
        five = line[2].strip(" five minutes: ").replace('%','')
        if int(ten) < 80 and int(five) < 80:
            cpu = "PASS"
        else:
            cpu = "FAIL"
    elif "Core 1: CPU utilization for five seconds: " in line:
        line = line.split(';')
        ten = line[1].strip(" one minute: ").replace('%','')
        five = line[2].strip(" five minutes: ").replace('%','')
        if int(ten) < 80 and int(five) < 80:
            cpu = "PASS"
        else:
            cpu = "FAIL"
    elif "Core 2: CPU utilization for five seconds: " in line:
        line = line.split(';')
        ten = line[1].strip(" one minute: ").replace('%','')
        five = line[2].strip(" five minutes: ").replace('%','')
        if int(ten) < 80 and int(five) < 80:
            cpu = "PASS"
        else:
            cpu = "FAIL"
    elif "Core 4: CPU utilization for five seconds: " in line:
        line = line.split(';')
        ten = line[1].strip(" one minute: ").replace('%','')
        five = line[2].strip(" five minutes: ").replace('%','')
        if int(ten) < 80 and int(five) < 80:
            cpu = "PASS"
        else:
            cpu = "FAIL"
    elif "CPU utilization for five seconds: " in line:
        line = line.split(';')
        one_min = line[1].lstrip(" one minute: ").replace('%','')
        five_min = line[2].lstrip(" five minutes: ").replace('%','')
        if int(one_min) < 80 and int(five_min) < 80:
            cpu = "PASS"
        else:
            cpu = "FAIL"
    else:
        cpu = "NOT FOUND"
    return cpu

