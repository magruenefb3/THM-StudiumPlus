# Aufgabensammlung Datenbanksysteme

Autor: Prof. Dr. Markus Grüne

_Hinweis:_ Die Aufgabensammlung enthält Musterfragen, die in dieser Form auch in der Klausur vorkommen können.  

Datum: 02.06.2025

------------------------
TODO: Lösungen löschen

## Aufgabe 1 - Einleitung

1) Beschreiben Sie, inwieweit sich die Begriffe "Digitalisierung" und "Digitale Transformation" unterscheiden.  

> **Digitalisierung**: Z.B. Umwandlung bestehender Dokumente in digitale Repräsentation, eher technische Betrachtung  
> **Digitale Transformation**: Automatisierung, Ersetzung von Systemen, tiefgreifender Transformationsprozess, der auf Digitalisierung basiert.

2) Erläutern Sie drei Gründe, wieso Künstliche Intelligenz-Systeme erst in den letzten Jahren aufgekommen sind.  

> Öffentliche Verfügbarkeit von großen Datenmengen, hoher Rechenleistungen (Cloud-Systemen), geeignete Programmieransätze, Investitionssummen gestiegen (öffentlich und private Investitionen)

3) Nennen und beschreiben Sie je einen Vor- und einen Nachteil des Cloud Computings für die Gestaltung von IT-Infrastrukturen in Unternehmen.  

> Vorteil des Cloud Computings: Rechenleistung kann nach Bedarf skaliert werden, Diense, z.B. für Datenanalysen, KI-Anwendungen können per pay-as-you-go gebucht werden.  
> Nachteil: Bindung an Anbieter - Lock-In  

4) Erläutern Sie, für welche Anwendungsfälle relationale Datenbanken geeignet sind und warum diese (nicht oder auf jeden Fall) in den nächsten Jahrzehnten in Unternehmen eingesetzt werden.  

RDBS sehr gut für Speicherung von strukturierten Daten --> gibt es immer noch, daher wird es weiter eingesetzt. Dagegen: Cloud-Systeme bauen auch auf anderen Datenhaltungssystemen auf und werden die RDBS langfristig verdrängen.

## Aufgabe 2 - Business Intelligence

1) Beschreiben Sie den Unterschied zwischen OLTP und OLAP-Systemen. Gehen Sie insbesondere auf die Einsatzzwecke der beiden Systemtypen ein.  

OLTP: Transkationsverarbeitendes System (online transaction processing), sinngem. Produktionssysteme, die im täglichen Betrieb eingesetzt werden (Durchführung von Geschäftsprozessen)

OLAP: Systeme für Analysen auf Datenbeständen, Analysen z.B. Produktgruppenanalysen (Umsätze, Deckungsbeiträge), Quartalszahlen ...

2) Definieren Sie den Begriff "ROLAP".  

ROLAP: Relational Online Analytical Processing - Star / Snowflake, OLAP auf relationalen Strukturen.

3) Erläutern Sie folgenden Sachverhalt an einem Beispiel:
Measures, die die Anforderung der summarizability erfüllen, müssen Disjunktheit der Instanzen aufweisen.

Ein Produkt kann nicht zu 2 Kategorien gehören, andernfalls würde ein Produktverkauf ggf. 2mal in einer Aggregation berücksichtigt werden.  

### Ausfülltext  

Kennzahlen in einem DWH basieren auf **Fakten**-Tabellen.  

Wenn ein OLAP-Würfel wenige Measures enthält, die mit Kombinationen von Dimensionswerten verbunden sind, ist der Würfel **sparse / spärlich** befüllt.  

Eine Dimensionsinstanz umfasst alle **Ausprägungen der Measures** auf allen Ebenen einer Dimension.  

### OLAP-Operationen

Gegeben sei die folgende SQL-Abfrage. Stellen Sie sich vor, dass diese auf einen Würfel ausgeführt wird. Welcher OLAP-Operation würde diese Abfrage entsprechen? Begründen Sie kurz!

