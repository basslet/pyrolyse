# Umrechnung von Kohlenstoff in CO2
molekulargewicht_c = 12  # Molekulargewicht von Kohlenstoff
molekulargewicht_co2 = 44  # Molekulargewicht von CO2
umrechnungsfaktor_c_zu_co2 = molekulargewicht_co2 / molekulargewicht_c

# Durchschnittsgewicht von 1 Kubikmeter Holz
gewicht_pro_kubikmeter_holz_tonnen = 0.6  # angenommener Durchschnittswert

# Kohlenstoffgehalt im Holz
kohlenstoffgehalt_holz = 0.50  # 50%

# Szenario 1: 8 Kubikmeter Zuwachs pro Hektar pro Jahr
zuwachs_pro_hektar_pro_jahr_kubikmeter_1 = 8
# Szenario 2: 12 Kubikmeter Zuwachs pro Hektar pro Jahr
zuwachs_pro_hektar_pro_jahr_kubikmeter_2 = 12

# Berechnung der gebundenen Kohlenstoffmenge und der entsprechenden CO2-Menge für beide Szenarien
def berechne_co2_bindung(zuwachs_pro_hektar_pro_jahr_kubikmeter):
    kohlenstoffmenge_tonnen = zuwachs_pro_hektar_pro_jahr_kubikmeter * gewicht_pro_kubikmeter_holz_tonnen * kohlenstoffgehalt_holz
    co2_menge_tonnen = kohlenstoffmenge_tonnen * umrechnungsfaktor_c_zu_co2
    return co2_menge_tonnen

co2_bindung_szenario_1 = berechne_co2_bindung(zuwachs_pro_hektar_pro_jahr_kubikmeter_1)
co2_bindung_szenario_2 = berechne_co2_bindung(zuwachs_pro_hektar_pro_jahr_kubikmeter_2)


print(f'Szenario 1 (8 KubikmZuwachs pro Hektar): {round(co2_bindung_szenario_1, 2)}')
print(f'Szenario 2 (12 KubikmZuwachs pro Hektar): {round(co2_bindung_szenario_2, 2)}')

