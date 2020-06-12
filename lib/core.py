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
            Version : 2.1   -   Author : Killian CASAROTTO   -  Updated : June 12, 2020           
    """ + MMCOLORS.ENDC)


def CLEAR():
    os.system("clear")


def VARNAME_CREATOR():
    VARNAME = ''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(random.randint(25, 50)))
    return VARNAME


def INT_CREATOR():
    INT = str(randrange(479844, 89745632))
    return INT


def MODULE_CHOICE():
    print(MMCOLORS.BLUE + MMCOLORS.BOLD + "\n[?] >>> " + MMCOLORS.ENDC + MMCOLORS.GREEN + MMCOLORS.BOLD + "[1] Windows Payloads - [0] Exit Software;" + MMCOLORS.ENDC)


def SHELLCODE_GENERATED():
    print(MMCOLORS.GREEN + MMCOLORS.BOLD + "[+] >>> Shellcode generated." + MMCOLORS.ENDC)


def DECOY_ADDED():
    print(MMCOLORS.GREEN + MMCOLORS.BOLD + "[+] >>> Decoy code added." + MMCOLORS.ENDC)


def EVASION_ADDED():
    print(MMCOLORS.GREEN + MMCOLORS.BOLD + "[+] >>> Evasion code added." + MMCOLORS.ENDC)


def COMPILATION_COMPLETED():
    print(MMCOLORS.GREEN + MMCOLORS.BOLD + "[+] >>> File compiled and stripped." + MMCOLORS.ENDC)


def RAR_COMPRESSED():
    print(MMCOLORS.GREEN + MMCOLORS.BOLD + "[+] >>> Exe file compressed to RAR file." + MMCOLORS.ENDC)


def VIRUSTOTAL():
    print(MMCOLORS.RED + MMCOLORS.BOLD + """
██████╗  ██████╗     ███╗   ██╗ ██████╗ ████████╗    ███████╗███████╗███╗   ██╗██████╗      ██████╗ ███╗   ██╗    ██╗   ██╗██╗██████╗ ██╗   ██╗███████╗████████╗ ██████╗ ████████╗ █████╗ ██╗     
██╔══██╗██╔═══██╗    ████╗  ██║██╔═══██╗╚══██╔══╝    ██╔════╝██╔════╝████╗  ██║██╔══██╗    ██╔═══██╗████╗  ██║    ██║   ██║██║██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔═══██╗╚══██╔══╝██╔══██╗██║     
██║  ██║██║   ██║    ██╔██╗ ██║██║   ██║   ██║       ███████╗█████╗  ██╔██╗ ██║██║  ██║    ██║   ██║██╔██╗ ██║    ██║   ██║██║██████╔╝██║   ██║███████╗   ██║   ██║   ██║   ██║   ███████║██║     
██║  ██║██║   ██║    ██║╚██╗██║██║   ██║   ██║       ╚════██║██╔══╝  ██║╚██╗██║██║  ██║    ██║   ██║██║╚██╗██║    ╚██╗ ██╔╝██║██╔══██╗██║   ██║╚════██║   ██║   ██║   ██║   ██║   ██╔══██║██║     
██████╔╝╚██████╔╝    ██║ ╚████║╚██████╔╝   ██║       ███████║███████╗██║ ╚████║██████╔╝    ╚██████╔╝██║ ╚████║     ╚████╔╝ ██║██║  ██║╚██████╔╝███████║   ██║   ╚██████╔╝   ██║   ██║  ██║███████╗
╚═════╝  ╚═════╝     ╚═╝  ╚═══╝ ╚═════╝    ╚═╝       ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝      ╚═════╝ ╚═╝  ╚═══╝      ╚═══╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝    ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝                                                                                                                                                                                               
    """ + MMCOLORS.ENDC)
