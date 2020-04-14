# MsfMania

MsfMania is a command line tool developed in Python, allowing to automatically produce a source code in C language that will be used to bypass antimalware before executing a metasploit payload.

Version 2.0 is the last one because the hunt for as much FUD as possible is not possible when it comes to open source tools. 
Indeed the argument "Don't send to VirusTotal.com" is not effective, often skids want to send the generated payload to infinity on the site to see if the payload is indeed FUD, except that it is a vicious circle.
This tool will be further developed if you offer me important additions or bug reports.

## Version 2.0
New features:
```
1- Redesign of the graphic charter, banners, exit messages, etc...
2- Restructured source code.
3- Bug correction.
4- Open source license added.
5- Removed predefined payload files and added support to choose any Windows payload available in MsfVenom.
6- MsfMania is 99% scalable.
7- "AccessMe" becomes "MsfMania".
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
2. python3 MsfMania.py
```

## Features
- x86/x64 staged payload meterpreter/shell.
- x86/x64 stageless payload meterpreter/shell.
- Cross-compiler MinGW.
- Polymorphic C source code.
- Strip with MinGW.
- Executable customizable with an icon.
- Local/Remote Thread Shellcode Injection
- Sandbox/Antivirus Evasion
