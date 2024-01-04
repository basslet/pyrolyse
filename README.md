# pyrolyse




## Holzzuwachs pro Hektar und Bedarf einer Pyrolyse BHKW (Beispiel Clinx 50) ##

Die Menge des Holzes, die ein Wald nachhaltig produzieren kann, hängt von vielen Faktoren ab, darunter die Art des Waldes, die Baumarten, das Klima, die Bodenbeschaffenheit und die Waldbewirtschaftungspraktiken. Ein Schlüsselfaktor ist die sogenannte "Zuwachsrate", die angibt, wie viel Holz pro Jahr pro Hektar wächst.

In gemäßigten Breiten wie in Deutschland kann die jährliche Zuwachsrate für gut bewirtschaftete Wälder je nach Baumart und Standort zwischen 8 und 12 Kubikmeter pro Hektar liegen. Für eine genauere Schätzung benötigt man jedoch spezifische Daten über den Wald und die Baumarten.

Um die notwendige Waldfläche für eine nachhaltige Produktion von 50 Tonnen Holz pro Woche zu schätzen, können wir folgende Berechnung durchführen:

1. Zuerst müssen wir die jährliche Menge an Holz berechnen, die produziert werden muss.
2. Dann verwenden wir eine durchschnittliche Zuwachsrate, um die benötigte Waldfläche zu schätzen.

Ein Kubikmeter Holz wiegt je nach Baumart und Feuchtigkeitsgehalt zwischen 0,4 und 0,8 Tonnen. Ich werde eine durchschnittliche Dichte von 0,6 Tonnen pro Kubikmeter für die Berechnung verwenden. Lassen Sie uns diese Berechnungen durchführen.

Um nachhaltig 50 Tonnen Holz pro Woche zu erforsten, benötigt man unter den Annahmen einer durchschnittlichen Holzdichte von 0,6 Tonnen pro Kubikmeter und einer Zuwachsrate von 10 Kubikmetern pro Hektar pro Jahr etwa 433 Hektar Wald. 

Hier ist die Berechnung: https://github.com/basslet/pyrolyse/blob/main/hektar_forst.py

- Jährlicher Bedarf: 2600 Tonnen Holz (50 Tonnen pro Woche über 52 Wochen).
- Umrechnung in Kubikmeter: Etwa 4333 Kubikmeter Holz pro Jahr (bei 0,6 Tonnen pro Kubikmeter).
- Benötigte Waldfläche: Ungefähr 433 Hektar, basierend auf einer Zuwachsrate von 10 Kubikmetern pro Hektar pro Jahr.

Diese Schätzung basiert auf Durchschnittswerten. Die tatsächlichen Werte können je nach Art des Waldes, den Baumarten und lokalen Bedingungen variieren.


## CO2 Bindung durch Holzzuwachs ##

Um zu berechnen, wie viel CO2 durch den Holzzuwachs in Wäldern gebunden und gespeichert wird, müssen wir ein paar Schritte durchlaufen:

1. **Bestimmung der Kohlenstoffmenge im Holz**: Durchschnittlich besteht trockenes Holz zu etwa 50% aus Kohlenstoff. Diese Zahl kann je nach Holzart und Feuchtigkeitsgehalt variieren.

2. **Umrechnung von Kohlenstoff in CO2**: Die Molekulargewichte von Kohlenstoff (C) und Sauerstoff (O) betragen 12 bzw. 16. Daher hat CO2 (mit einem Kohlenstoff- und zwei Sauerstoffatomen) ein Molekulargewicht von 44. Um die Menge des gebundenen Kohlenstoffs in CO2 umzurechnen, verwenden wir den Faktor 44/12, da CO2 44/12 mal schwerer als reiner Kohlenstoff ist.

3. **Berechnung der CO2-Bindung basierend auf dem Holzzuwachs**: Wir werden zwei Szenarien betrachten, einmal mit 8 Kubikmetern und einmal mit 12 Kubikmetern Zuwachs pro Hektar pro Jahr.

Angenommen, 1 Kubikmeter Holz wiegt durchschnittlich etwa 0,6 Tonnen (dies kann je nach Holzart und Wassergehalt variieren), dann können wir die gebundene Kohlenstoffmenge und die entsprechende CO2-Menge berechnen. Lassen Sie uns diese Berechnungen durchführen.

