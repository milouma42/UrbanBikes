import pandas as pd
import pm4py
import os

print("--- 1. Lade Daten... ---")
# Wir suchen den Ordner "data", der direkt NEBEN dieser Datei liegt
erp_path = os.path.join("data", "urbanbikes_erp_log.csv")
lager_path = os.path.join("data", "urbanbikes_lager_log.csv")

# Einlesen
df_erp = pd.read_csv(erp_path)
df_lager = pd.read_csv(lager_path)

# Datum formatieren
df_erp['Timestamp'] = pd.to_datetime(df_erp['Timestamp'])
df_lager['Timestamp'] = pd.to_datetime(df_lager['Timestamp'])

print("--- 2. Verbinde ERP und Lager... ---")
# Zusammenfügen
df_total = pd.concat([df_erp, df_lager], ignore_index=True)
df_total = df_total.sort_values(by=['Bestellnummer', 'Timestamp'])

print(f"Analyse bereit! {len(df_total)} Schritte gefunden.")

print("--- 3. Generiere Prozess-Diagramm... ---")
# Formatieren für Process Mining
event_log = pm4py.format_dataframe(df_total, case_id='Bestellnummer', activity_key='Aktivitaet', timestamp_key='Timestamp')

# Prozessmodell berechnen (BPMN)
process_model = pm4py.discover_bpmn_inductive(event_log)

print("--- 4. Öffne Grafik... (Ein neues Fenster sollte aufgehen) ---")
pm4py.view_bpmn(process_model)