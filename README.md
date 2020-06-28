# MsfMania
MsfMania is a command line tool developed in Python, allowing to automatically produce a source code in C language that will be used to bypass antimalware before executing a metasploit payload.

## Note that
I don't put an example of use so that the skids don't know how to use the tool. They will have to do without a basic tutorial ;p.
I leave only 4 sandbox escape functions because too many sandboxes kill the sandbox. I tried to put 18 then 12 then 4 and the result is better. It is necessary to look for new techniques and for a public tool I would prefer to keep things still unknown.
I thank @oddc0de for its junkcode functions < 3.
I thank @paranoidninja for its CarbonCopy tool.

## Version 2.3
New features:
```
1- Code fully reviewed and redrafted
2- Perfomance increase
3- A junkcode injection system has been added, it also allows to create functions containing junkcode (junkfunc).
4- Physical resources used with junkcodes can be duplicated with the intensity mode.
5- You can specify your own MsfVenom parameters.
6- You can now disable the Windows Firewall and updates.
7- You can steal a certificate and sign your executable with it.
8- Massive bug fix
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

## Features
- Polymorphic C/C++ source code.
- x86/x64 staged/stageless windows payload meterpreter/shell.
- Local/Remote Thread Shellcode Injection.
- XOR encryption based key lenght.
- Sandbox/Antivirus Evasion.
- Junkcode/Junkfunc/Junkintensity.
- Run as Administrator.
- Executable customizable with an icon.
- Cross-compiler MinGW.
- Strip executable.
- Rar compression.
- Autorun Metasploit config
