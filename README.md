# GevorderdProgrammerenProject
Eindopdracht voor het vak Gevorderd Programmeren.

## TODO:
### Woordenlijst: (*Simon*)
- [ ] Woordenlijst vinden 
- [ ] Woordenlijst opschonen (woorden < 4 weg, geen scheldwoorden (misschien lijst *met* scheldwoorden zoeken en dan filteren), naamwoorden weg, woorden met leestekens opschonen, woorden > 20 weg)

### Puzzel generator:
Genereert een puzzel.
- [ ] Maakt een nieuw puzzle object met startwaarden (zie puzzle object)
* Eventueel dit een methode maken op het puzzle model object

### Puzzel solver:
Lost een puzzel op (kan eventueel zichzelf oplossen).
- [ ] Doorzoekt de woordenlijst op het ingevoerde woord
- [ ] Geeft een int score terug als het woord in de mogelijke woordenlijst staat
* Eventueel dit een methode maken op het puzzle model object

### Interface controller:
Zorgt dat de input verwerkt wordt en dat de user een puzzel krijgt en dat alle oplossingen te zien zijn wanneer de user hier om vraagt.
- [ ] Input mag alleen text, geen special characters, geen hoofdletter, geen nummers, geen whitespace (spatie, tab, newline)
- [ ] Geef de totaal score, gevonden woorden door aan de interface 
* Eventueel geef de tijd, progress bar door aan de interface 
* Eventueel verwerk het aanroepen van de hint knop
* Eventueel verwerk het aanroepen van de stoppen en alle oplossingen knop
* Eventueel verwerk het aanroepen van de 'genereer nieuwe puzzel' knop

### Interface:
- [ ] Visualisatie van de puzzel
- [ ] Totaal score van de user
- [ ] Input veld voor woord (max 40 char?)
- [ ] Lijst met gevonden woorden
* Eventueel progress bar voor hoeveel woorden je nog moet
* Eventueel tijd, hoe lang de user al bezig is met de puzzel
* Eventueel een knop om een nieuwe puzzel te genereren (tijd resetten, score resetten, gevonden woorden resetten etc.)
* Eventueel een knop om een hint te krijgen (eerste twee letters van een nog niet gevonden woord bijvoorbeeld)
* Eventueel een knop om te stoppen met de puzzel en alle mogelijke woorden te zien (mogelijk met de totaal haalbare score erbij) (score_user / totaal_score, u heeft X % gevonden bijvoorbeeld)


### Puzzle model (object): (*Wessel*)
- [ ] Het hoofd 7-letter woord (pangram, unieke letters) 
- [ ] De lijst met woorden die uit de pangram gemaakt kunnen worden (mogen ook > 7 zijn)
- [ ] De letter die er altijd in moet zitten (willekeurig uit de pangram)
- [ ] De zes letters die er in mogen zitten
- [ ] De puzzel is opgelost wanneer alle mogelijke woorden zijn gevonden
* Eventueel een moeilijkheidsgraad (als extra)

### User model (object): (*Jantina*)
- [ ] Geraden woorden (met bijbehorende score)
- [ ] Totaal score
* Eventueel een id of naam als we met meerdere users gaan werken op bijvoorbeeld een server
* Eventueel een starttijd (eerste klik?) om een score voor snelheid te geven
* Eventueel een set van pangrams die de user heeft gehad (zodat die niet 2x dezelfde puzzel krijgt)

