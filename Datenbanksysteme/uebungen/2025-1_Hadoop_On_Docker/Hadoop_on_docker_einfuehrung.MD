# Einführung

Das Ziel dieses Tutorials ist es, ein Hadoop-System auf Basis von Docker aufzusetzen.
[Docker](https://www.docker.com/) wird genutzt, um Installationen auf dem lokalen Rechner weitgehend zu vermeiden.  
Anhand von Hadoop, das zwar eine ältere Technologie ist als Spark, soll demonstriert werden, wie verteilte Knoten gemeinsam Jobs abarbeiten können.  

## Vorteile 

Vorteile von Docker für Hadoop- und Spark-Entwicklung

* Isolierung und Reproduzierbarkeit: Docker-Container kapseln Anwendungen und deren Abhängigkeiten vollständig. Die erstellten Umgebungen sind konsistent.  
* Portabilität: erstellte Docker-Images können problemlos auf verschiedenen Systemen bereitgestellt werden (Entwicklerlaptops, Testservern, Cloud). Entwickler können schnell Umgebungen teilen und hochfahren können, die für Hadoop und Spark konfiguriert sind.
* Ressourceneffizienz: Container sind im Vgl. zu VMs wesentlich leichtgewichtiger. Sie teilen sich den Kernel des Host-Betriebssystems, was weniger Overhead bedeutet. Das schnelle Starten und Stoppen von Containern ermöglicht eine agile Entwicklung und das schnelle Testen von Änderungen an Hadoop-Algorithmen.
* Vereinfachtes Setup und Management: 
  * Komplexe Umgebungen wie ein Hadoop-Cluster oder eine Spark-Installation können in Docker-Images vorab konfiguriert werden. 
  * Mit docker-compose können Multi-Container-Anwendungen definiert und gestartet werden, was das Aufsetzen von beispielsweise einem Hadoop-Master und mehreren Worker-Nodes erheblich vereinfacht. Reduziert den administrativen Aufwand beim Einrichten und Verwalten von Entwicklungsumgebungen.
* Versionierung und Rollback:
  * Docker-Images können versioniert werden, was es ermöglicht, auf frühere stabile Konfigurationen zurückzugreifen, falls ein Problem auftritt.
  * Ermöglicht das Experimentieren mit verschiedenen Versionen von Hadoop, Spark oder Bibliotheken, ohne das Basissystem zu beeinträchtigen.
* Skalierbarkeit (für Demos/lokale Entwicklung): Für Demonstrationszwecke oder lokale Entwicklung können Sie schnell mehrere Spark-Worker-Container starten, um ein kleines verteiltes Szenario zu simulieren.

## Nachteile  

Nachteile von Docker für Hadoop- und Spark-Entwicklung
Overhead in Produktion (bei großen Clustern):

* Für große, produktive Hadoop- oder Spark-Cluster kann der zusätzliche Abstraktionslayer von Docker einen geringen Performance-Overhead mit sich bringen. Produktionsumgebungen nutzen oft dedizierte Cluster-Manager wie YARN oder Kubernetes direkt.
* Die Orchestrierung großer Docker-Cluster erfordert Tools wie Kubernetes, die selbst eine Lernkurve haben.
* Komplexität für Anfänger:Das Konzept von Containern, Images, Dockerfiles und Docker Compose kann für Entwickler, die noch nie damit gearbeitet haben, eine gewisse Einarbeitungszeit erfordern.
Fehler in Dockerfiles können zu schwer zu debuggenden Problemen führen.
* Debugging innerhalb von Containern: Das Debuggen von Anwendungen, die in Containern laufen, kann manchmal komplexer sein als das Debuggen auf dem Hostsystem, da man möglicherweise zusätzliche Schritte unternehmen muss, um sich an den Container anzuhängen oder Logs zu sammeln.

* Persistent Storage Management: Hadoop und Spark arbeiten oft mit großen Datenmengen, die persistent gespeichert werden müssen. Das Management von persistentem Speicher mit Docker-Volumes kann (insbesondere in komplexeren Szenarien) eine Herausforderung sein.
Die Leistung von Volumes kann je nach Implementierung variieren.
Netzwerk-Konfiguration:

* Die Netzwerk-Konfiguration für komplexe verteilte Systeme wie Hadoop und Spark innerhalb von Docker-Containern kann anspruchsvoll sein, insbesondere wenn Sie benutzerdefinierte Netzwerke oder Host-Port-Mappings benötigen.
Kein Ersatz für echte Cluster-Erfahrung:

## Literatur und Links

Ein Tutorial zum **Aufsetzen von Hadoop auf Docker** von _Sanny Garin Jr_ (19.11.2024):

* [Deploying Hadoop using Docker](https://medium.com/@garin.sanny07/hadoop-cluster-55477505d0ff)
* Im Tutorial wird folgendes Projekt verwendet: `git clone https://github.com/ibm-developer-skills-network/ooxwv-docker_hadoop.git`

Ein kurzer Überblick, wie ein **MapReduce-Job auf Hadoop/Docker** implementiert und ausgeführt werden kann von _Guillermo Velazquez_ (10.02.2022):

* [Setting up Hadoop with Docker and using MapReduce framework](https://medium.com/@guillermovc/setting-up-hadoop-with-docker-and-using-mapreduce-framework-c1cd125d4f7b)
