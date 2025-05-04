# Teil 2: MongoDB, Vergleich SQL mit JSON-Queries (v2)

Prof. Dr. Markus Grüne, 2025  

MongoDB ist ein Document Store, der verwendet werden kann, um XML- und JSON-Dateien zu speichern. In dieser Übung lernen Sie die Grundlagen von
MongoDB anhand eines Beispiels und durch die Gegenüberstellung von SQL- und MongoDB-Befehlen.

## 1. Die Unicorns-Datenbank

### 1.1 Vorbereitung

Legen Sie sich in MongoDB eine Datenbank mit dem Namen „Unicorns" an und erzeugen Sie in der Datenbank eine gleichnamige Collection „Unicorns".
Aktivieren Sie anschließend die Datenbank mit dem `USE`-Befehl.
Fügen Sie nun den in Moodle zu findenden Unicorns.txt per Copy Paste Compass Shell ein und führen Sie die Befehle aus. Sie sollten nun eine Unicorns-DB haben.  

Quelle zu dieser Übung: [Link](https://github.com/karlseguin/the-little-mongodb-book/blob/master/en/mongodb.markdown)

### 1.2 Befehle für die Unicorns-DB  

Lassen Sie sich nun die Wesen mit den jeweils folgenden Eigenschaften
anzeigen und speichern Sie sich die Anfragen!

- mit Namen Aurora
- alle Weibchen, welche Äpfel mögen.
- alle Weibchen, welche Äpfel und Karotte mögen.
- alle Weibchen, welche Äpfel oder Karotte mögen.
- alle Wesen, welche bis jetzt noch keine Vampire verspiesen haben.
- alle Männchen, welche ihr Gewicht zwischen 600 und 900 haben.

## 2. Vergleich der Befehle von MongoDB mit SQL (CRUD) / Terminologien vergleichen

Linkg zum offiziellen SQL-MongoDB-Vergleich: [Link](https://www.mongodb.com/docs/manual/reference/sql-comparison/)

Legen Sie ein **Excel-Dokument** mit folgendem Dateinamen an:  
_\<Nachname\>\_\<Vorname\>\_VergleichSQLMongoDB.xlsx_  

Geben Sie auch Beispielbefehle für die _Unicorns-Datenbank_ an.

| **CRUD-Operation** | **SQL (z. B. MySQL)** | **MongoDB** | **Beispiele**               |
|---------------|-----------------------|---------------------|----------------------------------|
| **Create** im Sinne von CRUD   (nicht mit SQL create zu verwechseln!) | `INSERT INTO table_name (column1, column2) VALUES (value1, value2);`                 | `db.collection.insertOne({ "field1": value1, "field2": value2 });`          | **SQL**: `INSERT INTO users (name, age) VALUES ('Alice', 25);`<br>  **MongoDB**: `db.users.insertOne({ "name": "Alice", "age": 25 });` <br> Bitte mit treffenden Abfragen gegen die Unicorns ersetzen! |
| CREATE im Sinne von SQL (inkl. Indexierung) |  |   | |  
| ALTER TABLE im Sinne von SQL | | | |  
| DROP TABLE im Sinne von SQL | | | |  
| INSERT | | | |  
| READ im Sinne von CRUD <br> D.h. SELECT FROM WHERE | | | |  
|   ... mit logischem AND | | | |  
|   ... mit logischem ODER | | | |  
|   ... mit Vergleichsprädikat (\>, \< ....) | | | |  
|  ... mit ORDER BY | | | |  
|  ...  mit COUNT | | | |  
| UPDATE im Sinne von CRUD und SQL | | | |  
| DELETE im Sinne von CRUD und SQL | | | |  
