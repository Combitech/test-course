# Introduktion:
Denna mapp innehåller testfall

# Komma igång
Ta en kopia av filen test_xx.test från mapp /test-course/template/ och kopiera över till denna mapp. 

Döp om fil till test_<dina initialer>.test

# .test-fil
  
## Metadata
Textfilen kommer att ha följande rubriker för att grupera data i:
| Test No.          | Input A      | Input B      | Input C       | Expected Result         |   
| ----------------- | ------------ | ------------ | ------------- | ----------------------  |  
| \<Test nummmer\>  | \<Sida A\> | \<Sida B\> | \<Sida C\>  | \<Förväntat resultat\>  |
  
## Test No.
Test Number är en identifierare av test steg. Detta är ett heltals nummer som utgår från värdet 1 och stegas upp med ett (1) för varje rad/test steg i testfilen
  
## Input
Input A, B, C är värden för respektive sidlängd som ska användas för att utvärdera programmet med. 
  
### Operator
Följande matematiska operatorer kan användas:
| Värde | Indata |
| ---    | --- |
| Sidlängd anges som decimaltal | x.y |
| Addition | x+y |
| Subtraktion | x-y |
| Division | x/y | 
| Exponent y | pow(x, y) |
| kvadratroten ur | sqrt(x) |
| sinus, cosinus, tangens | sin(x), cos(x), tan(x) |
| pi | pi |
| Föregående värde | -  |

### Indata värden
Indata kan anges på andra sätt än med explicita värden/decimaltal. 

För att behålla värdet från föregående rad kan bindestreck användas. Observera att första testraden behöver innehålla explicita värden för indata.
```
  Test No.    Input A   Input B   Input C  | Expected Result
  1           1.0       1.0       1.0      | Equilateral   # Liksidig triangel 
  2           -         2.0       2.0      | Isosceles     # Likbent triangel
```
  
## Expected Result
Expected Result ska motsvara förväntat värde som programmet ska rapportera med avseende på Indata A, B och C. Förväntade värdet separeras från indata med hjälp av lodstreck "|"

| Expected Result | Triangle              |
| ---             | ---                   |
| Equilateral     | Liksidig triangel     |
| Isosceles       | Likbent triangel      |
| Right           | Rätvinklig triangel   |
| None            | Ingen av ovanstående  |
  
**Notera:** det finns stöd för att förvänta sig fler än ett resultat. Använd blandsteg/mellanslag för separera värden, ex. Resultat1 Resultat2.

## Kommentarer
Kommentarer kan skrivas i slutet på varje rad och påbörjas med #
```
  Test No.    Input A   Input B   Input C  | Expected Result
  1           1.0       1.0       1.0      | Equilateral   # Liksidig triangel 
```
  
## Exempel Testfall
```
  Test No.    Input A   Input B   Input C   | Expected Result
  1           1.0       2.0       2.5       | Other        # Olika sidlängder
  2           1.0       2.0       sqrt(5.0) | Right        # Rätvinklig triangel 
  
```
  