Basierend auf den Berechnungen: https://github.com/basslet/pyrolyse/blob/main/holzzuwachs-co2.py

1. Bei einem jährlichen Holzzuwachs von 8 Kubikmetern pro Hektar bindet der Wald ungefähr 8,8 Tonnen CO2 pro Hektar pro Jahr.
2. Bei einem jährlichen Holzzuwachs von 12 Kubikmetern pro Hektar bindet der Wald etwa 13,2 Tonnen CO2 pro Hektar pro Jahr.

Diese Werte zeigen die Menge an CO2, die durch den Holzzuwachs in Wäldern gebunden und gespeichert wird. Sie basieren auf der Annahme, dass 1 Kubikmeter Holz durchschnittlich 0,6 Tonnen wiegt und zu 50% aus Kohlenstoff besteht.

## Verhältnis von Kohlenstoff Bindung in Pflanzenkohle und freigesetzter Kohlenstoff ##

Um zu berechnen, wie viel Prozent des Kohlenstoffs aus dem Holz in Form von Pflanzenkohle gebunden wird und wie viel in die Atmosphäre freigesetzt wird, müssen wir einige Annahmen über den Kohlenstoffgehalt des Holzes und der Pflanzenkohle treffen.

1. **Kohlenstoffgehalt des Holzes**: Holz besteht typischerweise zu etwa 50% aus Kohlenstoff. Dieser Wert kann je nach Holzart leicht variieren.

2. **Kohlenstoffgehalt der Pflanzenkohle**: Pflanzenkohle hat einen höheren Kohlenstoffgehalt, typischerweise etwa 70-80%.

Mit diesen Annahmen können wir den Kohlenstoffgehalt im Eingangsmaterial (Holz) und im Ausgangsmaterial (Pflanzenkohle) berechnen und daraus ableiten, wie viel Prozent des Kohlenstoffs gebunden bzw. freigesetzt wird.

Zuerst berechnen wir den Kohlenstoffgehalt im Holz:

- Holzmenge: 293 kg/h
- Kohlenstoffgehalt im Holz: 50%
- Kohlenstoff im Holz: 293 kg/h * 50% = 146,5 kg/h

Dann berechnen wir den Kohlenstoffgehalt in der Pflanzenkohle:

- Pflanzenkohlenmenge: 57 kg/h
- Kohlenstoffgehalt in der Pflanzenkohle: angenommen 75%
- Kohlenstoff in der Pflanzenkohle: 57 kg/h * 75% = 42,75 kg/h

Nun können wir den Prozentsatz des in der Pflanzenkohle gebundenen Kohlenstoffs berechnen:

- Gebundener Kohlenstoff: (Kohlenstoff in der Pflanzenkohle / Kohlenstoff im Holz) * 100%

Und den Prozentsatz des in die Atmosphäre freigesetzten Kohlenstoffs:

- Freigesetzter Kohlenstoff: 100% - Prozent des gebundenen Kohlenstoffs

Die Berechnungen: https://github.com/basslet/pyrolyse/blob/main/kohlenstoff_bindung.py

Aus den gegebenen Daten ergibt sich, dass etwa 29,18% des Kohlenstoffs aus dem Holz in Form von Pflanzenkohle gebunden werden. Die verbleibenden etwa 70,82% des Kohlenstoffs aus dem Holz werden freigesetzt, wahrscheinlich größtenteils in die Atmosphäre.




## CO2 Emmissionen bei der Stromproduktion eines Pyrolyse-BHKW ##

Um die CO2-Emissionen bei der Stromproduktion eines Pyrolyse-Blockheizkraftwerks (BHKW) mit den angegebenen Spezifikationen zu berechnen, müssen wir zunächst die Kohlenstofffreisetzung aus dem verbrannten Holzgas ermitteln und diese dann in CO2-Emissionen umrechnen.

1. **Kohlenstofffreisetzung aus dem Holzgas**:
   - Basierend auf der vorherigen Berechnung, werden etwa 29,18% des Kohlenstoffs aus dem Holz in Pflanzenkohle gebunden. Das bedeutet, dass 70,82% des Kohlenstoffs in Form von Holzgas freigesetzt werden.
   - Die Menge des Holzes ist 293 kg/h, und wir nehmen an, dass Holz zu etwa 50% aus Kohlenstoff besteht.

