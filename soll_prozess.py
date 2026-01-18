import pandas as pd
import pm4py
from datetime import datetime, timedelta

print("--- Erstelle Soll-Prozess-Modell (Happy Path) ---")

# Wir simulieren EINE perfekte Bestellung
start_time = datetime(2026, 1, 20, 9, 0, 0)

data = [
    # ERP
    {"Bestellnummer": "SOLL-001", "Aktivitaet": "Bestellung eingegangen", "Timestamp": start_time},
    {"Bestellnummer": "SOLL-001", "Aktivitaet": "Bonitätsprüfung automatisch", "Timestamp": start_time + timedelta(seconds=2)},
    {"Bestellnummer": "SOLL-001", "Aktivitaet": "Bestellung freigegeben", "Timestamp": start_time + timedelta(seconds=5)},
    {"Bestellnummer": "SOLL-001", "Aktivitaet": "Übermittlung an Lager (Echtzeit)", "Timestamp": start_time + timedelta(seconds=10)},
    
    # LAGER
    {"Bestellnummer": "SOLL-001", "Aktivitaet": "Wareneingang im LVS", "Timestamp": start_time + timedelta(minutes=1)},
    {"Bestellnummer": "SOLL-001", "Aktivitaet": "Kommissionierung gestartet", "Timestamp": start_time + timedelta(minutes=5)},
    {"Bestellnummer": "SOLL-001", "Aktivitaet": "Kommissionierung beendet", "Timestamp": start_time + timedelta(minutes=15)},
    {"Bestellnummer": "SOLL-001", "Aktivitaet": "Verpacken und Labeldruck", "Timestamp": start_time + timedelta(minutes=20)},
    {"Bestellnummer": "SOLL-001", "Aktivitaet": "Versandübergabe", "Timestamp": start_time + timedelta(minutes=25)}
]

df_soll = pd.DataFrame(data)

# --- HIER WAR DER FEHLER: Wir formatieren es jetzt richtig ---
print("Formatiere Daten...")
df_soll = pm4py.format_dataframe(df_soll, case_id='Bestellnummer', activity_key='Aktivitaet', timestamp_key='Timestamp')

# Prozess visualisieren
print("Generiere Grafik...")
process_model = pm4py.discover_bpmn_inductive(df_soll)

print("Öffne Fenster mit dem Soll-Prozess...")
pm4py.view_bpmn(process_model)