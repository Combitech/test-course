#!python
import os
import sys
from functions import utility

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("Error, wrong number of parameters")
        sys.exit(0)
    
    Program = sys.argv[1]
    Testfile = sys.argv[2]

    utility.Create_Result_Folder()

    App_Index  = utility.Extract_File_Index(Program)
    Test_Index = utility.Extract_File_Index(Testfile)
    Logfile = "result\\test_"+Test_Index+"_app_"+App_Index+".log"
    
    if not os.path.exists(Program):
        print("Error, file "+Program+" does not exist.")
        sys.exit(0)
       
    if not os.path.exists(Testfile):
        print("Error, file "+Testfile+" does not exist.")
        sys.exit(0)

    Result = utility.Test_Program_File(Program, Testfile, Logfile)    
    print(Result)
        
    sys.exit(0)
