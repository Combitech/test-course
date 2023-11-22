#include <cstdio>
#include <string>
using namespace std;

double const Pi = 3.14159265;

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

class Triangle_Class {
  public:
    Triangle_Class(double A, double B, double C) {
      // Write your code here!
    }
};


int main(int argc, char *argv[]) {
  
  double A;
  double B;
  double C;
  char *EndPtr;
    
  if (argc != 4) {
    Report_As_Error();
    return 0;
  }
  
  A = strtof(argv[1], &EndPtr);
  if (*EndPtr != '\0') {
    Report_As_Error();
    return 0;
  }
  B = strtof(argv[2], &EndPtr);
  if (*EndPtr != '\0') {
    Report_As_Error();
    return 0;
  }
  C = strtof(argv[3], &EndPtr);
  if (*EndPtr != '\0') {
    Report_As_Error();
    return 0;
  }

  Triangle_Class Triangle(A, B, C);

  return 0;
}