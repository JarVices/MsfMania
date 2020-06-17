from lib import core
import random


def fake_u(value):

    number_of_decoy = value

    if number_of_decoy != "":

        transform_to_int = int(number_of_decoy)

        number_of_decoy = 0
        decoy_code = ""

        while number_of_decoy != transform_to_int:
            number_of_decoy += 1

            memdmp1 = core.varname_creator()
            tac1 = core.varname_creator()
            tick1 = core.varname_creator()

            memdmp1_value = str(random.randint(70000000, 130000000))
            decoy_code += "char * " + memdmp1 + "= NULL;\n"
            decoy_code += memdmp1 + " = (char *)malloc(" + memdmp1_value + ");\n"
            decoy_code += "if (" + memdmp1 + " != NULL) {\n"
            decoy_code += "memset(" + memdmp1 + ", 00, " + memdmp1_value + ");}\n"
            decoy_code += "int " + tick1 + " = GetTickCount();\n"
            decoy_code += "Sleep(1000);\n"
            decoy_code += "int " + tac1 + " = GetTickCount();\n"
            decoy_code += "if ((" + tac1 + " - " + tick1 + ") < 1000) {exit(0);}\n"
            decoy_code += "free(" + memdmp1 + ");\n\n"

        core.decoy_added()

        return decoy_code

    elif number_of_decoy == "":
        return str('printf("' + core.varname_creator() + '");\n')
