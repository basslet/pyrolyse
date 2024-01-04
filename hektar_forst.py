# Jährliche Menge an Holz in Tonnen
holz_pro_woche_tonnen = 50
wochen_pro_jahr = 52
jahresmenge_holz_tonnen = holz_pro_woche_tonnen * wochen_pro_jahr

# Durchschnittliche Dichte von Holz (angenommen)
dichte_holz_tonnen_pro_kubikmeter = 0.6

# Umrechnung der jährlichen Holzmenge in Kubikmeter
jahresmenge_holz_kubikmeter = jahresmenge_holz_tonnen / dichte_holz_tonnen_pro_kubikmeter

# Durchschnittliche Zuwachsrate pro Hektar pro Jahr (angenommen)
zuwachsrate_pro_hektar_pro_jahr_kubikmeter = 10  # Kann je nach Waldtyp variieren

# Benötigte Waldfläche in Hektar
benoetigte_waldflaeche_hektar = jahresmenge_holz_kubikmeter / zuwachsrate_pro_hektar_pro_jahr_kubikmeter

jahresmenge_holz_tonnen, jahresmenge_holz_kubikmeter, benoetigte_waldflaeche_hektar
