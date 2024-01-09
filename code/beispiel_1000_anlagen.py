
def einsparung_pro_anlage_pro_tage(anzahl_anlagen=1000, anzahl_tage = 365):
    # Definieren der gegebenen Werte
    co2_einsparung_durch_ersatz_fossiler_energietraeger_g_per_kwh = 1150  # g CO2 pro kWh
    gebundener_kohlenstoff_g_per_kwh = 414  # g Kohlenstoff pro kWh
    leistung_pro_anlage_kwh = 182  # kWh

    stunden_pro_jahr = 24 * anzahl_tage  # Stunden
    holzverbrauch_kg_per_kwh = 1.6099  # kg pro kWh

    # Umrechnung von Kohlenstoff in CO2
    molekulargewicht_c = 12  # Molekulargewicht von Kohlenstoff
    molekulargewicht_co2 = 44  # Molekulargewicht von CO2
    umrechnungsfaktor_c_zu_co2 = molekulargewicht_co2 / molekulargewicht_c

    # Umrechnung des gebundenen Kohlenstoffs in CO2-Einsparung
    co2_einsparung_durch_kohlenstoffbindung_g_per_kwh = gebundener_kohlenstoff_g_per_kwh * umrechnungsfaktor_c_zu_co2

    # Gesamte CO2-Einsparung pro kWh und pro Anlage pro Jahr
    gesamte_co2_einsparung_pro_kwh = co2_einsparung_durch_ersatz_fossiler_energietraeger_g_per_kwh + co2_einsparung_durch_kohlenstoffbindung_g_per_kwh
    gesamte_co2_einsparung_pro_anlage_pro_jahr = gesamte_co2_einsparung_pro_kwh * leistung_pro_anlage_kwh * stunden_pro_jahr

    # Umrechnung von Gramm in Tonnen
    gesamte_co2_einsparung_pro_anlage_pro_jahr_tonnen = gesamte_co2_einsparung_pro_anlage_pro_jahr / 1e6

    # Gesamte jährliche CO2-Einsparung für 1000 Anlagen in Tonnen
    gesamte_jaehrliche_co2_einsparung_tonnen = gesamte_co2_einsparung_pro_anlage_pro_jahr_tonnen * anzahl_anlagen

    # Jährlicher Holzverbrauch pro Anlage und für 1000 Anlagen
    jahres_holzverbrauch_pro_anlage = holzverbrauch_kg_per_kwh * leistung_pro_anlage_kwh * stunden_pro_jahr
    gesamter_jaehrlicher_holzverbrauch = jahres_holzverbrauch_pro_anlage * anzahl_anlagen

    return gesamte_jaehrliche_co2_einsparung_tonnen, gesamter_jaehrlicher_holzverbrauch

gesamte_jaehrliche_co2_einsparung_tonnen, gesamter_jaehrlicher_holzverbrauch = einsparung_pro_anlage_pro_tage()

print(f'Gesamte jährlichen CO2 Einsparung: {round(gesamte_jaehrliche_co2_einsparung_tonnen,2)} t') # in Tonnen
print(f'Gesamter jährlicher Holzberbrauch: {gesamter_jaehrlicher_holzverbrauch} t')

gewuenschte_einsparung = 1000000000000 # 1 Gigatonne
beitrag_in_prozent = round(gesamte_jaehrliche_co2_einsparung_tonnen / 1000000000000, 8) * 100
print(f'Beitrag in Prozent: {beitrag_in_prozent}%')
