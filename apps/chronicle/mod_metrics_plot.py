from shiny import module, ui, render, reactive, event, App
import shiny.experimental as x
from shinywidgets import output_widget, render_widget

# UI ----
@module.ui
def metrics_plot_ui(header:str = "CPU"):
    return x.ui.card(
        x.ui.card_header(header),
        x.ui.card_body(
            output_widget(id = "out"),
        ),
        # height = 400,
        # max_height= 400,
        # fill = True
    )


# Server ----
def plot_from_config(df, config, service, metric):
    cf = config[service][metric]
    # print(cf)
    ### altair
    # fig = df.metrics.plot(cf["name"], cf["service"], cf["title"], engine = "altair")
    # fig.properties(
    #     # height = 'container',
    #     height = 200,
    #     width = 'container',
    # )
    ### plotly
    fig = df.metrics.plot(cf["name"], cf["service"], cf["title"], engine = "plotly")
    fig.layout.height = 350
    return fig

@module.server
def metrics_plot_server(input, output, session, metrics_data, service, metric, config):
    @output
    @render_widget
    def out():
        return plot_from_config(metrics_data, config, service, metric)