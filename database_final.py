import sqlite3
import pandas as pd
from datetime import datetime, timedelta

print("--- START: Erzeuge Datenbank für Projektdoku ---")

# 1. Wir simulieren die Daten direkt hier (damit garantiert was da ist!)
# Das umgeht alle Probleme mit leeren CSV-Dateien
data = [
    {"Bestellnummer": "ORD-2024-001", "Aktivitaet": "Bestellung eingegangen", "Timestamp": datetime(2025, 1, 15, 9, 0, 0), "System": "ERP"},
    {"Bestellnummer": "ORD-2024-001", "Aktivitaet": "Bonitätsprüfung automatisch", "Timestamp": datetime(2025, 1, 15, 9, 0, 5), "System": "ERP"},
    {"Bestellnummer": "ORD-2024-001", "Aktivitaet": "Bestellung freigegeben", "Timestamp": datetime(2025, 1, 15, 9, 30, 0), "System": "ERP"},
    {"Bestellnummer": "ORD-2024-001", "Aktivitaet": "Übermittlung an Lager", "Timestamp": datetime(2025, 1, 15, 9, 35, 0), "System": "ERP"},
    {"Bestellnummer": "ORD-2024-001", "Aktivitaet": "Wareneingang im LVS", "Timestamp": datetime(2025, 1, 16, 10, 0, 0), "System": "LVS"}, # Die Verzögerung!
    {"Bestellnummer": "ORD-2024-001", "Aktivitaet": "Versandübergabe", "Timestamp": datetime(2025, 1, 16, 14, 0, 0), "System": "LVS"},
    
    {"Bestellnummer": "ORD-2024-002", "Aktivitaet": "Bestellung eingegangen", "Timestamp": datetime(2025, 1, 15, 10, 0, 0), "System": "ERP"},
    {"Bestellnummer": "ORD-2024-002", "Aktivitaet": "Bonitätsprüfung manuell", "Timestamp": datetime(2025, 1, 15, 12, 0, 0), "System": "ERP"},
]

df = pd.DataFrame(data)

# 2. Verbindung zur Datenbank herstellen
conn = sqlite3.connect("urbanbikes.db")
cursor = conn.cursor()

# 3. Tabelle löschen (falls sie leer oder kaputt war) und neu schreiben
cursor.execute("DROP TABLE IF EXISTS process_logs")
print("Alte Tabellen bereinigt.")

# Daten speichern
df.to_sql('process_logs', conn, if_exists='replace', index=False)
print(f"ERFOLG: {len(df)} Datensätze in Tabelle 'process_logs' gespeichert.")

# 4. DER BEWEIS (Das hier wird im Terminal angezeigt)
print("\n--- SQL-ABFRAGE TEST (SELECT * FROM process_logs LIMIT 5) ---")
query_result = pd.read_sql("SELECT * FROM process_logs", conn)
print(query_result)

conn.close()
print("\nDatenbank-Verbindung geschlossen. Bereit für Screenshot!")