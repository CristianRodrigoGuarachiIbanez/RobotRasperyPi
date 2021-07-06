# Programmierung des PiBots

Grundsätzlich gibt es verschiedene Möglichkeiten zur Programmierung des Roboters. Die folgende Auflistung ist daher nicht abschließend.

## Möglichkeit 1: Direkt auf dem PiBot programmieren
> Empfohlene Methode!

Dies ist die einfachste Methode.
Durch den Anschluss von Maus, Tastatur und Bildschirm kann der PiBot wie ein normaler PC genutzt werden.

1. Schließen Sie zuerst die benötigten Peripheriegeräte an.
2. Starten die den PiBot wie [hier](https://gitlab.hrz.tu-chemnitz.de/ketf--tu-chemnitz.de/hufa-pibot/-/blob/master/README.md) beschrieben.
3. Offnen Sie den Ordner "hufa-pibot" (dieser befindet sich in /home/pi/).
4. Folgen Sie den Anweisungen in 03-task1.py.

## Möglichkeit 2: Programmieren auf der MicroSD Karte auf eingenem Endgerät
> Hinweis: Diese Methode funktioniert nur unter Linux, da Windows das Dateisystem des Raspberry Pi nicht lesen kann

1. Enfernen Sie die Speicherkarte aus dem Raspberry Pi.
2. Verbinden Sie die Speicherkarte (ggf. mit Adapter) mit Ihrem PC.
3. Öffnen Sie auf der Partition "rootfs" den Ordner "home/pi/hufa-pibot".
4. Folgen Sie den Anweisungen in 03-task1.py.

## Möglichkeit 3: Zugriff per ssh von eigenem Endgerät aus
> Hinweis: Diese Methode ist etwas fortgeschrittener und setzt Kenntnisse im Umgang mit einem Linux Terminal voraus. Lassen Sie sich ggf. helfen, falls die anderen Möglichkeiten nicht in Betracht kommen.

1. Zunächst ist auch hier ein Start des Raspberry Pi mit angeschlossenen Monitor, Maus und Tastatur notwendig.
2. Verbinden Sie den PiBot nun mit Ihrem WLAN (siehe [hier](https://gitlab.hrz.tu-chemnitz.de/ketf--tu-chemnitz.de/hufa-pibot/-/blob/master/README.md) unter Punkt "connect to the internet").
3. Öffnen Sie ein Terminal.
4. Geben Sie folgenden Befehl ein und notieren Sie sich die daraufhin angezeigte IP Adresse:
```bash
sudo ifconfig wlan0 | grep "inet " | cut -c 14-28
```
5. Öffnen Sie auf Ihrem PC ein Terminal.
6. Mit dem folgenden Befehl können Sie sich nun auf dem PiBot einloggen. XXX.XXX.XXX.XXX ist dabei durch die notierte IP Adresse zu ersetzen. Das Passwort lautet "ok".
```bash
ssh pi@XXX.XXX.XXX.XXX
```
7. Dateien können nun z.B. mit dem Editor Nano bearbeitet werden. Um eine Datei in Nano zu speichern drücken Sie `Strg + o` und `Enter` zum Schließen `Strg + x`.
```bash
nano dateiname.py
```
8. Folgen Sie den Anweisungen in 03-task1.py.

## Ausführung von Code
Sollten Sie sich für eine andere als Möglichkeit 1 zur Programmierung des PiBots entschieden haben, beachten Sie bitte, dass der Code nur auf dem Roboter selbst lauffähig ist.
Die Ausführung auf anderen Geräten ist mangels der pibot Bibliothek und falscher Systemarchitektur nicht möglich.

Eine Python Datei kann im Terminal mittels
```bash
python3 dateiname.py
```
ausgeführt werden.
> Hinweis: Da es sich empfiehlt den Roboter ohne angeschlossene Peripheriegeräte fahren zu lassen, sollte Ihr Programm idealerweise erst auf Knopfdruck, nach dem Entfernen von Maus, Tastatur und Monitor, starten. Siehe dazu "Auf den mittleren Button warten" weiter unten.

Die Ausführung von Code können Sie jederzeit mit `Strg + c` unterbrechen.
Unter Umständen ist es zusätzlich nötig, den Arduino Uno auf der Oberseite der Platine zu resetten.
Dazu drücken Sie einfach den kleinen schwarzen Taster in der Mitte des Arduinos (großes, blaues Rechteck).

Sollten Sie Möglichkeit 2 zur Programmierung nutzen, können Sie Ihren Code statt mit Hilfe von Maus, Monitor und Tastatur am Pi auch wie folgt starten:
Öffnen Sie die Datei boot.sh - diese befindet sich im Verzeichnis /home/pi.
Ergänzen Sie nun den Inhalt wie folgt:

Vorher:
```bash
#!/bin/bash
. /home/pi/venv/bin/activate
python3 boot.py
```
 Nachher:
 ```bash
#!/bin/bash
. /home/pi/venv/bin/activate
python3 boot.py &
cd hufa-pibot
python3 IhrDateiname.py
 ```
Ersetzen Sie dabei "IhrDateiname.py" durch den Namen der zu startenden Datei und vergessen Sie nicht das "&" in Zeile 3.

# Die pibot Bibliothek
Wie bereits in der Python Einführung erwähnt, erleichtert die pibot Bibliothek den Zugriff auf alle notwendigen Funktionen des Roboters.
Im Folgenden werden die verschiedenen Funktionalitäten des PiBots näher betrachtet.

## LEDs benutzen
```python
from pibot import leds
from pibot import constants as c

leds.init_leds() # Diese Zeile muss einmalig aufgerufen werden, bevor die LED's benutzt werden können

# Die frontalen LED's können nur an- oder ausgeschaltet werden:
leds.set_led(c.LED_FRONT_LEFT, c.ON)
leds.set_led(c.LED_FRONT_RIGHT, c.ON)
leds.set_led(c.LED_FRONT_LEFT, c.OFF)
leds.set_led(c.LED_FRONT_RIGHT, c.OFF)

# Die 3 LED's neben den Buttons können 3 Farben annehmen: RED, YELLOW, GREEN
leds.set_led(c.LED_LEFT, c.RED)
leds.set_led(c.LED_MID, c.YELLOW)
leds.set_led(c.LED_RIGHT, c.GREEN) 
```

## Buttons
```python
from pibot import buttons
from pibot import constants as c
from time import sleep

buttons.init_buttons() # Diese Zeile muss einmalig aufgerufen werden, bevor die Buttons benutzt werden können

# Auf den linken Button warten
print("Waiting for Left Button...")
buttons.wait_for_button(c.BUTTON_LEFT)

# Auf den mittleren Button warten
print("Waiting for Mid Button...")
buttons.wait_for_button(c.BUTTON_MID)

# Auf den rechten Button warten
print("Waiting for Right Button...")
buttons.wait_for_button(c.BUTTON_RIGHT)
```

## Motoren steuern
```python
from pibot.nano import Nano
from time import sleep

nano = Nano()   # Diese Zeile ist einmalig nötig um den Arduino Nano auf der Platine zu initialisieren
nano.set_motors(50, 50) # Die beiden Werte in der Klammer steuern die Geschwindigkeit des linken und rechten Rades.
                        # Auch negative Werte (für Rückwärtsdrehung) sind möglich.
sleep(3)
nano.set_motors(0, 0)  
```

## Encoder auslesen und zurücksetzen
Die Encoder zählen die Radumdrehungen. Der Wert 180 entspricht dabei in etwa einer Radumdrehung.
```python
from pibot.nano import Nano
from time import sleep

nano = Nano()

# Encoder auf 0 zurücksetzen
nano.reset_encoders()

# Motoren starten
nano.set_motors(50, 50)
for _ in range(10):
    # Der aktuelle Stand der Encoder wird als Tupel von 2 Werten zurückgegeben 
    print(nano.get_encoders()) 
    # alternativ:
    # left, right = nano.get_encoders()
    # print(left, right)
    sleep(0.5)
```

## Ultraschallsensoren
Der Rückgabewert der Funktion entspricht der gemessenen Distanz in cm.
> Wichtiger Hinweis: Beim Überschreiten der maximal messbaren Distanz wird der Wert 0 zurückgegeben!

```python
from pibot.nano import Nano
from time import sleep

nano = Nano()
while True:
    # nano.get_distances() gibt ein Tupel mit 3 Werten zurück
    dist = nano.get_distances()
    print(dist)
    # alternativ:
    # left, mid, right = nano.get_distances()
    sleep(0.5)
```

## Und jetzt?
Werfen Sie einen Blick in die Datei [03-task.py](https://gitlab.hrz.tu-chemnitz.de/ketf--tu-chemnitz.de/hufa-pibot/-/blob/master/03-tasks.py).
Diese Enthält Ihre Aufgaben und weitere Hinweise.
