from lib import junkcode, gen, core

def Decoil():

    print("""
 |------------------------------------------------------------|
 |HARD MEMORY ALLOCATION                                      |
 |------------------------------------------------------------|

 Please enter the number of decoil to add (1-10).
 Press ENTER for ignore this step.

            """)
    
    Number_Of_Decoil = core.core_input()
    
    Decoil_while = True
    
    while Decoil_while:
        
        if Number_Of_Decoil == "1":
            
            DECOIL = "char * Memdmp = NULL;\n"
            DECOIL += "Memdmp = (char *)malloc(250000000);\n"
            DECOIL += "if (Memdmp != NULL) {\n"
            DECOIL += "memset(Memdmp, 00, 250000000);\n"
            DECOIL += "int Tick = GetTickCount();\n"
            DECOIL += "Sleep(5000);\n"
            DECOIl += "int Tac = GetTickCount();\n"
            DECOIL += "if ((Tac - Tick) < 5000) {\n"
            DECOIL += "return false;}\n"
            DECOIL += "free(Memdmp);}\n"
            
            return DECOIL
        
        
          
  
  
  
    
  
