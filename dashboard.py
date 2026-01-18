import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Daten laden (Die Engpass-Datei, die wir eben erstellt haben)
print("Lade Analysedaten...")
df_engpass = pd.read_csv("ergebnis_engpaesse.csv")

# Spalten umbenennen für schönere Grafik
df_engpass.columns = ['Aktivitaet', 'Dauer']

# Die Dauer ist aktuell noch ein komplexer Text (z.B. "0 days 02:34..."). 
# Wir müssen das in "Stunden" umrechnen, damit man es zeichnen kann.
def dauer_in_stunden(dauer_str):
    # Wir nutzen Pandas Timedelta zum Umrechnen
    return pd.to_timedelta(dauer_str).total_seconds() / 3600

df_engpass['Stunden'] = df_engpass['Dauer'].apply(dauer_in_stunden)

# Wir sortieren, damit der größte Balken oben ist
df_engpass = df_engpass.sort_values(by='Stunden', ascending=False).head(5) # Top 5

# 2. Grafik erstellen (Dashboard-Style)
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

# Balkendiagramm
chart = sns.barplot(x="Stunden", y="Aktivitaet", data=df_engpass, palette="viridis")

plt.title("Durchschnittliche Dauer pro Prozessschritt (Top 5)", fontsize=16)
plt.xlabel("Dauer in Stunden", fontsize=12)
plt.ylabel("Prozessschritt", fontsize=12)

# Werte an die Balken schreiben
for i in chart.containers:
    chart.bar_label(i, fmt='%.1f Std', padding=3)

# Layout straffen
plt.tight_layout()

# 3. Speichern und Anzeigen
plt.savefig("dashboard_engpass.png")
print("Grafik wurde als 'dashboard_engpass.png' gespeichert!")
plt.show()
