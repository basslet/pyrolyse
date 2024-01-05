# Defining the variables
holzmenge_kg_h = 293  # Holzmenge in kg/h
kohlenstoffgehalt_holz = 0.50  # Kohlenstoffgehalt im Holz (50%)
freigesetzter_kohlenstoff_prozent = 50  # Prozentsatz des freigesetzten Kohlenstoffs (70,82%)

# Umrechnung von Kohlenstoff in CO2
molekulargewicht_c = 12  # Molekulargewicht von Kohlenstoff
molekulargewicht_co2 = 44  # Molekulargewicht von CO2
umrechnungsfaktor_c_zu_co2 = molekulargewicht_co2 / molekulargewicht_c

# Berechnung der freigesetzten Kohlenstoffmenge
freigesetzter_kohlenstoff_kg_h = holzmenge_kg_h * kohlenstoffgehalt_holz * (freigesetzter_kohlenstoff_prozent / 100)

# Umrechnung der Kohlenstoffmenge in CO2
co2_menge_kg_h = freigesetzter_kohlenstoff_kg_h * umrechnungsfaktor_c_zu_co2

# Berechnung der CO2-Emissionen pro MWh
elektrische_nettleistung_kw = 32  # Elektrische Nettoleistung in kW
elektrischer_wirkungsgrad = 0.19  # Elektrischer Wirkungsgrad (19%)
stunden_pro_mwh = 1000 / elektrische_nettleistung_kw  # Anzahl der Stunden, um 1 MWh zu produzieren
co2_emissionen_pro_mwh = co2_menge_kg_h * stunden_pro_mwh  # CO2-Emissionen pro MWh

print(f'CO2 Emissionen pro MWh: {round(co2_emissionen_pro_mwh, 1)} kgh')
