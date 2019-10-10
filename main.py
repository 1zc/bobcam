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
import configparser

os.system(clear)

print("Checking config files.")

initcfg = open('cfg/init.cfg', 'r+')

if initcfg.read(1) == '0':
    print("First time starting. Need to initialize.")
    # TO-DO: Start HTML setup user-interface.
    initcfg.close()
    initcfg = open('cfg/init.cfg', 'w')
    initcfg.write('1')
    initcfg.close()

print("Loading resources.")
import stream


print("Starting BobCAM.")
stream.startstream('640x480', 60)

