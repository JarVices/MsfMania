from lib import core
import subprocess
import os
import random


def auto_compile(filename, architecture, icon, require_admin):
    if architecture == "x64":
        if icon != "":

            rc = 'id ICON "icon/' + ''.join((icon, '"\n'))
            rc += rc_info_maker(filename, require_admin)

            with open('tmp/MsfMania.rc', 'w') as f:
                f.write(rc)

            os.system(f"x86_64-w64-mingw32-windres tmp/MsfMania.rc -O coff -o tmp/MsfMania.res && x86_64-w64-mingw32-gcc tmp/source.c tmp/MsfMania.res -s -w -o {filename} && rm tmp/*")

            core.compilation_completed()

        else:

            rc = rc_info_maker(filename, require_admin)

            with open('tmp/MsfMania.rc', 'w') as f:
                f.write(rc)

            os.system(f"x86_64-w64-mingw32-windres tmp/MsfMania.rc -O coff -o tmp/MsfMania.res && x86_64-w64-mingw32-gcc tmp/source.c tmp/MsfMania.res -s -w -o {filename} && rm tmp/*")

            core.compilation_completed()

    elif architecture == "x86":
        if icon != "":

            rc = 'id ICON "icon/' + ''.join((icon, '"\n'))
            rc += rc_info_maker(filename, require_admin)

            with open('tmp/MsfMania.rc', 'w') as f:
                f.write(rc)

            os.system(f"i686-w64-mingw32-windres tmp/MsfMania.rc -O coff -o tmp/MsfMania.res && i686-w64-mingw32-gcc tmp/source.c tmp/MsfMania.res -s -w -o {filename} && rm tmp/*")

            core.compilation_completed()

        else:

            rc = rc_info_maker(filename, require_admin)

            with open('tmp/MsfMania.rc', 'w') as f:
                f.write(rc)

            os.system(f"i686-w64-mingw32-windres tmp/MsfMania.rc -O coff -o tmp/MsfMania.res && i686-w64-mingw32-gcc tmp/source.c tmp/MsfMania.res -s -w -o {filename} && rm tmp/*")

            core.compilation_completed()


def rc_info_maker(filename, require_admin):
    rc_info = ""

    if require_admin == "yes":
        filename = filename.replace("output", "tmp") + '.manifest"'
        rc_info += '1 MANIFEST "' + filename + "\n"
        admin_privs(filename)

    rc_info += "1 VERSIONINFO\n"
    rc_info += "FILEVERSION     " + str(rc_version()) + "," + str(rc_version()) + "," + str(rc_version()) + "\n"
    rc_info += "PRODUCTVERSION  " + str(rc_version()) + "," + str(rc_version()) + "," + str(rc_version()) + "\n"
    rc_info += "BEGIN\n" + 'BLOCK "StringFileInfo"\n'
    rc_info += "BEGIN\n"
    rc_info += 'BLOCK "080904E4"\n'
    rc_info += 'BEGIN\n'
    rc_info += 'VALUE "CompanyName", "' + str(core.varname_creator()) + '"\n'
    rc_info += 'VALUE "FileDescription", "' + str(core.varname_creator()) + '"\n'
    rc_info += 'VALUE "FileVersion", "' + str(rc_version()) + "." + str(rc_version()) + "." + str(rc_version()) + "." + str(rc_version()) + "." + str(rc_version()) + "." + str(rc_version()) + "." + str(rc_version()) + '"\n'
    rc_info += 'VALUE "InternalName", "' + str(core.varname_creator()) + '"\n'
    rc_info += 'VALUE "LegalCopyright", "' + str(core.varname_creator()) + '"\n'
    rc_info += 'VALUE "OriginalFilename", "' + str(core.varname_creator()) + '"\n'
    rc_info += 'VALUE "ProductName", "' + str(core.varname_creator()) + '"\n'
    rc_info += 'VALUE "ProductVersion", "' + str(rc_version()) + "." + str(rc_version()) + "." + str(rc_version()) + "." + str(rc_version()) + "." + str(rc_version()) + "." + str(rc_version()) + "." + str(rc_version()) + '"\n'
    rc_info += 'END\n'
    rc_info += 'END\n'
    rc_info += 'BLOCK "VarFileInfo"\n'
    rc_info += 'BEGIN\n'
    rc_info += 'VALUE "Translation", 0x809, 1252\n'
    rc_info += 'END\n'
    rc_info += 'END\n'
    return rc_info


def rc_version():
    var_rc_version = str(random.randint(1, 999))
    return var_rc_version


def admin_privs(filename):
    manifest = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
    manifest += '<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">\n'
    manifest += '<trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">\n'
    manifest += '<security>\n'
    manifest += '<requestedPrivileges>\n'
    manifest += '<requestedExecutionLevel level="requireAdministrator" uiAccess="false"/>\n'
    manifest += '</requestedPrivileges>\n'
    manifest += '</security>\n'
    manifest += '</trustInfo>\n'
    manifest += '</assembly>\n'

    filename = filename.replace('"', '')
    with open(filename, 'w') as f:
        f.write(manifest)
