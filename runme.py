import os
from os import system
import time

## crappy licenses

Home = "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99"
HomeN = "3KHY7-WNT83-DGQKR-F7HPR-844BM"
HSL = "7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH"
HCS =  "PVMJN-6DFY6–9CCP6–7BKTT-D3WVR"
Pro =  "W269N-WFGWX-YVC9B-4J6C9-T83GX"
ProN = "MH37W-N47XK-V7XM9-C7227-GCQG9"
Edu = "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2"
EduN = "2WH4N-8QGBV-H22JP-CT43Q-MDWWJ"
Ent = "NPPR9-FWDCX-D2C8J-H872K-2YT43"
EntN = "DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4"

print(">  Hi Anon! So proud of you! first step in rejecting microsoft! ")
time.sleep(1)
print(">  ")
time.sleep(1)
print(">  Please share this repo!")
time.sleep(1)
print(">  ")
time.sleep(1)
print(">  If this gets popular enough, I'll make a batch script and maybe a GUI")
time.sleep(1)
print(">  ")
time.sleep(1)
print(">  https://github.com/sprmcell/WinActivator")
time.sleep(1)
print(">  ")
time.sleep(1)
print(">  running on python version")
time.sleep(1)
os.system("python --version")
time.sleep(1)
print(">  ")
time.sleep(1)
pvc=input(">  Is this correct? (y/n) ")

if pvc.lower()=="y":
    print(">  Great! Now we can move on!")
    time.sleep(1)
    print(">  Downloading Licenses!")
    time.sleep(2)
    print(">  .")
    print(">  ..")
    time.sleep(2)
    print(">  ...")
    time.sleep(3)
    print(">  Downloaded 10 licenses without errors!")
    time.sleep(1)

    print(">  Please select your Version; Note must be version installed on pc")
    time.sleep(1)
    print("""
    (1) Home
    (2) Home N
    (3) Home Single Language
    (4) Home Country Specific

    (5) Pro
    (6) Pro N

    (7) Educational
    (8) Educational N

    (9) Enterprise
    (10) Enterprise N
    """)
    time.sleep(1)

    vs=input(">  Pick your version 1-10: ")

    if vs.lower()=="1":
        os.system(f"slmgr /ipk {Home}")
        print(">  Please wait for a Window to pop up!")
    if vs.lower()=="2":
        os.system(f"slmgr /ipk {HomeN}")
        print(">  Please wait for a Window to pop up!")
    if vs.lower()=="3":
        os.system(f"slmgr /ipk {HSL}")
        print(">  Please wait for a Window to pop up!")
    if vs.lower()=="4":
        os.system(f"slmgr /ipk {HCS}")
        print(">  Please wait for a window to pop up!")
    if vs.lower()=="5":
        os.system(f"slmgr /ipk {Pro}")
        print(">  Please wait a window to pop up!")
    if vs.lower()=="6":
        os.system(f"slmgr /ipk {ProN}")
        print(">  Please wait for a window to pop up!")
    if vs.lower()=="7":
        os.system(f"slmgr /ipk {Edu}")
        print(">  Please wait for a window to pop up!")
    if vs.lower()=="8":
        os.system(f"slmgr /ipk {EduN}")
        print(">  Please wait for a window to pop up")
    if vs.lower()=="9":
        os.system(f"slmgr /ipk {Ent}")
        print(">  Please wait for a window to pop up!")
    if vs.lower()=="10":
        os.system(f"slmgr /ipk {EntN}")
        print(">  Please wait for a window to pop up!")

    time.sleep(2)
    print(">  Please wait for us to verify your license key!")
    os.system("slmgr /skms kms8.msguides.com")
    print(">  ")
    time.sleep(3)
    print(">  If a small window did not show for a bit, please wait")
    time.sleep(2)
    print(">  Please wait...")
    print(">  ")
    print(">  Applying license...")
    os.system("slmgr /ato")
    time.sleep(1)
    print(">  ")
    print(">  If a small window showed saying something like 'Product activated successfully', youre done!")
    print(">  ")
    print(">  Thanks for using :)")



if pvc.lower()=="n":
    print(">  please reinstall python or reboot")
    print(">  ")
    print(">  bye :(")
    os.system("exit")
