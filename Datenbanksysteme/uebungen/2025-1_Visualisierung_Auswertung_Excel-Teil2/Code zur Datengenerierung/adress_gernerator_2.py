# Importieren der notwendigen Bibliotheken
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import time  # Für Verzögerungen zwischen den Anfragen, um Rate Limits zu vermeiden
import csv   # Für das Lesen und Schreiben in CSV-Dateien
import random # Für die Generierung plausibler Adressen

# --- Konfiguration ---
# Name der Ausgabedatei für die geprüften Adressen
output_csv_filename = "gepruefte_adressen.csv"

# Initialisierung des Geokodierungsdienstes
# Wichtig: Geben Sie einen User-Agent an, da dies von vielen Geokodierungsdiensten verlangt wird.
geolocator = Nominatim(user_agent="mein-adresspruefer-app")

# --- Funktionen zur Adressgenerierung ---

def generate_plausible_german_address():
    """
    Generiert eine einzelne, plausible deutsche Adresse aus einer Liste
    von bekannten Kombinationen, um die Wahrscheinlichkeit der Geokodierung zu erhöhen.
    """
    
    # Eine Liste von plausiblen deutschen Adresskombinationen
    # Jedes Tupel enthält (Straße, Hausnummer, Postleitzahl, Stadt)
    plausible_addresses = [
        ("Hauptstraße", "15", "10115", "Berlin"),
        ("Blumenweg", "7", "20095", "Hamburg"),
        ("Goethestraße", "22A", "80331", "München"),
        ("Am Stadtpark", "3", "50667", "Köln"),
        ("Schillerplatz", "10", "70173", "Stuttgart"),
        ("Lindenallee", "45", "60311", "Frankfurt am Main"),
        ("Kirchgasse", "8", "04109", "Leipzig"),
        ("Bachstraße", "12", "40213", "Düsseldorf"),
        ("Waldweg", "20", "30159", "Hannover"),
        ("Brunnenstraße", "33", "90403", "Nürnberg"),
        ("Friedrichstraße", "98", "10117", "Berlin"),
        ("Mittelweg", "42", "20148", "Hamburg"),
        ("Leopoldstraße", "123", "80802", "München"),
        ("Hohe Straße", "15", "50667", "Köln"),
        ("Königstraße", "30", "70173", "Stuttgart"),
        ("Zeil", "65", "60313", "Frankfurt am Main"),
        ("Nikolaikirchhof", "3", "04109", "Leipzig"),
        ("Immermannstraße", "23", "40210", "Düsseldorf"),
        ("Georgsplatz", "10", "30159", "Hannover"),
        ("Königstraße", "55", "90402", "Nürnberg"),
        ("Breite Straße", "8", "23552", "Lübeck"),
        ("Ostwall", "33", "44135", "Dortmund"),
        ("Willy-Brandt-Platz", "5", "45127", "Essen"),
        ("Waller Heerstraße", "105", "28217", "Bremen"),
        ("Augustinergasse", "7", "97070", "Würzburg"),
        ("An der Alster", "28", "20099", "Hamburg"),
        ("Prager Straße", "10", "01069", "Dresden"),
        ("Kaiserstraße", "68", "76133", "Karlsruhe"),
        ("Bahnhofstraße", "12", "66111", "Saarbrücken"),
        ("Poststraße", "5", "93047", "Regensburg"),
        ("Rathausplatz", "1", "47051", "Duisburg"),
        ("Bismarckstraße", "70", "52066", "Aachen"),
        ("Hafenstraße", "20", "48153", "Münster"),
        ("Marktplatz", "9", "69117", "Heidelberg"),
        ("Ludwigsplatz", "4", "67059", "Ludwigshafen am Rhein"),
        ("Lange Straße", "40", "78050", "Villingen-Schwenningen"),
        ("Steinstraße", "18", "06108", "Halle (Saale)"),
        ("Domstraße", "10", "55116", "Mainz"),
        ("Schloßstraße", "25", "48143", "Münster"),
        ("Neustadt", "22", "38100", "Braunschweig"),
        ("Alter Markt", "11", "24103", "Kiel"),
        ("Bockenheimer Landstraße", "101", "60325", "Frankfurt am Main"),
        ("Arnulfstraße", "60", "80335", "München"),
        ("Grünberger Straße", "54", "35390", "Gießen"),
        ("Universitätsstraße", "14", "33615", "Bielefeld"),
        ("Königin-Luise-Straße", "15", "14195", "Berlin"),
        ("Innere Wiener Straße", "6", "81667", "München"),
        ("Rotebühlplatz", "17", "70178", "Stuttgart"),
        ("Am Sandtorkai", "70", "20457", "Hamburg"),
        ("Berliner Allee", "55", "40212", "Düsseldorf"),
    ]
    
    # Wählen Sie zufällig eine Adresse aus der plausiblen Liste aus
    chosen_address = random.choice(plausible_addresses)
    
    return {
        "Straße": chosen_address[0],
        "Hausnummer": chosen_address[1],
        "PLZ": chosen_address[2],
        "Stadt": chosen_address[3],
    }

