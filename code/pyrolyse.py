class EnergieTraeger:
    def __init__(self, energie_gehalt, kohlenstoff_gehalt, dichte_kg_pro_kubikmeter, zuwachsrate, name=""):
        self.energie_gehalt = energie_gehalt  # kWh
        self.kohlenstoff_gehalt = kohlenstoff_gehalt  # Prozentsatz
        self.zuwachsrate = zuwachsrate  # Kubikmeter pro Hektar pro Jahr
        self.dichte_kg_pro_kubikmeter = dichte_kg_pro_kubikmeter # Gewicht pro Kubikmeter in kg
        self.name = name
        print(f'Eingangsmaterial erstellt: {self.name}')



    def benoetigte_forstflaeche(self, verbrauch_pro_h):
        # Umrechnung der jährlichen Holzmenge in Kubikmeter
        jahresverbrauch = verbrauch_pro_h * 24 * 365  # in kg
        jahresmenge_holz_kubikmeter = jahresverbrauch / self.dichte_kg_pro_kubikmeter

        # Berechnung der benötigten Forstfläche in Hektar
        benoetigte_waldflaeche_hektar = jahresmenge_holz_kubikmeter / self.zuwachsrate
        return benoetigte_waldflaeche_hektar

    def berechne_co2_bindung(self, forstflaeche, zeit_in_h):
        # Berechnung des gebundenen CO2 in Tonnen
        jahresbindung = forstflaeche * self.zuwachsrate * self.kohlenstoff_gehalt * 44 / 12  # Umrechnung C zu CO2
        stundenbindung = jahresbindung / (365 * 24)  # Umrechnung auf Stunden
        gebundenes_co2 = stundenbindung * zeit_in_h
        return gebundenes_co2

# Jahresmenge Holz: 2559.908 t
# Jahresmenge Holz: 4266.5 Kubikmeter
# Benoetigte Waldflaeche: 426.7 Hektar

# jahresverbrauch 2566680
# jahresmenge_holz_kubikmeter 4277.8


class EnergieGewinnung:
    def __init__(self, eingangsmasse_pro_h,
                        ausgangs_energie_strom,
                        ausgangs_energie_waerme,
                        ratio_eingangsmasse_zu_pflanzenkohle,
                        kohlenstoffgehalt_pflanzenkohle,
                        anlagen_name="",
                        energie_klasse=None,
                        anzahl_anlagen = 1):
        self.eingangsmasse_pro_h = eingangsmasse_pro_h  # kg
        self.ausgangs_energie_strom = ausgangs_energie_strom  # kWh
        self.ausgangs_energie_waerme = ausgangs_energie_waerme  # kWh
        self.ratio_eingangsmasse_zu_pflanzenkohle = ratio_eingangsmasse_zu_pflanzenkohle
        self.kohlenstoffgehalt_pflanzenkohle = kohlenstoffgehalt_pflanzenkohle  # Prozentsatz
        self.anlagen_name = anlagen_name
        self.energie_klasse = energie_klasse
        self.anzahl_anlagen = anzahl_anlagen
        print(f'Anlage erstellt: {self.anlagen_name}')

    def kohlenstoff_emission_in_kg(self, laufzeit_in_h):
        # Berechnung der Kohlenstoffemission in kg
        gesamtenergie = (self.ausgangs_energie_strom + self.ausgangs_energie_waerme) * laufzeit_in_h
        gesamtkohlenstoff = self.eingangsmasse_pro_h * gesamtenergie * self.kohlenstoffgehalt_pflanzenkohle
        return gesamtkohlenstoff * self.anzahl_anlagen

    def eingangsmasse_in_kg(self, laufzeit_in_h):
        # Berechnung der gesamten Eingangsmasse in kg
        gesamteingangsmasse = self.eingangsmasse_pro_h * laufzeit_in_h
        return gesamteingangsmasse  * self.anzahl_anlagen # kg pro h

    def pflanzenkohle_in_kg(self, laufzeit_in_h):
        # Berechnung der erzeugten Pflanzenkohle in kg
        gesamtenergie = (self.ausgangs_energie_strom + self.ausgangs_energie_waerme) * laufzeit_in_h
        gesamtpflanzenkohle = self.eingangsmasse_pro_h * gesamtenergie * self.ratio_eingangsmasse_zu_pflanzenkohle
        return gesamtpflanzenkohle  * self.anzahl_anlagen

    def ausgangsleistung_ueber_zeitraum(self, laufzeit_in_h=1, waerme=True, strom=True):
        # Berechnung der gesamten Ausgangsleistung in kWh
        gesamtleistung = 0
        if strom:
            gesamtleistung += self.ausgangs_energie_strom * laufzeit_in_h
        if waerme:
            gesamtleistung += self.ausgangs_energie_waerme * laufzeit_in_h
        return gesamtleistung * self.anzahl_anlagen

    def benoetigte_flaeche(self):
        flaeche = self.energie_klasse.benoetigte_forstflaeche(self.eingangsmasse_pro_h)
        return flaeche * self.anzahl_anlagen

    def bericht(self):
        print(f'Anlage: {self.anlagen_name}')
        print(f'Anzahl der Anlagen: {self.anzahl_anlagen}')
        print('Gesamtleistung pro Stunde: ', smart_format(self.ausgangsleistung_ueber_zeitraum(), 'kWh') )
        print('Eingangsmasse pro Jahr: ', smart_format(self.eingangsmasse_in_kg(24), 'kg'))
        print('Benötigte Fläche: ', smart_format(self.benoetigte_flaeche(), 'Hektar'))


def smart_format(number, unit):

    if unit in ["kg", "kWh"]:
        scaled_unit=unit.replace('kg', 't').replace('kWh', 'MWh')
        if number >= 1000:
            return f"{number:,.2f} {unit} ({number / 1000:,.2f} {scaled_unit})"  # Für kg wird zu t und für kWh wird zu MWh
        else:
            return f"{number:,.2f} {unit}"
    else:
        return f"{number:,.0f} {unit}"  # Standardformatierung

stunden_pro_jahr = 24*365

# Umrechnung von Kohlenstoff in CO2
def umrechnungsfaktor_c_zu_co2():
    molekulargewicht_c = 12  # Molekulargewicht von Kohlenstoff
    molekulargewicht_co2 = 44  # Molekulargewicht von CO2
    umrechnungsfaktor_c_zu_co2 = molekulargewicht_co2 / molekulargewicht_c
    return umrechnungsfaktor_c_zu_co2

# Init

holz = EnergieTraeger(
    energie_gehalt = 4250, # kWh
    kohlenstoff_gehalt = 50, # Prozent
    dichte_kg_pro_kubikmeter = 600, # kg, Durchschnitt
    zuwachsrate = 10, # Kubikmeter Zuwachs pro Hektar pro Jahr
    name="Holz")

# Erstellen einer Instanz der Klasse EnergieGewinnung
clinx50 = EnergieGewinnung(
    eingangsmasse_pro_h = 295,
    ausgangs_energie_strom = 32,
    ausgangs_energie_waerme = 150,
    ratio_eingangsmasse_zu_pflanzenkohle = 1/3,
    kohlenstoffgehalt_pflanzenkohle = 90,
    anlagen_name='Clinx 50',
    energie_klasse=holz,
    anzahl_anlagen=1000
)

clinx50.bericht()
