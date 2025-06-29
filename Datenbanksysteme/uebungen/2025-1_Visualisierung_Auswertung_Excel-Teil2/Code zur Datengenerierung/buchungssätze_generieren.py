# Importieren der notwendigen Bibliotheken
import csv
import random
from datetime import date, timedelta

# --- Konfiguration ---
# Name der Ausgabedatei für die Buchungssätze wird dynamisch gesetzt
output_csv_filename = ""

# --- Definition von GuV-Konten (vereinfacht) ---
# Ertragskonten (Haben-Seite)
ertrags_konten = {
    8100: "Erlöse aus Warenverkauf",
    8200: "Erlöse aus Dienstleistungen",
    8300: "Sonstige betriebliche Erträge"
}

# Aufwandskonten (Soll-Seite)
aufwands_konten = {
    4000: "Wareneinsatz",
    4100: "Löhne und Gehälter",
    4200: "Sozialabgaben",
    4300: "Miete",
    4400: "Büromaterial",
    4500: "Reisekosten",
    4600: "Abschreibungen",
    4700: "Sonstige betriebliche Aufwendungen"
}

# Bankkonten (typischerweise Gegenkonto)
bank_konten = [1200] # Beispiel: Bank (Aktivkonto, Haben für Erträge, Soll für Aufwände)

# --- Funktionen zur Buchungssatzgenerierung ---

def generate_random_date(start_year, end_year):
    """Generiert ein zufälliges Datum innerhalb eines Jahresbereichs."""
    start_date = date(start_year, 1, 1)
    end_date = date(end_year, 12, 31)
    
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date

def generate_buchungssatz(mandanten_nr, current_year):
    """Generiert einen einzelnen, plausiblen Buchungssatz für die GuV."""
    
    datum = generate_random_date(current_year, current_year)
    betrag = round(random.uniform(50.00, 5000.00), 2) # Beträge zwischen 50 und 5000

    konto_soll = ""
    konto_haben = ""
    art_der_buchung = "" # Art der Buchung
    buchungstext = ""    # Detaillierter Buchungstext

    # Zufällig entscheiden, ob es ein Ertrags- oder Aufwandsbuchungssatz ist
    if random.random() < 0.5: # 50% Chance für Ertrag
        # Ertragsbuchungssatz: Bank an Ertragskonto
        konto_soll = random.choice(bank_konten) # Z.B. 1200 Bank
        konto_haben = random.choice(list(ertrags_konten.keys()))
        art_der_buchung = "Ertrag"
        
        # Spezifischere Buchungstexte für Erträge
        if konto_haben == 8100:
            buchungstext = random.choice([
                f"Verkauf von Waren (Rechnungsnr. {random.randint(10000, 99999)})",
                f"Erlös aus Produkt X (Kunde {random.randint(100, 999)})",
                f"Warenlieferung an Firma ABC"
            ])
        elif konto_haben == 8200:
            buchungstext = random.choice([
                f"Dienstleistungsgebühren (Projekt {chr(random.randint(65, 90))}{random.randint(10, 99)})",
                f"Beratungsleistung für Kunde DEF",
                f"Softwareentwicklung (Phase {random.randint(1, 3)})"
            ])
        elif konto_haben == 8300:
            buchungstext = random.choice([
                f"Zinsertrag aus Festgeldkonto",
                f"Erlös aus dem Verkauf von Altmaterialien",
                f"Mieteinahmen Nebengebäude"
            ])
    else:
        # Aufwandsbuchungssatz: Aufwandskonto an Bank
        konto_soll = random.choice(list(aufwands_konten.keys()))
        konto_haben = random.choice(bank_konten) # Z.B. 1200 Bank
        art_der_buchung = "Aufwand"
        
        # Spezifischere Buchungstexte für Aufwände
        if konto_soll == 4000:
            buchungstext = random.choice([
                f"Einkauf Rohmaterial für Produktion",
                f"Warenbezug für Verkauf (Lieferant Y)",
                f"Kosten für Handelswaren"
            ])
        elif konto_soll == 4100:
            buchungstext = f"Gehaltszahlung an Mitarbeiter für {datum.strftime('%B %Y')}"
        elif konto_soll == 4200:
            buchungstext = f"Abführung Sozialabgaben und Lohnsteuer für {datum.strftime('%B %Y')}"
        elif konto_soll == 4300:
            buchungstext = f"Mietzahlung für Büroräume, Fälligkeit {datum.strftime('%d.%m.%Y')}"
        elif konto_soll == 4400:
            buchungstext = random.choice([
                f"Kauf Briefmarken und Umschläge",
                f"Beschaffung Büromaterial (Stifte, Papier)",
                f"Kosten für Druckerpatronen"
            ])
        elif konto_soll == 4500:
            buchungstext = random.choice([
                f"Reisekostenabrechnung (Bahnfahrt Kunde GHI)",
                f"Hotelkosten für Geschäftsreise",
                f"Fahrtkostenpauschale Mitarbeiter"
            ])
        elif konto_soll == 4600:
            buchungstext = f"Planmäßige Abschreibung auf Anlagevermögen ({random.choice(['PKW', 'Maschine', 'Büromöbel'])})"
        elif konto_soll == 4700:
            buchungstext = random.choice([
                f"Werbekosten für Online-Kampagne",
                f"Telefon- und Internetkosten {datum.strftime('%B')}",
                f"Reparatur Bürostuhl"
            ])


    return {
        "Datum": datum.strftime("%Y-%m-%d"),
        "Sollkonto": konto_soll,
        "Habenkonto": konto_haben,
        "Betrag": f"{betrag:.2f}".replace('.', ','), # Format als deutscher Währungswert
        "Art der Buchung": art_der_buchung,         # Art der Buchung
        "Buchungstext": buchungstext,               # Detaillierter Buchungstext
        "Mandantennummer": mandanten_nr
    }

