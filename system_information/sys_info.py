import platform
from datetime import datetime

import psutil

print("+----------------------+")
print("|  System Information  |")
print("+----------------------+")
sys_info = platform.uname()
print("System Name: ", sys_info.system)
print("Version:", sys_info.version)
print("Release: ", sys_info.release)
print("Machine: ", sys_info.machine)
print("Processor: ", sys_info.processor)

b = psutil.boot_time()
bootTime = datetime.fromtimestamp(b)
print("Booted On")
print("Day:", bootTime.day, "/", bootTime.month, "/", bootTime.year)
print("Time:", bootTime.hour, ":", bootTime.minute, ":", bootTime.second)

print("+-------------------+")
print("|  CPU Information  |")
print("+-------------------+")
freq = psutil.cpu_freq()
print("Current Frequency: ", freq.current, "Mhz")
print("Maximum Frequency: ", freq.max, "Mhz")
print("Minimum Frequency: ", freq.min, "Mhz")

print("CPU Usage Per Core: ")
for c, p in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print("Core ", c, ": ", p, "%")
