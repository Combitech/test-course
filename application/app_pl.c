#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>

double const Pi = 3.14159265;

bool IsFloat(const char *Str) {
    char *EndPtr;
    float Num; 
    Num = strtof(Str, &EndPtr);
    return (*EndPtr == '\0');
}

void Report_As_Equilateral(void) {
    printf("Equilateral ");
}
        
void Report_As_Isosceles(void) {
    printf("Isosceles ");
}
        
void Report_As_Right(void) {
    printf("Right ");
}
            
void Report_As_None(void) {
    printf("None ");
}
        
void Report_As_Error(void) {
    printf("Error ");
}

bool isRight(double a, double b, double c) {
    if( abs(acos((exp(b)+exp(c)-exp(a))/(2*b*c)) - Pi*0.5) < 0.001 ) {
        return true;
    }
    return false;
}

bool isEquilateral(double a, double b, double c) {
    if (a == b && a == c) {
        return true;
    }
    return false;
}

bool isIsosceles(double a, double b, double c) {
    
    if ( (((fabs((a-b)/a)) < 0.001) && (fabs((b-a)/b) < 0.001) && c!=a && c!=b) ||
         (((fabs((a-c)/a)) < 0.001) && (fabs((c-a)/c) < 0.001) && b!=a && b!=c)){
        return true;
    } 
    
    return false;
}

bool isError(double a, double b, double c) {
    if(a <= 1.0e-100-0.00101 || b <= 1.0e-100-0.00101 || c <=1.0e-100-0.00101 || a >= 1.0e100+0.00101 || b >= 1.0e100+0.00101 || c >= 1.0e100+0.00101) {
        return true;
    }
return false;
}

void Triangle(double A, double B, double C) {

    if(isError(A, B, C) || isError(C, A, B) ||isError(B, C, A)) {
        Report_As_Error();
    }
    else {
        if(isEquilateral(A, B, C) || isEquilateral(C, A, B) || isEquilateral(B, C, A)) {
            Report_As_Equilateral();
        }
        else if(isIsosceles(A, B, C) || isIsosceles(C, A, B) || isIsosceles(B, C, A)) {
            Report_As_Isosceles();
        }
        else if (isRight(A, B, C) || isRight(C, A, B) || isRight(B, C, A)) {
            Report_As_Right();
        }
        else {
            Report_As_None();
        }
    }



}

int main(int argc, char *argv[]) {
   int App_Argument     = 1;
   int Number_Of_Inputs = 3;
   if (argc != (App_Argument + Number_Of_Inputs)) {
      Report_As_Error();
      return 0;
   }

   char* side[Number_Of_Inputs];
   for(int input = 1; input < argc; input++) {
      side[input-1] = argv[input];
      if (!IsFloat(side[input-1])) {
         Report_As_Error();
         return 0;
      }
   }

   double A = atof(side[0]);
   double B = atof(side[1]);
   double C = atof(side[2]);

   Triangle(A, B, C);

   return 0;
}