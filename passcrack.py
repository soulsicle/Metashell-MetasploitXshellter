import os
import random
import threading
import string
import subprocess

wifimode1 = 2
name = 1

user = input("wifi mode y/n?")
if user == "y":
    wifimode1 = 1
if user == "n":
    wifimode1 = 0
if wifimode1 == 1:
    name = input("ssid:")
Uselect = input("character length:")


def wifimode(name1,pass1):
    # function to establish a new connection
    def createNewConnection(name, SSID, password):
        config = """<?xml version=\"1.0\"?>
    <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
        <name>"""+name+"""</name>
        <SSIDConfig>
            <SSID>
                <name>"""+SSID+"""</name>
            </SSID>
        </SSIDConfig>
        <connectionType>ESS</connectionType>
        <connectionMode>auto</connectionMode>
        <MSM>
            <security>
                <authEncryption>
                    <authentication>WPA2PSK</authentication>
                    <encryption>AES</encryption>
                    <useOneX>false</useOneX>
                </authEncryption>
                <sharedKey>
                    <keyType>passPhrase</keyType>
                    <protected>false</protected>
                    <keyMaterial>"""+password+"""</keyMaterial>
                </sharedKey>
            </security>
        </MSM>
    </WLANProfile>"""
        command = "netsh wlan add profile filename=\""+name+".xml\""+" interface=Wi-Fi"
        with open(name+".xml", 'w') as file:
            file.write(config)
        os.system(command)
 
# function to connect to a network   
    def connect(name, SSID):
        command = "netsh wlan connect name=\""+name+"\" ssid=\""+SSID+"\" interface=Wi-Fi"
        os.system(command)
 
# input wifi name and password
    name = name1
    password = pass1
 
# establish new connection
    createNewConnection(name, name, password)
 
# connect to the wifi network
    connect(name, name)
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
def listo(f):
    l = (random_line('data.txt'))
    print(l)
    if wifimode1 == 1:
        wifimode(name,l)
    
def shuffle_words(word_a, word_b):
    word = word_a + word_b
    lst = list(word)
    random.shuffle(lst)
    shuffled_word = ''.join(lst[:len(word_a)]) + ' ' + ''.join(lst[len(word_a):]) 
    return shuffled_word
def rando(charnum):
    a = random.randint(0,int(charnum))
    b = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=20))
    a1 = str(a)
    c = shuffle_words(a1,b)
    print(c)
    if wifimode1 == 1:
        wifimode(name,c)

while 0<1:
    if __name__ =="__main__":
        if name in subprocess.check_output(["netsh", "wlan", "show", "interfaces"]).decode('utf-8'):
            print("complete!")
            exit()
        t1 = threading.Thread(target=rando, args=(10,))
        t2 = threading.Thread(target=listo, args=(10,))
        t3 = threading.Thread(target=rando, args=(10,))
        t4 = threading.Thread(target=listo, args=(10,))
        t5 = threading.Thread(target=rando, args=(10,))
        t6 = threading.Thread(target=listo, args=(10,))
        t7 = threading.Thread(target=rando, args=(10,))
        t8 = threading.Thread(target=listo, args=(10,))
        t9 = threading.Thread(target=rando, args=(10,))
        t10 = threading.Thread(target=listo, args=(10,))
        t11 = threading.Thread(target=rando, args=(10,))
        t12 = threading.Thread(target=listo, args=(10,))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        listo(1)
        rando(Uselect)