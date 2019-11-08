from lib import body, gen, core



#Step 1: Memory alloc 250Mb
#Step 2: Wait 5 seconds
#Step 3: Inject NULL octect
#Step 4: Free Memory
def Decoil():
    print("""
 |------------------------------------------------------------|
 |HARD MEMORY ALLOCATION                                      |
 |------------------------------------------------------------|
 Please enter the number of decoil to add (1-15).
 Press ENTER for ignore this step.
            """)

    Number_Of_Decoil = core.core_input()

    Decoil_while = True

    while Decoil_while:

        if Number_Of_Decoil == "1":

            Memdmp1 = gen.Varname_Creator()
            Tac1 = gen.Varname_Creator()
            Tick1 = gen.Varname_Creator()
            Decoil_Code = "char * " + Memdmp1 + "= NULL;\n"
            Decoil_Code += Memdmp1 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp1 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp1 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick1 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac1 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac1 + " - " + Tick1 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp1 + ");\n"

            return Decoil_Code


        elif Number_Of_Decoil == "2":

            Memdmp1 = gen.Varname_Creator()
            Tac1 = gen.Varname_Creator()
            Tick1 = gen.Varname_Creator()
            Decoil_Code = "char * " + Memdmp1 + "= NULL;\n"
            Decoil_Code += Memdmp1 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp1 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp1 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick1 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac1 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac1 + " - " + Tick1 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp1 + ");\n"

            Memdmp2 = gen.Varname_Creator()
            Tac2 = gen.Varname_Creator()
            Tick2 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp2 + "= NULL;\n"
            Decoil_Code += Memdmp2 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp2 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp2 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick2 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac2 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac2 + " - " + Tick2 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp2 + ");\n"

            return Decoil_Code


        elif Number_Of_Decoil == "3":

            Memdmp1 = gen.Varname_Creator()
            Tac1 = gen.Varname_Creator()
            Tick1 = gen.Varname_Creator()
            Decoil_Code = "char * " + Memdmp1 + "= NULL;\n"
            Decoil_Code += Memdmp1 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp1 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp1 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick1 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac1 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac1 + " - " + Tick1 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp1 + ");\n"

            Memdmp2 = gen.Varname_Creator()
            Tac2 = gen.Varname_Creator()
            Tick2 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp2 + "= NULL;\n"
            Decoil_Code += Memdmp2 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp2 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp2 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick2 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac2 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac2 + " - " + Tick2 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp2 + ");\n"

            Memdmp3 = gen.Varname_Creator()
            Tac3 = gen.Varname_Creator()
            Tick3 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp3 + "= NULL;\n"
            Decoil_Code += Memdmp3 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp3 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp3 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick3 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac3 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac3 + " - " + Tick3 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp3 + ");\n"

            return Decoil_Code


        elif Number_Of_Decoil == "4":

            Memdmp1 = gen.Varname_Creator()
            Tac1 = gen.Varname_Creator()
            Tick1 = gen.Varname_Creator()
            Decoil_Code = "char * " + Memdmp1 + "= NULL;\n"
            Decoil_Code += Memdmp1 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp1 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp1 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick1 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac1 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac1 + " - " + Tick1 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp1 + ");\n"

            Memdmp2 = gen.Varname_Creator()
            Tac2 = gen.Varname_Creator()
            Tick2 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp2 + "= NULL;\n"
            Decoil_Code += Memdmp2 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp2 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp2 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick2 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac2 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac2 + " - " + Tick2 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp2 + ");\n"

            Memdmp3 = gen.Varname_Creator()
            Tac3 = gen.Varname_Creator()
            Tick3 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp3 + "= NULL;\n"
            Decoil_Code += Memdmp3 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp3 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp3 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick3 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac3 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac3 + " - " + Tick3 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp3 + ");\n"

            Memdmp4 = gen.Varname_Creator()
            Tac4 = gen.Varname_Creator()
            Tick4 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp4 + "= NULL;\n"
            Decoil_Code += Memdmp4 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp4 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp4 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick4 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac4 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac4 + " - " + Tick4 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp4 + ");\n"

            return Decoil_Code


        elif Number_Of_Decoil == "5":

            Memdmp1 = gen.Varname_Creator()
            Tac1 = gen.Varname_Creator()
            Tick1 = gen.Varname_Creator()
            Decoil_Code = "char * " + Memdmp1 + "= NULL;\n"
            Decoil_Code += Memdmp1 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp1 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp1 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick1 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac1 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac1 + " - " + Tick1 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp1 + ");\n"

            Memdmp2 = gen.Varname_Creator()
            Tac2 = gen.Varname_Creator()
            Tick2 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp2 + "= NULL;\n"
            Decoil_Code += Memdmp2 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp2 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp2 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick2 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac2 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac2 + " - " + Tick2 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp2 + ");\n"

            Memdmp3 = gen.Varname_Creator()
            Tac3 = gen.Varname_Creator()
            Tick3 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp3 + "= NULL;\n"
            Decoil_Code += Memdmp3 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp3 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp3 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick3 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac3 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac3 + " - " + Tick3 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp3 + ");\n"

            Memdmp4 = gen.Varname_Creator()
            Tac4 = gen.Varname_Creator()
            Tick4 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp4 + "= NULL;\n"
            Decoil_Code += Memdmp4 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp4 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp4 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick4 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac4 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac4 + " - " + Tick4 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp4 + ");\n"

            Memdmp5 = gen.Varname_Creator()
            Tac5 = gen.Varname_Creator()
            Tick5 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp5 + "= NULL;\n"
            Decoil_Code += Memdmp5 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp5 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp5 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick5 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac5 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac5 + " - " + Tick5 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp5 + ");\n"

            return Decoil_Code


        elif Number_Of_Decoil == "6":

            Memdmp1 = gen.Varname_Creator()
            Tac1 = gen.Varname_Creator()
            Tick1 = gen.Varname_Creator()
            Decoil_Code = "char * " + Memdmp1 + "= NULL;\n"
            Decoil_Code += Memdmp1 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp1 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp1 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick1 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac1 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac1 + " - " + Tick1 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp1 + ");\n"

            Memdmp2 = gen.Varname_Creator()
            Tac2 = gen.Varname_Creator()
            Tick2 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp2 + "= NULL;\n"
            Decoil_Code += Memdmp2 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp2 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp2 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick2 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac2 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac2 + " - " + Tick2 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp2 + ");\n"

            Memdmp3 = gen.Varname_Creator()
            Tac3 = gen.Varname_Creator()
            Tick3 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp3 + "= NULL;\n"
            Decoil_Code += Memdmp3 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp3 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp3 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick3 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac3 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac3 + " - " + Tick3 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp3 + ");\n"

            Memdmp4 = gen.Varname_Creator()
            Tac4 = gen.Varname_Creator()
            Tick4 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp4 + "= NULL;\n"
            Decoil_Code += Memdmp4 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp4 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp4 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick4 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac4 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac4 + " - " + Tick4 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp4 + ");\n"

            Memdmp5 = gen.Varname_Creator()
            Tac5 = gen.Varname_Creator()
            Tick5 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp5 + "= NULL;\n"
            Decoil_Code += Memdmp5 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp5 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp5 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick5 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac5 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac5 + " - " + Tick5 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp5 + ");\n"

            Memdmp6 = gen.Varname_Creator()
            Tac6 = gen.Varname_Creator()
            Tick6 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp6 + "= NULL;\n"
            Decoil_Code += Memdmp6 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp6 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp6 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick6 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac6 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac6 + " - " + Tick6 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp6 + ");\n"

            return Decoil_Code


        elif Number_Of_Decoil == "7":

            Memdmp1 = gen.Varname_Creator()
            Tac1 = gen.Varname_Creator()
            Tick1 = gen.Varname_Creator()
            Decoil_Code = "char * " + Memdmp1 + "= NULL;\n"
            Decoil_Code += Memdmp1 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp1 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp1 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick1 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac1 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac1 + " - " + Tick1 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp1 + ");\n"

            Memdmp2 = gen.Varname_Creator()
            Tac2 = gen.Varname_Creator()
            Tick2 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp2 + "= NULL;\n"
            Decoil_Code += Memdmp2 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp2 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp2 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick2 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac2 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac2 + " - " + Tick2 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp2 + ");\n"

            Memdmp3 = gen.Varname_Creator()
            Tac3 = gen.Varname_Creator()
            Tick3 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp3 + "= NULL;\n"
            Decoil_Code += Memdmp3 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp3 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp3 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick3 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac3 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac3 + " - " + Tick3 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp3 + ");\n"

            Memdmp4 = gen.Varname_Creator()
            Tac4 = gen.Varname_Creator()
            Tick4 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp4 + "= NULL;\n"
            Decoil_Code += Memdmp4 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp4 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp4 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick4 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac4 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac4 + " - " + Tick4 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp4 + ");\n"

            Memdmp5 = gen.Varname_Creator()
            Tac5 = gen.Varname_Creator()
            Tick5 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp5 + "= NULL;\n"
            Decoil_Code += Memdmp5 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp5 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp5 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick5 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac5 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac5 + " - " + Tick5 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp5 + ");\n"

            Memdmp6 = gen.Varname_Creator()
            Tac6 = gen.Varname_Creator()
            Tick6 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp6 + "= NULL;\n"
            Decoil_Code += Memdmp6 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp6 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp6 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick6 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac6 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac6 + " - " + Tick6 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp6 + ");\n"

            Memdmp7 = gen.Varname_Creator()
            Tac7 = gen.Varname_Creator()
            Tick7 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp7 + "= NULL;\n"
            Decoil_Code += Memdmp7 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp7 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp7 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick7 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac7 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac7 + " - " + Tick7 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp7 + ");\n"

            return Decoil_Code


        elif Number_Of_Decoil == "8":

            Memdmp1 = gen.Varname_Creator()
            Tac1 = gen.Varname_Creator()
            Tick1 = gen.Varname_Creator()
            Decoil_Code = "char * " + Memdmp1 + "= NULL;\n"
            Decoil_Code += Memdmp1 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp1 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp1 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick1 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac1 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac1 + " - " + Tick1 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp1 + ");\n"

            Memdmp2 = gen.Varname_Creator()
            Tac2 = gen.Varname_Creator()
            Tick2 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp2 + "= NULL;\n"
            Decoil_Code += Memdmp2 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp2 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp2 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick2 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac2 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac2 + " - " + Tick2 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp2 + ");\n"

            Memdmp3 = gen.Varname_Creator()
            Tac3 = gen.Varname_Creator()
            Tick3 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp3 + "= NULL;\n"
            Decoil_Code += Memdmp3 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp3 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp3 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick3 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac3 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac3 + " - " + Tick3 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp3 + ");\n"

            Memdmp4 = gen.Varname_Creator()
            Tac4 = gen.Varname_Creator()
            Tick4 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp4 + "= NULL;\n"
            Decoil_Code += Memdmp4 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp4 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp4 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick4 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac4 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac4 + " - " + Tick4 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp4 + ");\n"

            Memdmp5 = gen.Varname_Creator()
            Tac5 = gen.Varname_Creator()
            Tick5 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp5 + "= NULL;\n"
            Decoil_Code += Memdmp5 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp5 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp5 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick5 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac5 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac5 + " - " + Tick5 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp5 + ");\n"

            Memdmp6 = gen.Varname_Creator()
            Tac6 = gen.Varname_Creator()
            Tick6 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp6 + "= NULL;\n"
            Decoil_Code += Memdmp6 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp6 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp6 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick6 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac6 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac6 + " - " + Tick6 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp6 + ");\n"

            Memdmp7 = gen.Varname_Creator()
            Tac7 = gen.Varname_Creator()
            Tick7 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp7 + "= NULL;\n"
            Decoil_Code += Memdmp7 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp7 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp7 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick7 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac7 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac7 + " - " + Tick7 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp7 + ");\n"

            Memdmp8 = gen.Varname_Creator()
            Tac8 = gen.Varname_Creator()
            Tick8 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp8 + "= NULL;\n"
            Decoil_Code += Memdmp8 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp8 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp8 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick8 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac8 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac8 + " - " + Tick8 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp8 + ");\n"

            return Decoil_Code


        elif Number_Of_Decoil == "9":

            Memdmp1 = gen.Varname_Creator()
            Tac1 = gen.Varname_Creator()
            Tick1 = gen.Varname_Creator()
            Decoil_Code = "char * " + Memdmp1 + "= NULL;\n"
            Decoil_Code += Memdmp1 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp1 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp1 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick1 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac1 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac1 + " - " + Tick1 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp1 + ");\n"

            Memdmp2 = gen.Varname_Creator()
            Tac2 = gen.Varname_Creator()
            Tick2 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp2 + "= NULL;\n"
            Decoil_Code += Memdmp2 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp2 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp2 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick2 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac2 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac2 + " - " + Tick2 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp2 + ");\n"

            Memdmp3 = gen.Varname_Creator()
            Tac3 = gen.Varname_Creator()
            Tick3 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp3 + "= NULL;\n"
            Decoil_Code += Memdmp3 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp3 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp3 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick3 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac3 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac3 + " - " + Tick3 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp3 + ");\n"

            Memdmp4 = gen.Varname_Creator()
            Tac4 = gen.Varname_Creator()
            Tick4 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp4 + "= NULL;\n"
            Decoil_Code += Memdmp4 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp4 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp4 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick4 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac4 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac4 + " - " + Tick4 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp4 + ");\n"

            Memdmp5 = gen.Varname_Creator()
            Tac5 = gen.Varname_Creator()
            Tick5 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp5 + "= NULL;\n"
            Decoil_Code += Memdmp5 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp5 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp5 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick5 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac5 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac5 + " - " + Tick5 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp5 + ");\n"

            Memdmp6 = gen.Varname_Creator()
            Tac6 = gen.Varname_Creator()
            Tick6 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp6 + "= NULL;\n"
            Decoil_Code += Memdmp6 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp6 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp6 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick6 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac6 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac6 + " - " + Tick6 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp6 + ");\n"

            Memdmp7 = gen.Varname_Creator()
            Tac7 = gen.Varname_Creator()
            Tick7 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp7 + "= NULL;\n"
            Decoil_Code += Memdmp7 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp7 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp7 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick7 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac7 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac7 + " - " + Tick7 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp7 + ");\n"

            Memdmp8 = gen.Varname_Creator()
            Tac8 = gen.Varname_Creator()
            Tick8 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp8 + "= NULL;\n"
            Decoil_Code += Memdmp8 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp8 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp8 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick8 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac8 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac8 + " - " + Tick8 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp8 + ");\n"

            Memdmp9 = gen.Varname_Creator()
            Tac9 = gen.Varname_Creator()
            Tick9 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp9 + "= NULL;\n"
            Decoil_Code += Memdmp9 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp9 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp9 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick9 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac9 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac9 + " - " + Tick9 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp9 + ");\n"

            return Decoil_Code


        elif Number_Of_Decoil == "10":

            Memdmp1 = gen.Varname_Creator()
            Tac1 = gen.Varname_Creator()
            Tick1 = gen.Varname_Creator()
            Decoil_Code = "char * " + Memdmp1 + "= NULL;\n"
            Decoil_Code += Memdmp1 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp1 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp1 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick1 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac1 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac1 + " - " + Tick1 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp1 + ");\n"

            Memdmp2 = gen.Varname_Creator()
            Tac2 = gen.Varname_Creator()
            Tick2 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp2 + "= NULL;\n"
            Decoil_Code += Memdmp2 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp2 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp2 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick2 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac2 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac2 + " - " + Tick2 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp2 + ");\n"

            Memdmp3 = gen.Varname_Creator()
            Tac3 = gen.Varname_Creator()
            Tick3 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp3 + "= NULL;\n"
            Decoil_Code += Memdmp3 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp3 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp3 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick3 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac3 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac3 + " - " + Tick3 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp3 + ");\n"

            Memdmp4 = gen.Varname_Creator()
            Tac4 = gen.Varname_Creator()
            Tick4 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp4 + "= NULL;\n"
            Decoil_Code += Memdmp4 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp4 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp4 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick4 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac4 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac4 + " - " + Tick4 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp4 + ");\n"

            Memdmp5 = gen.Varname_Creator()
            Tac5 = gen.Varname_Creator()
            Tick5 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp5 + "= NULL;\n"
            Decoil_Code += Memdmp5 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp5 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp5 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick5 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac5 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac5 + " - " + Tick5 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp5 + ");\n"

            Memdmp6 = gen.Varname_Creator()
            Tac6 = gen.Varname_Creator()
            Tick6 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp6 + "= NULL;\n"
            Decoil_Code += Memdmp6 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp6 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp6 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick6 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac6 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac6 + " - " + Tick6 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp6 + ");\n"

            Memdmp7 = gen.Varname_Creator()
            Tac7 = gen.Varname_Creator()
            Tick7 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp7 + "= NULL;\n"
            Decoil_Code += Memdmp7 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp7 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp7 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick7 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac7 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac7 + " - " + Tick7 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp7 + ");\n"

            Memdmp8 = gen.Varname_Creator()
            Tac8 = gen.Varname_Creator()
            Tick8 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp8 + "= NULL;\n"
            Decoil_Code += Memdmp8 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp8 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp8 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick8 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac8 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac8 + " - " + Tick8 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp8 + ");\n"

            Memdmp9 = gen.Varname_Creator()
            Tac9 = gen.Varname_Creator()
            Tick9 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp9 + "= NULL;\n"
            Decoil_Code += Memdmp9 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp9 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp9 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick9 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac9 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac9 + " - " + Tick9 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp9 + ");\n"

            Memdmp10 = gen.Varname_Creator()
            Tac10 = gen.Varname_Creator()
            Tick10 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp10 + "= NULL;\n"
            Decoil_Code += Memdmp10 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp10 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp10 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick10 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac10 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac10 + " - " + Tick10 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp10 + ");\n"

            return Decoil_Code


        elif Number_Of_Decoil == "11":

            Memdmp1 = gen.Varname_Creator()
            Tac1 = gen.Varname_Creator()
            Tick1 = gen.Varname_Creator()
            Decoil_Code = "char * " + Memdmp1 + "= NULL;\n"
            Decoil_Code += Memdmp1 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp1 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp1 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick1 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac1 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac1 + " - " + Tick1 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp1 + ");\n"

            Memdmp2 = gen.Varname_Creator()
            Tac2 = gen.Varname_Creator()
            Tick2 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp2 + "= NULL;\n"
            Decoil_Code += Memdmp2 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp2 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp2 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick2 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac2 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac2 + " - " + Tick2 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp2 + ");\n"

            Memdmp3 = gen.Varname_Creator()
            Tac3 = gen.Varname_Creator()
            Tick3 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp3 + "= NULL;\n"
            Decoil_Code += Memdmp3 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp3 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp3 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick3 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac3 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac3 + " - " + Tick3 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp3 + ");\n"

            Memdmp4 = gen.Varname_Creator()
            Tac4 = gen.Varname_Creator()
            Tick4 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp4 + "= NULL;\n"
            Decoil_Code += Memdmp4 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp4 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp4 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick4 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac4 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac4 + " - " + Tick4 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp4 + ");\n"

            Memdmp5 = gen.Varname_Creator()
            Tac5 = gen.Varname_Creator()
            Tick5 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp5 + "= NULL;\n"
            Decoil_Code += Memdmp5 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp5 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp5 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick5 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac5 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac5 + " - " + Tick5 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp5 + ");\n"

            Memdmp6 = gen.Varname_Creator()
            Tac6 = gen.Varname_Creator()
            Tick6 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp6 + "= NULL;\n"
            Decoil_Code += Memdmp6 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp6 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp6 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick6 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac6 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac6 + " - " + Tick6 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp6 + ");\n"

            Memdmp7 = gen.Varname_Creator()
            Tac7 = gen.Varname_Creator()
            Tick7 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp7 + "= NULL;\n"
            Decoil_Code += Memdmp7 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp7 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp7 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick7 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac7 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac7 + " - " + Tick7 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp7 + ");\n"

            Memdmp8 = gen.Varname_Creator()
            Tac8 = gen.Varname_Creator()
            Tick8 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp8 + "= NULL;\n"
            Decoil_Code += Memdmp8 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp8 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp8 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick8 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac8 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac8 + " - " + Tick8 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp8 + ");\n"

            Memdmp9 = gen.Varname_Creator()
            Tac9 = gen.Varname_Creator()
            Tick9 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp9 + "= NULL;\n"
            Decoil_Code += Memdmp9 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp9 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp9 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick9 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac9 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac9 + " - " + Tick9 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp9 + ");\n"

            Memdmp10 = gen.Varname_Creator()
            Tac10 = gen.Varname_Creator()
            Tick10 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp10 + "= NULL;\n"
            Decoil_Code += Memdmp10 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp10 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp10 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick10 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac10 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac10 + " - " + Tick10 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp10 + ");\n"

            Memdmp11 = gen.Varname_Creator()
            Tac11 = gen.Varname_Creator()
            Tick11 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp11 + "= NULL;\n"
            Decoil_Code += Memdmp11 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp11 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp11 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick11 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac11 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac11 + " - " + Tick11 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp11 + ");\n"

            return Decoil_Code


        elif Number_Of_Decoil == "12":

            Memdmp1 = gen.Varname_Creator()
            Tac1 = gen.Varname_Creator()
            Tick1 = gen.Varname_Creator()
            Decoil_Code = "char * " + Memdmp1 + "= NULL;\n"
            Decoil_Code += Memdmp1 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp1 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp1 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick1 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac1 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac1 + " - " + Tick1 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp1 + ");\n"

            Memdmp2 = gen.Varname_Creator()
            Tac2 = gen.Varname_Creator()
            Tick2 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp2 + "= NULL;\n"
            Decoil_Code += Memdmp2 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp2 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp2 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick2 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac2 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac2 + " - " + Tick2 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp2 + ");\n"

            Memdmp3 = gen.Varname_Creator()
            Tac3 = gen.Varname_Creator()
            Tick3 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp3 + "= NULL;\n"
            Decoil_Code += Memdmp3 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp3 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp3 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick3 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac3 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac3 + " - " + Tick3 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp3 + ");\n"

            Memdmp4 = gen.Varname_Creator()
            Tac4 = gen.Varname_Creator()
            Tick4 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp4 + "= NULL;\n"
            Decoil_Code += Memdmp4 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp4 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp4 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick4 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac4 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac4 + " - " + Tick4 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp4 + ");\n"

            Memdmp5 = gen.Varname_Creator()
            Tac5 = gen.Varname_Creator()
            Tick5 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp5 + "= NULL;\n"
            Decoil_Code += Memdmp5 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp5 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp5 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick5 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac5 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac5 + " - " + Tick5 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp5 + ");\n"

            Memdmp6 = gen.Varname_Creator()
            Tac6 = gen.Varname_Creator()
            Tick6 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp6 + "= NULL;\n"
            Decoil_Code += Memdmp6 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp6 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp6 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick6 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac6 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac6 + " - " + Tick6 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp6 + ");\n"

            Memdmp7 = gen.Varname_Creator()
            Tac7 = gen.Varname_Creator()
            Tick7 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp7 + "= NULL;\n"
            Decoil_Code += Memdmp7 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp7 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp7 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick7 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac7 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac7 + " - " + Tick7 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp7 + ");\n"

            Memdmp8 = gen.Varname_Creator()
            Tac8 = gen.Varname_Creator()
            Tick8 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp8 + "= NULL;\n"
            Decoil_Code += Memdmp8 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp8 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp8 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick8 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac8 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac8 + " - " + Tick8 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp8 + ");\n"

            Memdmp9 = gen.Varname_Creator()
            Tac9 = gen.Varname_Creator()
            Tick9 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp9 + "= NULL;\n"
            Decoil_Code += Memdmp9 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp9 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp9 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick9 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac9 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac9 + " - " + Tick9 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp9 + ");\n"

            Memdmp10 = gen.Varname_Creator()
            Tac10 = gen.Varname_Creator()
            Tick10 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp10 + "= NULL;\n"
            Decoil_Code += Memdmp10 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp10 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp10 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick10 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac10 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac10 + " - " + Tick10 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp10 + ");\n"

            Memdmp11 = gen.Varname_Creator()
            Tac11 = gen.Varname_Creator()
            Tick11 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp11 + "= NULL;\n"
            Decoil_Code += Memdmp11 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp11 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp11 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick11 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac11 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac11 + " - " + Tick11 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp11 + ");\n"

            Memdmp12 = gen.Varname_Creator()
            Tac12 = gen.Varname_Creator()
            Tick12 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp12 + "= NULL;\n"
            Decoil_Code += Memdmp12 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp12 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp12 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick12 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac12 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac12 + " - " + Tick12 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp12 + ");\n"

            return Decoil_Code


        elif Number_Of_Decoil == "13":

            Memdmp1 = gen.Varname_Creator()
            Tac1 = gen.Varname_Creator()
            Tick1 = gen.Varname_Creator()
            Decoil_Code = "char * " + Memdmp1 + "= NULL;\n"
            Decoil_Code += Memdmp1 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp1 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp1 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick1 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac1 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac1 + " - " + Tick1 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp1 + ");\n"

            Memdmp2 = gen.Varname_Creator()
            Tac2 = gen.Varname_Creator()
            Tick2 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp2 + "= NULL;\n"
            Decoil_Code += Memdmp2 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp2 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp2 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick2 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac2 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac2 + " - " + Tick2 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp2 + ");\n"

            Memdmp3 = gen.Varname_Creator()
            Tac3 = gen.Varname_Creator()
            Tick3 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp3 + "= NULL;\n"
            Decoil_Code += Memdmp3 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp3 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp3 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick3 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac3 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac3 + " - " + Tick3 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp3 + ");\n"

            Memdmp4 = gen.Varname_Creator()
            Tac4 = gen.Varname_Creator()
            Tick4 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp4 + "= NULL;\n"
            Decoil_Code += Memdmp4 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp4 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp4 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick4 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac4 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac4 + " - " + Tick4 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp4 + ");\n"

            Memdmp5 = gen.Varname_Creator()
            Tac5 = gen.Varname_Creator()
            Tick5 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp5 + "= NULL;\n"
            Decoil_Code += Memdmp5 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp5 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp5 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick5 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac5 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac5 + " - " + Tick5 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp5 + ");\n"

            Memdmp6 = gen.Varname_Creator()
            Tac6 = gen.Varname_Creator()
            Tick6 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp6 + "= NULL;\n"
            Decoil_Code += Memdmp6 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp6 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp6 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick6 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac6 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac6 + " - " + Tick6 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp6 + ");\n"

            Memdmp7 = gen.Varname_Creator()
            Tac7 = gen.Varname_Creator()
            Tick7 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp7 + "= NULL;\n"
            Decoil_Code += Memdmp7 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp7 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp7 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick7 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac7 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac7 + " - " + Tick7 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp7 + ");\n"

            Memdmp8 = gen.Varname_Creator()
            Tac8 = gen.Varname_Creator()
            Tick8 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp8 + "= NULL;\n"
            Decoil_Code += Memdmp8 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp8 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp8 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick8 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac8 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac8 + " - " + Tick8 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp8 + ");\n"

            Memdmp9 = gen.Varname_Creator()
            Tac9 = gen.Varname_Creator()
            Tick9 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp9 + "= NULL;\n"
            Decoil_Code += Memdmp9 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp9 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp9 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick9 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac9 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac9 + " - " + Tick9 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp9 + ");\n"

            Memdmp10 = gen.Varname_Creator()
            Tac10 = gen.Varname_Creator()
            Tick10 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp10 + "= NULL;\n"
            Decoil_Code += Memdmp10 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp10 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp10 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick10 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac10 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac10 + " - " + Tick10 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp10 + ");\n"

            Memdmp11 = gen.Varname_Creator()
            Tac11 = gen.Varname_Creator()
            Tick11 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp11 + "= NULL;\n"
            Decoil_Code += Memdmp11 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp11 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp11 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick11 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac11 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac11 + " - " + Tick11 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp11 + ");\n"

            Memdmp12 = gen.Varname_Creator()
            Tac12 = gen.Varname_Creator()
            Tick12 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp12 + "= NULL;\n"
            Decoil_Code += Memdmp12 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp12 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp12 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick12 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac12 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac12 + " - " + Tick12 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp12 + ");\n"

            Memdmp13 = gen.Varname_Creator()
            Tac13 = gen.Varname_Creator()
            Tick13 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp13 + "= NULL;\n"
            Decoil_Code += Memdmp13 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp13 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp13 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick13 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac13 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac13 + " - " + Tick13 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp13 + ");\n"

            return Decoil_Code


        elif Number_Of_Decoil == "14":

            Memdmp1 = gen.Varname_Creator()
            Tac1 = gen.Varname_Creator()
            Tick1 = gen.Varname_Creator()
            Decoil_Code = "char * " + Memdmp1 + "= NULL;\n"
            Decoil_Code += Memdmp1 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp1 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp1 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick1 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac1 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac1 + " - " + Tick1 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp1 + ");\n"

            Memdmp2 = gen.Varname_Creator()
            Tac2 = gen.Varname_Creator()
            Tick2 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp2 + "= NULL;\n"
            Decoil_Code += Memdmp2 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp2 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp2 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick2 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac2 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac2 + " - " + Tick2 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp2 + ");\n"

            Memdmp3 = gen.Varname_Creator()
            Tac3 = gen.Varname_Creator()
            Tick3 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp3 + "= NULL;\n"
            Decoil_Code += Memdmp3 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp3 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp3 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick3 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac3 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac3 + " - " + Tick3 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp3 + ");\n"

            Memdmp4 = gen.Varname_Creator()
            Tac4 = gen.Varname_Creator()
            Tick4 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp4 + "= NULL;\n"
            Decoil_Code += Memdmp4 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp4 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp4 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick4 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac4 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac4 + " - " + Tick4 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp4 + ");\n"

            Memdmp5 = gen.Varname_Creator()
            Tac5 = gen.Varname_Creator()
            Tick5 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp5 + "= NULL;\n"
            Decoil_Code += Memdmp5 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp5 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp5 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick5 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac5 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac5 + " - " + Tick5 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp5 + ");\n"

            Memdmp6 = gen.Varname_Creator()
            Tac6 = gen.Varname_Creator()
            Tick6 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp6 + "= NULL;\n"
            Decoil_Code += Memdmp6 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp6 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp6 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick6 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac6 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac6 + " - " + Tick6 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp6 + ");\n"

            Memdmp7 = gen.Varname_Creator()
            Tac7 = gen.Varname_Creator()
            Tick7 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp7 + "= NULL;\n"
            Decoil_Code += Memdmp7 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp7 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp7 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick7 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac7 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac7 + " - " + Tick7 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp7 + ");\n"

            Memdmp8 = gen.Varname_Creator()
            Tac8 = gen.Varname_Creator()
            Tick8 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp8 + "= NULL;\n"
            Decoil_Code += Memdmp8 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp8 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp8 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick8 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac8 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac8 + " - " + Tick8 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp8 + ");\n"

            Memdmp9 = gen.Varname_Creator()
            Tac9 = gen.Varname_Creator()
            Tick9 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp9 + "= NULL;\n"
            Decoil_Code += Memdmp9 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp9 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp9 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick9 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac9 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac9 + " - " + Tick9 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp9 + ");\n"

            Memdmp10 = gen.Varname_Creator()
            Tac10 = gen.Varname_Creator()
            Tick10 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp10 + "= NULL;\n"
            Decoil_Code += Memdmp10 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp10 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp10 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick10 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac10 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac10 + " - " + Tick10 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp10 + ");\n"

            Memdmp11 = gen.Varname_Creator()
            Tac11 = gen.Varname_Creator()
            Tick11 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp11 + "= NULL;\n"
            Decoil_Code += Memdmp11 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp11 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp11 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick11 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac11 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac11 + " - " + Tick11 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp11 + ");\n"

            Memdmp12 = gen.Varname_Creator()
            Tac12 = gen.Varname_Creator()
            Tick12 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp12 + "= NULL;\n"
            Decoil_Code += Memdmp12 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp12 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp12 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick12 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac12 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac12 + " - " + Tick12 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp12 + ");\n"

            Memdmp13 = gen.Varname_Creator()
            Tac13 = gen.Varname_Creator()
            Tick13 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp13 + "= NULL;\n"
            Decoil_Code += Memdmp13 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp13 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp13 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick13 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac13 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac13 + " - " + Tick13 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp13 + ");\n"

            Memdmp14 = gen.Varname_Creator()
            Tac14 = gen.Varname_Creator()
            Tick14 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp14 + "= NULL;\n"
            Decoil_Code += Memdmp14+ " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp14 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp14 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick14 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac14 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac14 + " - " + Tick14 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp14 + ");\n"

            return Decoil_Code


        elif Number_Of_Decoil == "15":

            Memdmp1 = gen.Varname_Creator()
            Tac1 = gen.Varname_Creator()
            Tick1 = gen.Varname_Creator()
            Decoil_Code = "char * " + Memdmp1 + "= NULL;\n"
            Decoil_Code += Memdmp1 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp1 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp1 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick1 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac1 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac1 + " - " + Tick1 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp1 + ");\n"

            Memdmp2 = gen.Varname_Creator()
            Tac2 = gen.Varname_Creator()
            Tick2 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp2 + "= NULL;\n"
            Decoil_Code += Memdmp2 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp2 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp2 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick2 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac2 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac2 + " - " + Tick2 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp2 + ");\n"

            Memdmp3 = gen.Varname_Creator()
            Tac3 = gen.Varname_Creator()
            Tick3 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp3 + "= NULL;\n"
            Decoil_Code += Memdmp3 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp3 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp3 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick3 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac3 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac3 + " - " + Tick3 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp3 + ");\n"

            Memdmp4 = gen.Varname_Creator()
            Tac4 = gen.Varname_Creator()
            Tick4 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp4 + "= NULL;\n"
            Decoil_Code += Memdmp4 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp4 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp4 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick4 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac4 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac4 + " - " + Tick4 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp4 + ");\n"

            Memdmp5 = gen.Varname_Creator()
            Tac5 = gen.Varname_Creator()
            Tick5 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp5 + "= NULL;\n"
            Decoil_Code += Memdmp5 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp5 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp5 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick5 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac5 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac5 + " - " + Tick5 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp5 + ");\n"

            Memdmp6 = gen.Varname_Creator()
            Tac6 = gen.Varname_Creator()
            Tick6 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp6 + "= NULL;\n"
            Decoil_Code += Memdmp6 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp6 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp6 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick6 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac6 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac6 + " - " + Tick6 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp6 + ");\n"

            Memdmp7 = gen.Varname_Creator()
            Tac7 = gen.Varname_Creator()
            Tick7 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp7 + "= NULL;\n"
            Decoil_Code += Memdmp7 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp7 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp7 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick7 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac7 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac7 + " - " + Tick7 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp7 + ");\n"

            Memdmp8 = gen.Varname_Creator()
            Tac8 = gen.Varname_Creator()
            Tick8 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp8 + "= NULL;\n"
            Decoil_Code += Memdmp8 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp8 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp8 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick8 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac8 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac8 + " - " + Tick8 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp8 + ");\n"

            Memdmp9 = gen.Varname_Creator()
            Tac9 = gen.Varname_Creator()
            Tick9 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp9 + "= NULL;\n"
            Decoil_Code += Memdmp9 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp9 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp9 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick9 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac9 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac9 + " - " + Tick9 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp9 + ");\n"

            Memdmp10 = gen.Varname_Creator()
            Tac10 = gen.Varname_Creator()
            Tick10 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp10 + "= NULL;\n"
            Decoil_Code += Memdmp10 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp10 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp10 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick10 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac10 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac10 + " - " + Tick10 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp10 + ");\n"

            Memdmp11 = gen.Varname_Creator()
            Tac11 = gen.Varname_Creator()
            Tick11 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp11 + "= NULL;\n"
            Decoil_Code += Memdmp11 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp11 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp11 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick11 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac11 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac11 + " - " + Tick11 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp11 + ");\n"

            Memdmp12 = gen.Varname_Creator()
            Tac12 = gen.Varname_Creator()
            Tick12 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp12 + "= NULL;\n"
            Decoil_Code += Memdmp12 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp12 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp12 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick12 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac12 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac12 + " - " + Tick12 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp12 + ");\n"

            Memdmp13 = gen.Varname_Creator()
            Tac13 = gen.Varname_Creator()
            Tick13 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp13 + "= NULL;\n"
            Decoil_Code += Memdmp13 + " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp13 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp13 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick13 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac13 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac13 + " - " + Tick13 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp13 + ");\n"

            Memdmp14 = gen.Varname_Creator()
            Tac14 = gen.Varname_Creator()
            Tick14 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp14 + "= NULL;\n"
            Decoil_Code += Memdmp14+ " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp14 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp14 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick14 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac14 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac14 + " - " + Tick14 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp14 + ");\n"

            Memdmp15 = gen.Varname_Creator()
            Tac15 = gen.Varname_Creator()
            Tick15 = gen.Varname_Creator()
            Decoil_Code += "char * " + Memdmp15 + "= NULL;\n"
            Decoil_Code += Memdmp15+ " = (char *)malloc(250000000);\n"
            Decoil_Code += "if (" + Memdmp15 + " != NULL) {\n"
            Decoil_Code += "memset(" + Memdmp15 + ", 00, 250000000);}\n"
            Decoil_Code += "int " + Tick15 + " = GetTickCount();\n"
            Decoil_Code += "Sleep(5000);\n"
            Decoil_Code += "int " + Tac15 + " = GetTickCount();\n"
            Decoil_Code += "if ((" + Tac15 + " - " + Tick15 + ") < 1000) {return 0;}\n"
            Decoil_Code += "free(" + Memdmp15 + ");\n"

            return Decoil_Code