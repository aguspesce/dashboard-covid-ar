# Dashboad con los datos de COVID-19 de Argentina | Dashboard for Argentina COVID-19 data

Código fuente del dashboard fue escrito en Python usando plotly Dash y un .css
de Bootstrap.

Anteriormente, usaba Heroku para desplegar el dashboard, pero debido a un
cambio de sus términos y condiciones ya no uso el servicio.

---

The source code for this dashboard was written in Python using Plotly Dash and a Bootstrap .css file for layout customization.

Previously, I deployed the dashboard on Heroku, but due to changes in their terms and conditions, I no longer use that service.

![screenshot](assets/img/screenshot.png)

## Dependencies

- pip
- pandas
- plotly
- dash
- ipywidgets
- gunicorn
- dash-bootstrap-components

## Local Deployment

If you already have Anaconda or Miniconda installed, you can skip this step.
Otherwise, follow the instructions for setting up Anaconda in your system:
[https://docs.anaconda.com/anaconda/install/](https://docs.anaconda.com/anaconda/install/)


Now you could install all the dependencies through the conda package manager:
```
conda env create -f environment.yml
```

And then activate the environment:
```
conda activate interactive
```

You can use the Makefile to build and server the dashboard:
```
make server
```
The dashboard will be open in your default browser.


## Data source

The data used to plot was obtained from the
[Covid19arData repository](https://github.com/SistemasMapache/Covid19arData)
collected by [Mapache System](https://smapache.com.ar/es/).


## License

The dashboard and the script to create it are licensed under a 
[Creative Commons Attribution 4.0 International License] [cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
