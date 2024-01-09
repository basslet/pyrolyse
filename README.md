# Pyrolyse Berechnungen #

Stand: 5. Januar 2024


## Übersicht ##
1. [Einleitung Pyrolyse](./README.md#pyrolyse_zusammenfassung)
2. [Meine Learnings](./README.md#meine-learnings-zur-pyrolyse)
2. [Grundlegende Annahmen und Variablen](./annahmen_und_variablen.md)
3. [Pyrolyse und Kohlenstoff Grundlagen Berechnung](./pyrolyse_de.md)
4. Carbon Removal - [Beispielrechnung 1000 dezentrale Anlagen](./beispielrechnung_1000_anlagen.md)
5. [Vergleich zu alternativen EEGs](./alternative_eegs.md) (wip)
6. Problemstellung [wip]
- Kohlenstoffentfernung
- Anlageneffizienz



## Pyrolyse Zusammenfassung ##
Pyrolyse ist ein thermochemischer Prozess, bei dem Biomasse wie Holz in Abwesenheit von Sauerstoff erhitzt wird. Dieser Prozess führt zur Zersetzung des Materials und zur Erzeugung von Pyrolysegas, Teer und Pflanzenkohle. Pyrolysegas kann als Brennstoff zur Energiegewinnung genutzt werden, während Pflanzenkohle Kohlenstoff bindet und als Bodenverbesserer eingesetzt werden kann. Pyrolyse trägt zur Verringerung von CO2-Emissionen bei, indem sie fossile Brennstoffe ersetzt und Kohlenstoff in Form von Pflanzenkohle speichert.

## Wie funktioniert eine Pyrolyse Anlage ##

- [Video zu Funktionsweise](https://youtu.be/BOpEtUhSWm0)
- [Referenz Anlage Clinx 50](https://pyro-power.com/pyro-clinx-system/)

## Warum ist Pyrolyse spannend? ##

Pyrolyse erscheint die einzige Carbon Removal Methode zu sein, die sowohl Energie (Kraft-Wärme-Kopplung) freigibt, als auch Kohlenstoff in fester Form bindet. Da Pyrolyse Energie aus Biomasse generiert, wird demnach kein neuer Kohlenstoff in den CO2 Kreislauf gegeben, sondern durch die Bindung wird CO2 reduziert.

Pyrolyse Anlagen ammortisieren sich durch
- Verkauf von Energie
- CO2 Zertifikate
- Pflanzenkohle

## Was sind die Herausforderungen bei Pyrolyse  ##

- hohe technische Anforderungen
- Biomasse erfordert dezentralen Einsatz, dadurch geringerer Wirkungsgrad als große Kraftwerke
- größere Menge an Eingangsmaterial ggü Kohle oder Erdgas, da der Energiegehalt in Holz niedriger ist als fossile Brennstoffe

## Meine Learnings zur Pyrolyse ##

- Pyrolyse Anlage (Clinx 50) verbraucht ca. 2600 Tonnen Holz pro Jahr (293 kg/h bei 4 kWh/kg)
- Benötigte Waldfläche: 433 Hektar bei 10 Kubikmeter Zuwachs pro Hektar pro Jahr (Zuwachs kann je nach Wald stark variieren)

- Während der Pyrolyse wird 50% des Kohlenstoffs in der Pflanzenkohle gebunden, die restlichen 50% werden wieder freigegeben
- Diese Anlage liefert 32 kWh Strom (netto) und 150 kWh Wärme

**Verbrauch und Emissionen für 1 MWh Strom:**
- Um 1 MWh Strom zu erzeugen, werden etwa 9156,25 kg Holz benötigt.
- Die Gesamtmenge des Kohlenstoffs in diesem Holz beträgt 4578,125 kg.
- Davon werden 2223,7 kg Kohlenstoff (48,6% des gesamten Kohlenstoffs) als Holzgas freigesetzt.
- Diese freigesetzte Kohlenstoffmenge entspricht CO2-Emissionen von etwa 8153 kg pro MWh.
- Im Vergleich erzeugt Kohle ca. 1 Tonne CO2-Emissionen, Erdgas lediglich 0,4 Tonnen CO2 (siehe dazu Notiz am Ende)


**Zugrundeliegende Annahmen:**
- 1 Kubikmeter Holz wiegt je nach Baumart und Feuchtigkeitsgehalt zwischen 0,4 und 0,8 Tonnen. Wir nehmen einen Durchschnittswert von 0,6 Tonnen und einen Kohlenstoff Gehalt von 50%
- Pflanzenkohle hat einen höheren Kohlenstoffgehalt, typischerweise etwa 90%
- Zuwachs in Deutschen Wäldern liegt zwischen 8 und 12 Kubikmeter pro Hektar pro Jahr

**Grundsatzfragen:**
- Wieviel Holz steht realistisch für Pyrolyse zur Verfügung? Holz wird bereits für viele andere Bereiche (Möbel, Hausbau) eingesetzt
- Wie realistisch ist es, die Anlagen zukünftig für ein breiteres Spektrum an Eingangsmaterial (Plastik, Reststoffe) einzusetzen?


### CO2 Gewicht ###
CO2 ist ca. 4 mal schwerer als reiner Kohlenstoff: Die Molekulargewichte von Kohlenstoff (C) und Sauerstoff (O) betragen 12 bzw. 16. Daher hat CO2 (mit einem Kohlenstoff- und zwei Sauerstoffatomen) ein Molekulargewicht von 44. Um die Menge des gebundenen Kohlenstoffs in CO2 umzurechnen, verwenden wir den Faktor 44/12, da CO2 44/12 mal schwerer als reiner Kohlenstoff ist.





Bei der Pyrolyse ist zu beachten, dass immerhin ca. 50% des gespeicherten Kohlenstoffs aus dem Holz auf lange Zeit in Form von Pflanzenkohle gebunden wird, und lediglich 50% des eingehenden Kohlenstoffs dem natürlichen Kreislauf zurück gegeben wird. Der Prozess ist demnach CO2-negativ, da CO2 aus dem Kreislauf entnommen und gebunden wird. Biogas und klassische BHKW sind CO2-neutral, während bei der Verbrennung fossilier Energieträger der gespeicherte Kohlenstoff dem bestehenden Kreislauf _hinzugefügt_ wird.

