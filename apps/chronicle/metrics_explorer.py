from shiny import module, ui, render, reactive, req
from shinywidgets import output_widget, render_widget, register_widget, reactive_read

@module.ui
def metrics_explorer_ui():
    return ui.div(
        ui.output_text_verbatim("selected_metric"),
        output_widget("metrics_plot"),
    )

@module.server
def metrics_explorer_server(input, output, session, metrics_data):
    # import ipydatagrid  

