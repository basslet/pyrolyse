from kohlenstoff_bindung import berechne_kohlenstoff_bindung
gebundener_kohlenstoff_prozent, freigesetzter_kohlenstoff_prozent = berechne_kohlenstoff_bindung()


# Überprüfung und Korrektur der CO2-Emissionen Berechnung für Pyrolyse BHKW

# Menge an Holz für 1 MWh Strom
holzmenge_pro_32kwh = 293  # kg Holz für 32 kWh
stunden_pro_1mwh = 1000 / 32  # Anzahl der Stunden, um 1 MWh zu produzieren
holzmenge_pro_1mwh = holzmenge_pro_32kwh * stunden_pro_1mwh  # Holzmenge für 1 MWh

# Kohlenstoffgehalt im Holz
kohlenstoffgehalt_holz = 0.50  # 50%

# Berechnung der gesamten Kohlenstoffmenge im Holz für 1 MWh
gesamter_kohlenstoff_pro_1mwh = holzmenge_pro_1mwh * kohlenstoffgehalt_holz

# Umrechnung von Kohlenstoff in CO2
molekulargewicht_c = 12  # Molekulargewicht von Kohlenstoff
molekulargewicht_co2 = 44  # Molekulargewicht von CO2
umrechnungsfaktor_c_zu_co2 = molekulargewicht_co2 / molekulargewicht_c

# Berechnung des freigesetzten Kohlenstoffs (nicht in Pflanzenkohle gebunden)
# Anteil des in Pflanzenkohle gebundenen Kohlenstoffs: 29,18%
freigesetzter_kohlenstoff_pro_1mwh = gesamter_kohlenstoff_pro_1mwh * ((100 - gebundener_kohlenstoff_prozent) / 100)

# Umrechnung des freigesetzten Kohlenstoffs in CO2
co2_pro_1mwh = freigesetzter_kohlenstoff_pro_1mwh * umrechnungsfaktor_c_zu_co2

print(f'== Emissionen pro 1MWh: ==')
print(f'Eingangsmasse Holz: {round(holzmenge_pro_1mwh, 1)} kg')
print(f'Gesamter Kohlenstoff: {round(gesamter_kohlenstoff_pro_1mwh, 1)} kg')
print(f'Freigesetzter: {round(freigesetzter_kohlenstoff_pro_1mwh, 1)} kg')
print(f'CO2 Emissionen: {round(co2_pro_1mwh, 1)} kg')

