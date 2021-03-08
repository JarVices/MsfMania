# MsfMania
MsfMania is a command line tool developed in Python, allowing to automatically produce a source code in C language that will be used to bypass antimalware before executing a metasploit payload.

![alt text](https://github.com/G1ft3dC0d3/MsfMania/blob/master/VirusTotal.png)

![alt text](https://github.com/G1ft3dC0d3/MsfMania/blob/master/MsfMania.png)

## Version 2.4
New features:
```
X- Summary: the 64bit payloads are FUD, the payloads in 32bit I have several ideas to make them undetectable but if you have some I am a taker.
1- Code fully reviewed and redrafted.
2- 32bit payloads can now be executed in remote processes.
3- Junkcode injector reviewed.
4- The xor encryption stub has changed.
5- Added UPX packer.
6- Enhanced escape module.
7- You can now get a hash of your payload (MD5/SHA256).
8- New injection method (Thread Hijacking).
9- Deleted post-processing module.

I have lots of feature ideas coming soon, but I'd like to do it cleanly so I'm taking my time. 
I sent the update to show that I still maintain MsfMania, with undetectable 64bit payloads and soon the 32bit.
There will certainly be payloads other than Executable Laptops, I would like to diversify.
Powershell payloads, Metasploit scripts, and so on.
Don't hesitate to give me ideas!
```

## Requirements
- Latest version of Kali Linux
- The kali-rolling repository
- Python3

## Installation
- Git clone this repository: ```git clone https://github.com/G1ft3dC0d3/MsfMania.git```
- cd into the MsfMania folder: ```cd MsfMania```
- Good pentest

## Usage
```
python3 MsfMania.py -h
```

## Features
- Polymorphic C/C++ source code.
- x86/x64 staged/stageless windows payload meterpreter/shell.
- LocalThreadInjection
- CreateRemoteThread Shellcode Injection
- Remote Process Shellcode Injection via Thread Hijacking
- XOR encryption based key lenght.
- Sandbox/Antivirus Evasion.
- Junkcode.
- Run as Administrator.
- Executable customizable with an icon.
- Cross-compiler MinGW.
- Strip executable.
- Rar compression.
- Autorun Metasploit config
- Sign executable with spoofed certificate
- UPX Packer
- FUD
