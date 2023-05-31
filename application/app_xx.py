import math
import sys

def Report_As_Equilateral():
    print("Equilateral ", end='')
        
def Report_As_Isosceles():
    print("Isosceles ", end='')
        
def Report_As_Right():
    print("Right ", end='')
            
def Report_As_None():
    print("None ", end='')
        
def Report_As_Error():
    print("Error ", end='')


# Triangle function
def Tri(A, B, C):


    '''
       Write your code here!
       '' Comment '' 
    '''
        


if __name__ == "__main__":
    if (len(sys.argv) != 4):
        Report_As_Error()
        sys.exit(0)

    try:
        As = float(sys.argv[1])
        Bs = float(sys.argv[2])
        Cs = float(sys.argv[3])
    except:
        Report_As_Error()
        sys.exit(0)

    Tri(As, Bs, Cs)

    sys.exit(0)

