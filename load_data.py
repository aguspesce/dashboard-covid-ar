import pandas as pd


def load_data(url):
    data = pd.read_csv(url, parse_dates=["fecha"], dayfirst=True)
    # Elimino columnas
    data = data.drop(
        [
            "dia_inicio",
            "dia_cuarentena_dnu260",
            "osm_admin_level_2",
            "osm_admin_level_8",
            "test_RT-PCR_negativos",
            "test_RT-PCR_total",
            "transmision_tipo",
            "informe_tipo",
            "informe_link",
            "observacion",
            "covid19argentina_admin_level_4",
            "tot_recuperados",
            "tot_terapia",
            "tot_casosconf",
            "tot_fallecidos",
        ],
        axis=1,
    )
    # Ordeno respecto a las fechas  y sumo losa casos diarios acumulativamente
    data.sort_values(by="fecha", inplace=True)
    data.loc[:, "total_infectados"] = data.nue_casosconf_diff.cumsum()
    data.loc[:, "total_fallecidos"] = data.nue_fallecidos_diff.cumsum()
    # Cambio el nombre de algunas columnas
    data = data.rename(
        columns={
            "osm_admin_level_4": "provincia",
            "nue_casosconf_diff": "casos_diarios",
            "nue_fallecidos_diff": "fallecidos_diarios",
        }
    )
    return data
