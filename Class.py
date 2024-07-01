class Person:
    def __init__(self, name, alter, geschlecht):
        self.name = name
        self.alter = alter
        self.geschlecht = geschlecht

    def exportieren(self, datei):
        with open(datei, 'a') as f:
            f.write(f"{type(self).__name__}: {self.name}, {self.alter}, {self.geschlecht}\n")

class Mitarbeiter(Person):
    def __init__(self, name, alter, geschlecht, mitarbeiter_id, abteilung):
        super().__init__(name, alter, geschlecht)
        self.mitarbeiter_id = mitarbeiter_id
        self.abteilung = abteilung

    def exportieren(self, datei):
        with open(datei, 'a') as f:
            f.write(f"{type(self).__name__} {self.mitarbeiter_id} : {self.name}, {self.alter}, {self.geschlecht}, {self.mitarbeiter_id}, {self.abteilung}\n")

class Kunde(Person):
    def __init__(self, name, alter, geschlecht, kundennummer, email):
        super().__init__(name, alter, geschlecht)
        self.kundennummer = kundennummer
        self.email = email

    def exportieren(self, datei):
        with open(datei, 'a') as f:
            f.write(f"{type(self).__name__} {self.kundennummer} : {self.name}, {self.alter}, {self.geschlecht}, {self.kundennummer}, {self.email}\n")

class Kurs:
    def __init__(self, kursname, kursleiter, datum):
        self.kursname = kursname
        self.kursleiter = kursleiter
        self.datum = datum

    def exportieren(self, datei):
        with open(datei, 'a') as f:
            f.write(f"{type(self).__name__}: {self.kursname}, {self.kursleiter}, {self.datum}\n")

