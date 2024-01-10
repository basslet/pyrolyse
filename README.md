# Pyrolyse Berechnungen #

Stand: 10. Januar 2024


## Übersicht ##
1. [Einleitung Pyrolyse](./README.md#einleitung-pyrolyse)
2. [Meine Learnings](./README.md#meine-learnings-zur-pyrolyse)
2. [Grundlegende Annahmen und Variablen](./annahmen_und_variablen.md)
3. [Pyrolyse und Kohlenstoff Grundlagen Berechnung](./pyrolyse_de.md)
4. [Beispielrechnung Clinx50 und Clinx150](./beispielrechnungen_clinx.md)
5. [Amortisation](./amortisation.md) (wip)
6. Problemstellung [wip]
- Kohlenstoffentfernung
- Anlageneffizienz
7. [Business Modell Optionen](./business_modell_optionen.md) [WIP]


## Einleitung Pyrolyse ##
Pyrolyse ist ein thermochemischer Prozess, bei dem Biomasse wie Holz in Abwesenheit von Sauerstoff erhitzt wird. Dieser Prozess führt zur Zersetzung des Materials und zur Erzeugung von Pyrolysegas, Teer und Pflanzenkohle. Pyrolysegas kann als Brennstoff zur Energiegewinnung genutzt werden, während Pflanzenkohle Kohlenstoff bindet und als Bodenverbesserer eingesetzt werden kann. Pyrolyse trägt zur Verringerung von CO2-Emissionen bei, indem sie fossile Brennstoffe ersetzt und Kohlenstoff in Form von Pflanzenkohle speichert.

## Wie funktioniert eine Pyrolyse Anlage ##

- [Video zu Funktionsweise](https://youtu.be/BOpEtUhSWm0)
- [Referenz Anlage Clinx 50](https://pyro-power.com/pyro-clinx-system/)

## Warum ist Pyrolyse spannend? ##

Pyrolyse gilt als eine der wenigen Carbon-Removal-Methoden, die Energie durch Kraft-Wärme-Kopplung freisetzt und gleichzeitig Kohlenstoff in fester Form bindet. Da Pyrolyse Energie aus Biomasse gewinnt, führt sie keinen neuen Kohlenstoff in den CO2-Kreislauf ein. Stattdessen trägt sie zur CO2-Reduzierung bei, indem sie Kohlenstoff in Pflanzenkohle bindet.

Pyrolyse-Anlagen können sich durch verschiedene Wege amortisieren:
- Verkauf von Energie (Strom und Wärme)
- Handel mit generierten CO2-Zertifikaten
- Verkauf von Pflanzenkohle

## Was sind die Herausforderungen in der Pyrolyse  ##

Die Pyrolyse als Verfahren zur Energiegewinnung und Kohlenstoffbindung aus Biomasse stellt verschiedene Herausforderungen dar:

- **Hohe technische Anforderungen für einen effizienten Betrieb**: Pyrolyseanlagen erfordern präzise Steuerung und fortgeschrittene Technologie, um einen reibungslosen und effizienten Betrieb sicherzustellen.
- **Notwendigkeit von homogenem Eingangsmaterial**: Die Qualität und Homogenität des Eingangsmaterials, typischerweise Holz oder andere Biomasse, beeinflusst maßgeblich die Effizienz des Pyrolyseprozesses.
- **Dezentraler Einsatz der Biomasse**: Aufgrund des meist regionalen Anfalls von Biomasse ist ein dezentraler Einsatz der Pyrolyseanlagen erforderlich. Dies kann zu einem geringeren Wirkungsgrad im Vergleich zu großen, zentralisierten Kraftwerken führen.
- **Größerer Materialbedarf im Vergleich zu fossilen Brennstoffen**: Biomasse wie Holz weist einen niedrigeren Energiegehalt im Vergleich zu fossilen Brennstoffen wie Kohle oder Erdgas auf. Dies erfordert größere Mengen an Eingangsmaterial, um die gleiche Energiemenge zu erzeugen.


## Meine Learnings zur Pyrolyse ##

- Pyrolyse Anlage (Clinx 50) verbraucht ca. 2600 Tonnen Holz pro Jahr (293 kg/h bei 4 kWh/kg)
- Benötigte Waldfläche für nachhaltige Gewinnung: 433 Hektar bei 10 Kubikmeter Zuwachs pro Hektar pro Jahr (Zuwachs kann je nach Wald stark variieren)
- Während der Pyrolyse wird 50% des Kohlenstoffs in der Pflanzenkohle gebunden, die restlichen 50% werden wieder freigegeben
- Diese Anlage liefert 32 kWh Strom (netto) und 150 kWh Wärme

**Verbrauch und Emissionen für 1 MWh Strom:**
- Um 1 MWh Strom zu erzeugen, werden etwa 9156,25 kg Holz benötigt.
- Die Gesamtmenge des Kohlenstoffs in diesem Holz beträgt 4578,125 kg.
- Davon werden 2223,7 kg Kohlenstoff (48,6% des gesamten Kohlenstoffs) als Holzgas freigesetzt.
- Diese freigesetzte Kohlenstoffmenge entspricht CO2-Emissionen von etwa 8153 kg pro MWh.
- Im Vergleich erzeugt Kohle ca. 1 Tonne CO2-Emissionen, Erdgas lediglich 0,4 Tonnen CO2
  - Referenzen zur Energiegewinnung und Emissionen sind nicht eindeutig, beispielsweise ist bei der Relation Energiegewinnung zu Emission unklar, ob sich die Werte auf die brutto oder netto Energiegewinnung beziehen, ob Abwärme mit einbezogen wurde, etc. Es fehlt ein klarer Standard. Das macht den Vergleich unterschiedlicher Energieträger um ein Vielfaches schwieriger.


**Zugrundeliegende Annahmen:**
- 1 Kubikmeter Holz wiegt je nach Baumart und Feuchtigkeitsgehalt zwischen 0,4 und 0,8 Tonnen. Wir nehmen einen Durchschnittswert von 0,6 Tonnen und einen Kohlenstoff Gehalt von 50%
- Pflanzenkohle hat einen höheren Kohlenstoffgehalt, typischerweise etwa 90%
- Zuwachs in Deutschen Wäldern liegt zwischen 8 und 12 Kubikmeter pro Hektar pro Jahr

**Grundsatzfragen:**
- Wieviel Holz steht realistisch für Pyrolyse zur Verfügung? Holz wird bereits für viele andere Bereiche (Möbel, Hausbau) eingesetzt
  - Der Deutsche Forstbestand nimmt zu - wieviel kg Holz stehen zur Energiegewinnung zur Verfügung
- Wie realistisch ist es, die Anlagen zukünftig für ein breiteres Spektrum an Eingangsmaterial (Plastik, Reststoffe) einzusetzen?


### CO2 Gewicht ###
CO2 ist ca. 4 mal schwerer als reiner Kohlenstoff: Die Molekulargewichte von Kohlenstoff (C) und Sauerstoff (O) betragen 12 bzw. 16. Daher hat CO2 (mit einem Kohlenstoff- und zwei Sauerstoffatomen) ein Molekulargewicht von 44. Um die Menge des gebundenen Kohlenstoffs in CO2 umzurechnen, verwenden wir den Faktor 44/12, da CO2 44/12 mal schwerer als reiner Kohlenstoff ist.




Beim Pyrolyseprozess ist hervorzuheben, dass etwa 50% des im Holz gespeicherten Kohlenstoffs dauerhaft in Form von Pflanzenkohle gebunden werden. Damit wird nur die Hälfte des ursprünglichen Kohlenstoffs an den natürlichen Kreislauf zurückgegeben. Dies macht den Prozess effektiv CO2-negativ, da CO2 aktiv aus dem Kreislauf entfernt und gespeichert wird. Im Gegensatz dazu gelten Biogas und konventionelle Blockheizkraftwerke (BHKW) als CO2-neutral, da sie keinen zusätzlichen Kohlenstoff in den Kreislauf einführen. Bei der Verbrennung fossiler Energieträger hingegen wird gespeicherter Kohlenstoff freigesetzt und damit dem bestehenden CO2-Kreislauf hinzugefügt.