# --- Hauptlogik ---
if __name__ == "__main__":
    print("Starte Adressprüfung und schreibe Ergebnisse in 'gepruefte_adressen.csv'...\n")

    num_addresses_str = input("Wie viele Adressen sollen generiert und geprüft werden? ")
    try:
        num_addresses_to_generate = int(num_addresses_str)
        if num_addresses_to_generate <= 0:
            print("Bitte geben Sie eine positive Zahl ein.")
            exit()
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")
        exit()

    # Öffne die Ausgabedatei zum Schreiben
    with open(output_csv_filename, 'w', newline='', encoding='utf-8') as outfile:
        csv_writer = csv.writer(outfile)

        # Schreibe den Header in die Ausgabedatei mit den gewünschten Feldern
        csv_writer.writerow([
            "Adress-ID", "Straße", "Hausnummer", "Stadtteil", "Postleitzahl", "Stadt", "Bundesland", "Breitengrad", "Längengrad"
        ])

        print(f"Generiere und prüfe {num_addresses_to_generate} Adressen...\n")

        found_addresses_count = 0
        total_attempts = 0 # Zähler für alle Prüfversuche
        
        # Schleife, die läuft, bis die gewünschte Anzahl gefundener Adressen erreicht ist
        while found_addresses_count < num_addresses_to_generate:
            total_attempts += 1
            generated_address = generate_plausible_german_address()
            
            strasse_orig = generated_address["Straße"]
            hausnummer_orig = generated_address["Hausnummer"]
            plz_orig = generated_address["PLZ"]
            stadt_orig = generated_address["Stadt"]
            
            # Aufbau der vollständigen Adresse für die Abfrage
            vollstaendige_adresse_query = f"{strasse_orig} {hausnummer_orig}, {plz_orig} {stadt_orig}, Deutschland"

            # Standardwerte für den Fall, dass die Adresse nicht gefunden wird
            geocoded_strasse = ""
            geocoded_hausnummer = ""
            geocoded_stadtteil = ""
            geocoded_plz = ""
            geocoded_stadt = ""
            geocoded_bundesland = "" 
            geocoded_latitude = ""
            geocoded_longitude = ""
            
            pruefergebnis_status = "NICHT gefunden"

            try:
                # Versuche, die Adresse zu finden
                # addressdetails=True ist entscheidend für detaillierte Rohdaten
                location = geolocator.geocode(vollstaendige_adresse_query, timeout=10, addressdetails=True) 
                
                if location:
                    pruefergebnis_status = "Gefunden"
                    # Extrahiere die gewünschten Felder aus den Rohdaten der Geokodierung
                    address_raw = location.raw.get('address', {})
                    
                    # --- DEBUG-AUSGABE (kann auskommentiert werden, wenn nicht mehr benötigt) ---
                    # print(f"  DEBUG: Komplette Rohdaten von Nominatim: {location.raw}") 
                    # print(f"  DEBUG: 'address' Teil der Rohdaten: {address_raw}")

                    # --- Erweiterte Logik zur Extraktion der Straße ---
                    geocoded_strasse = address_raw.get('road') or \
                                       address_raw.get('street') or \
                                       address_raw.get('square') or \
                                       address_raw.get('pedestrian') or \
                                       address_raw.get('footway') or \
                                       address_raw.get('path') or \
                                       address_raw.get('place') or \
                                       '' 

                    geocoded_hausnummer = address_raw.get('house_number', '')
                    
                    # 'suburb', 'neighbourhood', 'district', 'county' sind gängige Keys für Stadtteil
                    geocoded_stadtteil = address_raw.get('suburb') or \
                                         address_raw.get('neighbourhood') or \
                                         address_raw.get('district') or \
                                         address_raw.get('county') or \
                                         ''
                    geocoded_plz = address_raw.get('postcode', '')
                    # 'city', 'town', 'village' sind gängige Keys für Stadt
                    geocoded_stadt = address_raw.get('city') or \
                                     address_raw.get('town') or \
                                     address_raw.get('village') or \
                                     ''
                    
                    # Bundesland hinzufügen (oft unter dem Schlüssel 'state' oder 'region')
                    # Wenn kein spezifisches Bundesland gefunden wird (z.B. bei Stadtstaaten),
                    # die Stadt als Bundesland setzen.
                    geocoded_bundesland = address_raw.get('state') or \
                                          address_raw.get('region')
                    
                    if not geocoded_bundesland and geocoded_stadt:
                        geocoded_bundesland = geocoded_stadt
                    elif not geocoded_bundesland: # Wenn weder Bundesland noch Stadt gefunden
                        geocoded_bundesland = ''


                    # Latitude und Longitude hinzufügen
                    geocoded_latitude = location.latitude
                    geocoded_longitude = location.longitude
                    
                print(f"[Versuch {total_attempts}] - Gefunden: {found_addresses_count}/{num_addresses_to_generate} - Prüfe: '{vollstaendige_adresse_query}' -> Status: {pruefergebnis_status}")
                
                if pruefergebnis_status == "Gefunden":
                    print(f"  Gefunden: Straße='{geocoded_strasse}', Hausnr='{geocoded_hausnummer}', Stadtteil='{geocoded_stadtteil}', PLZ='{geocoded_plz}', Stadt='{geocoded_stadt}', Bundesland='{geocoded_bundesland}', Lat='{geocoded_latitude}', Lon='{geocoded_longitude}'")


            except GeocoderTimedOut:
                pruefergebnis_status = "Timeout"
                print(f"[Versuch {total_attempts}] -> Timeout bei der Prüfung von: '{vollstaendige_adresse_query}'")
            except GeocoderServiceError as e:
                pruefergebnis_status = f"Dienstfehler: {e}"
                print(f"[Versuch {total_attempts}] -> Dienstfehler bei der Prüfung von: '{vollstaendige_adresse_query}' ({e})")
            except Exception as e:
                pruefergebnis_status = f"Unerwarteter Fehler: {e}"
                print(f"[Versuch {total_attempts}] -> Ein unerwarteter Fehler ist aufgetreten: {e}")
            
            # Nur schreiben und Zähler erhöhen, wenn das Prüfergebnis "Gefunden" ist
            if pruefergebnis_status == "Gefunden":
                # Adress-ID generieren
                address_id = f"A-{found_addresses_count + 1:04d}" # Format A-0001, A-0002 etc.

                csv_writer.writerow([
                    address_id, # Adress-ID hinzufügen
                    geocoded_strasse, 
                    geocoded_hausnummer, 
                    geocoded_stadtteil, 
                    geocoded_plz, 
                    geocoded_stadt,
                    geocoded_bundesland, # Bundesland hinzufügen
                    geocoded_latitude,
                    geocoded_longitude
                ])
                found_addresses_count += 1
                # Bestätigung, dass der Datensatz geschrieben wurde
                print(f"  -> Datensatz {address_id} in '{output_csv_filename}' geschrieben: {geocoded_strasse} {geocoded_hausnummer}, {geocoded_plz} {geocoded_stadt}, {geocoded_bundesland}")
            
            # Eine kleine Pause einlegen, um die Rate Limits des Dienstes zu respektieren.
            time.sleep(1)

    print(f"\nAdressprüfung abgeschlossen. {found_addresses_count} Adressen als 'Gefunden' markiert und in '{output_csv_filename}' gespeichert.")