```SQL
SELECT
    d.Jahr,
    d.Monat,
    p.Kategorie,
    s.Region,
    SUM(f.Umsatz) AS GesamtUmsatz
FROM
    FaktVerkauf f
JOIN
    DimensionDatum d ON f.DatumID = d.DatumID
JOIN
    DimensionProdukt p ON f.ProduktID = p.ProduktID
JOIN
    DimensionStandort s ON f.StandortID = s.StandortID
WHERE
    d.Jahr = 2024
    AND d.Monat IN ('Januar', 'Februar', 'März') 
    AND p.Kategorie IN ('Elektronik', 'Haushaltsgeräte') 
    AND s.Region IN ('Nord', 'West') 
GROUP BY
    d.Jahr,
    d.Monat,
    p.Kategorie,
    s.Region
ORDER BY
    d.Jahr, d.Monat, p.Kategorie, s.Region;
```

Antwort:  
DICE-Operation
Das Ergebnis der Abfrage wäre ein Teilcube, der Ihnen den aggregierten Umsatz für jede Kombination aus den Monaten Januar, Februar, März 2024, den Produktkategorien Elektronik und Haushaltsgeräte, und den Regionen Nord und West anzeigt.

## Aufgabe 3 - Optimierung von DBn und Verteilung

### Wahr oder falsch?

|  Beispiel | Wahr | Falsch |
| -- | -- | -- |
| Ein Query Execution Plan kann verwendet werden, um zu prüfen, ob durch das Setzen eines Indexes die Performance einer Abfrage erhöht werden kann | x | |
| Bei einer Menge von vorher bekannten Werten, die ein Attribut aufnehmen kann, ist es aus Performance-Gründen sinnvoll, einen ENUM-Datentyp zu definieren. | x | |
| Abfragen, die auf Ungleichheit prüfen (!=) sind deutlich schneller als Abfragen, die auf Gleichheit prüfen. | | x |
| Spalten, die in Selektionskriterien verwendet werden, sollten i.d.R. indiziert werden, wenn die Performance nicht ausreicht. | x | |

### Optimierung

In der folgenden Abbildung finden Sie 4 Optimierungsregeln. Schildern Sie, in welchem Fall die 4. Regeln angewendet werden kann.  
![Optimierungsregeln](image.png)

Nur möglich, wenn die Join-Attribute auch in der "Auswahl" vorkommen.

### Trigger

```SQL
CREATE TRIGGER before_update_salary BEFORE UPDATE ON employees 
FOR EACH ROW 
BEGIN 
IF NEW.salary <> OLD.salary THEN 
    INSERT INTO salary_changes(employee_id,old_salary,new_salary) 
    VALUES(NEW.employee_id,OLD.salary,NEW.salary); 
END IF; 
END;
```

Erklären Sie, welche Funktion dieser Trigger hat und was unter `NEW` und `OLD` zu verstehen ist.  

Wenn Gehalt von MA aktualisiert, dann wir das alte Gehalte in salary_changes (old_salary) gespeichert.
NEW: Neue Werte, die zur Ersetzung verwendet werden. 
OLD: die alten Werte, vor Ersetzung

### Stored Procedure (ZU HAUSE)

Erstellen Sie eine Stored Procedure namens `berechneSumme`, die folgende Aufgabe ausführt:

* Es soll eine Rechnungssumme ermittelt werden.  
* Die Rechnungssumme wird aus den Preisen in der Tabelle `Rechnungsposition` ermittelt.  
* Rechnungspositionen umfassen die Rechnungsnummer (`Rg.ID`) sowie die fortlaufenden Positionsnummern.  
* Preise der Positionen errechnen sich aus der `Menge` in der Tabelle Position und dem `Einzelpreis`, der ebenfalls in der Tabelle Position gespeichert ist.  

Tabelle: _Rechnung_

| Rg.ID | Datum | Besteller |
| -- | -- | -- |
| R-1 | 13.10.2024 | A-Firma |
| R-2 | 14.10.2024 | B-Firma |

Tabelle: _Rechnungsposition_

| Rg.ID | Pos.ID | Artikel | Menge | Einzelpreis |
| -- | -- | -- | -- | -- |
| R-1 | P-1 | Schnappverschluss | 2 | 4.50 |
| R-1 | P-2 | Staubwedel | 1 | 12.90 |
| R-2 | P-1 | Schnürsenkel | 2 | 3.00 |
| R-2 | P-2 | Schuhcrème | 3 | 4.75 |

