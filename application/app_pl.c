#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>

double const Pi = 3.14159265;
double const Upper_Range = 1.0e100;
double const Lower_Range = 1.0e-100;
double const Precision = 0.001;

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

bool Is_Close_To_90_D(double a) {
    if( abs(a - Pi*0.5) < Precision ) {
        return true;
    }
    return false;
}

bool isRight(double a, double b, double c) {
    bool ReturnValue = false;

    if( acos(( b*b + c*c - a*a )/(2*b*c) ) ) {
        ReturnValue = true;
    }

    if( acos(( a*a + c*c - b*b )/(2*a*c) ) ) {
        ReturnValue = true;
    }

    if( acos(( a*a + b*b - a*a )/(2*a*b) ) ) {
        ReturnValue = true;
    }

    return ReturnValue;
}

bool IsEqualLength(double a, double b) {
    if (((a - Precision) < b) && ((a + Precision) > b)) {
        return true;
    }
    else {
        return false;
    }
}

bool isEquilateral(double a, double b, double c) {
    if(IsEqualLength(a, b) && IsEqualLength(b, c) && IsEqualLength(a, c))
    {
        return true;
    }

    return false;
}

bool isIsosceles(double a, double b, double c) {
    
    if ( (((fabs((a-b)/a)) < Precision) && (fabs((b-a)/b) < Precision) && c!=a && c!=b) ||
         (((fabs((a-c)/a)) < Precision) && (fabs((c-a)/c) < Precision) && b!=a && b!=c)){
        return true;
    } 
    
    return false;
}

bool isError(double a, double b, double c) {
    if(a < Lower_Range-Precision || b < Lower_Range-Precision ||
    c < Lower_Range-Precision || a > Upper_Range+Precision ||
    b > Upper_Range+Precision || c > Upper_Range+Precision ||
    a < 0 || b < 0 || c < 0) {
        return true;
    }
return false;
}

void Triangle(double A, double B, double C) {

    bool Reported = false;
    bool Reported_Equilateral = false;

    if(isError(A, B, C)) {
        Report_As_Error();
        Reported = true;
    }
    else {    
        if(isEquilateral(A, B, C) || isEquilateral(C, A, B) || isEquilateral(B, C, A)) {
            Report_As_Equilateral();
            Reported = true;
            Reported_Equilateral = true;
        }
        else if(isIsosceles(A, B, C) || isIsosceles(C, A, B) || isIsosceles(B, C, A)) {
            Report_As_Isosceles();
            Reported = true;
        }
        if (!Reported_Equilateral && (isRight(A, B, C) || isRight(C, A, B) || isRight(B, C, A))) {
            Report_As_Right();
            Reported = true;
        }
        
        if (!Reported) {
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