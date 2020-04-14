import os
import random
import string
from random import randrange


class MMCOLORS:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    OCRA = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DARKCYAN = '\033[36m'


def BANNER():
    # Univers ASCII banner
    print(MMCOLORS.BOLD + """                                                                                            
                ███╗   ███╗███████╗███████╗███╗   ███╗ █████╗ ███╗   ██╗██╗ █████╗ 
                ████╗ ████║██╔════╝██╔════╝████╗ ████║██╔══██╗████╗  ██║██║██╔══██╗
                ██╔████╔██║███████╗█████╗  ██╔████╔██║███████║██╔██╗ ██║██║███████║
                ██║╚██╔╝██║╚════██║██╔══╝  ██║╚██╔╝██║██╔══██║██║╚██╗██║██║██╔══██║
                ██║ ╚═╝ ██║███████║██║     ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║██║  ██║
                ╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝                                                                                                                                                                                                                   
            Version : 2.0   -   Author : Killian CASAROTTO   -  Updated : March 1, 2020           
    """ + MMCOLORS.ENDC)


def CLEAR():
    os.system("clear")


def BAD_CHOICE():
    print(MMCOLORS.RED + MMCOLORS.BOLD + "[x] Bad choice !!! Try again" + MMCOLORS.ENDC)


def CORE_INPUT():
    INPUT = input(
        MMCOLORS.DARKCYAN + MMCOLORS.BOLD + MMCOLORS.UNDERLINE + "Enter you choice" + MMCOLORS.ENDC + MMCOLORS.DARKCYAN + MMCOLORS.BOLD + " : " + MMCOLORS.ENDC)
    return INPUT


def EXIT_PROGRAM():
    exit()


def VARNAME_CREATOR():
    VARNAME = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase) for _ in range(random.randint(15, 25)))
    return VARNAME


def INT_CREATOR():
    INT = str(randrange(479844, 89745632))
    return INT


def MODULE_CHOICE():
    print(MMCOLORS.BLUE + MMCOLORS.BOLD + "\n[?] >>> " + MMCOLORS.ENDC + MMCOLORS.GREEN + MMCOLORS.BOLD + "[1] Windows Payloads - [0] Exit Software;" + MMCOLORS.ENDC)


def WINDOWS_TYPE_CHOICE():
    print(MMCOLORS.BLUE + MMCOLORS.BOLD + "\n[?] >>> " + MMCOLORS.ENDC + MMCOLORS.GREEN + MMCOLORS.BOLD + "[1] Staged Payloads - [2] Stageless Payloads - [0] Back;" + MMCOLORS.ENDC)


def WINDOWS_ARCHITECTURE_CHOICE():
    print(MMCOLORS.BLUE + MMCOLORS.BOLD + "\n[?] >>> " + MMCOLORS.ENDC + MMCOLORS.GREEN + MMCOLORS.BOLD + "[1] x86 Payloads - [2] x64 Payloads - [0] Back;" + MMCOLORS.ENDC)


def X86_WINDOWS_STAGED_CHOICE():
    print(MMCOLORS.BLUE + MMCOLORS.BOLD + "\n[?] >>> " + MMCOLORS.ENDC + MMCOLORS.GREEN + MMCOLORS.BOLD + "Select Windows x86 Staged Payload - [0] Back" + MMCOLORS.ENDC + MMCOLORS.BOLD + "|" + MMCOLORS.ENDC + MMCOLORS.BOLD + MMCOLORS.OCRA + " [*] (exemple : windows/meterpreter/reverse_tcp)" + MMCOLORS.ENDC)


def X64_WINDOWS_STAGED_CHOICE():
    print(MMCOLORS.BLUE + MMCOLORS.BOLD + "\n[?] >>> " + MMCOLORS.ENDC + MMCOLORS.GREEN + MMCOLORS.BOLD + "Select Windows x64 Staged Payload - [0] Back" + MMCOLORS.ENDC + MMCOLORS.BOLD + "|" + MMCOLORS.ENDC + MMCOLORS.BOLD + MMCOLORS.OCRA + " [*] (exemple : windows/x64/meterpreter/reverse_tcp)" + MMCOLORS.ENDC)


def X86_WINDOWS_STAGELESS_CHOICE():
    print(MMCOLORS.BLUE + MMCOLORS.BOLD + "\n[?] >>> " + MMCOLORS.ENDC + MMCOLORS.GREEN + MMCOLORS.BOLD + "Select Windows x86 Stageless Payload - [0] Back" + MMCOLORS.ENDC + MMCOLORS.BOLD + "|" + MMCOLORS.ENDC + MMCOLORS.BOLD + MMCOLORS.OCRA + " [*] (exemple : windows/meterpreter_reverse_tcp)" + MMCOLORS.ENDC)


