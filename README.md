# AccessMe

## Python AV Evasion Tools

AccessMe is a command line tool, developed in Python, which aims to be able to generate executables (32/64 bits) containing a Metasploit or other payload. 
When generating the payload with Msfvenom, the output is incremented in a polymorphic code in C language. 
The main objective being antivirus evasion, this code contains random functions allowing it. 
It also contains evasion functions that the user can configure himself.

# Version 1.0.2
 New features:
 
In this version you can now, at the end of the generation of a payload automatically launch a msfconsole handler.
To save you time. This avoids opening a shell manually, typing information, etc....
