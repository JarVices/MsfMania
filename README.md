# AccessMe

# Python AV Evasion Tools

AccessMe is a command line tool, developed in Python, which aims to be able to generate executables (32/64 bits) containing a Metasploit or other payload. 
When generating the payload with Msfvenom, the output is incremented in a polymorphic code in C language. 
The main objective being antivirus evasion, this code contains random functions allowing it. 
It also contains evasion functions that the user can configure himself.

# Version 1.1.0.1
New features:
```
1- Restructured source code.
2- Bug correction.
```

# Requirements
```
1. Latest version of Kali Linux
2. The kali-rolling repository
3. Python3
```
# Usage
```
1. python3 setup.py (Execute only one times)
2. python3 AccessMe.py
```
# Features
```
- x86 and x64 staged payload meterpreter.
- x86 and x64 stageless payload meterpreter (windows/x64/meterpreter_reverse_https, windows/x64/meterpreter_reverse_http, 
windows/x64/meterpreter_reverse_tcp, windows/x64/shell_reverse_tcp).
- Cross-compiler MinGW.
- Polymorphic C source code.
- Strip with MinGW
-
```

# C Payload
## Staged
- windows/x64/meterpreter/reverse_https 
- windows/x64/meterpreter/reverse_http
- windows/x64/meterpreter/reverse_tcp
- windows/x64/shell/reverse_tcp
- windows/x86/meterpreter/reverse_https 
- windows/x86/meterpreter/reverse_http
- windows/x86/meterpreter/reverse_tcp
- windows/x86/shell/reverse_tcp
## Stageless
- windows/x64/meterpreter_reverse_https
- windows/x64/meterpreter_reverse_http
- windows/x64/meterpreter_reverse_tcp 
- windows/x64/shell_reverse_tcp
- windows/x86/meterpreter_reverse_https 
- windows/x86/meterpreter_reverse_http
- windows/x86/meterpreter_reverse_tcp
- windows/x86/shell_reverse_tcp
