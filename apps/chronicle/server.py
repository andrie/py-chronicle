# import ipydatagrid
from shiny import App, render, ui, req, reactive
from shinywidgets import render_widget, register_widget, reactive_read
import chronicle.core as chr
from config import config_get
import vega
from mod_metrics_explorer import metrics_explorer_server
from mod_logs_explorer import logs_explorer_server

metrics_dsn = "./nbs/data"
metrics_data = chr.scan_chronicle_metrics(metrics_dsn, "2023/04/03")

logs_dsn = "./nbs/data"
logs_data = chr.scan_chronicle_logs(logs_dsn)

# import altair as alt
# alt.renderers.enable('notebook')

from mod_metrics_plot import metrics_plot_server
    
def server(input, output, session):
    # return


    ### overview -------------------------------------------------------

    @output(id="ov_pwb_cpu")
    @render.text
    def _():
        x = config_get("workbench")["cpu"]
        return str(x)
    
    config = config_get()
    metrics_plot_server("ov_pwb_1", metrics_data, "workbench", "cpu", config)
    metrics_plot_server("ov_pwb_2", metrics_data, "workbench", "cpu_user", config)
    metrics_plot_server("ov_pwb_3", metrics_data, "workbench", "ram", config)

    metrics_plot_server("ov_pct_1", metrics_data, "connect", "cpu", config)
    metrics_plot_server("ov_pct_2", metrics_data, "connect", "cpu_user", config)
    metrics_plot_server("ov_pct_3", metrics_data, "connect", "ram", config)
    metrics_plot_server("ov_pct_4", metrics_data, "connect", "license_users", config)
    
        
    ### logins -------------------------------------------------------

    import ipydatagrid
    @output(id="logins_pwb")
    @render_widget
    def _():
        dat = logs_data.logs.workbench_logins().to_pandas()
        grid = ipydatagrid.DataGrid(
            dat, 
            selection_mode = "row",
            # layout = {"height": "16em"}, 
            base_column_size=100,
            # column_widths = {"name": 150, "description": 300}
        )
        register_widget("logins_pwb", grid, session = session)
        return grid

    @output(id="logins_pct")
    @render_widget
    def _():
        dat = logs_data.logs.connect_logins().to_pandas()
        grid = ipydatagrid.DataGrid(
            dat, 
            selection_mode = "row",
            # layout = {"height": "16em"}, 
            base_column_size=100,
            # column_widths = {"name": 150, "description": 300}
        )
        register_widget("logins_pct", grid, session = session)
        return grid


    ### metrics explorer -------------------------------------------------------
    metrics_explorer_server("metrics_explorer", metrics_data)


    ### logs explorer -------------------------------------------------------

    logs_explorer_server("logs_explorer", logs_data, "workbench")
