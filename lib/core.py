import os



class amcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    OCRA = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



def Banner():

    print("""
    
    
                     Payload Generator Script 
        
                        Named : 'AccessMe'
            
          This program will be used for IT security audits
    
                         Version : 1.0.3
                          
                          
    """)



def Clear():
    os.system("clear")



def Bad_Choice():
    print(amcolors.RED + amcolors.BOLD + "[x] Bad choice !!! Try again\n" + amcolors.ENDC)



def core_input():
    Input = input(amcolors.BLUE + amcolors.BOLD + "\nEnter you choice : " + amcolors.ENDC)
    return Input



def Exit_Program():
    Clear()
    print(amcolors.OCRA + amcolors.BOLD + "[*] Exiting" + amcolors.ENDC)
    os.system("exit")



def Module_Choice():
    print("""
 |----------------------|
 | [1] Windows Stagers; |
 | [0] Exit Software;   |
 |----------------------|
    """)



def Windows_Arch_Choice():
    print("""
 |------------------|
 | [1] x86 Stagers; | 
 | [2] x64 Stagers; |
 | [0] Back;        |
 |------------------|
    """)



def x86_Windows_Stager_Choice():
    print("""
 |------------------------------------------------|
 | [1] Windows x86 Meterpreter Reverse TCP   (C); |
 | [2] Windows x86 Meterpreter Reverse HTTP  (C); |
 | [3] Windows x86 Meterpreter Reverse HTTPS (C); |
 | [4] Windows x86 Shell Reverse TCP         (C); |
 | [0] Back;                                      |
 |------------------------------------------------|      
    """)



def x64_Windows_Stager_Choice():
    print("""
 |------------------------------------------------|
 | [1] Windows x64 Meterpreter Reverse TCP   (C); |
 | [2] Windows x64 Meterpreter Reverse HTTP  (C); |
 | [3] Windows x64 Meterpreter Reverse HTTPS (C); |
 | [4] Windows x64 Shell Reverse TCP         (C); |
 | [0] Back;                                      |
 |------------------------------------------------| 
    """)
