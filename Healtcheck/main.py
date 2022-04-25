import glob
from prettytable import PrettyTable
from commands import *

x = PrettyTable()
x.field_names = ["No","Hostname","PID","CPU"]
files = glob.glob(r"C:\Users\hawijaya\OneDrive - Cisco\DATA\04.Marina Bay Sands DOCUMENTS\MBS Healtcheck\HealthCheckLogs_22Mar2022\*.log")
i=1

for file in files:
    with open(file) as f:
        line = f.readline()
        joinstr = []
        while line:
            line = f.readline()
            if Hostname(line) != "NOT FOUND":
                hostname = Hostname(line)
            if PID(line) != "NOT FOUND":
                pid = PID(line)
            if CPU(line) != "NOT FOUND":
                joinstr.append(CPU(line))
    ### PRINT TABLE ###    
    x.add_row([i,hostname,pid,JoinCPU(joinstr)])
    i+=1

print(x)

