from applikation import Applikation

if __name__ == "__main__":
    app = Applikation()

    while True:
        auswahl = input(f"\n{app.gruessen()} Willkommen im Kursverwaltungsprogramm! \n"
                        f"Wählen Sie: \n (k) Kunde hinzufügen \n (m) Mitarbeiter hinzufügen \n (c) Kurs hinzufügen \n (a) Gesamte Daten anzeigen \n (f) Filtern \n (b) Beenden \n")

        if auswahl.lower() == 'k':
            app.person_hinzufuegen('k')
        elif auswahl.lower() == 'm':
            app.person_hinzufuegen('m')
        elif auswahl.lower() == 'a':
            app.gesamte_daten_anzeigen()
        elif auswahl.lower() == 'c':
            app.kurs_hinzufuegen()
        elif auswahl.lower() == 'f':
            app.filtern()
        elif auswahl.lower() == 'b':
            print("Programm wird beendet.")
            break
        else:
            print("Ungültige Eingabe.")
