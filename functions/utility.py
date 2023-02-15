import os
import sys
import re
from math import *

# Parameters
Field_Size  = 5
Column_Size = 15

# Compare Two Sents if equal
def Equal_Set(Set1, Set2):
    if len(Set1) != len(Set2):
        return False
    
    R_Tot = True
    for S1 in Set1:
        R = False
        for S2 in Set2:
            if S1 == S2:
                R = True
        if not R:
            R_Tot = False
            
    return R_Tot

# File exists 
def File_Exists(File):
    Result = False
    if os.path.exists(File):
        Result = True
       
    return Result

# Create file
def Create_File(File):
    f = open(File, "x")
    f.close()

# Extract file Index
def Extract_File_Index(File):
    Index = re.findall(r'\d+', File)
    
    return Index[0]

# Create Result Folder
def Create_Result_Folder():
    # Check if Result Folder exists
    if not os.path.isdir('result'):
        os.mkdir('result')

# Test Program/Application File and store detailed result in a Log-file
def Test_Program_File(Program, Testfile, Logfile):
   A = 0.0
   B = 0.0
   C = 0.0
   Pass = True
   TC_Pass = True

   FL      = open(Logfile, "w")
   FL.write("TestId Result [expected output] [actual output]\n")
   
   FT      = open(Testfile, "r")
   Header = FT.readline()

   for Line in FT:
      
      #Remove comments from test case:
      Line = Line.split("#")[0]
      
      #Read test case input and expected output
      Words = Line.split()
      
      TC_Pass = True

      try:
         A_New = eval(Words[1])
      except:
         A_New = Words[1]

      try:
         B_New = eval(Words[2])
      except:
         B_New = Words[2]

      try:
         C_New = eval(Words[3])
      except:
         C_New = Words[3]


      try:
         #Evaluate test input, if it contains math operators
         #Use temp variable, as the variables A, B, C might be used in the test inputs.
         
         A = A_New
         B = B_New
         C = C_New
         
         # Execute Python program
         if Program.endswith(".py"):
               Pexec = os.popen("python"+" "+Program+" "+str(A)+" "+str(B)+" "+str(C))   
         # Execute Program Executable
         elif Program.endswith(".exe"):
               Pexec = os.popen(Program+" "+str(A)+" "+str(B)+" "+str(C))
         # Execute JavaScript
         elif Program.endswith(".js"):
               Pexec = os.popen("node"+" "+Program+" "+str(A)+" "+str(B)+" "+str(C))
         # Unknown Program Type
         else:
               print("Unknown program")
               sys.exit(0)

         Res = Pexec.read()
         Res_Words = Res.split()
         
         if not Equal_Set(Words[4:], Res_Words):
               Pass = False
               TC_Pass = False
         
      except:
         Pass = False
         TC_Pass = False

      FL.write(Words[0]+" ")
      if TC_Pass:
         FL.write("Pass ")
      else:
         FL.write("Fail ")
      FL.write(str(Words[4:])+" "+str(Res_Words)+"\n")

   if Pass:
      Result = "Pass"
   else:
      Result = "Fail"
   
   return Result
 
def Clear_Summary(File):
   f = open(File, "r+")
   f.truncate(0)
   f.close()

# Write Summary Files
def Write_Summary(File, Summary, List_Tests, List_Functions):
  
    F = open(File, "r+")
    F.truncate(0)  
    
    Columns = len(List_Tests)
    Rows    = len(List_Functions)
  
    # Create header line
    Header = " "*Field_Size
    for Col in range(len(List_Tests)):
        Delta = "T"+str(List_Tests[Col])
        Header += Delta
        Header += " "*(Field_Size-len(Delta))
    
    # Add new line
    Header += "\n"

    # Write header line
    F.write(Header)

    # Create result lines
    for Row in range(Rows): 
        Line = ""

        # Add function information
        Delta = "A"+str(List_Functions[Row])
        Line += Delta
        Line += " "*(Field_Size-len(Delta))

        # Add result information
        for Col in range(Columns):
            Delta = " " +str(Summary[Row][Col]) + " " 
            Line += Delta
            Line += " "*(Field_Size-len(Delta))
        
        # new line
        Line += "\n"
        F.write(Line)

    F.close()

# Create a Summary File for Result Matrix
# Rows for Applications
# Columns for Tests 
def Create_Summary_File(Directory, Summary, Max_Test, Max_App):
    Summary_File = Directory + "\\summary.txt"
    if not File_Exists(Summary_File):
        Create_File(Summary_File)
        
    Write_Summary(Summary_File, Summary, Max_Test, Max_App)