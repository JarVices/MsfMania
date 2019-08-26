#Import
import os

from lib import core
from payload.x86_Stager.Windows import x86_Win_Meterpreter_Rev_Http, x86_Win_Meterpreter_Rev_Https, x86_Win_Meterpreter_Rev_Tcp
from payload.x64_Stager.Windows import x64_Win_Meterpreter_Rev_Http, x64_Win_Meterpreter_Rev_Https, x64_Win_Meterpreter_Rev_Tcp


#def Check_Environnement():
#ln -s /usr/bin/x86_64-w64-mingw32-gcc /usr/bin/windres
#ln -s /usr/bin/i686-w64-mingw32-windres /usr/bin/windres_1



#Main function
def Modules():

    try:

        core.Clear()
        core.Banner()
        core.Module_Choice()

        Modules_while = True

        while Modules_while:

            Choice = core.core_input()

            if Choice == "1":
                Advanced_Windows_Meterpreter()
                Modules_while = False

            elif Choice == "0":
                core.Clear()
                print("Exiting...")
                break

            else:
                core.Clear()
                core.Module_Choice()
                core.Bad_Choice()
                continue

    except KeyboardInterrupt:
        core.Exit_Program()



#Function to select Windows modules
def Advanced_Windows_Meterpreter():

    try:

        core.Clear()
        core.Windows_Arch_Choice()

        AWM_while = True

        while AWM_while:

            Choice = core.core_input()

            if Choice == "1":
                AWM_x86()
                AWM_while = False

            elif Choice == "2":
                AWM_x64()
                AWM_while = False

            elif Choice == "0":
                Modules()
                AWM_while = False

            else:
                core.Clear()
                core.Windows_Arch_Choice()
                core.Bad_Choice()
                continue

    except KeyboardInterrupt:
        core.Exit_Program()



#Function to select x86 Windows payload
def AWM_x86():

    try:

        core.Clear()
        core.x86_Windows_Stager_Choice()

        AWM_x86_while = True

        while AWM_x86_while:

            Choice = core.core_input()

            if Choice == "1":
                x86_Win_Meterpreter_Rev_Tcp.Construction()
                AWM_x86_while = False

            elif Choice == "2":
                x86_Win_Meterpreter_Rev_Http.Construction()
                AWM_x86_while = False

            elif Choice == "3":
                x86_Win_Meterpreter_Rev_Https.Construction()
                AWM_x86_while = False

            elif Choice == "0":
                Advanced_Windows_Meterpreter()
                AWM_x86_while = False

            else:
                core.Clear()
                core.x86_Windows_Stager_Choice()
                core.Bad_Choice()
                continue

    except KeyboardInterrupt:
        core.Exit_Program()



#Function to select x64 Windows payload
def AWM_x64():

    try:

        core.Clear()
        core.x64_Windows_Stager_Choice()

        AWM_x64_while = True

        while AWM_x64_while:

            Choice = core.core_input()

            if Choice == "1":
                x64_Win_Meterpreter_Rev_Tcp.Construction()
                AWM_x64_while = False

            elif Choice == "2":
                x64_Win_Meterpreter_Rev_Http.Construction()
                AWM_x64_while = False

            elif Choice == "3":
                x64_Win_Meterpreter_Rev_Https.Construction()
                AWM_x64_while = False

            elif Choice == "0":
                Advanced_Windows_Meterpreter()
                AWM_x64_while = False

            else:
                core.Clear()
                core.x64_Windows_Stager_Choice()
                core.Bad_Choice()
                continue

    except KeyboardInterrupt:
        core.Exit_Program()


#Exec modules function
Modules()







