# Fallstudie: Steuerliche Datenanalyse für Kleinunternehmer

## 1) Einleitung / Szenario

### Szenario

Herr Paul Meier ist ein selbstständiger IT-Berater und Kleinunternehmer. Für das erste Quartal des Geschäftsjahres 2024 (Januar bis März) hat er seine Geschäftsausgaben in einer einfachen Buchhaltungssoftware erfasst. Nun möchte er seinen Jahresabschluss vorbereiten und die erfassten Ausgaben mit seinen Banktransaktionen abgleichen, um sicherzustellen, dass alle relevanten Ausgaben korrekt erfasst und keine möglichen Abzüge vergessen wurden. Außerdem möchte er einen Überblick über seine Einnahmen und Ausgaben pro Kategorie und Monat erhalten.

Die Daten aus der Buchhaltungssoftware liegen als CSV-Export vor und enthalten nur Ausgaben. Die Banktransaktionen liegen als Excel-Export vor und enthalten sowohl Abbuchungen (Ausgaben) als auch Gutschriften (Einnahmen). Die Kategorisierung in der Buchhaltungssoftware und die Beschreibungen in den Banktransaktionen sind nicht immer identisch, und es gibt Transaktionen in der Bank, die nicht in der Buchhaltung erfasst wurden (und umgekehrt).

Literatur / Quellen:

* Eine Einführung in die Sprache M Transformation Language, die zur Datentransformation in Power Query verwendet wird, finden Sie unter: <https://learn.microsoft.com/en-us/powerquery-m/m-spec-introduction>

## 2) Lernziele

Nach Bearbeitung dieser Fallstudie können Sie:

* Daten aus verschiedenen Quellen (CSV, Excel) in Excel Power Query laden.
* einfache Datenbereinigungs- und Transformationsschritte in Power Query ausführen (Datentypen anpassen, Spalten umbenennen, neue Spalten berechnen, bedingte Logik anwenden).
* Daten basierend auf Textinhalten kategorisieren.
* Daten aus unterschiedlichen Quellen konsolidieren.
* Pivot-Tabellen und Pivot-Charts zur Analyse von Finanzdaten erstellen.
* Diskrepanzen zwischen verschiedenen Datenquellen identifizieren

Bereitgestellte Daten:

1) [Bank-Transaktionen](bank_transaktionen_q1_2024.xlsx)  
2) [Export aus Buchhaltungssoftware](buchhaltung_ausgaben_q1_2024.csv)

## 3) Daten laden und transformieren in Power Query

### Starten des Power Query Editor

* Erstellen Sie eine Excel-Datei mit dem Namen `Übung_ETL.xlsx`
* Öffnen Sie ein leeres Excel-Arbeitsblatt.
* Gehen Sie zu `Daten > Daten abrufen > Aus Datei > Aus Excel-Arbeitsmappe` (für die folgende Excel-Datei) bzw. `Aus Text/CSV` (für die CSV-Datei).  

## 3 a) Laden und Transformieren der buchhaltung_ausgaben_q1_2024.csv

* Laden Sie die CSV-Datei wie oben beschrieben und klicken Sie dann auf `Daten transformieren`.
![alt text](image.png)

* Datentypen anpassen: Stellen Sie sicher, dass vor dem Laden das `Datum` als Datum und `Betrag_EUR` als Währung erkannt werden. Klicken Sie oben links auf den Datentyp und ändern Sie diesen. Bestätigen Sie mit `Aktuelle ersetzen`
![alt text](image-1.png)

* Spalten umbenennen: Benennen Sie zur Konsistenzsicherung die Spalten um:
  * Datum -> Transaktionsdatum
  * Beschreibung -> Details
  * Kategorie_Buchhaltung -> Kategorie
  * Betrag_EUR -> Betrag
![alt text](image-2.png)

* Neue Spalte 'Quelle' hinzufügen: Fügen Sie eine benutzerdefinierte Spalte namens Quelle hinzu, die den Wert "Buchhaltung" enthält.  
<img src="./image-3.png" alt="drawing" width="150"/>  <img src="./image-4.png" alt="drawing" width="500"/>

* Erstellen Sie analog zum vorherigen Schritt eine neue Spalte 'Typ'. Diese soll den Wert "Ausgabe" enthalten (da diese Datei nur Ausgaben enthält).
* Das Ergebnis sollte nun so aussehen:
![alt text](image-5.png)
* Der **Betrag muss noch korrigiert werden**; er ist um den Faktor 100 zu groß. Ausgaben sollen negative Werte sein, Einnahmen positive. Entsprechend müssen wir die Ausgaben der Buchhaltung durch 100 teilen und mit minus 1 multiplizieren:  > Transformieren > Standard > Multiplizieren (mit -(0.01)) oder / Teilen (durch -100)  