## Aufgabe 4 - NoSQL

### Dokumentorientierte Datenbanken

1) Was verstehen Sie unter einem Dokument im Sinne einer dokumentorientierten DB? Inwieweit unterscheidet sich dies von einem herkömmlichen Dokument, z.B. einem Word-Dokument?  

Ein Dokument im Sinne einer Dokumenten-DB ist eine Dateninstanz, die einem Vokabular folgt, dass z.B. angibt, welche Tags im Dokument in welche Reihenfolge und Schachtelung verwendet werden dürfen. 

2) Das CAP-Theorem besagt, dass nur zwei der folgenden Eigenschaften durch eine Datenspeicherlösung umgesetzt werden können: Consistency, Availability, Partition Tolerance. Erläutern Sie die drei Eigenschaften.  

> **Eigenarbeit**

Consistency: Daten sind über alle Knoten konsistent, egal auf welchem Knoten die Daten abgerufen werden und spiegeln alle Update-Operationen wieder.  
Availability:  
Partition Tolerance:

## Aufgabe 5 - Datenformate

1) Erklären Sie, wozu XML aus geschäftlicher Sicht verwendet werden kann.  
Z.B. für die Konfiguration von Anwendungen, Definition von Datenaustauschformaten (Nachrichtenformate für Rechnungen)

2) XML-Dokumente können nach dem Parsen in einem DOM vorliegen. Was ist damit gemeint und wozu kann das DOM verwendet werden?

DOM: Objektbaum / Document Object Model: interne Repräsentation eines Dokumentes als Baum, die dazu verwendet werden kann, Elemente zu ändern, neue einzufügen, oder zu löschen. 

### YAML nach JSON - Transformationsaufgabe

Forme das folgende YAML-Dokument in ein JSON-Dokument um:

```YAML
person:
  name:
    vorname: Lang
    nachname: Lang
  geburtsdatum: 1982-06-14
  geburtsort: Shenyang, China
  nationalitaet: Chinesisch
  webseite: https://www.langlang.com

musikalische_informationen:
  instrumente:
    - Klavier
  ausbildung:
    - institution: Zentrales Musikkonservatorium Peking
      ort: Peking, China
      abschlussjahr: null # Jahr ist nicht explizit genannt
    - institution: Curtis Institute of Music
      ort: Philadelphia, USA
      abschlussjahr: 2008 # Beispielhaftes Abschlussjahr
```

```JSON
{
  "person": {
    "name": {
      "vorname": "Lang",
      "nachname": "Lang"
    },
    "geburtsdatum": "1982-06-14",
    "geburtsort": "Shenyang, China",
    "nationalitaet": "Chinesisch",
    "webseite": "https://www.langlang.com"
  },
  "musikalische_informationen": {
    "instrumente": [
      "Klavier"
    ],
    "ausbildung": [
      {
        "institution": "Zentrales Musikkonservatorium Peking",
        "ort": "Peking, China",
        "abschlussjahr": null
      },
      {
        "institution": "Curtis Institute of Music",
        "ort": "Philadelphia, USA",
        "abschlussjahr": 2008
      }
    ]
  }
}
```

## Aufgabe 6 - MongoDB

Vorbereitung: Erstellen Sie sich eine MongoDB-Datenbank mit dem Namen `Aufgabe_6`. In der DB erstellen Sie zwei Collections mit den Namen 'studierende' und 'referenten'.

Laden Sie die beiden Dateien in die Collections:
[studierende.json](studierende.json) und [referenten.json](referenten.json)  

1) Wieviele Dokumente befinden sich nun in den Collections?

TODO

2) Was macht die folgende Abfrage:

