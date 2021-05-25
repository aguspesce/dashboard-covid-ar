import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from load_data import load_data
from plot_argentina import (
    plot_casos_argentina,
    plot_fallecidos_argentina,
    plot_casos_acum_argentina,
    plot_fallecidos_acum_argentina,
)

# ---------- Load the data ---------- 
url = "https://docs.google.com/spreadsheets/d/16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA/export?format=csv&id=16-bnsDdmmgtSxdWbVMboIHo5FRuz76DBxsz_BbsEVWA&gid=0"
data = load_data(url)

# ---------- Load the Markdown text ---------
with open("text_block.md", "r") as f:
    intro_md = f.readlines()[0]
with open("text_block.md", "r") as f:
    footer_md = f.readlines()[1:4]
with open("text_block.md", "r") as f:
    sintomas_md = f.readlines()[6]
with open("text_block.md", "r") as f:
    sintomas2_md = f.readlines()[7:]

# --------- Generate the option for the Dropdown ----------
provincias = [
    "CABA",
    "Buenos Aires",
    "San Luis",
    "Chaco",
    "Río Negro",
    "Santa Fe",
    "Tierra del Fuego",
    "Córdoba",
    "Jujuy",
    "Salta",
    "Entre Ríos",
    "Santa Cruz",
    "Tucumán",
    "Corrientes",
    "Neuquén",
    "Santiago del Estero",
    "Mendoza",
    "La Pampa",
    "Misiones",
    "San Juan",
    "La Rioja",
    "Chubut",
    "Formosa",
    "Catamarca",
]
provincias.sort()
options = [{"label": provincia, "value": provincia} for provincia in provincias]
controls = (
    dbc.FormGroup(
        [
            dbc.Label("Provincia"),
            dcc.Dropdown(
                id="selector-provincia",
                options=options,
                value="Buenos Aires",
            ),
        ]
    ),
)

# ---------- Create the Argentina plot ----------
data_arg = data.groupby("fecha").sum()
plot_casos_argentina = plot_casos_argentina(data_arg)
plot_fallecidos_argentina = plot_fallecidos_argentina(data_arg)
plot_casos_acum_argentina = plot_casos_acum_argentina(data_arg)
plot_fallecidos_acum_argentina = plot_fallecidos_acum_argentina(data_arg)

# --------- Create the tabs contest ----------
tab1_content = dbc.Card(
    dbc.CardBody(
        [
            html.H2(
                "Análisis de la situación a nivel nacional.",
                className="card-title",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Graph(figure=plot_casos_argentina),
                        md=6, 
                        sm=12
                    ),
                    dbc.Col(
                        dcc.Graph(figure=plot_fallecidos_argentina),
                        md=6,
                        sm=12,
                    ),
                ],
                style={"margin-bottom": "20px", "margin-top": "20px"}
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Graph(figure=plot_casos_acum_argentina),
                        md=6,
                        sm=12,
                    ),
                    dbc.Col(
                        dcc.Graph(figure=plot_fallecidos_acum_argentina),
                        md=6,
                        sm=12,
                    ),
                ],
                style={"margin-bottom": "20px", "margin-top": "20px"}
            ),
            dbc.Row(dcc.Markdown(intro_md, dangerously_allow_html=True)),
        ]
    ),
    className="mt-3",
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.H2(
                "Análisis de la situación en cada provincia de la Argentina",
                className="card-title",
            ),
            # Primera fila con el dropdown
            dbc.Row(
                dbc.Col(controls, width=6), 
                align="center", 
                style={"margin-bottom": "20px", "margin-top": "20px"}
                ),
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Graph(id="casos_diarios", figure={}), 
                        md=6,
                        sm=12
                    ),
                    dbc.Col(
                        dcc.Graph(id="fallecidos_diarios", figure={}),
                        md=6,
                        sm=12,
                    ),
                ],
                justify="around",
                style={"margin-bottom": "20px", "margin-top": "20px"}
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Graph(id="casos_acumulados", figure={}),
                        md=6,
                        sm=12,
                    ),
                    dbc.Col(
                        dcc.Graph(id="fallecidos_acumulados", figure={}),
                        md=6,
                        sm=12,
                    ),
                ],
                justify="around",
                style={"margin-bottom": "20px", "margin-top": "20px"}
            ),
            dbc.Row(
                dcc.Markdown(intro_md, dangerously_allow_html=True),
                style={"margin-bottom": "20px", "margin-top": "20px"}
                ),
        ]
    ),
    className="mt-3",
)

tab3_content = [
    dbc.Card(
        dbc.CardBody(
            [
                html.H2("Sintomas", className="card-title"),
                html.P(
                    dcc.Markdown(sintomas_md, dangerously_allow_html=True),
                    className="card-text",
                ),
                dbc.CardImg(
                    src="assets/img/sintomas.jpg",
                    style={"margin-bottom": "20px", "margin-top": "20px"}
                ),
                html.P(
                    dcc.Markdown(sintomas2_md, dangerously_allow_html=True),
                    className="card-text",
                ),
            ]
        ),
        style={"margin-bottom": "20px", "margin-top": "20px"}
    ),
    dbc.Card(
        dbc.CardBody(
            [
                html.H2("Prevención", className="card-title"),
                dbc.CardImg(
                    src="assets/img/recomendaciones.jpg", 
                    bottom=True, 
                    style={"margin-bottom": "20px", "margin-top": "20px"}
                ),
            ]
        ),
        style={"margin-bottom": "20px", "margin-top": "20px"}
    ),
]