* Ergebnis:
![alt text](image-12.png)

Klicken Sie nun im Power Query-Editor auf `Schließen und Laden`.  

## 3 b) Laden und Transformieren der bank_transaktionen_q1_2024.xlsx

* Laden Sie die Excel-Datei.
* Datentypen anpassen: Stellen Sie sicher, dass `Transaktionsdatum` als `Datum` und `Abbuchung_EUR` sowie `Gutschrift_EUR` als Währung erkannt werden.
* 'Betrag'-Spalte erstellen: Fügen Sie eine benutzerdefinierte Spalte namens `Betrag` hinzu, die die Werte aus `Abbuchung_EUR` und Gutschrift_EUR kombiniert:
  * Wenn `Abbuchung_EUR` einen Wert hat, soll der Betrag `-Abbuchung_EUR` sein (negativ für Ausgaben).
  * Wenn `Gutschrift_EUR` einen Wert hat, soll der Betrag `Gutschrift_EUR` sein (positiv für Einnahmen).

```M
if [Abbuchung_EUR] <> null then -[Abbuchung_EUR]
else if [Gutschrift_EUR] <> null then [Gutschrift_EUR]
else 0)
```

![alt text](image-6.png)

* Neue Spalte 'Quelle' hinzufügen: Fügen Sie eine benutzerdefinierte Spalte namens Quelle hinzu, die den Wert "Bank" enthält.
* Neue Spalte 'Typ' hinzufügen: Fügen Sie eine benutzerdefinierte Spalte namens Typ hinzu:
  * Wenn `Abbuchung_EUR` einen Wert hat, soll der Typ "Ausgabe" sein.
  * Wenn `Gutschrift_EUR` einen Wert hat, soll der Typ "Einnahme" sein.

```M
if [Abbuchung_EUR] <> null then "Ausgabe" 
else if [Gutschrift_EUR] <> null then "Einnahme" 
else "ungültig"
```

* Neue Spalte 'Kategorie' hinzufügen (Herausforderung!): Fügen Sie eine benutzerdefinierte Spalte namens Kategorie hinzu. Diese soll die Transaktionen basierend auf dem `Details`-Text einer Kategorie zuordnen. Wenn keine Kategorie erkannt wird, verwenden Sie "Sonstiges".

```M
if Text.Contains([Details], "Mietzahlung")            then "Miete"
else if  Text.Contains([Details], "Microsoft") 
      or Text.Contains([Details], "Cloud") 
      or Text.Contains([Details], "Software")         then "Software"
else if  Text.Contains([Details], "Büromaterial") 
      or Text.Contains([Details], "Papier") 
      or Text.Contains([Details], "Elektrofachmarkt") then "Bürobedarf"
else if  Text.Contains([Details], "DB Ticket") 
      or Text.Contains([Details], "Taxi") 
      or Text.Contains([Details], "Parkgebühren")     then "Reisekosten"
else if  Text.Contains([Details], "Restaurant")       then "Bewirtung"
else if  Text.Contains([Details], "Online Kurs")      then "Fortbildung"
else if  Text.Contains([Details], "Honorar Kunde")    then "Einnahmen"
else                                                        "Sonstiges"
```

* Unnötige Spalten entfernen: Entfernen Sie die Spalten `Abbuchung_EUR` und `Gutschrift_EUR`.

### Daten konsolidieren

* Benennen Sie die Abfrage `buchhaltung_ausgaben_q1_2024` um in `Buchhaltung`
* Verwenden Sie Abfragen anfügen (Append Queries) im Power Query Editor.
* Fügen Sie die transformierte Bank-Transaktionen-Tabelle an die transformierte Buchhaltungs-Ausgaben-Tabelle an. Nennen Sie die neue Abfrage `Konsolidierung`. Verwenden Sie dazu "Abfragen als neu anfügen".  

Ergebnis:  
![alt text](image-13.png)

* Stellen Sie auch hier wieder sicher, dass Transaktionsdatum und Betrag korrekt formatiert sind (Datum bzw. Währung).
* Gruppieren Sie zuletzt die drei Abfragen in die Gruppe `Buchungssätze`. Gruppierungen sind hilfreich, um bei komplexeren Datenbereinigungen den Überblick über einzelne Schritte zu behalten.