```JSON
--- Abfrage 1

db.referenten.insertOne(
  {
    "anrede": "Frau",
    "titel": "Dr.",
    "vorname": "Lena",
    "nachname": "Müller",
    "telefon": "+49 30 99887766",
    "email": "lena.mueller@intern.de",
    "adresse": "Hauptstr. 5, 10115 Berlin",
    "strasse": "Hauptstr.",
    "plz": "10115",
    "ort": "Berlin",
    "hausNr": "5",
    "idReferent": 29, // Beispiel für eine neue, eindeutige ID
    "istExtern": 0,   // 0 für intern
    "adrHinweis": ""
  }
);

Fügt ein JSON-Dokument für Frau Dr. Müller der Datenbank / collection hinzu.

--- Abfrage 2
db.referenten.updateOne(
  { "idReferent": 1 }, 
  { $set: { "mittelname": "Kemal" } } 
);

```

Setzt bei Person mit ID 1 den mittelname auf Kemal, wenn dieser noch nicht vorhanden, wird das Attribut außerdem angelegt. 

AB HIER AM 16.6.25

## Aufgabe 7 - Graphen(datenbanken)

1) Zeichnen Sie einen ungerichteten Graphen mit 4 Knoten und 5 Kanten.  
![Diagramm](A7.1%20Diagramm.jpg)
2) Beschreiben Sie einen Anwendungsfall, für den Graphendatenbanken wie Neo4J besser geeignet sind als relationale Datenbanken.  

Analyse von Netzen, z.B. um Beziehungen zwischen Knoten zu finden. Relationale Datenbanken können Beziehungen nur über Joins darstellen.

3) Erstellen Sie eine Neo4J-Datenbank mit folgender Spezifikation  

* Es sollen die Schulfächer Mathematik, Englisch und Deutsch erfasst werden.  
* Es sollen vier Schüler erfasst werden, die die Fächer belegen. Nicht alle sollen dieselben Fächerkombinationen belegen. Die Schüler haben einen Vornamen und einen Nachnamen sowie ein Alter in Jahren.  
* Ein Schüler bzw. eine Schülerin schreibt eine Klausur in Mathematik am 4.6.2025. Ein/e weitere/r schreibt am 7.6.2025 eine Klausur in Englisch.  

* Dumpen Sie die Datenbank und laden Sie diese auf den Stick. Der Name des Dumps muss Ihrem Nachnamen entsprechen.  

```Cypher
// 1. Alle vorhandenen Daten löschen (nur wenn es eine leere Datenbank sein soll)
MATCH (n) DETACH DELETE n;

// 2. Schulfächer erfassen
CREATE (m:Fach {name: 'Mathematik'})
CREATE (e:Fach {name: 'Englisch'})
CREATE (d:Fach {name: 'Deutsch'});

// 3. Schüler erfassen mit Vorname, Nachname und Alter
CREATE (s1:Schueler {vorname: 'Lena', nachname: 'Meyer', alter: 16});
CREATE (s2:Schueler {vorname: 'Max', nachname: 'Huber', alter: 17});
CREATE (s3:Schueler {vorname: 'Mia', nachname: 'Schulz', alter: 18});
CREATE (s4:Schueler {vorname: 'Tim', nachname: 'Wagner', alter: 16});

// 4. Schüler Fächer belegen (verschiedene Kombinationen)
MATCH (s1:Schueler {vorname: 'Lena'}), (m:Fach {name: 'Mathematik'}), (e:Fach {name: 'Englisch'})
CREATE (s1)-[:BELEGT]->(m), (s1)-[:BELEGT]->(e);

MATCH (s2:Schueler {vorname: 'Max'}), (e:Fach {name: 'Englisch'}), (d:Fach {name: 'Deutsch'})
CREATE (s2)-[:BELEGT]->(e), (s2)-[:BELEGT]->(d);

MATCH (s3:Schueler {vorname: 'Mia'}), (m:Fach {name: 'Mathematik'}), (d:Fach {name: 'Deutsch'})
CREATE (s3)-[:BELEGT]->(m), (s3)-[:BELEGT]->(d);

MATCH (s4:Schueler {vorname: 'Tim'}), (e:Fach {name: 'Englisch'}), (m:Fach {name: 'Mathematik'})
CREATE (s4)-[:BELEGT]->(e), (s4)-[:BELEGT]->(m);


// 5. Klausuren erfassen
// Lena schreibt Mathe-Klausur am 4.6.2025
MATCH (s:Schueler {vorname: 'Lena'}), (f:Fach {name: 'Mathematik'})
CREATE (s)-[:SCHREIBT_KLAUSUR {fach: 'Mathematik', datum: date('2025-06-04')}]->(f);

// Max schreibt Englisch-Klausur am 7.6.2025
MATCH (s:Schueler {vorname: 'Max'}), (f:Fach {name: 'Englisch'})
CREATE (s)-[:SCHREIBT_KLAUSUR {fach: 'Englisch', datum: date('2025-06-07')}]->(f);

// Optional: Alle erstellten Knoten und Beziehungen anzeigen zur Kontrolle
MATCH (n)-[r]->(m) RETURN n, r, m;
MATCH (n) WHERE NOT (n)-[]-() RETURN n; // Zeigt Knoten ohne Beziehungen (hier die Fächer, wenn noch kein Schüler sie belegt)
```