def X64_WINDOWS_STAGELESS_CHOICE():
    print(MMCOLORS.BLUE + MMCOLORS.BOLD + "\n[?] >>> " + MMCOLORS.ENDC + MMCOLORS.GREEN + MMCOLORS.BOLD + "Select Windows x64 Stageless Payload - [0] Back" + MMCOLORS.ENDC + MMCOLORS.BOLD + "|" + MMCOLORS.ENDC + MMCOLORS.BOLD + MMCOLORS.OCRA + " [*] (exemple : windows/x64/meterpreter_reverse_tcp)" + MMCOLORS.ENDC)


def LHOST_CHOICE():
    print(MMCOLORS.BLUE + MMCOLORS.BOLD + "\n[?] >>> " + MMCOLORS.ENDC + MMCOLORS.GREEN + MMCOLORS.BOLD + "Enter you LHOST - [0] Back;" + MMCOLORS.ENDC)


def LPORT_CHOICE():
    print(MMCOLORS.BLUE + MMCOLORS.BOLD + "\n[?] >>> " + MMCOLORS.ENDC + MMCOLORS.GREEN + MMCOLORS.BOLD + "Enter you LPORT - [0] Back;" + MMCOLORS.ENDC)


def FILENAME():
    print(MMCOLORS.BLUE + MMCOLORS.BOLD + "\n[?] >>> " + MMCOLORS.ENDC + MMCOLORS.GREEN + MMCOLORS.BOLD + "Select you filename " + MMCOLORS.ENDC + MMCOLORS.BOLD + "|" + MMCOLORS.ENDC + MMCOLORS.BOLD + MMCOLORS.OCRA + " [*] (exemple : What A Malware) - [0] Back;" + MMCOLORS.ENDC)


def GENERATING_SHELLCODE():
    print(MMCOLORS.OCRA + MMCOLORS.BOLD + "\n[*] >>> Generating shellcode." + MMCOLORS.ENDC)


def SHELLCODE_GENERATED():
    print(MMCOLORS.GREEN + MMCOLORS.BOLD + "[+] >>> Shellcode generated." + MMCOLORS.ENDC)


def ADD_DECOY():
    print(MMCOLORS.BLUE + MMCOLORS.BOLD + "\n[?] >>> " + MMCOLORS.ENDC + MMCOLORS.GREEN + MMCOLORS.BOLD + "Number of decoys to add (unlimited) " + MMCOLORS.ENDC + MMCOLORS.BOLD + "|" + MMCOLORS.OCRA + " [*] PS : 1 decoy = 1 secondes to sleep." + MMCOLORS.ENDC)
    print(MMCOLORS.DARKCYAN + MMCOLORS.BOLD + "[!] >>> Press ENTER for ignore this step." + MMCOLORS.ENDC)


def ADDING_DECOY():
    print(MMCOLORS.OCRA + MMCOLORS.BOLD + "\n[*] >>> Adding decoy code." + MMCOLORS.ENDC)


def DECOY_ADDED():
    print(MMCOLORS.GREEN + MMCOLORS.BOLD + "[+] >>> Decoy code added." + MMCOLORS.ENDC)


def ADDING_EVASION():
    print(MMCOLORS.OCRA + MMCOLORS.BOLD + "\n[*] >>> Adding evasion code." + MMCOLORS.ENDC)


def EVASION_ADDED():
    print(MMCOLORS.GREEN + MMCOLORS.BOLD + "[+] >>> Evasion code added." + MMCOLORS.ENDC)


def LOCAL_OR_REMOTE():
    print(
        MMCOLORS.BLUE + MMCOLORS.BOLD + "\n[?] >>> " + MMCOLORS.ENDC + MMCOLORS.GREEN + MMCOLORS.BOLD + "[1] Local Thread Injection (DEFAULT) - [2] Remote Thread Injection;" + MMCOLORS.ENDC)
    print(MMCOLORS.DARKCYAN + MMCOLORS.BOLD + "[!] >>> Press ENTER to set DEFAULT." + MMCOLORS.ENDC)


def WHICH_PROCESS():
    print(MMCOLORS.BLUE + MMCOLORS.BOLD + "\n[?] >>> " + MMCOLORS.ENDC + MMCOLORS.GREEN + MMCOLORS.BOLD + "Select process to inject " + MMCOLORS.ENDC + MMCOLORS.BOLD + "|" + MMCOLORS.OCRA + " [*] (DEFAULT = explorer.exe)." + MMCOLORS.ENDC)
    print(MMCOLORS.DARKCYAN + MMCOLORS.BOLD + "[!] >>> Press ENTER to set DEFAULT." + MMCOLORS.ENDC)


