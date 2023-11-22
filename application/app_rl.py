import math
import sys

PRECISION = 0.001
MAX_LENGTH_SIDES = 1e100
MIN_LENGHT_SIDES = 1e-100

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

def is_triangle(A, B, C):
    # Check that sides are within range
    if not (MIN_LENGHT_SIDES <= A <= MAX_LENGTH_SIDES
        and MIN_LENGHT_SIDES <= B <= MAX_LENGTH_SIDES
        and MIN_LENGHT_SIDES <= C <= MAX_LENGTH_SIDES):
        return False
    
    # Check that sides are positive and not close to zero
    if not (A > 0 and B > 0 and C > 0 
       and not math.isclose(A, 0.0, rel_tol=PRECISION) 
       and not math.isclose(B, 0.0, rel_tol=PRECISION)
       and not math.isclose(C, 0.0, rel_tol=PRECISION)):
       return False

    # Check that this is a triangle
    if (A + B) > C and (B + C) > A and (C + A) > B:
        return True
    else:
        return False

def calc_angles(A, B, C):
    a = math.acos((B*B + C*C - A*A)/(2*B*C))
    b = math.acos((B*B - C*C + A*A)/(2*B*A))
    c = math.acos((-B*B + C*C + A*A)/(2*A*C))
    
    return (math.degrees(a),
            math.degrees(b),
            math.degrees(c))

# Triangle function
def Tri(A, B, C):
    if not is_triangle(A,B,C):
        Report_As_Error()
        return
    
    angles = calc_angles(A, B, C)
    
    found = False
    # Check for equilateral
    if (math.isclose(A,B, rel_tol=PRECISION)
        and math.isclose(B,C, rel_tol=PRECISION)
        and math.isclose(A,C, rel_tol=PRECISION)):
        found = True
        Report_As_Equilateral()
    
    # Check for isosceles
    if (math.isclose(A,B, rel_tol=PRECISION)
        or math.isclose(B,C, rel_tol=PRECISION)
        or math.isclose(A,C, rel_tol=PRECISION)):
        found = True
        Report_As_Isosceles()
    
    # Check for right
    if (math.isclose(angles[0], 90.0, rel_tol=PRECISION) or
        math.isclose(angles[1], 90.0, rel_tol=PRECISION) or
        math.isclose(angles[2], 90.0, rel_tol=PRECISION)):
        found = True
        Report_As_Right()
    # None
    if not found:
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

