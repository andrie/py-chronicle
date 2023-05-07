from shiny import App, render, ui, req, reactive
from shinywidgets import render_widget, register_widget, reactive_read
import chronicle.core as chr
from config import config_get
# from metrics_explorer import metrics_explorer_server

metrics_dsn = "./nbs/data"
metrics_data = chr.scan_chronicle_metrics(metrics_dsn, "2023/04/03")
    
def server(input, output, session):

    ### metrics server
    import ipydatagrid
    df = metrics_data.metrics.describe()

    @reactive.Calc
    def exp_dat():
        # return df
        f = input.exp_filter_names()
        dat = df
        if f != "":
            dat = dat[dat.name.str.contains(f)]
        f = input.exp_filter_service()
        if f != "":
            dat = dat[dat.service.str.contains(f)]
        return dat
    

    @reactive.Calc
    def exp_metrics_grid():
        grid = ipydatagrid.DataGrid(
            exp_dat(), 
            selection_mode = "row",
            layout = {"height": "16em"}, 
            base_column_size=100,
            column_widths = {"name": 150, "description": 300}
        )
        register_widget("exp_metrics_grid", grid, session = session)
        return grid
    # metrics_explorer_server(input, output, session, metrics_data)
    
    @reactive.Calc
    def exp_extract_metric():
        req(reactive_read(exp_metrics_grid(), "selections"))
        z = reactive_read(exp_metrics_grid(), "selected_cell_values")
        return z[1]

    @output(id="exp_selected_metric")
    @render.text
    def _():
        req(exp_extract_metric())
        return str(exp_extract_metric())

    @output(id="exp_metrics_plot")
    @render_widget
    def _():
        return metrics_data.metrics.plot(exp_extract_metric(), exp_extract_metric())


    @output
    @render.ui
    @reactive.event(input.btn)
    def btn_value():
        return str(input.btn())
