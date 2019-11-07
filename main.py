###############################################################################
#                                                                             #
#     A project by:                                                           #
#                     -----------------------------------                     #
#                         L I A M  Z.  C H A R L E S                          #
#                     -----------------------------------                     #
#                                                                             #
#                                                                             #
#                              github.com/1zc                                 #
###############################################################################

# DEVELOPED FOR PY3 COMPATIBILITY ONLY.

import time
import RPi.GPIO as GPIO
import os
import subprocess
import requests
import threading
import configparser

os.system("clear")

print("Loading config files.")

initcfg = open('cfg/init.cfg', 'r+')
syscfg = 'cfg/sys.ini'
config = configparser.ConfigParser()

if initcfg.read(1) == '0':
    initcfg.close()
    print("First time starting. Configuration will commence in the CMDline in a few seconds. The web-interface is currently unavailable. ")
    # TO-DO: Start HTML setup user-interface.
    #raise SystemExit(0)

    # For now, use cmdline for config interface.
    print("\n\n\n#####################################\n")
    print("Welcome to the bobCAM First-Time Configuration!\n\nYou will be asked a few questions to set up your new bobCAM device.\n")
    print("#####################################\n\n")
    cfgsysname = input("How would you like the name your bobCAM? \n(Example: Liam's bobCAM, Living Room Cam)\n\n>>>")
    cfglocmemo = input("\nEnter a brief memo on the location for this bobCAM, useful when you're setting up a network of them. *Leave blank if you'd like to skip this* \n(Example: bobCAM watching the living room from the shelf)\n\n>>>")
    print("\n\nGreat, we've just completed your bobCAM's first-time configuration! Please wait while we save your settings.")
    config['sys'] = {}
    config['sys']['sysname'] = cfgsysname
    config['sys']['locmemo'] = cfglocmemo
    config['sys']['strmport'] = "1245"  # Video stream port, can be asked but probably shouldn't be.
    # Ask for video settings - todo later (Could be selected from presets or auto determined)
    config['vid'] = {}
    config['vid']['res'] = "640x480"
    config['vid']['resw'] = "640"
    config['vid']['resh'] = "480"
    config['vid']['fps'] = "24"
    # Default parameters
    config['DEFAULT'] = {}
    config['DEFAULT']['strmport'] = "1245"
    with open(syscfg, 'w') as configfile:
        config.write(configfile)

    initcfg = open('cfg/init.cfg', 'w')
    initcfg.write('1')
    initcfg.close()

initcfg.close()

config.read(syscfg)
cfgres = config['vid']['res']
resw = int(config['vid']['resw'])
resh = int(config['vid']['resh'])
cfgfps = int(config['vid']['fps'])
rawfps = config['vid']['fps']
rawstrmport = config['sys']['strmport']
cfgstrmport = int(config['sys']['strmport'])

print("Loading resources.")
import stream


print("Starting BobCAM.\n\n")
print("Using res= "+cfgres+" | fps= "+rawfps+" ")
print("Streaming on network port: "+rawstrmport+"\n\n")
stream.startstream(cfgfps, resw, resh, cfgstrmport)