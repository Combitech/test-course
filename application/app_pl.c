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


void Triangle(double A, double B, double C) {
   
   /* 
      Write your code here!
   */

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