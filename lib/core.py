import random
import string
from shutil import which
from random import randrange
import subprocess

class MmColors:
    blue = '\033[94m'
    green = '\033[92m'
    ocra = '\033[93m'
    red = '\033[91m'
    endc = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
    darkcyan = '\033[36m'


def banner():
    # Univers ASCII banner
    print(MmColors.bold + """                                                                                            
                ███╗   ███╗███████╗███████╗███╗   ███╗ █████╗ ███╗   ██╗██╗ █████╗ 
                ████╗ ████║██╔════╝██╔════╝████╗ ████║██╔══██╗████╗  ██║██║██╔══██╗
                ██╔████╔██║███████╗█████╗  ██╔████╔██║███████║██╔██╗ ██║██║███████║
                ██║╚██╔╝██║╚════██║██╔══╝  ██║╚██╔╝██║██╔══██║██║╚██╗██║██║██╔══██║
                ██║ ╚═╝ ██║███████║██║     ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║██║  ██║
                ╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝                                                                                                                                                                                                                   
            Version : 2.2   -   Author : Killian CASAROTTO   -  Updated : June 18, 2020           
    """ + MmColors.endc)


def check_requirements():
    required = ["x86_64-w64-mingw32-windres", "x86_64-w64-mingw32-gcc", "i686-w64-mingw32-windres", "i686-w64-mingw32-gcc", "rar", "msfvenom"]
    to_install = ["mingw-w64", "rar", "metasploit-framework"]
    not_installed = []
    for i in required:
        a = which(i)
        if a is None:
            print(MmColors.red + MmColors.bold + "[x] >>> '" + i + "' is not installed." + MmColors.endc)
            not_installed.append(i)

    if len(not_installed) != 0:
        for package in to_install:
            subprocess.call(['apt-get', '-y', 'install', package])



def error_injectionType():
    print(MmColors.red + MmColors.bold + "[x] >>> 'Remote' injection only works with x64 architectures. " + MmColors.ocra + "Changing the parameter to 'local'." + MmColors.endc)


def varname_creator():
    VARNAME = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(random.randint(8, 12)))
    return VARNAME


def int_creator():
    INT = str(randrange(479844, 89745632))
    return INT


def shellcode_generated():
    print(MmColors.green + MmColors.bold + "[+] >>> Shellcode generated." + MmColors.endc)


def shellcode_encrypted():
    print(MmColors.green + MmColors.bold + "[+] >>> Shellcode encrypted." + MmColors.endc)


def decoy_added():
    print(MmColors.green + MmColors.bold + "[+] >>> Decoy code added." + MmColors.endc)


def evasion_added():
    print(MmColors.green + MmColors.bold + "[+] >>> Evasion code added." + MmColors.endc)


def compilation_completed():
    print(MmColors.green + MmColors.bold + "[+] >>> File compiled and stripped." + MmColors.endc)


def rar_compressed():
    print(MmColors.green + MmColors.bold + "[+] >>> Exe file compressed to RAR file." + MmColors.endc)


def virustotal():
    print(MmColors.red + MmColors.bold + """
██████╗  ██████╗     ███╗   ██╗ ██████╗ ████████╗    ███████╗███████╗███╗   ██╗██████╗      ██████╗ ███╗   ██╗    ██╗   ██╗██╗██████╗ ██╗   ██╗███████╗████████╗ ██████╗ ████████╗ █████╗ ██╗     
██╔══██╗██╔═══██╗    ████╗  ██║██╔═══██╗╚══██╔══╝    ██╔════╝██╔════╝████╗  ██║██╔══██╗    ██╔═══██╗████╗  ██║    ██║   ██║██║██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔═══██╗╚══██╔══╝██╔══██╗██║     
██║  ██║██║   ██║    ██╔██╗ ██║██║   ██║   ██║       ███████╗█████╗  ██╔██╗ ██║██║  ██║    ██║   ██║██╔██╗ ██║    ██║   ██║██║██████╔╝██║   ██║███████╗   ██║   ██║   ██║   ██║   ███████║██║     
██║  ██║██║   ██║    ██║╚██╗██║██║   ██║   ██║       ╚════██║██╔══╝  ██║╚██╗██║██║  ██║    ██║   ██║██║╚██╗██║    ╚██╗ ██╔╝██║██╔══██╗██║   ██║╚════██║   ██║   ██║   ██║   ██║   ██╔══██║██║     
██████╔╝╚██████╔╝    ██║ ╚████║╚██████╔╝   ██║       ███████║███████╗██║ ╚████║██████╔╝    ╚██████╔╝██║ ╚████║     ╚████╔╝ ██║██║  ██║╚██████╔╝███████║   ██║   ╚██████╔╝   ██║   ██║  ██║███████╗
╚═════╝  ╚═════╝     ╚═╝  ╚═══╝ ╚═════╝    ╚═╝       ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝      ╚═════╝ ╚═╝  ╚═══╝      ╚═══╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝    ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝                                                                                                                                                                                               
    """ + MmColors.endc)
