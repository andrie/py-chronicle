from shiny import module, ui, render, reactive, event, App
import shiny.experimental as x
from shinywidgets import output_widget, render_widget
from chronicle.plot import *

# UI ----
@module.ui
def metrics_plot_ui(header:str = "CPU"):
    return x.ui.card(
        x.ui.card_header(header),
        x.ui.card_body(
            output_widget(id = "out"),
        ),
    )


# Server ----
def plot_from_config(df, config, service, metric):
    cf = config[service][metric]
    # print(cf)
    fig = df.metrics.plot(cf["name"], cf["service"], cf["title"], cf["name"])
    margin = 10
    fig.update_layout(
        margin=dict(l=margin, r=margin, t=margin, b=margin),
    )
    fig.layout.height = 250
    return fig

@module.server
def metrics_plot_server(input, output, session, metrics_data, service, metric, config):
    @output(id="out")
    @render_widget
    def _():
        # print("computing metrics_plot_server")
        return plot_from_config(metrics_data, config, service, metric)