4) Ermitteln Sie mit jeweils einer Abfrage  

* alle Schüler, die Klausuren schreiben.

`MATCH (s:Schueler)-[:SCHREIBT_KLAUSUR]->(:Fach)
RETURN DISTINCT s.vorname, s.nachname`

* alle Schüler, die das Fach Englisch belegt haben.  

`MATCH (s:Schueler)-[:BELEGT]->(f:Fach {name: 'Englisch'})
RETURN s.vorname, s.nachname`

* alle Schüler, die zwischen 16 und 18 Jahren alt sind. 

`MATCH (s:Schueler)
WHERE s.alter >= 16 AND s.alter <= 18
RETURN s.vorname, s.nachname, s.alter`

## Aufgabe 8 - verteilte Datenverarbeitung

![alt text](image-1.png)
Quelle: <https://www.informatica.com/blogs/adopt-a-kappa-architecture-for-streaming-and-ingesting-data.html>

1) Beschreiben Sie die Aufgaben des Streaming Layers in der Kappa-Architektur anhand der obigen Grafik.

* Erfassung, Verarbeitung und Speicherung von Live-Streaming-Daten in großer Menge
* wird in der Regel mit einer Stream-Processing-Engine wie Apache Flink, Apache Storm, Apache Kinesis, Apache Kafka implementiert 
* zuverlässiger Zugriff auf Abfrageergebnisse.
Die Speed Layer in der Kappa-Architektur ist in zwei Hauptkomponenten unterteilt: die Ingestion Component und die Processing Component; hier nur die Processing Component

2) Inwieweit unterscheidet sich die Kappa-Architektur von der Lambda-Architektur?

Lambda enthält außerdem einen klassischen Verarbeitungsstream (Data at Rest) analog zu klass. BI-Lösung

3) Die Firma Siddhi vertreibt ein System, das in folgender Abbildung architektonisch sehr abstrakt dargestellt ist.  

![alt text](image-2.png)

Beschreiben Sie anhand der Vorlesung, um welche Art von System es sich hier handeln könnte.  

Spark-System, links Quellen, Auswertung mit SQL, Lieferung an Datensenken (Sinks)

## Aufgabe 9 - Apache Hadoop

./.

## Aufgabe 10 - Datenintegration

1) Beschreiben Sie, inwieweit Distribution, Autonomie und Heterogenität Herausforderungen für die Integration von separat vorliegenden Datenbeständen stellen können.  

* **Distribution** bezieht sich darauf, dass Daten nicht zentral an einem Ort liegen, sondern physisch (auf separaten Systemen) oder logisch (ein Datensatz auf mehreren Systemen verteilt) über ein Netzwerk verteilt sind.  
  * **Netzwerkebene und Adressierbarkeit**:  physisch separate Netzwerkknoten müssen identifizierbar und ansprechbar sein müssen (z.B. über TCP/IP). Ansonsten keine Verbindung zu verteilten Datenquellen hergestellt werden.
  * **Schemaverteilung und Abfragesprachen**: Daten sind oft in unterschiedlichen Schemata auf den Netzwerkknoten verteilt --> mehrere Query Languages für das Retrieval oder eine einzige, die mehrere Schemata beherrschen kann.  
  * **Abfrageoptimierung**: muss u.a. die Netzwerklast berücksichtigen, da das Verschieben von Daten über das Netzwerk erhebliche Latenz verursachen kann.
  * **Logische Verteilungsprobleme**: überlappende Daten können mit demselben Inhalt/Bedeutung existieren, was zu Redundanzen führt. 

