# Themen 05.05.2025  

Vorlesung: Datenbanksysteme

## 1. Einreichaufgaben  

Die Einreichaufgaben wurden neu geordnet!
Anbei die Fristen und Themen.  

1. Professoren-Datenbank mit Stored Procedures etc. --> 2P bis 7.5.25 12 Uhr
2. Hashing --> 1P bis 14.5.25 23:59
3. Datenformate --> 1P bis 10.5.25 18:36
4. SQL - MongoDB --> 1P bis 19.05.25 19:00
5. SPEED-Aufgabe!!! MongoDB-Datenbank für Professoren-Informationssystem --> 1P bis 07.05.2025

## 2. Unicorns-Aufgaben

Lösungen zu den Aufgaben:  

* db.unicorns.find({name:'Aurora'})
* db.unicorns.find({gender:'f', loves:{$all:['apple', 'carrot']}})
* db.unicorns.find({gender:'f', $or: [{loves:'apple'},{loves: 'carrot'}]})
* db.unicorns.find({$or:[{vampires: {$exists:false}},{vampires: {$lte:0}}]})
* db.unicorns.find({gender:'m',$and:[{weight:{$gte:600}},{weight:{$lte:900}}]})

## 3. Zip-Code-Datenbank

* zip code datenbank laden --> LE6  
* Aufgaben zur Zip-Code-Datenbank gemeinsam durchgehen

## 4. Eigenarbeit  

Vergleich der SQL-Befehle mit MongoDB --> in erster Stunde in Eigenarbeit durcharbeiten.  

## 5. DB für Professoren-Informationssystem  

Siehe Aufgabenstellen in adaptiertem Übungsblatt

## 6. Python  

Installieren Sie Python und eine IDE Ihrer Wahl, z.B. Pycharm oder VSCode.  
Verbindung mit MongoDB herstellen, DB erzeugen, Dokument erzeugen etc.
