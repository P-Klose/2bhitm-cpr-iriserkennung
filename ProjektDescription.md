# Iris Erkennung mittels Kamera und ResPi

## Überblick
### 

## Ziele
* Erkennen der Iris
* Server läuft
* Iris erkennbar
* Ansprechendes Design
* Abglichen von Mustern (ist es einer der Ersteller)
* Programmier Sprache JS

## Nicht Ziele
* Erkennung mit Namen

## Themenbeschreibung
  Es wird eine Schaltung und ein Programm entwickelt, das mithilfe von einer Kamera und der nötigen Soft und Hardware die Iris eines Menschen erkennt.
  Eventuell ist es möglich ein Schloss zu entwickeln, welches sich nur durch den Abgleich der richtigen Iris öffnet.

## Verwendete Technologie
  ResPi
  ResPi Cam
  
## Team-zusammenstellung
### Teamleader
  Peter Klose
### Teammitglieder
  Lukas Lummerstorfer
  Teofan Mihaescu
  Jakob Scheuer
  
## Zeitplan
### 11.3.21
  Teameinteilung, Informationen sammeln für eigenen Meilenstein.
  Besprechung vor 18.3.21 zur Koordination.
### 18.3.21
  Ersten Prototypen entwickeln und Lösungsideen für eventuelle Probleme         sammeln
### 25.3.21
  Prototypen erweitern/verbessern
### xx.xx.21
  Problemlosen Prototypen vorstellen
  
## Protokoll
### Anwesenhiet
Zuerst wurde auf die SD Kart ein passendes Image gespielt und der Raspberry zum laufen gebracht.

In weiterer Folge war die Aufgabe, dass die Kamera funktionen soll. 
Dies war durch ein Tutorial nicht sehr Kompliziert Link: https://www.youtube.com/watch?v=bpzGN35oaJ4&t=106s

Nach einigem Probieren und Rückschlägen durch zB.: Defektes Kameramodul, SD Karte zu langsam, usw. Ist es gelungen die Kamera zum laufen zu bringen und ein Bild/Video aufzunehmen.

Bereitstellung eines Codes durch den Professor. Dieser muss in anschließender Folge noch bearbeitet und adaptiert werden.
Durch den Bereitgestellten Code wurde das Gesicht erkannt und muss nun auf die Iris adaptiert werden.

### Distance
Server Programmieren und zum laufen gebracht.
Recherge, dass man die Neuen Daten auf den Server bekommt und darstellen kann.

Darstellung erfolgt durch NODE.js bei uns handelt es sich um einen Linien Chart.
Der Chart wird mit Daten von dem Python Programms versogt.
  Das Programm soll die Daten mithlfe von dem Request Module senden.
  
  Theorie Besprechung, recherge zu den anschließenden Aufgaben (OpenCV Iris),(von Py Program zu HTML Chart)


### Vorgegebene Technologien
#### SW
- OpenCV: https://opencv.org/
- Java Framework: highChart oder chartJS
- Docker: www.docker.com
#### HW
- Raspberry PI
- Raspberry PI Webcam https://at.rs-online.com/web/p/raspberry-pi-kameras/9132664/
- Raspberry PI IR Cam https://at.rs-online.com/web/p/raspberry-pi-kameras/9132673/


