#Import
from lib import core
from payload.x86_Stager.Windows import x86_Win_Meterpreter_Rev_Http, x86_Win_Meterpreter_Rev_Https, x86_Win_Meterpreter_Rev_Tcp
from payload.x64_Stager.Windows import x64_Win_Meterpreter_Rev_Http, x64_Win_Meterpreter_Rev_Https, x64_Win_Meterpreter_Rev_Tcp


#Displays the main banner
core.Banner()


#Main function
def Modules():

    core.Module_Choice()

    Modules_while = True

    while Modules_while:
        Choice = core.core_input()

        if Choice == "1":
            Advanced_Windows_Meterpreter()
            Modules_while = False

        else:
            core.Clear()
            core.Module_Choice()
            core.Bad_Choice()
            continue


#Function to select Windows modules
def Advanced_Windows_Meterpreter():

    core.Windows_Arch_Choice()

    AWM_while = True

    while AWM_while:
        Choice = core.core_input()

        if Choice == "1":
            core.x86_Windows_Stager_Choice()
            AWM_while = False

        elif Choice == "2":
            core.x64_Windows_Stager_Choice()
            AWM_while = False

        else:
            core.Clear()
            core.Windows_Arch_Choice()
            core.Bad_Choice()
            continue


#Function to select x86 Windows payload
def AWM_x86():

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

        else:
            core.Clear()
            core.x86_Windows_Stager_Choice()
            core.Bad_Choice()
            continue


#Function to select x64 Windows payload
def AWM_x64():

    core.x64_Windows_Stager_Choice()

    AWM_x64_while = True

    while AWM_x64_while:
        Choice = core.core_input()

        if Choice == "1":
            x64_Win_Meterpreter_Rev_Tcp.Construction()

        elif Choice == "2":
            x64_Win_Meterpreter_Rev_Http.Construction()

        elif Choice == "3":
            x64_Win_Meterpreter_Rev_Https.Construction()

        else:
            core.Clear()
            core.x64_Windows_Stager_Choice()
            core.Bad_Choice()
            continue


#Exec modules function
Modules()







