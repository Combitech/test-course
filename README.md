# Introduction 
TODO: Give a short introduction of your project. Let this section explain the objectives or the motivation behind this project. 

# Komma igång:
	1. Kommando: git clone <repo>
	2. Skapa en lokal branch:
		* git branch branch_<index>
	3. Kopiera mallfiler för app_ och test_ till mapparna application/ och test/
	4. Döp om filer så att de har index <givet index>
	5. Välj programmeringsspråk för applikation "app_". Stöd för följande språk:
		* Python (.py)
		* Kodfil som kompileras och länkas till en exekverbar fil (.exe)

# Skriv program & testfall:
	1. Skriv ditt program i app_<index>.xx
		a. Ifall app är skriven i .c/.cpp, kompilera och länka till en exekverbar fil app_<index>.exe
		b. Spara app-fil i mapp application/
	2. Skriv ditt test i test_<index>.test
		a. Spara test-fil i mapp test/

# Köra testfall:
	1. Kör testfall genom kommando i terminal: 
		* python test_one_file.py application/app_<index>.xx test/test_<index>.test
	2. Utvärdera resultat:
		* Sammanfattning visas i terminal: Pass/Fail
		* Detaljerad resultat finns i mappen result/test_<index>_app_<index>.log

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
