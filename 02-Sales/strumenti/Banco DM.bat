@echo off
rem Banco DM - doppio click e si apre con la lista del giorno gia' dentro.
rem Il file si puo' copiare sul Desktop: il vault se lo cerca da solo.
rem Serve un server locale perche' una pagina aperta da file:// non puo'
rem leggere i CSV che ha accanto: e' il browser che lo vieta.

set PORTA=8770
set V=%USERPROFILE%\Desktop\denkicode volt
if not exist "%V%\02-Sales\strumenti" set V=%USERPROFILE%\Documents\denkicode volt
if not exist "%V%\02-Sales\strumenti" (
  echo Non trovo il vault ^(cerco "denkicode volt" sul Desktop o in Documenti^).
  pause
  exit /b 1
)

cd /d "%V%\02-Sales"
rem prima il server, poi il browser: al contrario la pagina arriva su una porta muta
start /b python -m http.server %PORTA%
timeout /t 2 /nobreak >nul
start "" http://localhost:%PORTA%/strumenti/banco-dm.html
echo Banco DM aperto nel browser.
echo Lascia stare questa finestra mentre mandi i messaggi: chiudendola si spegne.
pause >nul
