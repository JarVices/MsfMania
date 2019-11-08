from lib import core

from payload.x86_Stager.Windows import x86_Win_Meterpreter_Rev_Http, x86_Win_Meterpreter_Rev_Https, x86_Win_Meterpreter_Rev_Tcp, x86_Win_Shell_Rev_Tcp
from payload.x86_Stageless.Windows import x86_Stageless_Win_Meterpreter_Rev_Http, x86_Stageless_Win_Meterpreter_Rev_Https, x86_Stageless_Win_Meterpreter_Rev_Tcp, x86_Stageless_Win_Shell_Rev_Tcp

from payload.x64_Stager.Windows import x64_Win_Meterpreter_Rev_Http, x64_Win_Meterpreter_Rev_Https, x64_Win_Meterpreter_Rev_Tcp, x64_Win_Shell_Rev_Tcp
from payload.x64_Stageless.Windows import x64_Stageless_Win_Meterpreter_Rev_Http, x64_Stageless_Win_Meterpreter_Rev_Https, x64_Stageless_Win_Meterpreter_Rev_Tcp, x64_Stageless_Win_Shell_Rev_Tcp



#Main function
def Modules():

    try:

        core.Module_Choice()

        Modules_while = True

        while Modules_while:

            Choice = core.core_input()

            if Choice == "1":

                Windows_Staged_Or_No()
                Modules_while = False

            elif Choice == "0":

                core.Exit_Program()
                Modules_while = False

            else:
                core.Bad_Choice()

    except KeyboardInterrupt:
        core.Exit_Program()



#Function to select whether the payload will be "staged" or "stageless"
def Windows_Staged_Or_No():

    try:

        core.Windows_Method_Choice()

        WSON_while = True

        while WSON_while:

            Choice = core.core_input()

            if Choice == "1":

                Advanced_Windows_Staged_Meterpreter()
                WSON_while = False

            elif Choice == "2":

                Advanced_Windows_Stageless_Meterpreter()
                WSON_while = False

            elif Choice == "0":

                Modules()
                WSON_while = False

            else:
                core.Bad_Choice()

    except KeyboardInterrupt:
        core.Exit_Program()



#Function to select Windows which payload arch to use for staged payload
def Advanced_Windows_Staged_Meterpreter():

    try:

        core.Windows_Arch_Choice()

        AWSM_while = True

        while AWSM_while:

            Choice = core.core_input()

            if Choice == "1":

                AWSM_x86()
                AWSM_while = False

            elif Choice == "2":

                AWSM_x64()
                AWSM_while = False

            elif Choice == "0":

                Windows_Staged_Or_No()
                AWSM_while = False

            else:

                core.Bad_Choice()

    except KeyboardInterrupt:
        core.Exit_Program()



#Function to select x86 Windows Staged payload
def AWSM_x86():

    try:

        core.x86_Windows_Staged_Choice()

        AWSM_while = True

        while AWSM_while:

            Choice = core.core_input()

            if Choice == "1":

                x86_Win_Meterpreter_Rev_Tcp.Construction()
                AWSM_while = False

            elif Choice == "2":

                x86_Win_Meterpreter_Rev_Http.Construction()
                AWSM_while = False

            elif Choice == "3":

                x86_Win_Meterpreter_Rev_Https.Construction()
                AWSM_while = False

            elif Choice == "4":

                x86_Win_Shell_Rev_Tcp.Construction()
                AWSM_while = False

            elif Choice == "0":

                Advanced_Windows_Staged_Meterpreter()
                AWSM_while = False

            else:
                core.Bad_Choice()

    except KeyboardInterrupt:
        core.Exit_Program()



#Function to select x64 Windows Staged payload
def AWSM_x64():

    try:

        core.x64_Windows_Staged_Choice()

        AWSM_while = True

        while AWSM_while:

            Choice = core.core_input()

            if Choice == "1":

                x64_Win_Meterpreter_Rev_Tcp.Construction()
                AWSM_while = False

            elif Choice == "2":

                x64_Win_Meterpreter_Rev_Http.Construction()
                AWSM_while = False

            elif Choice == "3":

                x64_Win_Meterpreter_Rev_Https.Construction()
                AWSM_while = False

            elif Choice == "4":

                x64_Win_Shell_Rev_Tcp.Construction()
                AWSM_while = False

            elif Choice == "0":

                Advanced_Windows_Staged_Meterpreter()
                AWSM_while = False

            else:
                core.Bad_Choice()

    except KeyboardInterrupt:
        core.Exit_Program()



#Function to select Windows which payload arch to use for stageless payload
def Advanced_Windows_Stageless_Meterpreter():

    try:

        core.Windows_Arch_Choice()

        AWSM_while = True

        while AWSM_while:

            Choice = core.core_input()

            if Choice == "1":

                AWM_x86()
                AWSM_while = False

            elif Choice == "2":

                AWM_x64()
                AWSM_while = False

            elif Choice == "0":

                Windows_Staged_Or_No()
                AWSM_while = False

            else:
                core.Bad_Choice()

    except KeyboardInterrupt:
        core.Exit_Program()



#Function to select x86 Windows Stageless payload
def AWM_x86():

    try:

        core.x86_Windows_Stageless_Choice()

        AWM_while = True

        while AWM_while:

            Choice = core.core_input()

            if Choice == "1":

                x86_Stageless_Win_Meterpreter_Rev_Tcp.Construction()
                AWM_while = False

            elif Choice == "2":

                x86_Stageless_Win_Meterpreter_Rev_Http.Construction()
                AWM_while = False

            elif Choice == "3":

                x86_Stageless_Win_Meterpreter_Rev_Https.Construction()
                AWM_while = False

            elif Choice == "4":

                x86_Stageless_Win_Shell_Rev_Tcp.Construction()
                AWM_while = False

            elif Choice == "0":

                Advanced_Windows_Stageless_Meterpreter()
                AWM_while = False

            else:
                core.Bad_Choice()

    except KeyboardInterrupt:
        core.Exit_Program()



#Function to select x64 Windows Stageless payload
def AWM_x64():

    try:

        core.x64_Windows_Stageless_Choice()

        AWM_while = True

        while AWM_while:

            Choice = core.core_input()

            if Choice == "1":

                x64_Stageless_Win_Meterpreter_Rev_Tcp.Construction()
                AWM_while = False

            elif Choice == "2":

                x64_Stageless_Win_Meterpreter_Rev_Http.Construction()
                AWM_while = False

            elif Choice == "3":

                x64_Stageless_Win_Meterpreter_Rev_Https.Construction()
                AWM_while = False

            elif Choice == "4":

                x64_Stageless_Win_Shell_Rev_Tcp.Construction()
                AWM_while = False

            elif Choice == "0":

                Advanced_Windows_Staged_Meterpreter()
                AWM_while = False

            else:
                core.Bad_Choice()

    except KeyboardInterrupt:
        core.Exit_Program()



#Exec main func
core.Banner()
Modules()