### Laden der Daten

* Klicken Sie auf Schließen & laden > Schließen & laden in... > Nur Verbindung erstellen. (Dies ist besser, da die Daten direkt in das Datenmodell geladen werden und nicht erneut in Excel).
* Rechtsklicken Sie im Abfragebereich auf `Konsolidierung` und wählen Sie Laden in... > Nur Verbindung erstellen. Dies lädt die Daten ins Power Pivot Datenmodell.

## 4) Report erstellen mit Pivot-Charts

Verwenden Sie die geladene `Konsolidierung` , um die folgenden Pivot-Charts zu erstellen:

## 4 a) Monatliche Entwicklung der Einnahmen und Ausgaben nach Quelle

### Pivottabelle erstellen  

* Erstellen Sie eine Pivot-Tabelle basierend auf `Konsolidierung`. Verwenden Sie dazu "Empfohlene PivotTabellen"
* Ziehen Sie Transaktionsdatum in die Zeilen und gruppieren Sie es nach Jahren und Monaten.
* Ziehen Sie Quelle in die Spalten.
* Ziehen Sie Betrag in die Werte (Summe).
* Fügen Sie einen Slicer für Typ hinzu (filterbar auf "Einnahme" oder "Ausgabe").
  * Schritt-für-Schritt-Anleitung:
    * Wählen Sie eine Zelle innerhalb Ihrer Pivot-Tabelle aus.
    * Das ist wichtig, da die Registerkarten "PivotTable-Analyse" (oder "PivotTable-Tools") und "Einfügen" nur dann sichtbar werden.
    * Gehen Sie zur Registerkarte "PivotTable-Analyse" (oder "Analysieren" bei älteren Excel-Versionen) im Menüband.
    * Klicken Sie in der Gruppe "Filtern" auf "Datenschnitt einfügen" (oder "Slicer einfügen").

### Säulendiagrmm erstellen  

* Erstellen Sie ein Gruppiertes Säulendiagramm (oder Liniendiagramm), das die monatlichen Einnahmen/Ausgaben pro Quelle (Bank vs. Buchhaltung) visualisiert.

## 4 b) Vergleich der Ausgabenkategorien nach Quelle

### Pivottabelle erstellen (2)  

* Erstellen Sie eine neue Pivot-Tabelle.
* Ziehen Sie Kategorie in die Zeilen.
* Ziehen Sie Quelle in die Spalten.
* Ziehen Sie Betrag in die Werte (Summe). Stellen Sie sicher, dass es nur Ausgaben sind (Slicer Typ auf "Ausgabe" setzen).

### Säulendiagrmm erstellen (2)  

* Erstellen Sie ein Gruppiertes Säulendiagramm oder ein Balkendiagramm, um die Ausgaben pro Kategorie aus der Buchhaltung und von der Bank gegenüberzustellen.

## 4 c) Top-Ausgabenkategorien gesamt  

* Erstellen Sie eine neue Pivot-Tabelle.
* Ziehen Sie Kategorie in die Zeilen.
* Ziehen Sie Betrag in die Werte (Summe). Stellen Sie sicher, dass es nur Ausgaben sind (Slicer Typ auf "Ausgabe" setzen).
Wenden Sie einen Wertfilter auf Kategorie an, um z.B. die Top 5 oder Top 10 Kategorien anzuzeigen.
*Erstellen Sie ein Säulendiagramm oder Balkendiagramm.

## 5) Fragen zur Analyse und Reflexion

Nachdem Sie die Pivot-Tabellen und -Charts erstellt haben, beantworten Sie folgende Fragen:

* Identifizieren Sie Transaktionen, die in den Bankdaten auftauchen, aber nicht in den Buchhaltungsdaten oder umgekehrt.  
* Gibt es Kategorien, bei denen die Ausgaben zwischen Buchhaltung und Bank voneinander abweichen? Welche Gründe könnten hierfür vorliegen?
* Betrachten Sie die Kategorie-Spalte, die Sie in Power Query erstellt haben. Wie robust ist Ihre Kategorisierungslogik? Welche Herausforderungen gab es bei der Zuordnung von Banktransaktionen zu Kategorien, und wie könnten Sie diese verbessern?
* Welchen Vorteil bietet die Konsolidierung von Daten aus verschiedenen Quellen für die Erstellung eines Jahresabschlusses und die Steuererklärung?
