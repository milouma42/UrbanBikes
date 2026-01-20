UrbanBikes Prozessanalyse


Willkommen in meinem Projekt zur Analyse und Optimierung des Bestellprozesses der UrbanBikes GmbH.
Hier findet man das komplette Repositority. 

Projektziel

Das Ziel war es herauszufinden, weshalb die Bearbeitung von eingehenden Bestellungen bei UrbanBikes zu lange dauern ("Order-to-Ship-Time"). 
Dafür wurden Log-Daten aus dem ERP- und Lagersystem mittels Python und Process Mining analysiert, Engpässe identifiziert und eine SQL-Datenbank aufgebaut.

Technologien

Folgende Tools und Bibliotheken wurden verwendet:

Python 3.13 (Hauptsprache)

Pandas (Datenaufbereitung / ETL)

PM4Py (Process Mining Visualisierung)

SQLite (Datenbank-Speicherung)

Tableau Public (Dashboard & Visualisierung)

Git & GitHub (Versionsverwaltung)
____________________________________________________________________________

Projektstruktur (Was ist wo?):

analyse_prozess.py - Das Hauptskript: Liest Daten ein, führt sie zusammen und zeigt den Prozess-Graphen.

analyse_kpis.py - Berechnet die Durchlaufzeiten für das Tableau-Dashboard.

database_final.py - Erzeugt die SQL-Datenbank (urbanbikes.db) und speichert die bereinigten Daten.

soll_prozess.py - Generiert den optimierten "Soll-Prozess" (Happy Path) als Grafik.

urbanbikes.db - Die fertige SQLite-Datenbank mit den Prozess-Logs.

ergebnis_engpaesse.csv - Die Datenbasis für das Tableau-Dashboard.

Installation & Ausführung
Um das Projekt lokal auf einem Rechner zu starten:

Repository klonen:

Bash
git clone https://github.com/milouma42/UrbanBikes.git
cd UrbanBikes


Abhängigkeiten installieren: 

Python und folgende Pakete müssen installiert sein:

Bash
pip install pandas pm4py matplotlib seaborn
Skripte ausführen:

Um die Datenbank zu erstellen: python database_final.py

Um den Prozess zu visualisieren: python analyse_prozess.py

Ergebnisse der Analyse

Die Analyse hat folgende Engpässe aufgedeckt:

Hauptproblem: Der Schritt Wareneingang im LVS dauert durchschnittlich > 24 Stunden

Lösungsvorschlag: Implementierung einer Echtzeit-API Schnittstelle statt Batch-Verarbeitung

Potenzial: Durch die Optimierung kann die Lieferzeit um 1 Werktag verkürzt werden

Autor
Michelle Louise Martin 
Fachinformatikerin für Daten- und Prozessanalyse
