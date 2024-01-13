## Erneuerbare Energie Gewinnung in Deutschland ##


- https://strom-report.com/strommix/
- https://strom-report.com/windenergie/
- https://www.bmwk.de/Redaktion/DE/Pressemitteilungen/2022/03/20220315-treibhausgasemissionen-stiegen-2021-um-45-prozent.html
- https://www.ise.fraunhofer.de/de/presse-und-medien/presseinformationen/2023/nettostromerzeugung-in-deutschland-2022-wind-und-photovoltaik-haben-deutlich-zugelegt.html


Gesamter CO2-Ausstoß in Deutschland in 2021: 762 Millionen Tonnen
Anteil der Energiewirtschaft: 34%

CO2-Emissionen der Energiewirtschaft:
- 762 Mio. t CO2 x 0.34 =

Anteile der CO2-neutralen Energieerzeuger:
- Windkraft: 25%
- Solarstrom: 10.4%
- Biomasse: 9.3%
- Wasserkraft: 3.7%

Berechnung der CO2-Einsparungen pro Energieerzeuger:
- CO2-Einsparung durch Windkraft:
  259.08 Mio. t CO2  x 0.25 = 64.77 Mio. t CO2
- CO2-Einsparung durch Solarstrom:
  259.08 Mio. t CO2  x 0.104 = 26.94 Mio. t CO2
- CO2-Einsparung durch Biomasse:
  259.08 Mio. t CO2  x 0.093 = 24.09 Mio. t CO2
- CO2-Einsparung durch Wasserkraft:
  259.08 Mio. t CO2 x 0.037 = 9.59 Mio. t CO2
- CO2-Einsparung durch 1000 Clinx 150 Kraftwerke:
  259.08 Mio. t CO2 x 33,066 TWh / 489 TWh Gesamstrom = 1,624 t CO2

Diese Werte geben an, wie viele Tonnen CO2 in 2021 durch den Einsatz der jeweiligen erneuerbaren Energieerzeuger in der Energiewirtschaft Deutschlands eingespart wurden. [> code](./code/berechnung_co2.py)


Folgende Tabelle zeigt sowohl CO2 Einsparung als CO2 Impakt durch Carbon Removal (CR):

Annahme: 1000 Clinx 150 Kraftwerke für Pyrolyse. Die Berechnung der CO2 Reduktion durch Carbon Removal ergab 3,155,101,714 kg (3,155,102 t) pro Jahr für 1000 BHKW.

|Typ|Anteil|Einsparung|% ohne CR|% mit CR|
|---|---|---|---|---|
|Windkraft|25 %|64,770,000 t|51 %|51 %|
|Solar|10 %|26,944,320 t|21 %|21 %|
|Biomasse|9 %|24,094,440 t|19 %|19 %|
|Wasserkraft|4 %|9,585,960 t|8 %|8 %|
|Pyrolyse|1 %|1,624,416 t|1 %|4 %|