# ----------------------------
# Dash app con bootstrap style
# ----------------------------
app = dash.Dash(
    __name__,
    external_stylesheets=[
        # dbc.themes.BOOTSTRAP
    ],
    suppress_callback_exceptions=True,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)
app.title = "Casos Covid"

app.layout = dbc.Container(
    [
        # Titulo
        html.H1(
            "Datos COVID-19 en Argentina",
            className="text-center",
            style={
                "margin-top": "20px",
            },
        ),
        html.Hr(),
        dbc.Row(
            dbc.Tabs(
                [
                    dbc.Tab(tab1_content, label="Argentina"),
                    dbc.Tab(tab2_content, label="Provincias"),
                    dbc.Tab(tab3_content, label="Sintomas y Precauciones"),
                ]
            )
        ),
        html.Hr(),
        html.Div(
            html.P(
                dcc.Markdown(footer_md, dangerously_allow_html=True),
                className="text-center"
            ),
        ),
    ],
    fluid=True,
    style={
        "max-width": "1600px",
        "margin": "auto",
    },
)

# -------------------------
# Seccion con los Callbacks
# -------------------------
aspect_ratio = (480, 640)
tempate_fig = "seaborn"
legend = dict(x=0.02, y=0.98, bordercolor="Black", borderwidth=1)

# Grafica de los casos diarios
@app.callback(
    Output("casos_diarios", "figure"),
    [Input("selector-provincia", "value")],
)
def update_graph(selected_provincia):
    data_prov = data.loc[data.provincia == selected_provincia]
    fig_casos = go.Figure(
        data=[
            go.Bar(
                name="Casos diarios",
                x=data_prov["fecha"],
                y=data_prov["casos_diarios"],
                hovertemplate="<b>Casos diarios</b><br>"
                + "%{x}<br>"
                + "%{y}<br>"
                + "<extra></extra>",
            )
        ]
    )
    fig_casos.add_trace(
        go.Scatter(
            name="Casos promediados a 7 dias",
            x=data_prov["fecha"],
            y=data_prov["casos_diarios"].rolling(window=7).mean(),
            hovertemplate="<b>Casos promediados</b><br>"
            + "%{x}<br>"
            + "%{y}<br>"
            + "<extra></extra>",
        )
    )
    fig_casos.update_layout(
        # height=aspect_ratio[0],
        # width=aspect_ratio[1],
        legend=legend,
        template=tempate_fig,
        title_text="Nuevos casos diarios",
        yaxis_title="Numero de casos",
    )
    return fig_casos


# Grafiaca de los fallecidos diarios
@app.callback(
    Output("fallecidos_diarios", "figure"),
    [Input("selector-provincia", "value")],
)
def update_graph(selected_provincia):
    data_prov = data.loc[data.provincia == selected_provincia]
    fig_fallecidos = go.Figure(
        data=[
            go.Bar(
                name="Casos diarios",
                x=data_prov["fecha"],
                y=data_prov["fallecidos_diarios"],
                hovertemplate="<b>Casos diarios</b><br>"
                + "%{x}<br>"
                + "%{y}<br>"
                + "<extra></extra>",
            )
        ]
    )
    fig_fallecidos.add_trace(
        go.Scatter(
            name="Casos promediados a 7 dias",
            x=data_prov["fecha"],
            y=data_prov["fallecidos_diarios"].rolling(window=7).mean(),
            hovertemplate="<b>Casos promediados</b><br>"
            + "%{x}<br>"
            + "%{y}<br>"
            + "<extra></extra>",
        )
    )
    fig_fallecidos.update_layout(
        # height=aspect_ratio[0],
        # width=aspect_ratio[1],
        legend=legend,
        template=tempate_fig,
        title_text="Fallecidos diarios",
        yaxis_title="Numero de fallecidos",
    )
    return fig_fallecidos


# Grafica de los casos acumulados
@app.callback(
    Output("casos_acumulados", "figure"),
    [Input("selector-provincia", "value")],
)
def update_graph(selected_provincia):
    data_prov = data.loc[data.provincia == selected_provincia]
    fig_casos_acum = go.Figure(
        data=[
            go.Scatter(
                x=data_prov["fecha"],
                y=data_prov["casos_diarios"].cumsum(),
                hovertemplate="%{x}<br>" + "%{y}<br>" + "<extra></extra>",
            )
        ]
    )
    fig_casos_acum.update_layout(
        # height=aspect_ratio[0],
        # width=aspect_ratio[1],
        legend=legend,
        template=tempate_fig,
        title_text="Cantidad de casos acumulados",
        yaxis_title="Numero de casos",
    )
    return fig_casos_acum


# Grafica de los fallecidos acumulados
@app.callback(
    Output("fallecidos_acumulados", "figure"),
    [Input("selector-provincia", "value")],
)
def update_graph(selected_provincia):
    data_prov = data.loc[data.provincia == selected_provincia]
    fig_fallecidos_acum = go.Figure(
        data=[
            go.Scatter(
                x=data_prov["fecha"],
                y=data_prov["fallecidos_diarios"].cumsum(),
                hovertemplate="%{x}<br>" + "%{y}<br>" + "<extra></extra>",
            )
        ]
    )
    fig_fallecidos_acum.update_layout(
        # height=aspect_ratio[0],
        # width=aspect_ratio[1],
        legend=legend,
        template=tempate_fig,
        title_text="Cantidad acumulada de fallecidos",
        yaxis_title="Numero de fallecidos",
    )
    return fig_fallecidos_acum


if __name__ == "__main__":
    app.run_server(debug=True, port=8888)
