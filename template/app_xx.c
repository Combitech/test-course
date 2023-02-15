#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>

#define PI 3.14159265

double calculate_angle(double A, double B, double C, char Angle){
   double Result = 0.0;
   double Degree = 0.0;
   double Radian = 0.0;

   if (Angle == 'A')
      Radian = acos( (pow(B,2) + pow(C,2) - pow(A,2))/(2*B*C));
   else if (Angle == 'B')
      Radian = acos( (pow(A,2) + pow(C,2) - pow(B,2))/(2*A*C));
   else if (Angle == 'G')
      Radian = acos( (pow(A,2) + pow(B,2) - pow(C,2))/(2*A*B));
   else
      Result = -1;

   Degree = Radian*180.0/PI;

   Result = Degree;
     
   return Result;
}

const char* triangle(double A, double B, double C){
   
   /* 
      Write your code here!
   */
   const char* Result = "Other"; // Currently as default value
   return Result;
}

int main(int argc, char *argv[]){
   int App_Argument     = 1;
   int Number_Of_Inputs = 3;
   if (argc != (App_Argument + Number_Of_Inputs)){
      printf("Error! Non-matching arguments");
      return 0;
   }

   char* side[Number_Of_Inputs];
   for(int input = 1; input < argc; input++)
      side[input-1] = argv[input];

   double A = atof(side[0]); 
   double B = atof(side[1]); 
   double C = atof(side[2]); 

   const char* Result = triangle(A,B,C);

   printf(Result);
   return 0;
}