import marimo

__generated_with = "0.1.76"
app = marimo.App(width="full")


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __():
    import sys
    import copy

    sys.path.insert(0, './code/')
    from pyrolyse import EnergieGewinnung, EnergieTraeger, helper
    return EnergieGewinnung, EnergieTraeger, copy, helper, sys


@app.cell
def __(helper):
    # Init
    h = helper()
    return h,


@app.cell
def __(EnergieTraeger):
    holz = EnergieTraeger(
        energie_gehalt = 4250, # kWh
        kohlenstoff_gehalt = 50, # Prozent
        dichte_kg_pro_kubikmeter = 600, # kg, Durchschnitt
        zuwachsrate = 10, # Kubikmeter Zuwachs pro Hektar pro Jahr
        name="Holz")
    return holz,


@app.cell
def __(EnergieGewinnung, holz):
    # Erstellen einer Instanz der Klasse EnergieGewinnung
    clinx50 = EnergieGewinnung(
        eingangsmasse_pro_h = 295,
        ausgangs_energie_strom = 32,
        ausgangs_energie_waerme = 150,
        ratio_eingangsmasse_zu_pflanzenkohle = 1/3.5,
        kohlenstoffgehalt_pflanzenkohle = 90,
        anlagen_name='Clinx 50',
        energie_klasse=holz,
        anzahl_anlagen=1
    )
    return clinx50,


@app.cell
def __(EnergieGewinnung, holz):
    clinx150 = EnergieGewinnung(
        eingangsmasse_pro_h = 382,
        ausgangs_energie_strom = 100,
        ausgangs_energie_waerme = 250,
        ratio_eingangsmasse_zu_pflanzenkohle = 1/3.5,
        kohlenstoffgehalt_pflanzenkohle = 90,
        anlagen_name='Clinx 150',
        energie_klasse=holz,
        anzahl_anlagen=1
    )
    return clinx150,


@app.cell
def __(clinx50, mo):
    mo.md(clinx50.bericht(1))
    return


@app.cell
def __(clinx50, h, mo):
    mo.md(clinx50.bericht(h.stunden_pro_jahr))
    return


@app.cell
def __(clinx150, mo):
    mo.md(clinx150.bericht(1))
    return


@app.cell
def __(clinx150, h, mo):
    mo.md(clinx150.bericht(h.stunden_pro_jahr))
    return


@app.cell
def __(clinx50, copy, h, mo):
    clinx50_1000 = copy.copy(clinx50)
    clinx50_1000.anzahl_anlagen = 1000
    mo.md(clinx50_1000.bericht(h.stunden_pro_jahr))
    return clinx50_1000,


@app.cell
def __(clinx150, copy, h, mo):
    clinx150_1000 = copy.copy(clinx150)
    clinx150_1000.anzahl_anlagen = 1000
    mo.md(clinx150_1000.bericht(h.stunden_pro_jahr))
    return clinx150_1000,


@app.cell(hide_code=True)
def __(mo):
    strom_eur_slider = mo.ui.slider(value=0.08, start=0, stop= 0.25, step=0.01)
    waerme_eur_slider = mo.ui.slider(value=0.08, start=0, stop= 0.25, step=0.01)
    pflanzenkohle_eur_slider = mo.ui.slider(value=0.1*0.3, start=0, stop= 2.0, step=0.1)
    co2_zertifikat_eur_slider = mo.ui.slider(value=0.05, start=0, stop= 0.5, step=0.01)

    mo.md(
        f"""
        Strom Euro pro kWh : {strom_eur_slider} 

        Wärme Euro pro kwh : {waerme_eur_slider}

        Pflanzenkohle Euro pro kg: {pflanzenkohle_eur_slider} 70% Marge und Steuer

        CO2 Zertifikat Euro pro kg: {co2_zertifikat_eur_slider}

        - Der Preis für CO2-Zertifikate in Europa, die im Rahmen des EU-Emissionshandelssystems (EU ETS) gehandelt werden, variiert ständig, ähnlich wie Aktienkurse. Zum Stand meines letzten Trainings im April 2023 lagen die Preise für CO2-Zertifikate in der Regel zwischen 50 und 90 Euro pro Tonne CO2. Es ist jedoch wichtig zu beachten, dass diese Preise Schwankungen unterliegen, basierend auf Marktdynamiken, politischen Entscheidungen und anderen Faktoren.
        - Statista: Während der Preis für ein CO2-Zertifikat im EU Emissions Trading System (EU-ETS) in 2007 noch durchschnittlich bei etwa 0,70 Euro lag, stieg er bis 2022² auf durchschnittlich ca. 81 Euro an.
        """
    )
    return (
        co2_zertifikat_eur_slider,
        pflanzenkohle_eur_slider,
        strom_eur_slider,
        waerme_eur_slider,
    )


@app.cell(hide_code=True)
def __(
    clinx50_1000,
    co2_zertifikat_eur_slider,
    helper,
    mo,
    pflanzenkohle_eur_slider,
    strom_eur_slider,
    waerme_eur_slider,
):
    mo.md(
        helper.amortisation(
            strom_eur_slider.value,
            waerme_eur_slider.value,
            pflanzenkohle_eur_slider.value,
            co2_zertifikat_eur_slider.value,
            clinx50_1000
        )
    )
    return


@app.cell(hide_code=True)
def __(
    clinx150_1000,
    co2_zertifikat_eur_slider,
    helper,
    mo,
    pflanzenkohle_eur_slider,
    strom_eur_slider,
    waerme_eur_slider,
):
    mo.md(
        helper.amortisation(
            strom_eur_slider.value,
            waerme_eur_slider.value,
            pflanzenkohle_eur_slider.value,
            co2_zertifikat_eur_slider.value,
            clinx150_1000
        )
    )
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
