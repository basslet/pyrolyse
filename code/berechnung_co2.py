from pyrolyse import helper
h = helper()

# Gesamter CO2-Ausstoß in Deutschland in 2021
gesamt_strom_kwh = 489e9  # in kWh
gesamt_co2_ausstoss_t = 762e6  # in Tonnen

# Anteil der Energiewirtschaft am gesamten CO2-Ausstoß
anteil_energiewirtschaft = 0.34

# CO2-Emissionen der Energiewirtschaft
co2_energiewirtschaft_t = gesamt_co2_ausstoss_t * anteil_energiewirtschaft

# Anteile der CO2-neutralen Energieerzeuger innerhalb der Energiewirtschaft
anteil_windkraft = 0.25
anteil_solar = 0.104
anteil_biomasse = 0.093
anteil_wasserkraft = 0.037
theoretischer_anteil_clinx = 3066e6/gesamt_strom_kwh # Leistung 1000 Clinx 150 / gesamt_strom

# Berechnung der CO2-Einsparungen pro Energieerzeuger
co2_einsparung_windkraft_t = co2_energiewirtschaft_t * anteil_windkraft
co2_einsparung_solar_t = co2_energiewirtschaft_t * anteil_solar
co2_einsparung_biomasse_t = co2_energiewirtschaft_t * anteil_biomasse
co2_einsparung_wasserkraft_t = co2_energiewirtschaft_t * anteil_wasserkraft
co2_einsparung_clinx_t = co2_energiewirtschaft_t * theoretischer_anteil_clinx
co2_bindung_clinx_t = 3155102 # t


dict = {'Windkraft':[anteil_windkraft,co2_einsparung_windkraft_t],
        'Solar':[anteil_solar,co2_einsparung_solar_t],
        'Biomasse':[anteil_biomasse,co2_einsparung_biomasse_t],
        'Wasserkraft':[anteil_wasserkraft,co2_einsparung_wasserkraft_t],
        'Pyrolyse':[theoretischer_anteil_clinx,co2_einsparung_clinx_t]}



gesamt_einsparung = co2_einsparung_windkraft_t + co2_einsparung_solar_t + co2_einsparung_biomasse_t + co2_einsparung_wasserkraft_t + co2_einsparung_clinx_t

# table header
print('|Typ|Anteil|Einsparung|% ohne CR|% mit CR|')
print('|---|---|---|---|---|')
# data
for k, v in dict.items():
    anteil = h.smart_format(v[0]*100, '%')
    einsparung = h.smart_format(v[1], 't')
    prozentual = h.smart_format(v[1]/gesamt_einsparung*100, '%')
    prozent_mit_cr = prozentual
    if k == 'Pyrolyse':
        prozent_mit_cr = h.smart_format((v[1]+co2_bindung_clinx_t)/gesamt_einsparung*100, '%')

    print(f'|{k}|{anteil}|{einsparung}|{prozentual}|{prozent_mit_cr}|')

