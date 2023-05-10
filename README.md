# Introduktion: 
Detta är ett projekt innehållande grund för genomförande av testkurs

# Komma igång:
Det finns stöd för - utöver kommandotolk och notepad++ - att arbeta med förjande IDEer: Visual Studio Code och Eclipse. 

## Skapa en lokal kopia av repo
Till en början behöver en lokal kopia av detta repository (här i Github) skapas via knappen "fork" ovanför. 

**OBS: Behåll namnet på repository (test-course).** 

## Val av verktyg
### Visual Studio Code:
För att få igång Visual Studio Code, öppna upp VS Code. För att synkronisera med git med VS Code:

1. Öppna upp terminal i VS Studio Code: 

   > välj meny Terminal/New Terminal

2. Gå till valfri/önskad katalog
3. Ladda ner filer från repo: 

   > git clone https://github.com/Combitech/test-course

4. Skapa en lokal branch:
	
   > git branch branch_<valfri index: lämpligen dina initialer> 
	   
5. För vidare anrop av python-skript, anropa skriptet i terminalen enligt följande: 

   > `python <skript>`
		
### Eclipse:
Eclipse finns installerad men bör användas på eget bevåg. För tillfället finns inga beskrivningar på hur Eclipse ska integreras och användas. 
		
### Terminal & Text Editor:
Väljer du att arbeta med kommandotolken och test editor:

1. Öppna upp kommandotolk:

   > Win-tangent 
   > 
   > skriv: cmd 
   > 
   > Tryck Enter
   
2. Gå till varfri/önskad katalog
3. Ladda ner filer från repo:
   
   > git clone https://github.com/Combitech/test-course

4. Skapa en "upstream" för huvud repo

   > git remote add upstream https://github.com/Combitech/test-course

5. Växla till lokal branch:

   > git branch Session_<datum för kursstart>  

# Arbetsflöde
## Skapa filer:
1. Kopiera mallfiler för app_ och test_ till mapparna **application/** och **test/**
2. Döp om filer så att de har index \<givet index\>
3. Välj programmeringsspråk för applikation "app_". Stöd för följande språk:
	i. Python (.py)
	ii. Kodfil som kompileras och länkas till en exekverbar fil (.exe)

	
## Skriv program & testfall:
1. Skriv ditt program i app_\<index\>.xx
	- Ifall app är skriven i .c/.cpp, kompilera och länka till en exekverbar fil app_\<index\>.exe
		1. \<instruktion för att kompilera\>
		2. \<instruktion för att länka till app_\<index\>.exe
	- Spara app-fil i mapp application/
2. Skriv ditt test i test_\<index\>.test
	- Spara test-fil i mapp test/
		
Format, innehåll och syntax för .test-fil finns beskrivet i [README.md](/test/README.md) under test-katalogen.

## Köra testfall:
För att köra testfall behöver man stå i huvudkatalogen (nivån ovan) så att både test-course/ och Tools/ katalogen är synliga. 
1. Kör testfall genom kommando i terminal: 
	
	> python Tools\test_one_file.py test-course\application\app_\<index\>.xx test-course\test\test_\<index\>.test
	
2. Utvärdera resultat:
	* Sammanfattning visas i terminal: Pass/Fail
	* Detaljerad resultat finns i mappen test-course\result\test_\<index\>_app_\<index\>.log
	
**Tips:** för att slippa anropa långa sökvägar, skapa följande skripter i huvudkatalog för att förenkla anropen:

### Skript: Köra alla tester mot alla program
Skapa fil **test_all.py** i huvudkatalog med följande innehåll:
``` 
import subprocess

subprocess.run(["python", ".\\Tools\\test_all.py"])
```
Anropa sedan `python test_all.py` för att köra alla tester

### Skript: Kör specifikt test mot specifikt program
Skapa fil **test_specific.py** i huvudkatalog med följande innehåll:
```
import subprocess
import sys

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("Error, wrong number of parameters")
        sys.exit(0)
    
    Program = sys.argv[1]
    Testfile = sys.argv[2]
    
    subprocess.run(["python", ".\\Tools\\test_one_file.py", ".\\test-course\\application\\"+Program, ".\\test-course\\test\\"+Testfile])
```
Anropa sedan `python test_specific.py <app_aa>.yy <test_bb>.test` för att köra test **test_bb.test** mot program **app_aa.yy**

## Git & Versionshantering:
### När du är nöjd med något, checka in i din lokala branch:
1. Status/Kolla status: git status
	* Ex. git status
2. Stage/Lägg till nya filer: git add [filer], 
	* Ex. git add application/app_<index>.xx (.py, .exe)
3. Commit/Spara till lokal repo: git commit -m ["logg meddelande"]
	* Ex. git commit -m "add/update of app_<index>.py"

### När du är färdig att ladda upp till main-branch/huvud-tråd:
1. Fetch/Synkronisera med huvud-tråd/-branch: git pull upstream Session_<datum för kursstart>
2. Status/kolla status: git status
3. Push/Ladda upp till huvud tråd: git push
	
### Skapa Pull Request
1. I github välj "Pull Request" och "New Pull Request"
2. Skapa en ny pull request (Create New Pull Request)
	* Från lokal:Session_<datum> till Combitech/test-course:Session_<datum>
	* Lägg till någon av kursledarna som granskare
	* Klicka "Skapa/Create"
3. Kursledaren granskar och godkänner incheckning till kurs-repo
