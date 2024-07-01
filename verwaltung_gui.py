import tkinter as tk
from tkinter import messagebox
from applikation import Applikation
from Class import Kurs, Mitarbeiter, Kunde, Person
class GUI:
    def __init__(self, root):
        self.app = Applikation()
        self.root = root
        self.root.title("Kursverwaltungsprogramm")

        # Hauptmenü
        self.main_menu = tk.Frame(self.root)
        self.main_menu.pack()

        self.label = tk.Label(self.main_menu, text=self.app.gruessen() + " Willkommen im Kursverwaltungsprogramm!")
        self.label.pack()

        self.kunde_btn = tk.Button(self.main_menu, text="Kunde hinzufügen", command=self.kunde_hinzufuegen)
        self.kunde_btn.pack()

        self.mitarbeiter_btn = tk.Button(self.main_menu, text="Mitarbeiter hinzufügen", command=self.mitarbeiter_hinzufuegen)
        self.mitarbeiter_btn.pack()

        self.kurs_btn = tk.Button(self.main_menu, text="Kurs hinzufügen", command=self.kurs_hinzufuegen)
        self.kurs_btn.pack()

        self.anzeigen_btn = tk.Button(self.main_menu, text="Gesamte Daten anzeigen", command=self.gesamte_daten_anzeigen)
        self.anzeigen_btn.pack()

        self.filtern_btn = tk.Button(self.main_menu, text="Filtern", command=self.filtern)
        self.filtern_btn.pack()

        self.beenden_btn = tk.Button(self.main_menu, text="Beenden", command=self.root.quit)
        self.beenden_btn.pack()

    def kunde_hinzufuegen(self):
        self.person_hinzufuegen('k')

    def mitarbeiter_hinzufuegen(self):
        self.person_hinzufuegen('m')

    def kurs_hinzufuegen(self):
        self.kurs_dialog()

    def gesamte_daten_anzeigen(self):
        self.app.gesamte_daten_anzeigen()

    def filtern(self):
        self.filtern_dialog()

    def person_hinzufuegen(self, typ):
        dialog = tk.Toplevel(self.root)
        dialog.title("Person hinzufügen")

        tk.Label(dialog, text="Name:").pack()
        name_entry = tk.Entry(dialog)
        name_entry.pack()

        tk.Label(dialog, text="Alter:").pack()
        alter_entry = tk.Entry(dialog)
        alter_entry.pack()

        tk.Label(dialog, text="Geschlecht (m/w):").pack()
        geschlecht_entry = tk.Entry(dialog)
        geschlecht_entry.pack()

        if typ == 'k':
            tk.Label(dialog, text="Kundennummer:").pack()
            kundennummer_entry = tk.Entry(dialog)
            kundennummer_entry.pack()

            tk.Label(dialog, text="Email:").pack()
            email_entry = tk.Entry(dialog)
            email_entry.pack()

            def save_kunde():
                name = name_entry.get()
                alter = int(alter_entry.get())
                geschlecht = geschlecht_entry.get()
                kundennummer = int(kundennummer_entry.get())
                email = email_entry.get()

                person = Kunde(name, alter, geschlecht, kundennummer, email)
                self.app.personenliste.append(person)
                person.exportieren("kundenliste.txt")
                messagebox.showinfo("Erfolg", "Kunde erfolgreich hinzugefügt.")
                dialog.destroy()

            save_btn = tk.Button(dialog, text="Speichern", command=save_kunde)
            save_btn.pack()

        elif typ == 'm':
            tk.Label(dialog, text="Mitarbeiter-ID:").pack()
            mitarbeiter_id_entry = tk.Entry(dialog)
            mitarbeiter_id_entry.pack()

            tk.Label(dialog, text="Abteilung:").pack()
            abteilung_entry = tk.Entry(dialog)
            abteilung_entry.pack()

            def save_mitarbeiter():
                name = name_entry.get()
                alter = int(alter_entry.get())
                geschlecht = geschlecht_entry.get()
                mitarbeiter_id = int(mitarbeiter_id_entry.get())
                abteilung = abteilung_entry.get()

                person = Mitarbeiter(name, alter, geschlecht, mitarbeiter_id, abteilung)
                self.app.personenliste.append(person)
                person.exportieren("mitarbeiterliste.txt")
                messagebox.showinfo("Erfolg", "Mitarbeiter erfolgreich hinzugefügt.")
                dialog.destroy()

            save_btn = tk.Button(dialog, text="Speichern", command=save_mitarbeiter)
            save_btn.pack()

    def kurs_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Kurs hinzufügen")

        tk.Label(dialog, text="Kursname:").pack()
        kursname_entry = tk.Entry(dialog)
        kursname_entry.pack()

        tk.Label(dialog, text="Kursleiter:").pack()
        kursleiter_entry = tk.Entry(dialog)
        kursleiter_entry.pack()

        tk.Label(dialog, text="Datum (YYYY-MM-DD):").pack()
        datum_entry = tk.Entry(dialog)
        datum_entry.pack()

        def save_kurs():
            kursname = kursname_entry.get()
            kursleiter = kursleiter_entry.get()
            datum = datum_entry.get()

            kurs = Kurs(kursname, kursleiter, datum)
            self.app.kursliste.append(kurs)
            kurs.exportieren("kursliste.txt")
            messagebox.showinfo("Erfolg", "Kurs erfolgreich hinzugefügt.")
            dialog.destroy()

        save_btn = tk.Button(dialog, text="Speichern", command=save_kurs)
        save_btn.pack()

    def filtern_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Filtern")

        tk.Label(dialog, text="Möchten Sie die Kundenliste (k) oder Mitarbeiterliste (m) filtern und anzeigen?").pack()
        filtern_entry = tk.Entry(dialog)
        filtern_entry.pack()

        tk.Label(dialog, text="Nach welchem Wert möchten Sie suchen (Name/Kundennummer/Email für Kunden oder Name/Mitarbeiter-ID/Abteilung für Mitarbeiter)?").pack()
        filterattribut_entry = tk.Entry(dialog)
        filterattribut_entry.pack()

        tk.Label(dialog, text="Geben Sie den Filterwert ein:").pack()
        filterwert_entry = tk.Entry(dialog)
        filterwert_entry.pack()

        def apply_filter():
            filtern = filtern_entry.get().lower()
            filterattribut = filterattribut_entry.get()
            filterwert = filterwert_entry.get()

            if filtern == 'k':
                self.app.kunden_filtern("kundenliste.txt", filterattribut, filterwert)
            elif filtern == 'm':
                self.app.mitarbeiter_filtern("mitarbeiterliste.txt", filterattribut, filterwert)
            else:
                messagebox.showerror("Fehler", "Ungültige Eingabe.")
                return
            dialog.destroy()

        apply_btn = tk.Button(dialog, text="Anwenden", command=apply_filter)
        apply_btn.pack()

if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