* **Autonomie** bedeutet, dass die einzelnen Datenquellen (z.B. von verschiedenen Teams) selbstständig über ihre Datenstrukturen und den Zugriff darauf entscheiden. Dies führt zu inhärenten Integrationsschwierigkeiten.
  * Arten der Autonomie: Design, Interface, Access, Rechtliche Autonomie

* **Heterogenität** entsteht oft aus der Autonomie und beschreibt die Vielfalt / Unterschiedlichkeit der Datenbestände.
  * **Technische Heterogenität**: Probleme bei der technischen Umsetzung von Zugängen zu verschiedenen Systemen (z.B. unterschiedliche APIs, Treiber).
  * **Syntaktische Heterogenität**: Dieselben Fakten werden unterschiedlich repräsentiert. Beispiele:
Dezimalzeichen (Punkt/Komma), Währungssymbole (€/Euro)
Trennzeichen (Comma-separated/Tab-separated)
Zeichensätze (EBCDIC/ASCII/Unicode)
Notendarstellung (A-F, "sehr gut", "gut")
Diverse Datumsformate (12. September 2016; Sept 12, 2016; 16092016)
Binary coding vs. characters
  * **Data Model Heterogenität / Strukturelle Heterogenität**: Schemata, die dasselbe Objekt beschreiben, sind unterschiedlich aufgebaut.
  * **Semantische Heterogenität**: Hier liegen die größten Herausforderungen. Elemente in verschiedenen Schemata mögen den gleichen Namen tragen, aber unterschiedliche Bedeutungen haben (Homonyme), oder unterschiedliche Namen dieselbe Bedeutung (Synonyme). Die Bedeutung eines Tabellen- oder Attributnamens kann variieren.


2) Nennen Sie Integrationsprobleme auf der technischen Ebene, denen Sie z.B. während der Integrationsaufgabe im Kurs begegnen mussten.  

Falsche Lokalisierung / Collation
Falsche Feldlängen
Unterschiedliche Benennungen (Heteronyme)

3) Geben Sie ein Beispiel für Schema-Heterogenität.  


* Marketing-Abteilung pflegt eine Datenbank für ihre E-Mail-Kampagnen und Kundenbindungsprogramme.
* Vertriebs-Abteilung nutzt ein eigenes CRM-System (Customer Relationship Management) zur Verwaltung von Verkaufsaktivitäten und Kundenaufträgen.

Marketing-Datenbank (vereinfacht):


| Feldname	 | Datentyp	| Beschreibung |
|--|--|--|
|KundenID	| INT	| Eindeutige ID des Marketing-Kunden|
|EMail	|VARCHAR(255)|E-Mail-Adresse für Kampagnen|
|Vorname	|VARCHAR(100)	|Vorname des Kunden|
|Nachname	|VARCHAR(100)	|Nachname des Kunden|
|PLZ	|VARCHAR(10)	|Postleitzahl des Kunden für regionale Angebote|
|Registrierungsdatum	|DATE	|Datum der ersten Registrierung|
|OptInNewsletter	|BOOLEAN	|Hat der Kunde dem Newsletter zugestimmt?|

Vertriebs-Datenbank (vereinfachte):

| Feldname	 | Datentyp	| Beschreibung |
|--|--|--|
|CustomerID	|UUID	|Globale eindeutige ID des Kunden|
|FirstName	|VARCHAR(100)	|Vorname|
|LastName	|VARCHAR(100)	|Nachname|
|Straße	|VARCHAR(200)	|Straße der Rechnungsadresse|
|Hausnummer	|VARCHAR(10)	|Hausnummer der Rechnungsadresse|
|Ort	|VARCHAR(100)	|Ort der Rechnungsadresse|
|PLZ	|VARCHAR(10)	|Postleitzahl der Rechnungsadresse|
|LandCode	|CHAR(2)	|ISO-Ländercode (z.B. DE, US)|
|LetzterBestellwert	|DECIMAL(10,2)	|Summe des letzten getätigten Auftrags|
