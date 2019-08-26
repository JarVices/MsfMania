import subprocess


ICON = "test.ico"
RC = 'id ICON "/root/AccessMe/icon/'
RC += ''.join((ICON, '"'))
with open('/root/AccessMe/icon/AccessMe.rc', 'w') as f:
    f.write(RC)

WINDRES = ['windres', '/root/AccessMe/icon/AccessMe.rc', '-O', 'coff', '-o', '/root/AccessMe/icon/AccessMe.res']
subprocess.run(WINDRES, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')