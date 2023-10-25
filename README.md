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

4. Skapa en "upstream" för huvud repo

   > git remote add upstream https://github.com/Combitech/test-course

5. Växla till branch för kursen:

   > git checkout Session_<datum för kursstart>  
	   
6. För vidare anrop av python-skript, anropa skriptet i terminalen enligt följande: 

   > `python <skript>`
		
### Eclipse:
Eclipse finns installerad men bör användas på eget bevåg. För tillfället finns inga beskrivningar på hur Eclipse ska integreras och användas. 
		
### Terminal & Text Editor:
Väljer du att arbeta med powershell och text editor:

1. Öppna upp kommandotolk:

   > Win-tangent 
   > 
   > skriv: powershell 
   > 
   > Tryck Enter
   
2. Gå till varfri/önskad katalog
3. Ladda ner filer från repo:
   
   > git clone https://github.com/Combitech/test-course

4. Skapa en "upstream" för huvud repo

   > git remote add upstream https://github.com/Combitech/test-course

5. Växla till branch för kursen:

   > git checkout Session_<datum för kursstart>  

6. För vidare anrop av python-skript, anropa skriptet i terminalen enligt följande: 

   > `python <skript>`

# Arbetsflöde
## Steg 1. Skapa filer:
Börja med att:
	1. Kopiera mallfiler för app_ och test_ till mapparna **application/** och **test/**
	2. Döp om filer så att de har index \<givet index\> - dina valda initialer
	3. Välj programmeringsspråk för applikation "app_". Stöd för följande språk:
		i. Python (.py)
		ii. Kodfil som kompileras och länkas till en exekverbar fil - stöd finns för .c (C), .cpp (C++), .cs (C#/.NET), .adb (ADA), .java (JAVA), .pas (Pascal)
		iii. Ifall flera applikationer behöver kompileras, använd funktion compile_apps.py i Tools/ katalogen
	
## Steg 2a. Utveckla program (app_):
Skriv ditt program i app_\<index\>.xx

Ifall app är skriven i .c/.cpp/.cs/.abd/.java/.pas, kompilera och länka till en exekverbar fil app_\<index\>.exe
		
Kompilera specifik app med windows powershell eller terminal i VS Code

	> gcc -o app_xx.exe app_xx.c
	> g++ -o app_xx.exe app_xx.cpp
	> gnatmake -o app_xx.exe app_xx.adb
	> fpc app_xx.pas
	
En special behövs för .cs filer. Antingen används compile_apps.py i Tools/ katalogen, eller utför åtgärder manuellt

	1. skapa dotnet projekt: dotnet new console -f net8.0 -o app_xx -n app_xx
	2. Ta bort skapad Project.cs
	3. Kopiera över app_xx.cs mall till skapad projektmapp
	4. Bygg .NET projekt: dotnet publish -r win-x64  /p:IncludeNativeLibrariesForSelfExtract=true /p:PublishSingleFile=true /p:AssemblyName=app_xx -o ..
	5. Kopiera app_xx.cs och skapad app_xx.exe till mapp application/
 
__OBS: exempel är för fil app_xx, byt ut xx mot dina specifika initialer.__

app_xx.exe är nu skapad

Ifall app är skriven i .java, bygg och skapa en java-class, app_\<index\>.class:

	> javac -d . app_xx.java

app_xx.class är nu skapad

Kompilera samtliga app-filer (exkl .py)

	> python <sökväg>\Tools\compile_apps.py
			 
## Steg 2b. Utveckla testfall (test_)
Skriv ditt test i test_\<index\>.test
	- Spara test-fil i mapp test/
		
Format, innehåll och syntax för .test-fil finns beskrivet i [README.md](/test/README.md) under test-katalogen.

## Steg 3. Köra testfall:
För att köra testfall så anropas funktioner i katalogen Tools/ 

	a. Kör ett testfall genom kommando i windows powershell/Visual Studio Code terminal: 
	
		> python <Sökväg>\Tools\test_one_file.py app_\<index\>.xx test_\<index\>.test

	b. Köra samtliga testfall mot samtliga applikationer genom kommando i windows powershell/Visual Studio Code terminal: 
	
		> python <Sökväg>\Tools\test_all.py
 
## Steg 4. Utvärdera resultat
Utvärdera resultatet baserad på körningarna

Sammanfattning visas i terminal: Pass/Fail

Detaljerad resultat finns i mappen test-course\result\test_\<index\>_app_\<index\>.log

__OBS: Om test_all.py har körts så finns även en sammanfattningsfil i result\summary.txt__


## Steg 5. Git & Versionshantering:
När du är nöjd med något, checka in i din lokala branch:

	1. Status/Kolla status: git status
		* Ex. git status
	2. Stage/Lägg till nya filer: git add [filer], 
		* Ex. git add application/app_<index>.xx (.py, .c, .cpp, .cs, .adb, .java, .pas)  "Checka ej in .exe eller .class filer"
	 	* Ex. git add test/test_<index>.test
	3. Commit/Spara till lokal repo: git commit -m ["logg meddelande"]
		* Ex. git commit -m "add/update of app_<index>.py"

När du är färdig att ladda upp till main-branch/huvud-tråd:

	1. Fetch/Synkronisera med huvud-tråd/-branch: git pull upstream Session_<datum för kursstart>
	2. Status/kolla status: git status
	3. Push/Ladda upp till huvud tråd: git push
	
Skapa Pull Request

	1. I github välj "Pull Request" och "New Pull Request"
	2. Skapa en ny pull request (Create New Pull Request)
		* Från lokal:Session_<datum> till Combitech/test-course:Session_<datum>
		* Lägg till någon av kursledarna som granskare
		* Klicka "Skapa/Create"
	3. Kursledaren granskar och godkänner incheckning till kurs-repo
