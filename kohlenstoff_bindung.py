# Berechnung des gebundenen und freigesetzten Kohlenstoffs

# Kohlenstoffgehalt im Holz und in der Pflanzenkohle
kohlenstoffgehalt_holz = 0.50  # 50%
kohlenstoffgehalt_biokohle = 0.75  # 75%

# Holz- und Pflanzenkohlenmenge
holzmenge_kg_h = 293  # kg/h
biokohlenmenge_kg_h = 57  # kg/h

# Kohlenstoff im Holz
kohlenstoff_holz_kg_h = holzmenge_kg_h * kohlenstoffgehalt_holz

# Kohlenstoff in der Pflanzenkohle
kohlenstoff_biokohle_kg_h = biokohlenmenge_kg_h * kohlenstoffgehalt_biokohle

# Prozentualer Anteil des gebundenen Kohlenstoffs
gebundener_kohlenstoff_prozent = (kohlenstoff_biokohle_kg_h / kohlenstoff_holz_kg_h) * 100

# Prozentualer Anteil des freigesetzten Kohlenstoffs
freigesetzter_kohlenstoff_prozent = 100 - gebundener_kohlenstoff_prozent

gebundener_kohlenstoff_prozent, freigesetzter_kohlenstoff_prozent
