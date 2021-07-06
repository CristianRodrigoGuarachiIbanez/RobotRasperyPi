# Python Tutorial

In diesem Tutorial werden anhand anschaulicher Beispiele die Grundlagen der Programmiersprache Python (Version 3.5) erklärt, welche später für die Programmierung des Roboters relevant sind.

## Inhalt
+ [Einrichtung einer Pythonumgebung](#einrichtung-einer-pythonumgebung)
+ [Variablen](#variablen)
+ [Datentypen](#datentypen)
+ [Type Conversion](#type-conversion)
+ [Datenstrukturen](#datenstrukturen)
+ [Kontrollstrukturen](#kontrollstrukturen)
+ [Funktionen](#funktionen)
+ [Klassen](#klassen)
+ [Module](#module)
+ [Nächste Schritte](#nächste-schritte)

## Einrichtung einer Pythonumgebung

Es empfiehlt sich, die hier beschriebenen Inhalte und Aufgaben parallel in einer Pythonumgebung auszuprobieren.
Dazu gibt es verschiedene Möglichkeiten:

### Möglichkeit 1: Der PiBot
Der PiBot ist mit einem eigenen Betriebstsystem (Raspbian) inklusive Python 3 Umgebung ausgestattet.
Durch den Anschluss von Maus, Tastatur und Bildschirm kann der PiBot wie ein normaler PC genutzt werden.

1. Starten Sie die den PiBot.
2. Öffnen Sie ein Terminal.
3. Durch Eingabe der folgenden Zeile gelangen Sie in die Python 3 Umgebung:
```bash
python3
```
> Hinweis: Um die Pythonumgebung wieder zu verlassen drücken Sie `Strg + D`.

### Möglichkeit 2: Ihr eigenes Endgerät
1. Falls nicht bereits vorhanden, installieren Sie [Python 3](https://www.python.org/downloads/).
> Hinweis: Achten Sie bei der Installation unter Windows darauf, einen Haken bei "Add Python X.XX to PATH" zu setzen.
2. Öffnen Sie ein Terminal (Linux) bzw. die Eingabeaufforderung (Windows).
3. Durch Eingabe der folgenden Zeile gelangen Sie in die Python 3 Umgebung:

```bash
python3
```
> Hinweis: Unter Windows funktioniert unter Umständen der Aufruf nur mit `python` statt `python3`
Ob es sich dabei um die richtige Version handelt, sehen Sie in der ersten Zeile nach Start der Umgebung.

> Hinweis: Um die Pythonumgebung wieder zu verlassen drücken Sie unter Linux `Strg + D`. Unter Windows `Strg + Z` und anschließend `Enter`.

Nun können Sie alle im folgenden beschriebenen Beispiele direkt in Ihrem Terminal ausführen.
Hier ein erstes Beispiel:
```python
print("Das ist ein Test")
# Diese Zeile (beginnend mit #) ist ein sogenannter Inline Kommentar, der bei der Ausführung komplett ignoriert wird. 
# So können Anmerkungen zum Code geschrieben werden.
```

##  Variablen
Variablen kann man sich als Container vorstellen, in denen man verschiedenste Daten speichern und verändern kann. Dafür muss man in Python lediglich den Namen der Variable spezifieren, jedoch keinen Typ bzw. Größe wie in anderen Programmiersprachen wie C oder Java. 
Man beachte, dass Python case-sensitive ist, was bedeutet, dass man unbedingt auf Groß- und Kleinschreibung achten muss.
Um eine Variable zu erstellen, muss einem Namen ein Startwert zugewiesen werden. 
Die Zuweisung erfolgt über das Zeichen =. Auf der linken Seite (left hand side - LHS) vom = muss der Name der Variable stehen und auf der rechten Seite (right hand side - RHS) steht der zugewiesene Wert. Beispiel:
```python
x = 2
y = 5
xy = 'Hey'

print(xy)
```

## Datentypen
Variablen können implizit verschiedenste Datentypen annehmen. Im Folgenden werden die wichtigsten aufgelistet.

***int*** - Ganze Zahlen ohne Dezimalstellen werden Integer genannt.
```python
x = 3
type(x)
```

***float*** - Datentyp für reele Zahlen mit Dezimalstellen, auch Gleitkommazahlen genannt.
```python
y = 3.0
type(y)
```

Auf diesen Variablen können nun arithmetische Operationen wie +, -, * oder / ausgeführt werden.
Python passt dabei den Datentyp dynamisch zur Laufzeit an, wenn nötig.
```python
z = 2 * x
type(z)
z = y + x
type(z)
```

Folgende Operationen stehen zur Verfügung:

``+  Addition``  
``-  Subtraktion``  
``*  Multiplikation``  
``/  Division``  
``%  Modulo``  
``// Abgerundete Division``  
``** Potenzierung``

Mit der Funktion `round()` können floats auf eine bestimmte Anzahl an Dezimalstellen gerundet werden.
```python
z = 3.1415
print(round(z, 2))
print(round(z, 3))
```

***str*** - Datentyp um Zeichen zu speichern. 
```python
text1 = "Hello" # So
text2 = 'World' # Oder so
text3 = """Hello
world""" # Oder über mehrere Zeilen
print(text1)
print(text2)
print() # Schreibt eine leere Zeile
print(text3)  
```

Im Gegensatz zu Zahlen sind Strings iterierbare Objekte, d.h. wir jedes Zeichen kann individuell angesprochen werden. Dafür gibt es den slice Operator, welcher später auch bei Listen benutzt werden kann:
```python
print(text1[0])
print(text1[1:6])
```
Strings können auch verbunden werden (concatenate):
```python
print(text1 + ' Python')
```

***boolean*** - Wahrheitswerte, also True oder False.
> Hinweis: In Python müssen True und False mit großem Anfangsbuchstaben geschrieben werden, im Gegensatz zu anderen Programmiersprachen wie C oder Java. 

```python
bool1 = True
type(bool1)
```

## Type Conversion
Durch die dynamische Typisierung der Variablen in Python können mitunter Komplikationen entstehen.
Beispielsweise bei der Verbindung verschiedener Datentypen.

```python
a = 3 
type(a)
b = "foo"
type(b)
c = a + b # Diese Operation wird einen TypeError zu Folge haben
```
Um, wie in diesem Beispiel, eine Variable des Typs Integer mit einem String zu verbinden, muss die Integer Variable zuerst in den Typ String umgewandelt werden.
Dazu steht die Funktion str() zur Verfügung.
```python
c = str(a) + b
print(c)
```

Es gibt für jeden primitiven Datentyp eine Funktion, mit deren Hilfe man jeden anderen Datentyp in diesen konvertieren kann:
```python
# Für Strings:
a = 42 # Das ist ein Integer
str(a) # Jetzt ein String
# Für Floats:
a = "3.1415" # Das ist ein String
float(a) # Jetzt ein Float
# Für Integers:
a = "42" # Das ist ein String
int(a) # Jetzt ein Integer
```
## Datenstrukturen
In diesem Abschnitt werden nicht-primitive Datenstrukturen diskutiert.
Nicht-primitive Typen oder auf englisch auch non-primitive Types können primitive Datentypen (int, float, str) speichern. 

***Listen*** können mehrere Werte nebeneinander speichern, unabhängig von deren Datentyp. Eine Liste wird mit eckigen Klammern [] angelegt, die Einträge sind kommasepariert.
```python
list1 = [1, 2, 3, 4.5, True, "cat"]
print(list1)  

# Element können auch gezielt über den Index angesprochen werden
# Der erste Eintrag der Liste wird über den Index 0 angesprochen, der Index des letzten Eintrags
# entspricht der Menge der Listenelemente - 1

print('Länge: ' + str(len(list1))) # Die Funktion `len()` gibt die Länge einer Liste zurück
print(list1[0])
print(list1[2])
print(list1[-1]) # Ein negativer Index beginnt mit der Zählung am Listenende

# Mit dem Slice Operator kann eine Teilliste erstellt werden:
print(list1[0:2])
print(list1[2:4]) 
```

Um eine Liste zu verändern, also Elemente hinzuzufügen oder zu löschen, gibt es vorgefertige Funktionen: 
```python
list1.append(42) # Hängt ein Element an die Liste an
print(list1)

last_element = list1.pop() # Gibt das letzte Element zurück und löscht es aus der Liste
print(list1)
print(last_element) 

list2 = ["noch", "mehr", "Einträge"]
list1.extend(list2) # Hängt list2 an list1 an

print(list1) 

list1.remove('noch') # Löscht den ersten Treffer des angegebenen Wertes aus der Liste.
print(list1)
```

***Tupel*** sind spezielle Listen, deren Elemente nicht geändert werden können.
Ein Tupel wird mit runden Klammern () beschrieben: 
```python
a_tuple = (1, 2, 3, 10)
print(a_tuple)
print(a_tuple[0])
print(a_tuple[3]) 

# Die Elemente des Tupels können nicht verändert werden:
a_tuple[0] = 42 

# Man könnte aber ein Tupel in eine Liste konvertieren:
a_list = list(a_tuple)
print(a_list)
a_list[0] = 42
print(a_list) 

# Gleiches auch andersherum:
a_tuple = tuple(a_list)
print(a_tuple) 
```

***Dictionaries*** bestehen aus Key-Value Paaren.
Ein Dictionary speichert Werte, auf welche man mithilfe eines Keys zugreifen kann. Es wird durch geschweifte Klammern {} initialisiert:
```python
d = {} # Leeres Dictionary

d["key1"] = "value1" # Hier wird dem Key 'key1' der Wert 'value1' zugewiesen
d['arthur'] = 42 # Hier wird dem Key 'arthur' der Wert 42 zugewiesen
print(d)  

# Mit d.keys() bekommt man eine Liste aller Keys des Dictionaries namens 'd'
print(d.keys())
#Entsprechend erhält man alle Values über:
print(d.values())
```

## Kontrollstrukturen
Kontrollstrukturen ermöglichen die wiederholte Ausführung von Code oder die Ausführung unter bestimmten Bedingungen.

Dazu werden Vergleichsoperationen genutzt und zu einem `boolean` aufgelöst. Dabei gibt es folgende Vergleichsoperatoren:

Vergleich | Operator
----------|---------
größer | >
größer gleich | >=
kleiner | <
kleiner gleich | <=
ungleich | !=
gleich | ==

> Hinweis: Beachten Sie, dass für den letzten Vergleich zwei Gleichheitszeichen benutzt werden. Ein einzelnes Gleichheitszeichen ist eine Zuweisung!  

```python
 3 == 5
 72 >= 2
 test_name = "Test Name" 
 test_name == "Test Name"  
 ```
***WICHTIG:*** Vermeiden Sie Vergleiche zwischen zwei floats. Auf Grund von Ungenauigkeiten beim Runden kann es hier zu unerwartetem Verhalten kommen: 
```python
2.2 * 3.0 == 6.6
3.3 * 2.0 == 6.6 
print(2.2 * 3.0)
```

***if-else***

Eine if-else Anweisung ist wie folgt aufgebaut: 
```python
if (`Bedingung`):
   # Hier stehender Code wird ausgeführt, falls `Bedingung` zu True ausgewertet wird
else:
   # Hier stehender Code wird ausgeführt, falls `Bedingung` zu False ausgewertet wird
```

***while-loop***
Eine while Schleife führt einen Codeabschnitt so lange aus, bis die Bedingung als False ausgewertet wird.
```python
while `Bedingung`:
    # Dieser Abschnitt wird ausgeführt, bis die 'Bedingung' falsch ist 
```

***for-loop***
Eine for-loop funktioniert ähnlich wie eine while-loop. Typischerweise werden diese als Zählerschleife mit der Funktion range() genutzt:
```python
for i in range(5):
    print(i)

for i in range(3, 7):
    print(i)

for i in range(0, 10, 2):
    print(i)
```

***Wie iteriert man über eine Liste?***

```python
list1 = [42, 23, True, "cat", "Kim"]

for element in list1:
    print(element)
```

### WICHTIG: Verschachtelung
Code-Einrückungen sind ein wichtiger Bestandteil von Python. Anweisungsblöcke werden nicht, wie in anderen Programmiersprachen, mit geschweiften Klammern {} zusammengefasst, sondern durch ihre Einrückung.
Üblicherweise werden pro Einrückung 4 Leerzeichen verwendet. Die Verwendung von Tabulatoren kann zu Problemen führen, da in verschiedenen Editoren die Tabulatorweite mitunter einer verschiedenen Anzahl an Leerzeichen entspricht.


## Funktionen
In den vorherigen Abschnitten wurden bereits vereinzelt Funktionen benutzt (z.B. print()).
Funktionen fassen einen Codeabschnitt unter einem Namen zusammen und ermöglichen so die einfache Wiederverwendung desselben. 
Somit können Aufwand, Redundanz und damit Fehlerquellen minimiert werden.

> Hinweis: Weiterführende Informationen zu Prinzipien guter Programmierung finden sich unter den Begriffen KISS (keep it small and simple), DRY (don't repeat yourself) und SPOT (single point of truth).

Um eine Funktion benutzen zu können, muss diese zunächst nach folgender Struktur erstellt werden:
```python
# Funktionskopf
def name_der_funktion(x, y): # in der Klammer werdenan die an die Funktion zu übergebende Argumente genannt
    # Funktionsrumpf - auszuführender Code bei Aufruf
    z = x + y
    # Rückgabewert
    return z
    
# Benutzung:
ergebnis = name_der_funktion(2, 4)
print(ergebnis)

# Das Ganze lässt sich natürlich auch noch weiter vereinfachen:
def add_numbers(x, y):
    return x + y
    
add_numbers(5, 9)
```

Funktionen können auch mehr oder weniger Argumente übernehmen, als in obigem Beispiel.
Außerdem können Funktionen in Python auch mehrere Werte zurückgeben:
```python
def do_some_magic(x, y, z, a, b, c, some_text):
    sum = x + y + z + a + b + c
    prod1 = x * y * z
    prod2 = a * b * c
    new_text = "Summe: " + str(sum) + " " + some_text
    
    return sum, prod1, prod2, new_text
    
rueckgabe = do_some_magic(2, 5, 8, 3, 6, 7, "Tadaa")
print(rueckgabe[3])

```

## Klassen
Python unterstützt Objektorientierung, ähnlich wie Java oder C++. 
Das Grundkonzept der objektorientierten Programmierung besteht darin, Daten und deren Funktionen (Methoden) in einem Objekt zusammenzufassen. 

Eine Klasse ist zunächst eine formale Beschreibung eines Objekts, quasi eine Schablone zur Erstellung von Objekten. Ein realweltliches Beispiel: der Begriff "Toaster" steht nur stellvertretend für die Beschreibung von bestimmten Rahmenbedingungen, inklusive erwarteter Funktionalitäten.
Ein konkreter, real existierender Toaster stellt nun allerdings ein Objekt (auch Instanz genannt) der Klasse "Toaster" dar.

Klassen in Python:
```python
class Toaster():
    # Es folgt der Konstruktor - eine Methode der Klasse die sofort aufgerufen wird, wenn ein Objekt der Klasse erstellt wird
    def __init__(self, col):    # In jeder Methode einer Klasse muss als erster Parameter `self` stehen. Dies ist eine Referenz auf
                                # das Objekt selbst. Mit dieser Referenz kann mann auf Attribute oder Methoden des Objektes zugreifen.
        
        # Hier wird das Attribut `color` auf den Wert gesetzt, der dem Konstruktor übergeben wurde
        self.color = col
```
Nachdem die Klasse beschrieben wurde, können Instanzen dieser erstellt werden:
```python
# Die Instanziierung einer Klasse erfolgt wie der Aufruf einer Funktion mit dem Namen der Klasse und `()`.
# Das erstellte Objekt speichern wir in einer Variable:
t1 = Toaster("blau")

# Nun kann man mit dem `.` Operator auf Attribute und Methoden des Objektes zugreifen.
print(toaster.color)
```

Methoden in Klassen:
```python
# Beschreibung der Klasse
class Flasche():
    # Konstruktor
    def __init__(self, vol):
        # Hier wird das Volumen der Flasche deklariert und initialisert
        self.volumen = vol
        # Dieses Attribut enthält den aktuellen Füllstand der Flasche
        self.fuellstand
    # Methoden:
    def einfuellen(self, menge):
        if self.fuellstand + menge <= self.volumen:
            self.fuellstand += menge
        else:
            # Hier könnte man beispielsweise prüfen, ob die Flasche überlaufen würde
            print("Fehler")
    def leeren(self, menge):
        if self.fuellstand - menge >= 0:
            self.fuellstand -= menge
        else:
            # Hier könnte man beispielsweise prüfen, ob die Flasche nicht genug gefüllt ist
            print("Fehler")
```

Die Methoden der Klasse kann man nun wie folgt benutzen:
```python
f1 = Flasche(1.5)
f1.einfuellen(0.3)
print(f1.fuellstand)
f1.entnehmen(0.1)
print(f1.fuellstand)
```

## Python Module
Python ist eine modulare Sprache. Das bedeutet, jedes Python File <name_des_files>.py ist ein eigenständiges Modul, welches an anderen Stellen eingebunden werden kann. Für das einbinden von Modulen wird das Schlüsselwort import benutzt.
Es existiert bereits eine Vielzahl an vorgefertigten Modulen (auch Bibliotheken genannt), welche genutzt werden können.
Ein Beispiel ist die Bibliothek "time". Diese stellt bestimmte Funktionalitäten, wie das Auslesen der Systemzeit oder das Pausieren des Programmablaufs zur Verfügung. 
Beispiel:
```python
import time # importiert das komplette Modul `time`
print("Hello")
# Das Modul time enthält die Funktion namens `sleep()`, welche das Programm für eine bestimmt Zeit anhält (in s)
time.sleep(2)
print("World")
```

Werden nur bestimmte Funktionen aus einer Bibliothek benötigt, können diese auch gezielt importiert werden:
```python
from time import sleep
print("Hello")
sleep(2)
print("World")
```

## Nächste Schritte
Hier endet die kurze Zusammenfassung der wichtigsten Pythonkonzepte zur Nutzung des PiBots.
Um die Programmierung des Roboters für Sie zu erleichtern, existiert auch bereits eine entsprechende Bibliothek, welche den Zugriff auf alle grundlegenden Funktionen des Roboters ermöglicht.
Details zu deren Anwendung finden Sie in [02-PiBot_Programming_Guide.md](https://gitlab.hrz.tu-chemnitz.de/ketf--tu-chemnitz.de/hufa-pibot/-/blob/master/02-PiBot_Programming_Guide.md).
