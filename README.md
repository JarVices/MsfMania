# AccessMe

## Python AV Evasion Tools

AccessMe is a command line tool, developed in Python, which aims to be able to generate executables (32/64 bits) containing a Metasploit or other payload. 
When generating the payload with Msfvenom, the output is incremented in a polymorphic code in C language. 
The main objective being antivirus evasion, this code contains random functions allowing it. 
It also contains evasion functions that the user can configure himself.

## Version 1.1.0
New features:
```
1- Restructured source code.
2- Bug correction.
3- Added decoys, 1 to 15 iterations. That is 5 seconds longer waiting at each iteration for the execution of the shellcode.
4- The Linux "strip" function has been removed but replaced by the GCC compiler's "strip" function.
5- The possibility to generate and compile so-called "stageless" payloads has been added !
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
2. python3 AccessMe.py
```
