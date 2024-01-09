# Pyrolyse Berechnungen

Stand: 5. Januar 2024

## Pyrolyse Zusammenfassung ##
Pyrolyse ist ein thermochemischer Prozess, bei dem Biomasse wie Holz in Abwesenheit von Sauerstoff erhitzt wird. Dieser Prozess führt zur Zersetzung des Materials und zur Erzeugung von Pyrolysegas, Teer und Pflanzenkohle. Pyrolysegas kann als Brennstoff zur Energiegewinnung genutzt werden, während Pflanzenkohle Kohlenstoff bindet und als Bodenverbesserer eingesetzt werden kann. Pyrolyse trägt zur Verringerung von CO2-Emissionen bei, indem sie fossile Brennstoffe ersetzt und Kohlenstoff in Form von Pflanzenkohle speichert.

## Wie funktioniert eine Pyrolyse Anlage ##

- [Video zu Funktionsweise](https://youtu.be/BOpEtUhSWm0)
- [Referenz Anlage Clinx 50](https://pyro-power.com/pyro-clinx-system/)

## Warum finde ich Pyrolyse spannend? ##

Pyrolyse scheint die einzige Carbon Removal Methode zu sein, die sowohl Energie (Kraft-Wärme-Kopplung) freigibt, als auch Kohlenstoff in fester Form bindet. Da Pyrolyse aus Biomasse generiert, wird demnach kein neuer Kohlenstoff in den CO2 Kreislauf gegeben, sondern durch die Bindung wird CO2 reduziert.

Pyrolyse Anlagen ammortisieren sich durch
- Verkauf von Energie
- CO2 Zertifikate
- Pflanzenkohle

## Was sind die Herausforderungen bei Pyrolyse  ##

- hohe technische Anforderungen
- Biomasse erfordert dezentralen Einsatz, dadurch geringerer Wirkungsgrad als große Kraftwerke

## Meine Learnings zur Pyrolyse ##

- Pyrolyse Anlage (Clinx 50) verbraucht ca. 2600 Tonnen Holz pro Jahr (293 kg/h bei 4 kWh/kg)
- Benötigte Waldfläche: 433 Hektar bei 10 Kubikmeter Zuwachs pro Hektar pro Jahr (Zuwachs kann je nach Wald stark variieren)
- Während der Pyrolyse wird 50% des Kohlenstoffs in der Pflanzenkohle gebunden, die restlichen 50% werden freigegeben
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


0. [Grundlegende Annahmen und Variablen](./annahmen_und_variablen.md)
1. [Pyrolyse und Kohlenstoff Grundlagen Berechnung](./pyrolyse_de.md)
2. Carbon Removal - [Beispielrechnung 1000 dezentrale Anlagen](./beispielrechnung_1000_anlagen.md)
3. Problemstellung [wip]
- Kohlenstoffentfernung
- Anlageneffizienz



