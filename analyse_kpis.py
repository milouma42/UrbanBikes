import pandas as pd
import os

print("--- 1. Lade und bereite Daten vor... ---")
# Pfade (genau wie vorher)
erp_path = os.path.join("data", "urbanbikes_erp_log.csv")
lager_path = os.path.join("data", "urbanbikes_lager_log.csv")

# Laden
df_erp = pd.read_csv(erp_path)
df_lager = pd.read_csv(lager_path)

# Zeitstempel reparieren
df_erp['Timestamp'] = pd.to_datetime(df_erp['Timestamp'])
df_lager['Timestamp'] = pd.to_datetime(df_lager['Timestamp'])

# Zusammenfügen
df = pd.concat([df_erp, df_lager], ignore_index=True)
df = df.sort_values(by=['Bestellnummer', 'Timestamp'])

print(f"Daten geladen: {len(df)} Events.")

print("\n--- 2. Berechne Durchlaufzeiten (Order-to-Ship) ---")
# Wir gruppieren nach Bestellung und nehmen Min-Zeit (Start) und Max-Zeit (Ende)
case_times = df.groupby('Bestellnummer')['Timestamp'].agg(['min', 'max'])
case_times['Dauer'] = case_times['max'] - case_times['min']

# Durchschnitt berechnen
durchschnitt = case_times['Dauer'].mean()
print(f"DURCHSCHNITTLICHE DURCHLAUFZEIT: {durchschnitt}")
print(f"Schnellste Bestellung: {case_times['Dauer'].min()}")
print(f"Langsamste Bestellung: {case_times['Dauer'].max()}")

print("\n--- 3. Wo sind die Engpässe? (Dauer zwischen Schritten) ---")
# Wir berechnen die Zeit zwischen zwei aufeinanderfolgenden Schritten
df['Nächster_Timestamp'] = df.groupby('Bestellnummer')['Timestamp'].shift(-1)
df['Dauer_bis_nächster_Schritt'] = df['Nächster_Timestamp'] - df['Timestamp']

# Wir schauen uns an, nach welcher Aktivität es am längsten dauert (im Schnitt)
engpaesse = df.groupby('Aktivitaet')['Dauer_bis_nächster_Schritt'].mean().sort_values(ascending=False)

print("TOP 3 ZEITFRESSER (Hier warten die Bestellungen am längsten):")
print(engpaesse.head(3))

print("\n--- 4. Speichere Ergebnisse für Excel/Dashboard ---")
# Wir speichern diese KPI-Tabelle, damit du sie in Power BI oder Excel laden kannst
engpaesse.to_csv("ergebnis_engpaesse.csv")
print("Datei 'ergebnis_engpaesse.csv' wurde gespeichert!")