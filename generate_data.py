import pandas as pd
import random
from datetime import datetime, timedelta

# Konfiguration
ANZAHL_BESTELLUNGEN = 500
START_DATUM = datetime(2025, 9, 1)

data_erp = []
data_lager = []

print("Generiere Daten... Bitte warten.")

for i in range(1, ANZAHL_BESTELLUNGEN + 1):
    # Generiere eine eindeutige Bestellnummer (Case ID)
    bestell_nr = f"ORD-{10000+i}"
    
    # Zufälliger Startzeitpunkt der Bestellung (innerhalb von 60 Tagen)
    zeitpunkt = START_DATUM + timedelta(days=random.randint(0, 60), hours=random.randint(8, 18), minutes=random.randint(0, 59))
    
    # --- ERP SYSTEM PROZESSE ---
    
    # 1. Bestellung geht ein
    data_erp.append({
        "Bestellnummer": bestell_nr,
        "Aktivitaet": "Bestellung eingegangen",
        "Timestamp": zeitpunkt,
        "User": "System"
    })
    
    # 2. Bonitätsprüfung (dauert 1-10 Minuten)
    zeitpunkt += timedelta(minutes=random.randint(1, 10))
    data_erp.append({
        "Bestellnummer": bestell_nr,
        "Aktivitaet": "Bonitätsprüfung automatisch",
        "Timestamp": zeitpunkt,
        "User": "System"
    })
    
    # PROZESS-ABWEICHUNG: "Unnötige Schleife" [cite: 6]
    # Bei 15% der Fälle schlägt die Automatik fehl -> Manuelle Prüfung nötig
    if random.random() < 0.15:
        zeitpunkt += timedelta(hours=random.randint(2, 24)) # Liegezeit!
        data_erp.append({
            "Bestellnummer": bestell_nr,
            "Aktivitaet": "Bonitätsprüfung manuell",
            "Timestamp": zeitpunkt,
            "User": "Mitarbeiter_FiBu"
        })
        # Schleife zurück zur Freigabe
        zeitpunkt += timedelta(minutes=random.randint(10, 30))
        data_erp.append({
            "Bestellnummer": bestell_nr,
            "Aktivitaet": "Bestellung freigegeben",
            "Timestamp": zeitpunkt,
            "User": "Mitarbeiter_FiBu"
        })
    
    # 3. Daten an Lager senden
    zeitpunkt += timedelta(minutes=random.randint(5, 60))
    # Dieser Schritt taucht oft in beiden Systemen auf (Schnittstelle)
    data_erp.append({
        "Bestellnummer": bestell_nr,
        "Aktivitaet": "Übermittlung an Lager",
        "Timestamp": zeitpunkt,
        "User": "System Interface"
    })
    
    # --- LAGER SYSTEM PROZESSE (Ab hier neuer DataFrame) ---
    
    # Synchronisationszeit (simuliert)
    lager_zeitpunkt = zeitpunkt + timedelta(seconds=random.randint(10, 120))
    
    data_lager.append({
        "Bestellnummer": bestell_nr,
        "Aktivitaet": "Wareneingang im LVS",
        "Timestamp": lager_zeitpunkt,
        "Station": "Server"
    })
    
    # 4. Kommissionierung
    # ENGPASS SIMULATION[cite: 6]: Dauert hier viel zu lange (2-48 Stunden Liegezeit)
    lager_zeitpunkt += timedelta(hours=random.randint(2, 48)) 
    
    data_lager.append({
        "Bestellnummer": bestell_nr,
        "Aktivitaet": "Kommissionierung gestartet",
        "Timestamp": lager_zeitpunkt,
        "Station": "Lagerhalle A"
    })
    
    lager_zeitpunkt += timedelta(minutes=random.randint(15, 45))
    data_lager.append({
        "Bestellnummer": bestell_nr,
        "Aktivitaet": "Kommissionierung beendet",
        "Timestamp": lager_zeitpunkt,
        "Station": "Lagerhalle A"
    })
    
    # 5. Verpacken
    lager_zeitpunkt += timedelta(minutes=random.randint(10, 120))
    data_lager.append({
        "Bestellnummer": bestell_nr,
        "Aktivitaet": "Verpacken und Labeldruck",
        "Timestamp": lager_zeitpunkt,
        "Station": "Packtisch 3"
    })
    
    # 6. Versand
    lager_zeitpunkt += timedelta(hours=random.randint(1, 4))
    data_lager.append({
        "Bestellnummer": bestell_nr,
        "Aktivitaet": "Versandübergabe",
        "Timestamp": lager_zeitpunkt,
        "Station": "Rampe 1"
    })

# DataFrames erstellen
df_erp = pd.DataFrame(data_erp)
df_lager = pd.DataFrame(data_lager)

# CSVs speichern (ohne Index, damit es sauber aussieht)
df_erp.to_csv("urbanbikes_erp_log.csv", index=False)
df_lager.to_csv("urbanbikes_lager_log.csv", index=False)

print(f"Fertig! Es wurden {len(df_erp)} ERP-Zeilen und {len(df_lager)} Lager-Zeilen generiert.")
print("Dateien 'urbanbikes_erp_log.csv' und 'urbanbikes_lager_log.csv' wurden erstellt.")