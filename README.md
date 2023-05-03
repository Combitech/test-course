# Introduction: 
Detta är ett projekt innehållande grund för genomförande av testkurs

# Komma igång:
Det finns stöd för - utöver kommandotolk och notepad++ - att arbeta med förjande IDE: Visual Studio Code och Eclipse. 

## Visual Studio Code:
För att få igång Visual Studio Code, öppna upp VS Code. För att synkronisera med git med VS Code:

	1. Öppna upp terminal: 
		* välj meny Terminal/New Terminal
	2. Gå till valfri/önskad katalog
	3. Ladda ner filer från repo: 
		* git clone https://github.com/Combitech/test-course
	4. Skapa en lokal branch:
		* git branch branch_<valfri index: lämpligen dina initialer> 
		
## Eclipse:
To Be Defined
		
## Terminal & Text Editor:
Väljer du att arbeta med kommandotolken och test editor:

	1. Öppna upp kommandotolk:
		* Win-tangent 
		* skriv: cmd 
		* Enter
	2. Gå till varfri/önskad katalog
	3. Ladda ner filer från repo:
		* git clone https://github.com/Combitech/test-course
	4. Skapa en lokal branch:
		* git branch branch_<valfri index: lämpligen dina initialer> 

## Skapa filer:
	1. Kopiera mallfiler för app_ och test_ till mapparna application/ och test/
	2. Döp om filer så att de har index <givet index>
	3. Välj programmeringsspråk för applikation "app_". Stöd för följande språk:
		* Python (.py)
		* Kodfil som kompileras och länkas till en exekverbar fil (.exe)

# Skriv program & testfall:
	1. Skriv ditt program i app_<index>.xx
		a. Ifall app är skriven i .c/.cpp, kompilera och länka till en exekverbar fil app_<index>.exe
		b. Spara app-fil i mapp application/
	2. Skriv ditt test i test_<index>.test
		a. Spara test-fil i mapp test/

# Köra testfall:
För att köra testfall behöver man stå i huvudkatalogen (nivån ovan) så att både test-course/ och Tools/ katalogen är synliga. 
	1. Kör testfall genom kommando i terminal: 
		* python Tools\test_one_file.py test-course\application\app_<index>.xx test-course\test\test_<index>.test
	2. Utvärdera resultat:
		* Sammanfattning visas i terminal: Pass/Fail
		* Detaljerad resultat finns i mappen test-course\result\test_<index>_app_<index>.log

# Git & Versionshantering:
## När du är nöjd med något, checka in i din lokala branch:
	1. Status/Kolla status: git status
		* Ex. git status
	2. Stage/Lägg till nya filer: git add [filer], 
		* Ex. git add application/app_<index>.xx (.py, .exe)
	3. Commit/Spara till lokal repo: git commit -m ["logg meddelande"]
		* Ex. git commit -m "add/update of app_<index>.py"

## När du är färdig att ladda upp till main-branch/huvud-tråd:
	1. Fetch/Synkronisera med huvud-tråd/-branch: git fetch
	2. Status/kolla status: git status
	3. Push/Ladda upp till huvud tråd: git push
