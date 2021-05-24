import psutil
import time;
from functools import cmp_to_key

def log(line):
    print(line)
    with open("log.txt", "a") as f:
        f.write("{}\n".format(line))

def cmpCpu(a, b):
    a = a['cpu']
    b = b['cpu']
    if a > b:
        return -1
    elif a == b:
        return 0
    else:
        return 1

def cmpMemory(a, b):
    a = a['memory']
    b = b['memory']
    if a > b:
        return -1
    elif a == b:
        return 0
    else:
        return 1

while True:
    localtime = time.localtime(time.time())
    timestamp = str(localtime.tm_hour)+":"+str(localtime.tm_min)
    log(timestamp)

    #Collect information for each process
    processes = []
    for proc in psutil.process_iter(attrs=['name', 'cpu_percent', 'memory_info']):
        processes.append({'name': proc.info['name'], 'cpu': proc.info['cpu_percent'], 'memory': int(proc.info['memory_info'].rss/1024/1024)})

    #Sort by cpu usage
    log("CPU:")
    processes.sort(key=cmp_to_key(cmpCpu))
    for i in range(5):
        info = processes[i]
        info = info['name']+", "+str(info['cpu'])+"%"
        log(info)

    #Sort by memory usage
    log("Memory:")
    processes.sort(key=cmp_to_key(cmpMemory))
    for i in range(5):
        info = processes[i]
        info = info['name']+", "+str(info['memory'])+"MB"
        log(info)

    time.sleep(60)