2. **Umrechnung von Kohlenstoff in CO2**:
   - Die Molekulargewichte von Kohlenstoff (C) und Sauerstoff (O) betragen 12 bzw. 16, daher hat CO2 ein Molekulargewicht von 44. Um die Menge des freigesetzten Kohlenstoffs in CO2 umzurechnen, verwenden wir den Faktor 44/12.

3. **Berechnung der CO2-Emissionen pro MWh**:
   - Die elektrische Nettoleistung des BHKW beträgt 32 kW, und der elektrische Wirkungsgrad ist 19%. Dies bedeutet, dass zur Erzeugung von 1 MWh Strom eine erhebliche Menge an Holz verbrannt werden muss.

Zur Berechnung: https://github.com/basslet/pyrolyse/blob/main/co2_1mwh_pyrolyse.py

Beginnen wir mit der Berechnung des Kohlenstoffgehalts im Holz und der daraus resultierenden CO2-Emissionen. Anschließend berechnen wir, wie viel CO2 pro erzeugter MWh Strom freigesetzt wird.

Bei der Produktion von 1 MWh Strom durch ein Pyrolyse-Blockheizkraftwerk (BHKW) mit den angegebenen Spezifikationen entstehen ungefähr 11.888 kg CO2. 

Diese Berechnung basiert auf der Annahme, dass 70,82% des Kohlenstoffs aus dem Holz freigesetzt werden und die elektrische Nettoleistung des BHKW 32 kW mit einem elektrischen Wirkungsgrad von 19% beträgt.




## Überprüfung ##

Lassen Sie uns die Berechnung überprüfen und korrigieren.

Wir haben festgestellt, dass durch die Zunahme des Holzvorrats jährlich zusätzlich 1,1 Tonnen Kohlenstoff pro Hektar gespeichert werden, was etwa 4,03 Tonnen CO2 entspricht. Dies impliziert, dass nicht alle Kohlenstoffatome im Holz in CO2 umgewandelt werden, da ein Teil als Kohlenstoff in der Biomasse gebunden bleibt.

Für die Berechnung der CO2-Emissionen bei der Stromerzeugung durch Pyrolyse sollten wir berücksichtigen, dass nur der nicht in Pflanzenkohle gebundene Kohlenstoff freigesetzt wird. Die ursprüngliche Annahme, dass 70,82% des Kohlenstoffs aus dem Holz freigesetzt werden, ist möglicherweise zu hoch. Wir sollten die tatsächliche Menge an Kohlenstoff, die in das Holzgas übergeht und dann verbrannt wird, genauer berechnen.

Lassen Sie uns die Berechnung mit den genauen Mengen von Holz, das verbrannt wird, und der Menge an Kohlenstoff, die tatsächlich freigesetzt wird, erneut durchführen.

Nach der Überprüfung und Korrektur der Berechnungen erhalten wir die folgenden Ergebnisse für die Pyrolyse-BHKW-Stromproduktion:

- Um 1 MWh Strom zu erzeugen, werden etwa 9156,25 kg Holz benötigt.
- Die Gesamtmenge des Kohlenstoffs in diesem Holz beträgt 4578,125 kg.
- Davon werden 3242,23 kg Kohlenstoff (70,82% des gesamten Kohlenstoffs) als Holzgas freigesetzt.
- Diese freigesetzte Kohlenstoffmenge entspricht CO2-Emissionen von etwa 11.888 kg (oder 11,888 Tonnen) pro MWh.

Berechnung: https://github.com/basslet/pyrolyse/blob/main/ueberpruefung_co2_pro_mwh.py

Die Berechnung zeigt, dass trotz des relativ hohen Wirkungsgrades des Pyrolyseverfahrens bei der Umwandlung von Holz in Energie, immer noch eine erhebliche Menge an CO2 freigesetzt wird. Es ist wichtig zu betonen, dass diese Berechnung von spezifischen Annahmen und Durchschnittswerten ausgeht und die tatsächlichen Emissionen je nach der Effizienz des spezifischen Pyrolyse-Prozesses und den Eigenschaften des verwendeten Holzes variieren können.

