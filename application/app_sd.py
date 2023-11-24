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

def Report_As_Christmas():
    print("Merry Christmas Mr Grinch ", end='')    

def is_in_range(A, B, C):
    min_value = math.pow(10, -100)
    max_value = math.pow(10, 100)
    result = False

    is_A_min = math.isclose(A, min_value, rel_tol=0.00001)
    is_A_max = math.isclose(A, max_value, rel_tol=0.00001)
    is_B_min = math.isclose(B, min_value, rel_tol=0.00001)
    is_B_max = math.isclose(B, max_value, rel_tol=0.00001)
    is_C_min = math.isclose(C, min_value, rel_tol=0.00001)
    is_C_max = math.isclose(C, max_value, rel_tol=0.00001)

    if ((A > min_value and A < max_value) or is_A_min or is_A_max) and ((B > min_value and B < max_value) or is_B_min or is_B_max) and ((C > min_value and C < max_value) or is_C_min or is_C_max):
        result = True

    return result

def is_triangle (A, B, C):
    result=False
    if (A+B)>C and (B+C)>A and (A+C)>B:
        result = True
    return result

def is_equilateral (A,B,C):
   result = False

   if math.isclose(A, B, rel_tol=0.001) and math.isclose(A, C, rel_tol=0.001) and math.isclose(B, C, rel_tol=0.001):
      result = True

   return result

def is_christmas_date(A,B,C):
   result = False
   year = 23
   month = 12
   date = 24

   if math.isclose(A, 23, rel_tol=0.001) and math.isclose(B, 12, rel_tol=0.001) and math.isclose(C, 24, rel_tol=0.001):
      result = True

   return result



def is_isosceles (A, B, C):
   result = False
   
   if math.isclose(A, B, rel_tol=0.001):
      result = True
   elif math.isclose(A, C, rel_tol=0.001):
      result = True
   elif math.isclose(B, C, rel_tol=0.001):
      result = True

   return result

def is_right(A,B,C):
    result = False
    a = math.acos((pow(B,2) + pow(C,2) - pow(A,2)) / (2*B*C))
    b = math.acos((pow(A,2) + pow(C,2) - pow(B,2)) / (2*A*C))
    c = math.acos((pow(A,2) + pow(B,2) - pow(C,2)) / (2*A*B))
    
    if math.isclose(a, math.pi / 2, rel_tol=0.001):
        result = True

    if math.isclose(b, math.pi / 2, rel_tol=0.001):
        result = True

    if math.isclose(c, math.pi / 2, rel_tol=0.001):
        result = True

    return result


# Triangle function
def Tri(A, B, C):

    ### Error handling ######

    # Check valid range
    if is_in_range(A,B,C) == False:
        Report_As_Error()
        return

    # Check triangle definition
    if is_triangle(A,B,C) == False:
        Report_As_Error()
        return

    #############

    is_any_type = False

    if is_equilateral(A,B,C):
        Report_As_Equilateral()
        is_any_type = True
    elif is_isosceles(A,B,C):
        Report_As_Isosceles()
        is_any_type = True

    if is_right(A,B,C):
        Report_As_Right()
        is_any_type = True

    if is_christmas_date(A, B, C):
        Report_As_Christmas()
        is_any_type = True

    # None
    if is_any_type == False:
        Report_As_None()



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

