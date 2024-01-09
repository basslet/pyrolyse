## Carbon Removal - Beispielrechnung ##

Um die jährliche CO2-Einsparung beim Betrieb von 1000 Pyrolyse-Anlagen zu berechnen, verwenden wir die angegebenen Daten:

1. **Jährliche CO2-Emissionen von Braunkohle**:
   - Emissionen: 1150 g CO2 pro kWh
   - Gesamtleistung pro Pyrolyse Referenz-Anlage: 182 kWh (Strom und Wärme)
   - Jährliche Emissionen pro Braunkohleanlage in kg: 182 kWh * 1.150kg/kWh * 24 Stunden * 365 Tage

2. **Jährliche CO2-Emissionen einer Pyrolyse-Anlage**:
   - Emissionen: 1433.6 kg CO2 pro MWh
   - Jährliche Emissionen pro Pyrolyse-Anlage: 182 * 1.4336 kg/kWh * 24 Stunden/Tag * 365 Tage/Jahr
   - Wir beziehen diese Zahl nicht in der Berechnung ein, da die CO2 Emissionen wie bei Biogas durch den natürlichen Kreislauf gebunden wurden und daher in der Bilanz keine zusätzliche CO2 Belastung darstellen

3. **CO2-Einsparung pro Pyrolyse-Anlage**:
   - Kohlenstoff-Bindung pro kWh: 414 g
   - CO2-Einsparung durch Kohlenstoff-Bindung pro kWh: 1.517 kg
   - Jährliche CO2 Einsparung pro Anlage durch Bindung in kg: 182 * 1.517 kg/kWh * 24 Tage * 365 Tage/Jahr

4. **Gesamte jährliche Einsparung für 1000 Anlagen**:
   - Gesamteinsparung pro Pyrolyse Anlage: Jährliche CO2 Einsparung pro Anlage durch Bindung in kg + Jährliche Emissionen pro Braunkohleanlage in kg
   - Gesamteinsparung pro Pyrolyse Anlage * 1000


Diese Berechnung gibt eine Schätzung der CO2-Einsparung, basierend auf den Emissionen von Pyrolyse-Anlagen im Vergleich zu Braunkohlekraftwerken: [beispiel_1000_anlagen.py](code/beispiel_1000_anlagen.py)

- **Gesamte jährlichen CO2 Einsparung**: 4,253,645.76 t
- **Gesamter jährlicher Holzberbrauch**: 2,566,695,768.0 t
- **Beitrag in Prozent**: 0.000425% der gewünschten 1 Gigatonnen CO2