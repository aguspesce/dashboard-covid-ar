import plotly.graph_objs as go

aspect_ratio = (480, 640)
tempate_fig = "seaborn"
legend = dict(x=0.02, y=0.98, bordercolor="Black", borderwidth=1)

# Grafica de los casos diarios
def plot_casos_argentina(data_plot):
    fig_casos = go.Figure(
        data=[
            go.Bar(
                name="Casos diarios",
                x=data_plot.index,
                y=data_plot["casos_diarios"],
                # marker_color="firebrick",
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
            x=data_plot.index,
            y=data_plot["casos_diarios"].rolling(window=7).mean(),
            hovertemplate="<b>Casos promediados</b><br>"
            + "%{x}<br>"
            + "%{y}<br>"
            + "<extra></extra>",
        )
    )
    fig_casos.update_layout(
        # xaxis=dict(
        # tickangle=-90,
        # ),
        # height=aspect_ratio[0],
        # width=aspect_ratio[1],
        legend=legend,
        template=tempate_fig,
        title_text="Nuevos casos diarios",
        yaxis_title="Numero de casos",
    )
    return fig_casos


# Grafica de los fallecidos diarios en Argentina
def plot_fallecidos_argentina(data):
    fig_fallecidos = go.Figure(
        data=[
            go.Bar(
                name="Casos diarios",
                x=data.index,
                y=data["fallecidos_diarios"],
                # marker_color="firebrick",
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
            x=data.index,
            y=data["fallecidos_diarios"].rolling(window=7).mean(),
            hovertemplate="<b>Casos promediados</b><br>"
            + "%{x}<br>"
            + "%{y}<br>"
            + "<extra></extra>",
        )
    )
    fig_fallecidos.update_layout(
        # xaxis=dict(
        # tickangle=-90,
        # ),
        # height=aspect_ratio[0],
        # width=aspect_ratio[1],
        legend=legend,
        template=tempate_fig,
        title_text="Fallecidos diarios",
        yaxis_title="Numero de fallecidos",
    )
    return fig_fallecidos


# Grafica de los casos acumulados en Argentina
def plot_casos_acum_argentina(data):
    fig_casos_acum = go.Figure(
        data=[
            go.Scatter(
                x=data.index,
                y=data["casos_diarios"].cumsum(),
                hovertemplate="%{x}<br>" + "%{y}<br>" + "<extra></extra>",
            )
        ]
    )
    fig_casos_acum.update_layout(
        # xaxis=dict(
        # tickangle=-90,
        # ),
        # height=aspect_ratio[0],
        # width=aspect_ratio[1],
        legend=legend,
        template=tempate_fig,
        title_text="Cantidad de casos acumulados",
        yaxis_title="Numero de casos",
    )
    return fig_casos_acum


# Grafica de los fallecidos acumulados
def plot_fallecidos_acum_argentina(data):
    fig_fallecidos_acum = go.Figure(
        data=[
            go.Scatter(
                x=data.index,
                y=data["fallecidos_diarios"].cumsum(),
                hovertemplate="%{x}<br>" + "%{y}<br>" + "<extra></extra>",
            )
        ]
    )
    fig_fallecidos_acum.update_layout(
        # xaxis=dict(
        # tickangle=-90,
        # ),
        # height=aspect_ratio[0],
        # width=aspect_ratio[1],
        legend=legend,
        template=tempate_fig,
        title_text="Cantidad acumulada de fallecidos",
        yaxis_title="Numero de fallecidos",
    )
    return fig_fallecidos_acum
