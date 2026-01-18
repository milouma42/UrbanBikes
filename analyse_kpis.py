import pandas as pd
import os

print("--- KPI Analyse für Tableau ---")
erp_path = os.path.join("data", "urbanbikes_erp_log.csv")
lager_path = os.path.join("data", "urbanbikes_lager_log.csv")

df_erp = pd.read_csv(erp_path)
df_lager = pd.read_csv(lager_path)

df_erp['Timestamp'] = pd.to_datetime(df_erp['Timestamp'])
df_lager['Timestamp'] = pd.to_datetime(df_lager['Timestamp'])

df = pd.concat([df_erp, df_lager], ignore_index=True)
df = df.sort_values(by=['Bestellnummer', 'Timestamp'])

# Dauer berechnen
df['Nächster_Timestamp'] = df.groupby('Bestellnummer')['Timestamp'].shift(-1)
df['Dauer_Objekt'] = df['Nächster_Timestamp'] - df['Timestamp']

# Gruppieren
engpaesse = df.groupby('Aktivitaet')['Dauer_Objekt'].mean().reset_index()

# TRICK FÜR TABLEAU: Wir rechnen die Zeit in Stunden um (als Zahl!)
engpaesse['Dauer_in_Stunden'] = engpaesse['Dauer_Objekt'].dt.total_seconds() / 3600

# Speichern
engpaesse.to_csv("ergebnis_engpaesse.csv", index=False)
print("Datei aktualisiert! Jetzt hast du eine Zahlen-Spalte für Tableau.")