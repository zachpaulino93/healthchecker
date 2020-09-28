#!/usr/bin/env python3
# we are importing files here
import shutil
import psutil
import resource
# for ip internect check
import socket
#checking disk disk_usage
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    print(free, du)
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1) / 1000
    print(usage, "this is usage")
    return usage < 75

def check_no_network():
    try:
        socket.gethostbyname("www.google.com")
        return False    
    except:
        return True

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR! check cpu usage")
else:
    print("everything is good to go here")
# testing stuff

ram = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000
for i in range(1,50,5):
    print(ram)
