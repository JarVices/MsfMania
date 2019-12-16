# MsfMania

## Python AV Evasion Tools

MsfMania is a command line tool, developed in Python, which aims to be able to generate executables (32/64 bits) containing a Metasploit or other payload. 
When generating the payload with Msfvenom, the output is incremented in a polymorphic code in C language. 
The main objective being antivirus evasion, this code contains random functions allowing it. 
It also contains evasion functions that the user can configure himself.

## Version 1.2
New features:
```
1- You can choose either "Local Thread Shellcode Injection" or "Remote Thread Shellcode Injection".
2- Restructured source code.
3- Bug correction.
```

## Requirements
```
1. Latest version of Kali Linux
2. The kali-rolling repository
3. Python3
```

## Usage
```
1. python3 setup.py (Execute only one times)
2. python3 NsfVenom.py
```

## Features
- x86/x64 staged payload meterpreter/shell.
- x86/x64 stageless payload meterpreter/shell.
- Cross-compiler MinGW.
- Polymorphic C source code.
- Strip with MinGW.
- Customize the executable with an icon.
- Local/Remote Thread Shellcode Injection
- Sandbox Evasion 
- Antivirus Evasion

## C Payload
### Staged
```
- windows/x64/meterpreter/reverse_https 
- windows/x64/meterpreter/reverse_http
- windows/x64/meterpreter/reverse_tcp
- windows/x64/shell/reverse_tcp

- windows/x86/meterpreter/reverse_https 
- windows/x86/meterpreter/reverse_http
- windows/x86/meterpreter/reverse_tcp
- windows/x86/shell/reverse_tcp
```
### Stageless
```
- windows/x64/meterpreter_reverse_https
- windows/x64/meterpreter_reverse_http
- windows/x64/meterpreter_reverse_tcp 
- windows/x64/shell_reverse_tcp

- windows/x86/meterpreter_reverse_https 
- windows/x86/meterpreter_reverse_http
- windows/x86/meterpreter_reverse_tcp
- windows/x86/shell_reverse_tcp
```
