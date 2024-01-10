class helper:
    def __init__(self):
        self.stunden_pro_jahr = 24*365
        self.stunden_pro_woche = 24*7
# ------------------------------------------------------------------------------------
    def smart_format(self, number, unit):
        unit_dict = {"kg":"t", "kWh":"MWh"}
        if unit in unit_dict.keys():
            scaled_unit=unit_dict[unit] # Für kg wird zu t und für kWh wird zu MWh
            if number >= 1000:
                scaled_number = number / 1000
                formatted_number = f"{scaled_number:,.2f}".rstrip('0').rstrip('.') if scaled_number % 1 != 0 else f"{scaled_number:,.0f}"
                return f"{number:,.0f} {unit} ({formatted_number} {scaled_unit})"
            else:
                formatted_number = f"{number:,.2f}".rstrip('0').rstrip('.') if number % 1 != 0 else f"{number:,.0f}"
                return f"{formatted_number} {unit}"
        else:
            return f"{number:,.0f} {unit}"  # Standardformatierung
# ------------------------------------------------------------------------------------
    def umrechnungsfaktor_c_zu_co2(self):
        # Umrechnung von Kohlenstoff in CO2
        molekulargewicht_c = 12  # Molekulargewicht von Kohlenstoff
        molekulargewicht_co2 = 44  # Molekulargewicht von CO2
        umrechnungsfaktor_c_zu_co2 = molekulargewicht_co2 / molekulargewicht_c
        return umrechnungsfaktor_c_zu_co2
# ------------------------------------------------------------------------------------



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
        gesamtkohlenstoff = self.eingangsmasse_pro_h * (self.energie_klasse.kohlenstoff_gehalt/100) * laufzeit_in_h
        kohlenstoff_emission = gesamtkohlenstoff - self.gebundener_kohlenstoff(laufzeit_in_h)
        return kohlenstoff_emission * self.anzahl_anlagen

    def co2_emission_in_kg(self, laufzeit_in_h):
        # Berechnung der CO2 in kg
        gesamt_co2 = self.kohlenstoff_emission_in_kg(laufzeit_in_h) * h.umrechnungsfaktor_c_zu_co2()
        return gesamt_co2 * self.anzahl_anlagen

    def eingangsmasse_in_kg(self, laufzeit_in_h):
        # Berechnung der gesamten Eingangsmasse in kg
        gesamteingangsmasse = self.eingangsmasse_pro_h * laufzeit_in_h
        return gesamteingangsmasse  * self.anzahl_anlagen # kg pro h

    def pflanzenkohle_in_kg(self, laufzeit_in_h):
        # Berechnung der erzeugten Pflanzenkohle in kg
        gesamtpflanzenkohle = self.eingangsmasse_pro_h * self.ratio_eingangsmasse_zu_pflanzenkohle * laufzeit_in_h
        return gesamtpflanzenkohle * self.anzahl_anlagen

    def gebundener_kohlenstoff(self, laufzeit_in_h):
        return self.pflanzenkohle_in_kg(laufzeit_in_h) * (self.kohlenstoffgehalt_pflanzenkohle/100)



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

    def bericht(self, zeitraum_in_h=1):
        if zeitraum_in_h >= h.stunden_pro_jahr:
            zeitraum_string = h.smart_format(zeitraum_in_h / h.stunden_pro_jahr, 'Jahr(e)')
        elif zeitraum_in_h >= h.stunden_pro_woche:
            zeitraum_string = h.smart_format(zeitraum_in_h / h.stunden_pro_woche, 'Woche(n)')
        elif zeitraum_in_h >= 24:
            zeitraum_string = h.smart_format(zeitraum_in_h / 24, 'Tag(e)')
        else:
            zeitraum_string = h.smart_format(zeitraum_in_h, 'Stunde(n)')

        print(f'## {self.anzahl_anlagen} {self.anlagen_name} Anlage über {zeitraum_string} ##')

        print('- Gesamtleistung:',h.smart_format(self.ausgangsleistung_ueber_zeitraum(zeitraum_in_h), 'kWh') )
        print('- Elektrische Netoleistung:',h.smart_format(self.ausgangsleistung_ueber_zeitraum(zeitraum_in_h, waerme=False), 'kWh') )
        print('- Benötigte Forstfläche:',h.smart_format(self.benoetigte_flaeche(), 'Hektar'))
        print('- Benötigte Menge Holz:',h.smart_format(self.eingangsmasse_in_kg(zeitraum_in_h), 'kg'))
        print('- Kohlenstoff Emission:',h.smart_format(self.kohlenstoff_emission_in_kg(zeitraum_in_h), 'kg'))
        print('- CO2 Emission:',h.smart_format(self.co2_emission_in_kg(zeitraum_in_h), 'kg'))
        print('- Pflanzenkohle Erzeugung:',h.smart_format(self.pflanzenkohle_in_kg(zeitraum_in_h), 'kg'))
        print('- Kohlenstoff Bindung:',h.smart_format(self.gebundener_kohlenstoff(zeitraum_in_h), 'kg'))
        print('- CO2 Reduktion:',h.smart_format(self.gebundener_kohlenstoff(zeitraum_in_h)*h.umrechnungsfaktor_c_zu_co2(), 'kg'))
        print()


h = helper()


