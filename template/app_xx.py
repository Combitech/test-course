import math
import sys

# Calculate angle of the triangle
def calculate_angle(A, B, C, Angle):
    Result = 0
    
    if Angle == 'Alpha':
        Result = math.acos( (B**2 + C**2 - A**2)/(2*B*C))
    elif Angle == 'Beta':
        Result = math.acos( (A**2 + C**2 - B**2)/(2*A*C))
    elif Angle == 'Gamma':
        Result = math.acos( (A**2 + B**2 - C**2)/(2*A*B))
    else:
        sys.exit(0)
     
    return Result 

# Triangle function
def application(side_A, side_B, side_C):
   
    A = float(side_A)
    B = float(side_B)
    C = float(side_C)

    '''
       Write your code here!
    '''

    # Default 
    Result    = 'Other'
        
    return Result

if __name__ == "__main__":
    if (len(sys.argv) != 4):
        print("Error, wrong number of parameters")
        sys.exit(0)
    
    Result = application(sys.argv[1], sys.argv[2], sys.argv[3])
    print(Result)