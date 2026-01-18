import pandas as pd
import sqlite3
import os

print("--- Start: Daten in SQL-Datenbank speichern ---")

# 1. Wir laden unsere sauberen, zusammengefügten Daten (aus dem Merging-Schritt)
erp_path = os.path.join("data", "urbanbikes_erp_log.csv")
lager_path = os.path.join("data", "urbanbikes_lager_log.csv")

df_erp = pd.read_csv(erp_path)
df_lager = pd.read_csv(lager_path)

# Zusammenfügen (gleiche Logik wie vorher)
df_total = pd.concat([df_erp, df_lager], ignore_index=True)
df_total['Timestamp'] = pd.to_datetime(df_total['Timestamp'])
df_total = df_total.sort_values(by=['Bestellnummer', 'Timestamp'])

print(f"Daten geladen: {len(df_total)} Zeilen.")

# 2. Verbindung zur SQL-Datenbank herstellen
# Das erstellt automatisch eine Datei 'urbanbikes.db'
connection = sqlite3.connect("urbanbikes.db")
cursor = connection.cursor()

# 3. Daten schreiben (Pandas macht das automatisch für uns!)
# Wir nennen die Tabelle "process_logs"
print("Schreibe Daten in Tabelle 'process_logs'...")
df_total.to_sql('process_logs', connection, if_exists='replace', index=False)

# 4. BEWEIS: Wir machen eine SQL-Abfrage, um zu zeigen, dass es geklappt hat
print("\n--- SQL-Abfrage Test: Zeige die ersten 3 Einträge ---")
query = "SELECT * FROM process_logs LIMIT 3"
ergebnis = pd.read_sql_query(query, connection)

print(ergebnis)

connection.close()
print("\nERFOLG: Datenbank 'urbanbikes.db' wurde erstellt und gefüllt.")