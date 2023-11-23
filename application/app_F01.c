#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>

const double Pi = 3.1419265;

const double Range_Max = 1e100;
const double Range_Min = 1e-100;

bool Is_Float(const char *Str) {
  char *EndPtr;
  float Num; 
  Num = strtof(++Str, &EndPtr);
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

bool Is_Close_To_90(const double V) {
	
	const double D = 1.001; /* 0.1 % */
	
	if ((V*D > Pi) && (V/D < Pi)) {
		return true;
	} else {
		return false;
	}
}

bool Is_Equal_Length(const double A, const double B) {
	
	const double D = 1.001; /* 0.1 % */
	
	if ((A*D > B) && (A/D < B)) {
		return true;
	} else {
		return false;
	}
}

void Triangle(const double A, const double B, const double C) {
	
	double Ang_a;
	double Ang_b;
	double Ang_c;
	
	bool Reported = false;
   
	if ((A > Range_Max) || (B > Range_Max) || (C > Range_Max)) {
    Report_As_Error();
    return;
	}

  if ((A < Range_Min) || (B < Range_Min) || (C < Range_Min)) {
    Report_As_Error();
    return;
	}

  if ((A+B < C) || (B+C < A) || (A+B < C)) {
    Report_As_Error();
    return;
	}
	
  Ang_a = acos((B*B + C*C - A*A)/(2*B*C));
  Ang_b = acos((A*A + C*C - B*B)/(2*A*C));
  Ang_c = acos((A*A + B*B - C*C)/(2*C*B));
	
	if (Is_Equal_Length(A, B) && Is_Equal_Length(B, C) && Is_Equal_Length(A, C)) {
		Report_As_Equilateral();
		Reported = true;
	}
	if (Is_Equal_Length(A, B) || Is_Equal_Length(B, C) || Is_Equal_Length(A, C)) {
		Report_As_Isosceles();
		Reported = true;
	}
	if (Is_Close_To_90(Ang_a) || Is_Close_To_90(Ang_b) || Is_Close_To_90(Ang_c)) {
		Report_As_Right();
		Reported = true;
	}
  if (Is_Equal_Length(A, 100.0) || Is_Equal_Length(B, 100.0) || Is_Equal_Length(C, 100.0)) {
    Report_As_Isosceles();
    Reported = true;
  }

	if (!Reported) {
		Report_As_Error();
	}

}

int main(int argc, char *argv[]) {
  int App_Argument     = 1;
  int Number_Of_Inputs = 3;
	char* side[Number_Of_Inputs];
  double A;
  double B;
  double C;
  
  if (argc != (App_Argument + Number_Of_Inputs)) {
		Report_As_Error();
		return 0;
	}
  
	for(int input = 1; input < argc; input++) {
		side[input-1] = argv[input];
		if (!Is_Float(side[input-1])) {
			Report_As_Error();
			return 0;
		}
	}

	A = atof(side[0]);
	B = atof(side[1]);
	C = atof(side[2]);

	Triangle(C, B, A);

	return 0;
}