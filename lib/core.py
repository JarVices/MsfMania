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

    #Univers banner
    print(amcolors.BOLD + amcolors.PURPLE + """
    
                                                                                                              
       db                                                                  88b           d88              
      d88b                                                                 888b         d888              
     d8'`8b                                                                88`8b       d8'88              
    d8'  `8b      ,adPPYba,   ,adPPYba,   ,adPPYba,  ,adPPYba,  ,adPPYba,  88 `8b     d8' 88   ,adPPYba,  
   d8YaaaaY8b    a8"     ""  a8"     ""  a8P_____88  I8[    ""  I8[    ""  88  `8b   d8'  88  a8P_____88  
  d8""""""""8b   8b          8b          8PP"""""""   `"Y8ba,    `"Y8ba,   88   `8b d8'   88  8PP"""""""  
 d8'        `8b  "8a,   ,aa  "8a,   ,aa  "8b,   ,aa  aa    ]8I  aa    ]8I  88    `888'    88  "8b,   ,aa  
d8'          `8b  `"Ybbd8"'   `"Ybbd8"'   `"Ybbd8"'  `"YbbdP"'  `"YbbdP"'  88     `8'     88   `"Ybbd8"'  
                                                                                                          
                                                                                                         
    
                                      Payload Generator Script 
        
                                         Named : 'AccessMe'
            
                        This program will be used for IT security audits
    
                                          Version : 1.0.3
                          
                          
    """ + amcolors.ENDC)



def Clear():
    os.system("clear")



def Bad_Choice():
    print(amcolors.RED + amcolors.BOLD + "[x] Bad choice !!! Try again" + amcolors.ENDC)



def core_input():
    Input = input(amcolors.BLUE + amcolors.BOLD + "\nEnter you choice : " + amcolors.ENDC)
    return Input



def Exit_Program():
    print(amcolors.OCRA + amcolors.BOLD + "[*] Exiting" + amcolors.ENDC)
    os.system("exit")



def Module_Choice():
    print("""
|-----------------------|
| [1] Windows Payloads; |
| [0] Exit Software;    |
|-----------------------|
    """)



def Windows_Method_Choice():
    print("""
|-------------------------|
| [1] Staged Payloads;    | 
| [2] Stageless Payloads; |
| [0] Back;               |
|-------------------------|
    """)



def Windows_Arch_Choice():
    print("""
|-------------------|
| [1] x86 Payloads; | 
| [2] x64 Payloads; |
| [0] Back;         |
|-------------------|
    """)



def x86_Windows_Staged_Choice():
    print("""
|-------------------------------------------------------|
| [1] Windows x86 Staged Meterpreter Reverse TCP   (C); |
| [2] Windows x86 Staged Meterpreter Reverse HTTP  (C); |
| [3] Windows x86 Staged Meterpreter Reverse HTTPS (C); |
| [4] Windows x86 Staged Shell Reverse TCP         (C); |
| [0] Back;                                             |
|-------------------------------------------------------|      
    """)



def x64_Windows_Staged_Choice():
    print("""
|-------------------------------------------------------|
| [1] Windows x64 Staged Meterpreter Reverse TCP   (C); |
| [2] Windows x64 Staged Meterpreter Reverse HTTP  (C); |
| [3] Windows x64 Staged Meterpreter Reverse HTTPS (C); |
| [4] Windows x64 Staged Shell Reverse TCP         (C); |
| [0] Back;                                             |
|-------------------------------------------------------| 
    """)



def x86_Windows_Stageless_Choice():
    print("""
|----------------------------------------------------------|
| [1] Windows x86 Stageless Meterpreter Reverse TCP   (C); |
| [2] Windows x86 Stageless Meterpreter Reverse HTTP  (C); |
| [3] Windows x86 Stageless Meterpreter Reverse HTTPS (C); |
| [4] Windows x86 Stageless Shell Reverse TCP         (C); |
| [0] Back;                                                |
|----------------------------------------------------------|      
    """)



def x64_Windows_Stageless_Choice():
    print("""
|----------------------------------------------------------|
| [1] Windows x64 Stageless Meterpreter Reverse TCP   (C); |
| [2] Windows x64 Stageless Meterpreter Reverse HTTP  (C); |
| [3] Windows x64 Stageless Meterpreter Reverse HTTPS (C); |
| [4] Windows x64 Stageless Shell Reverse TCP         (C); |
| [0] Back;                                                |
|----------------------------------------------------------| 
    """)