def ICON():
    print(MMCOLORS.BLUE + MMCOLORS.BOLD + "\n[?] >>> " + MMCOLORS.ENDC + MMCOLORS.GREEN + MMCOLORS.BOLD + "Select you icon name " + MMCOLORS.ENDC + MMCOLORS.BOLD + "|" + MMCOLORS.ENDC + MMCOLORS.BOLD + MMCOLORS.OCRA + " [*] (exemple : my_icon_name.ico)" + MMCOLORS.ENDC)
    print(MMCOLORS.DARKCYAN + MMCOLORS.BOLD + "[!] >>> In the 'icon' folder, put your icon files in it." + MMCOLORS.ENDC)
    print(MMCOLORS.DARKCYAN + MMCOLORS.BOLD + "[!] >>> Press ENTER if you do not have an icon." + MMCOLORS.ENDC)


def COMPILATION_STARTED():
    print(MMCOLORS.OCRA + MMCOLORS.BOLD + "\n[*] >>> Compiling and stripping file." + MMCOLORS.ENDC)


def COMPILATION_COMPLETED():
    print(MMCOLORS.GREEN + MMCOLORS.BOLD + "[+] >>> File compiled and stripped." + MMCOLORS.ENDC)


def RAR_COMPRESSION():
    print(MMCOLORS.BLUE + MMCOLORS.BOLD + "\n[?] >>> " + MMCOLORS.ENDC + MMCOLORS.GREEN + MMCOLORS.BOLD + "[1] Don't compress (DEFAULT) - [2] Compress to RAR;" + MMCOLORS.ENDC)
    print(MMCOLORS.DARKCYAN + MMCOLORS.BOLD + "[!] >>> Press ENTER to set DEFAULT." + MMCOLORS.ENDC)


def RAR_COMPRESSING():
    print(MMCOLORS.OCRA + MMCOLORS.BOLD + "\n[*] >>> Compressing EXE file to RAR file." + MMCOLORS.ENDC)


def RAR_COMPRESSED():
    print(MMCOLORS.GREEN + MMCOLORS.BOLD + "[+] >>> Exe file compressed to RAR file." + MMCOLORS.ENDC)


def RUN_METERPRETER_SCRIPT():
    print(MMCOLORS.BLUE + MMCOLORS.BOLD + "\n[?] >>> " + MMCOLORS.ENDC + MMCOLORS.GREEN + MMCOLORS.BOLD + "Run multi/handler script - [1] Don't run (DEFAULT) - [2] Run multi/handler script;" + MMCOLORS.ENDC)
    print(MMCOLORS.DARKCYAN + MMCOLORS.BOLD + "[!] >>> Press ENTER to set DEFAULT." + MMCOLORS.ENDC)


def DELETING_RC_FILE():
    print(MMCOLORS.OCRA + MMCOLORS.BOLD + "\n""[*] >>> Deletion of the RC file in 12 seconds." + MMCOLORS.ENDC)


def RC_FILE_DELETED():
    print(MMCOLORS.GREEN + MMCOLORS.BOLD + "[+] >>> RC file deleted." + MMCOLORS.ENDC)


def VIRUSTOTAL():
    print(MMCOLORS.RED + MMCOLORS.BOLD + """
██████╗  ██████╗     ███╗   ██╗ ██████╗ ████████╗    ███████╗███████╗███╗   ██╗██████╗      ██████╗ ███╗   ██╗    ██╗   ██╗██╗██████╗ ██╗   ██╗███████╗████████╗ ██████╗ ████████╗ █████╗ ██╗     
██╔══██╗██╔═══██╗    ████╗  ██║██╔═══██╗╚══██╔══╝    ██╔════╝██╔════╝████╗  ██║██╔══██╗    ██╔═══██╗████╗  ██║    ██║   ██║██║██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔═══██╗╚══██╔══╝██╔══██╗██║     
██║  ██║██║   ██║    ██╔██╗ ██║██║   ██║   ██║       ███████╗█████╗  ██╔██╗ ██║██║  ██║    ██║   ██║██╔██╗ ██║    ██║   ██║██║██████╔╝██║   ██║███████╗   ██║   ██║   ██║   ██║   ███████║██║     
██║  ██║██║   ██║    ██║╚██╗██║██║   ██║   ██║       ╚════██║██╔══╝  ██║╚██╗██║██║  ██║    ██║   ██║██║╚██╗██║    ╚██╗ ██╔╝██║██╔══██╗██║   ██║╚════██║   ██║   ██║   ██║   ██║   ██╔══██║██║     
██████╔╝╚██████╔╝    ██║ ╚████║╚██████╔╝   ██║       ███████║███████╗██║ ╚████║██████╔╝    ╚██████╔╝██║ ╚████║     ╚████╔╝ ██║██║  ██║╚██████╔╝███████║   ██║   ╚██████╔╝   ██║   ██║  ██║███████╗
╚═════╝  ╚═════╝     ╚═╝  ╚═══╝ ╚═════╝    ╚═╝       ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝      ╚═════╝ ╚═╝  ╚═══╝      ╚═══╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝    ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝                                                                                                                                                                                               
    """ + MMCOLORS.ENDC)