# Definieren der gegebenen Werte
co2_einsparung_durch_ersatz_fossiler_energietraeger_g_per_kwh = 1150
gebundener_kohlenstoff_g_per_kwh = 414
leistung_pro_anlage_kwh = 182 # Strom und Wärme; Referenz: Clinx50
anzahl_anlagen = 1000
stunden_pro_jahr = 24 * 365
holzverbrauch_kg_per_kwh = 1.6099

# Umrechnung von Kohlenstoff in CO2
molekulargewicht_c = 12  # Molekulargewicht von Kohlenstoff
molekulargewicht_co2 = 44  # Molekulargewicht von CO2
umrechnungsfaktor_c_zu_co2 = molekulargewicht_co2 / molekulargewicht_c

# Umrechnung des gebundenen Kohlenstoffs in CO2-Einsparung
co2_einsparung_durch_kohlenstoffbindung_g_per_kwh = gebundener_kohlenstoff_g_per_kwh * umrechnungsfaktor_c_zu_co2

# Gesamte CO2-Einsparung pro kWh und pro Anlage pro Jahr
gesamte_co2_einsparung_pro_kwh = co2_einsparung_durch_ersatz_fossiler_energietraeger_g_per_kwh + co2_einsparung_durch_kohlenstoffbindung_g_per_kwh
gesamte_co2_einsparung_pro_anlage_pro_jahr = gesamte_co2_einsparung_pro_kwh * leistung_pro_anlage_kwh * stunden_pro_jahr

# Gesamte jährliche CO2-Einsparung für 1000 Anlagen
gesamte_jaehrliche_co2_einsparung = gesamte_co2_einsparung_pro_anlage_pro_jahr * anzahl_anlagen # in gramm

# Jährlicher Holzverbrauch pro Anlage und für 1000 Anlagen
jahres_holzverbrauch_pro_anlage = holzverbrauch_kg_per_kwh * leistung_pro_anlage_kwh * stunden_pro_jahr
gesamter_jaehrlicher_holzverbrauch = jahres_holzverbrauch_pro_anlage * anzahl_anlagen

print(gesamte_jaehrliche_co2_einsparung/1000/1000) # in Tonnen
print(gesamter_jaehrlicher_holzverbrauch)

gewuenschte_einsparung = 1000000000000 # 1 Gigatonne