# --- Hauptlogik ---
if __name__ == "__main__":
    print("Starte Generierung von GuV-Buchungssätzen...\n")

    num_entries_str = input("Wie viele Buchungssätze sollen generiert werden? ")
    try:
        num_entries_to_generate = int(num_entries_str)
        if num_entries_to_generate <= 0:
            print("Bitte geben Sie eine positive Zahl ein.")
            exit()
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")
        exit()

    mandanten_nr = input("Bitte geben Sie die Mandantennummer ein (z.B. M-0001): ")
    if not mandanten_nr:
        print("Mandantennummer darf nicht leer sein.")
        exit()

    # Dynamische Anpassung des Dateinamens
    output_csv_filename = f"buchungssaetze_guv_{mandanten_nr}.csv"

    # Öffne die Ausgabedatei zum Schreiben
    with open(output_csv_filename, 'w', newline='', encoding='utf-8') as outfile:
        csv_writer = csv.writer(outfile, delimiter=';') # Semikolon als Trennzeichen

        # Schreibe den Header in die Ausgabedatei
        csv_writer.writerow([
            "Datum", "Sollkonto", "Habenkonto", "Betrag", "Art der Buchung", "Buchungstext", "Mandantennummer"
        ])

        print(f"Generiere {num_entries_to_generate} Buchungssätze für Mandant {mandanten_nr}...\n")

        # Generiere Buchungssätze für 2024 und 2025
        for i in range(num_entries_to_generate):
            target_year = random.choice([2024, 2025]) # Zufällige Zuweisung zu 2024 oder 2025
            buchungssatz = generate_buchungssatz(mandanten_nr, target_year)
            
            csv_writer.writerow([
                buchungssatz["Datum"],
                buchungssatz["Sollkonto"],
                buchungssatz["Habenkonto"],
                buchungssatz["Betrag"],
                buchungssatz["Art der Buchung"],
                buchungssatz["Buchungstext"],
                buchungssatz["Mandantennummer"]
            ])
            print(f"Buchungssatz {i+1}/{num_entries_to_generate} generiert: {buchungssatz['Datum']}, Typ: {buchungssatz['Art der Buchung']}, Soll: {buchungssatz['Sollkonto']}, Haben: {buchungssatz['Habenkonto']}, Betrag: {buchungssatz['Betrag']}")

    print(f"\nGenerierung abgeschlossen. Buchungssätze wurden in '{output_csv_filename}' gespeichert.")
