# Erstellung einer Geographie-Dimension in Power Query

Dieses Dokument beschreibt die Schritte zur Erstellung einer Geographie-Dimension in Power Query, basierend auf den bereitgestellten Adressdaten. Eine Geographie-Dimension ermöglicht das Filtern und Analysieren von Daten nach geographischen Kriterien in Berichten und Visualisierungen.

## Voraussetzungen  

Kopieren Sie die folgende Datei:  
`Schritt2_Dimensionstabelle_für_Datum_anlegen.xlsx`
nach  
`Schritt3_Dimensionstabelle_für_Geografie_anlegen.xlsx`

## Schritt-für-Schritt-Anleitung

### 1. Abfrage duplizieren (Empfohlen)

Es ist gute Praxis, die ursprüngliche Datenabfrage beizubehalten und eine Kopie für die Dimensionstabelle zu verwenden.

* Im Power Query Editor, klicke mit der **rechten Maustaste** auf deine bestehende Abfrage im **"Abfragen"**-Bereich (Queries) auf der linken Seite.
* Wähle **"Duplizieren"** (Duplicate).
* Benenne die neue Abfrage um, z.B. in `Geography_Dimension`.

### 2. Relevante Spalten auswählen

Eine Dimensionstabelle sollte nur die Spalten enthalten, die für ihre spezifische Funktion (hier: Geographie) relevant sind.

* Wähle im Menüband **"Start"** > **"Spalten auswählen"**  
* **Entferne die Häkchen** bei allen Spalten, die *nicht* in die Geographie-Dimension gehören. Behalte folgende Spalten:
  * `Adress-ID` (als Primärschlüssel)
  * `Straße` 
  * `Hausnummer`
  * `Postleitzahl`
  * `Stadt`
  * `Bundesland`
  * `Land`
  * `Breitengrad` (Latitude)
  * `Längengrad` (Longitude)

### 3. Duplikate entfernen

Stelle sicher, dass jede Adresse in der Dimensionstabelle eindeutig ist. `Adress-ID` sollte hier der eindeutige Schlüssel sein.

* Wähle die Spalte **`Adress-ID`** aus.
* Klicke mit der **rechten Maustaste** auf den Spaltenkopf und wähle **"Duplikate entfernen"** (Remove Duplicates).

### 4. Spalten umbenennen (Optional)

Passe die Spaltennamen bei Bedarf an, um sie sprechender und konsistenter zu machen (z.B. keine Leerzeichen oder Sonderzeichen, wenn sie später in Power BI verwendet werden).

* **Doppelklicke** auf einen Spaltenkopf, um ihn umzubenennen.

### 5. Datentypen überprüfen und anpassen

Korrekte Datentypen sind entscheidend für die Funktionalität und Leistung.

* Klicke auf das **Symbol links neben dem Spaltennamen** (zeigt den aktuellen Datentyp an).
* Wähle den passenden Datentyp aus der Liste:
  * `Adress-ID`: Text oder Ganze Zahl (wenn nur Zahlen)
  * `Straße`, `Hausnummer`, `Stadtteil`, `Postleitzahl`, `Stadt`, `Bundesland`, `Land`: **Text**
  * `Breitengrad`, `Längengrad`: **Decimal Number**

### 6. Zusätzliche Spalten für Hierarchien (Optional)

Erstelle kombinierte Spalten, die nützlich für Hierarchien und die Anzeige sind.

* **Beispiel: `Vollständige_Adresse`**
  * Wähle die Spalten `Straße`, `Hausnummer`, `Postleitzahl`, `Stadt`, `Bundesland`, `Land` aus (halte die `Strg`-Taste gedrückt, um mehrere Spalten zu wählen).
  * Gehe im Menüband zu **"Spalte hinzufügen"** (Add Column) > **"Spalten aus Text"** (Text from Columns) > **"Spalten zusammenführen"** (Merge Columns).
  * Wähle ein geeignetes Trennzeichen (z.B. **Komma und Leerzeichen ", "**).
  * Benenne die neue Spalte **`Vollständige_Adresse`**.

### 7. Power Query schließen und anwenden

Wenn alle Transformationen abgeschlossen sind, lade die Daten in dein Datenmodell.

* Klicke im Power Query Editor auf **"Schließen & Laden"** (Close & Load) oder **"Schließen & Laden in..."** (Close & Load To...).
  * Wenn du Excel verwendest, wähle **"Tabelle"** (Table) und den Ort, wo die Tabelle platziert werden soll.
  * Wenn du Power BI Desktop verwendest, wähle einfach **"Schließen & Anwenden"** (Close & Apply).

## Nach dem Laden in Power BI Desktop

Nachdem die `"Geography_Dimension` Tabelle in Power BI geladen wurde, führe folgende Schritte aus:

### 1. Beziehung erstellen

Verknüpfe deine neue Dimensionstabelle mit deinen Faktentabellen.

* Wechsle zur **Modellansicht** (Model View) in Power BI Desktop.
* Erstelle eine Beziehung zwischen deiner **Faktentabelle** (z.B. deine Kunden- oder Umsatzdaten) und der **`"Geography_Dimension`** Tabelle.
* Ziehe die Spalte **`Adress-ID`** von der `"Geography_Dimension` (die "Eine"-Seite) zur entsprechenden `Adress-ID`-Spalte in deiner Faktentabelle (die "Viele"-Seite).
* Stelle sicher, dass die Kardinalität **"Eins zu Viele"** (One-to-Many) ist und die Kreuzfilterrichtung **"Einzeln"** (Single) oder **"Beide"** (Both) (je nach Bedarf) ist.

### 2. Geographische Kategorien zuweisen (Power BI)

Dies ist entscheidend, damit Power BI die Daten für Karten-Visualisierungen korrekt interpretiert.

* Wechsle zur **Datenansicht** (Data View) oder **Berichtsansicht** (Report View).
* Wähle die **`"Geography_Dimension`** Tabelle im Bereich "Felder" (Fields) aus.
* Wähle nacheinander folgende Spalten aus und weise ihnen im **"Spaltentools"** (Column Tools) oder **"Modellierung"** (Modeling) Menüband die entsprechende **"Datenkategorie"** (Data Category) zu:
  * `Land`: **Land oder Region** (Country or Region)
  * `Bundesland`: **Bundesland oder Provinz** (State or Province)
  * `Stadt`: **Ort** (City)
  * `Postleitzahl`: **Postleitzahl** (Postal Code)
  * `Breitengrad`: **Breitengrad** (Latitude)
  * `Längengrad`: **Längengrad** (Longitude)
