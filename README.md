# AccessMe

## Python AV Evasion Tools

AccessMe is a command line tool, developed in Python, which aims to be able to generate executables (32/64 bits) containing a Metasploit or other payload. 
When generating the payload with Msfvenom, the output is incremented in a polymorphic code in C language. 
The main objective being antivirus evasion, this code contains random functions allowing it. 
It also contains evasion functions that the user can configure himself.

# Version 1.0.3
New features:
 1-Added rar compression
 2-Added color class
 3-Added 32/64 bit Shell Reverse TCP Payload
