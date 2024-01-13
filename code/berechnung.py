from pyrolyse import EnergieGewinnung, EnergieTraeger, helper

# Init
h = helper()


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
    ratio_eingangsmasse_zu_pflanzenkohle = 1/3.5,
    kohlenstoffgehalt_pflanzenkohle = 90,
    anlagen_name='Clinx 50',
    energie_klasse=holz,
    anzahl_anlagen=1
)

clinx150 = EnergieGewinnung(
    eingangsmasse_pro_h = 382,
    ausgangs_energie_strom = 100,
    ausgangs_energie_waerme = 250,
    ratio_eingangsmasse_zu_pflanzenkohle = 1/3.5,
    kohlenstoffgehalt_pflanzenkohle = 90,
    anlagen_name='Clinx 150',
    energie_klasse=holz,
    anzahl_anlagen=1
)

print(clinx50.bericht(1))
print(clinx50.bericht(h.stunden_pro_jahr))

print(clinx150.bericht(1))
print(clinx150.bericht(h.stunden_pro_jahr))

print()
print('## 1000 Anlagen über 1 Jahr ##')
print()
clinx50.anzahl_anlagen = 1000
clinx150.anzahl_anlagen = 1000
print(clinx50.bericht(h.stunden_pro_jahr))
print(clinx150.bericht(h.stunden_pro_jahr))


strom_eur = 0.08 # pro kWh
waerme_eur = 0.08 # pro kWh
pflanzenkohle_eur = 0.1 * 0.3 # 1 EUR pro kg, 70% Marge und Steuer
co2_zertifikat_eur = 0.05 # 0.05 EUR pro kg
# Der Preis für CO2-Zertifikate in Europa, die im Rahmen des EU-Emissionshandelssystems (EU ETS) gehandelt werden, variiert ständig, ähnlich wie Aktienkurse. Zum Stand meines letzten Trainings im April 2023 lagen die Preise für CO2-Zertifikate in der Regel zwischen 50 und 90 Euro pro Tonne CO2. Es ist jedoch wichtig zu beachten, dass diese Preise Schwankungen unterliegen, basierend auf Marktdynamiken, politischen Entscheidungen und anderen Faktoren.
# Statista: Während der Preis für ein CO2-Zertifikat im EU Emissions Trading System (EU-ETS) in 2007 noch durchschnittlich bei etwa 0,70 Euro lag, stieg er bis 2022² auf durchschnittlich ca. 81 Euro an.


def amortisation(anlage):
    anlage.anzahl_anlagen = 1
    zeitraum_in_h = h.stunden_pro_jahr
    strom_ertrag = anlage.ausgangsleistung_ueber_zeitraum(zeitraum_in_h, waerme=False) * strom_eur
    waerme_ertrag = anlage.ausgangsleistung_ueber_zeitraum(zeitraum_in_h, strom=False) * waerme_eur
    pflanzenkohle_ertrag = anlage.pflanzenkohle_in_kg(zeitraum_in_h) * pflanzenkohle_eur
    co2_zertifikat_ertrag = anlage.gebundener_kohlenstoff(zeitraum_in_h)*h.umrechnungsfaktor_c_zu_co2() * co2_zertifikat_eur
    fte = 2*-50000
    biomasse = -700*52*(anlage.eingangsmasse_pro_h/295)
    einnahmen = strom_ertrag + waerme_ertrag + pflanzenkohle_ertrag + co2_zertifikat_ertrag

    print(f'## {anlage.anlagen_name} Amortisation über 1 Jahr ##' )
    print('|| pro Jahr | Basis |')
    print('|---|---|---|')
    print('| Strom |',h.smart_format(strom_ertrag, f'EUR | {strom_eur} EUR/kWh | ') )
    print('| Wärme |',h.smart_format(waerme_ertrag, f'EUR | {waerme_eur} EUR/kWh |') )
    print('| Pflanzenkohle |',h.smart_format(pflanzenkohle_ertrag, f'EUR | {pflanzenkohle_eur} EUR/kg |') )
    print('| CO2 Zertifikate |',h.smart_format(co2_zertifikat_ertrag, f'EUR | {co2_zertifikat_eur} EUR/kg |'))
    print('| 2 FTE Mitarbeiter |',h.smart_format(fte, "EUR"), '| |')
    print('| Biomasse |',h.smart_format(biomasse, "EUR"), '| 700EUR/Woche/295kg/h|')
    print('| **Einnahmen** |',h.smart_format(einnahmen, 'EUR'), '| |' )
    print('| **Amortisation** |',h.smart_format(einnahmen+fte+biomasse, 'EUR'), '| |' )



amortisation(clinx50)
print()
amortisation(clinx150)
