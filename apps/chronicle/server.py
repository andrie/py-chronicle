from shiny import App, render, ui, req, reactive
from shinywidgets import output_widget, render_widget, register_widget, reactive_read
import chronicle.core as chr

metrics_dsn = "./nbs/data"
metrics_data = chr.scan_chronicle_metrics(metrics_dsn, "2023/04/03")

def server(input, output, session):

    import ipydatagrid
    dat = metrics_data.metrics.describe()
    metrics_grid = ipydatagrid.DataGrid(dat, 
        selection_mode = "row",
        layout = {"height": "16em"}, 
        base_column_size=100,
        column_widths = {"name": 150, "description": 300}
    )
    register_widget("metrics_grid", metrics_grid)

    @output
    @render.ui
    @reactive.event(input.btn)
    def btn_value():
        return str(input.btn())

    @reactive.Calc
    def extract_metric():
        req(reactive_read(metrics_grid, "selections"))
        z = reactive_read(metrics_grid, "selected_cell_values")
        return z[1]

    @output
    @render.text
    def selected_metric():
        req(extract_metric())
        return str(extract_metric())
    
    @output(id="metrics_plot")
    @render_widget
    def _():
        return metrics_data.metrics.plot(extract_metric(), extract_metric())
