from datetime import datetime
from Class import Mitarbeiter, Kunde, Kurs


class Applikation:
    def __init__(self):
        self.personenliste = []
        self.kundenliste = []
        self.mitarbeiterliste = []
        self.kursliste = []

    def person_hinzufuegen(self, typ):
        name = input("Name: ")
        alter = int(input("Alter: "))
        geschlecht = input("Geschlecht (m/w): ")

        if typ.lower() == 'k':
            kundennummer = int(input("Kundennummer: "))
            email = input("Email: ")
            person = Kunde(name, alter, geschlecht, kundennummer, email)
            self.personenliste.append(person)
            datei = "kundenliste.txt"
        elif typ.lower() == 'm':
            mitarbeiter_id = int(input("Mitarbeiter-ID: "))
            abteilung = input("Abteilung: ")
            person = Mitarbeiter(name, alter, geschlecht, mitarbeiter_id, abteilung)
            self.personenliste.append(person)
            datei = "mitarbeiterliste.txt"
        else:
            print("Ungültige Eingabe. Es wurde keine Person hinzugefügt.")
            return

        person.exportieren(datei)
        print(f"{type(person).__name__} {person.name} erfolgreich hinzugefügt.")

    def personen_aus_datei_laden(self, datei):
        try:
            with open(datei, 'r') as f:
                for line in f:
                    parts = line.strip().split(': ')
                    if len(parts) >= 2:
                        typ = parts[0]
                        daten = parts[1]

                        if typ == "Kunde":
                            kunde_daten = daten.split(', ')
                            if len(kunde_daten) == 5:
                                name, alter, geschlecht, kundennummer, email = kunde_daten
                                kunde = Kunde(name, int(alter), geschlecht, int(kundennummer), email)
                                self.personenliste.append(kunde)
                                self.kundenliste.append(kunde)
                        elif typ == "Mitarbeiter":
                            mitarbeiter_daten = daten.split(', ')
                            if len(mitarbeiter_daten) == 5:
                                name, alter, geschlecht, mitarbeiter_id, abteilung = mitarbeiter_daten
                                mitarbeiter = Mitarbeiter(name, int(alter), geschlecht, int(mitarbeiter_id), abteilung)
                                self.personenliste.append(mitarbeiter)
                                self.mitarbeiterliste.append(mitarbeiter)
                        elif typ == "Kurs":
                            kurs_daten = daten.split(', ')
                            if len(kurs_daten) == 3:
                                kursname, kursleiter, datum = kurs_daten
                                kurs = Kurs(kursname, kursleiter, datum)
                                self.kursliste.append(kurs)

                    else:
                        print(f"Ungültiges Format in der Datei: {line.strip()}")

        except FileNotFoundError:
            print(f"Die Datei '{datei}' wurde nicht gefunden.")

    def kurs_hinzufuegen(self):
        print("\nNeuen Kurs hinzufügen:")
        kursname = input("Kursname: ")
        kursleiter = input("Kursleiter: ")
        datum = input("Datum (YYYY-MM-DD): ")
        kurs = Kurs(kursname, kursleiter, datum)
        self.kursliste.append(kurs)
        kurs.exportieren("kursliste.txt")
        print("Kurs erfolgreich hinzugefügt.")

    def alle_kurse_anzeigen(self):
        for kurs in self.kursliste:
            print(f"Kursname: {kurs.kursname} , Kursleiter: {kurs.kursleiter}, Datum: {kurs.datum}")

    def kunden_filtern(self, eingangsdatei, filterattribut, filterwert):
        try:
            gefilterte_kunden = []
            with open(eingangsdatei, 'r') as f_in:
                for line in f_in:
                    if 'Kunde' in line:
                        if filterattribut == 'Name' and filterwert.lower() in line.split(': ')[1].split(', ')[0].lower():
                            gefilterte_kunden.append(line.strip())
                        elif filterattribut == 'Kundennummer' and filterwert in line.split(', ')[3]:
                            gefilterte_kunden.append(line.strip())
                        elif filterattribut == 'Email' and filterwert.lower() in line.split(', ')[4].lower():
                            gefilterte_kunden.append(line.strip())

            if gefilterte_kunden:
                print(f"\nGefilterte Kunden für '{filterwert}':")
                for kunde in gefilterte_kunden:
                    print(kunde)
                with open("gefilterte_kunden.txt", 'w') as f_out:
                    for kunde in gefilterte_kunden:
                        f_out.write(f"{kunde}\n")
                print(f"Gefilterte Kunden für '{filterwert}' in 'gefilterte_kunden.txt' gespeichert.")
            else:
                print(f"Keine gefilterten Kunden für '{filterwert}' gefunden.")
        except FileNotFoundError:
            print(f"Die Datei '{eingangsdatei}' wurde nicht gefunden.")

    def mitarbeiter_filtern(self, eingangsdatei, filterattribut, filterwert):
        try:
            gefilterte_mitarbeiter = []
            with open(eingangsdatei, 'r') as f_in:
                for line in f_in:
                    if 'Mitarbeiter' in line:
                        if filterattribut == 'Name' and filterwert.lower() in line.split(': ')[1].split(', ')[0].lower():
                            gefilterte_mitarbeiter.append(line.strip())
                        elif filterattribut == 'Mitarbeiter-ID' and filterwert in line.split(', ')[3]:
                            gefilterte_mitarbeiter.append(line.strip())
                        elif filterattribut == 'Abteilung' and filterwert.lower() in line.split(', ')[4].lower():
                            gefilterte_mitarbeiter.append(line.strip())

            if gefilterte_mitarbeiter:
                print(f"\nGefilterte Mitarbeiter für '{filterwert}':")
                for mitarbeiter in gefilterte_mitarbeiter:
                    print(mitarbeiter)
                with open("gefilterte_mitarbeiter.txt", 'w') as f_out:
                    for mitarbeiter in gefilterte_mitarbeiter:
                        f_out.write(f"{mitarbeiter}\n")
                print(f"Gefilterte Mitarbeiter für '{filterwert}' in 'gefilterte_mitarbeiter.txt' gespeichert.")
            else:
                print(f"Keine gefilterten Mitarbeiter für '{filterwert}' gefunden.")
        except FileNotFoundError:
            print(f"Die Datei '{eingangsdatei}' wurde nicht gefunden.")

    def gesamte_daten_anzeigen(self):
        print("\nGesamte Daten:")
        self.personen_aus_datei_laden("kundenliste.txt")
        self.personen_aus_datei_laden("mitarbeiterliste.txt")
        self.personen_aus_datei_laden("kursliste.txt")

        for person in self.personenliste:
            print(f"{type(person).__name__} : {person.name}, {person.alter}, {person.geschlecht}")

        self.alle_kurse_anzeigen()

    def gruessen(self):
        jetzt = datetime.now()
        aktuelle_stunde = jetzt.hour
        aktuelles_datum_zeit = jetzt.strftime("%Y-%m-%d %H:%M:%S")

        if aktuelle_stunde < 12:
            begruessung = f"Guten Morgen! Heute ist der {aktuelles_datum_zeit}\n"
        elif 12 <= aktuelle_stunde < 18:
            begruessung = f"Guten Tag! Heute ist der {aktuelles_datum_zeit}\n"
        else:
            begruessung = f"Guten Abend! Heute ist der {aktuelles_datum_zeit}\n"

        return begruessung

    def filtern(self):
        filtern = input("\nMöchten Sie die Kundenliste (k) oder Mitarbeiterliste (m) filtern und anzeigen? ").lower()
        if filtern == 'k':
            filterattribut = input("Nach welchen Wert möchten Sie suchen (Name/Kundennummer/Email)? ")
            filterwert = input(f"Geben Sie den Filterwert für {filterattribut} ein: ")
            self.kunden_filtern("kundenliste.txt", filterattribut, filterwert)
        elif filtern == 'm':
            filterattribut = input("Nach welchen Wert möchten Sie suchen (Name/Mitarbeiter-ID/Abteilung)? ")
            filterwert = input(f"Geben Sie den Filterwert für {filterattribut} ein: ")
            self.mitarbeiter_filtern("mitarbeiterliste.txt", filterattribut, filterwert)
        else:
            print("Ungültige Eingabe.")
