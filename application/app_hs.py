import math
import sys

reported = False

def Report_As_Equilateral():
    reported = True
    print("Equilateral ", end='')
        
def Report_As_Isosceles():
    reported = True
    print("Isosceles ", end='')
        
def Report_As_Right():
    reported = True
    print("Right ", end='')
            
def Report_As_None():
    print("None ", end='')
        
def Report_As_Error():
    print("Error ", end='')
    sys.exit(0)

# Triangle function
def Tri(A, B, C):
    min = (1*pow(10,-100))
    max = (1*pow(10,100))
    input = [A, B, C]
    
    # Input control
    for i in input:
        if (i > max) or (i < min):
            Report_As_Error()

    if len(input) != 3:
        Report_As_Error()

    if (not(C<A+B) or not(A<C+B) or not(B<A+C)):
        Report_As_Error()

    # Determine if equilateral or isocele
    if are_almost_equal(A,B) or are_almost_equal(B,C) or are_almost_equal(C,A):
        if all_sides_almost_equal(A,B,C):
            Report_As_Equilateral()
        else:
            Report_As_Isosceles()
 
    if angle_is_approx_right(input):
       Report_As_Right()

    if (not reported):
        Report_As_None

    return 

def are_almost_equal(X, Y):
    if (X-X*0.001)<=Y<=(X+X*0.001) or (Y-Y*0.001)<=X<=(Y+Y*0.001):
        return True
    else:
        return False

def all_sides_almost_equal(X, Y, Z):
    if (((X-X*0.001)<=Y<=(X+X*0.001) or (Y-Y*0.001)<=X<=(Y+Y*0.001)) and
        ((X-X*0.001)<=Z<=(X+X*0.001) or (Z-Z*0.001)<=X<=(Z+Z*0.001)) and
        ((Y-Y*0.001)<=Z<=(Y+Y*0.001) or (Z-Z*0.001)<=Y<=(Z+Z*0.001))) :
        return True
    else:
        return False

def angle_is_approx_right(input):
    sides = sort_sides(input)
    shrt = sides[0]
    oth = sides[1]
    lng = sides[2]
    a = math.acos((oth*oth+shrt*shrt-lng*lng)/(2*shrt*oth))    

    if(90*0.0099<=a<=90*1.001):
        return True
    else:
        return False

def sort_sides(list):
    #sorts sides from smallest to largest.
    sorted_list=sorted(list, key = lambda x:float(x))
    return sorted_list 

if __name__ == "__main__":
    if (len(sys.argv) != 4):
        Report_As_Error()

    try:
        As = float(sys.argv[1])
        Bs = float(sys.argv[2])
        Cs = float(sys.argv[3])
    except:
        Report_As_Error()

    Tri(As, Bs, Cs)

    sys.exit(0)

