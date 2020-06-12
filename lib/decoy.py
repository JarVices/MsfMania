from lib import core
import random


def FAKE_U(VALUE):

    NUMBER_OF_DECOY = VALUE

    if NUMBER_OF_DECOY != "":

        TRANSFORM_TO_INT = int(NUMBER_OF_DECOY)

        NUMBER_OF_DECOY = 0
        DECOY_CODE = ""

        while NUMBER_OF_DECOY != TRANSFORM_TO_INT:
            NUMBER_OF_DECOY += 1

            MEMDMP1 = core.VARNAME_CREATOR()
            TAC1 = core.VARNAME_CREATOR()
            TICK1 = core.VARNAME_CREATOR()

            MEMDMP1_VALUE = str(random.randint(70000000, 130000000))
            DECOY_CODE += "char * " + MEMDMP1 + "= NULL;\n"
            DECOY_CODE += MEMDMP1 + " = (char *)malloc(" + MEMDMP1_VALUE + ");\n"
            DECOY_CODE += "if (" + MEMDMP1 + " != NULL) {\n"
            DECOY_CODE += "memset(" + MEMDMP1 + ", 00, " + MEMDMP1_VALUE + ");}\n"
            DECOY_CODE += "int " + TICK1 + " = GetTickCount();\n"
            DECOY_CODE += "Sleep(1000);\n"
            DECOY_CODE += "int " + TAC1 + " = GetTickCount();\n"
            DECOY_CODE += "if ((" + TAC1 + " - " + TICK1 + ") < 1000) {exit(0);}\n"
            DECOY_CODE += "free(" + MEMDMP1 + ");\n\n"

        core.DECOY_ADDED()

        return DECOY_CODE

    elif NUMBER_OF_DECOY == "":
        return 'printf("nothing");\n'
