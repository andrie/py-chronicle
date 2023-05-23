# import ipydatagrid
from shiny import App, render, ui, req, reactive
from shinywidgets import render_widget, register_widget, reactive_read
import chronicle.core as chr
from config import config_get
import vega
# from metrics_explorer import metrics_explorer_server

metrics_dsn = "./nbs/data"
metrics_data = chr.scan_chronicle_metrics(metrics_dsn, "2023/04/03")

logs_dsn = "./nbs/data"
logs_data = chr.scan_chronicle_logs(logs_dsn)

# import altair as alt
# alt.renderers.enable('notebook')
    
def server(input, output, session):


    ### overview -------------------------------------------------------

    @output(id="ov_pwb_cpu")
    @render.text
    def _():
        x = config_get("workbench")["cpu"]
        return str(x)
    
    def plot_from_config(df, service, config):
        cf = config_get(service)[config]
        # print(cf)
        # fig = df.metrics.plot(cf["name"], cf["service"], cf["title"], engine = "plotly")
        fig = df.metrics.plot(cf["name"], cf["service"], cf["title"], engine = "altair")
        ### altair
        # fig.properties(
        #     # height = 'container',
        #     height = 200,
        #     width = 'container',
        # )
        # fig.layout.height = 350
        return fig

    @output(id="ov_pwb_1")
    @render_widget
    def _():
        return plot_from_config(metrics_data, "workbench", "cpu")
        
    @output(id="ov_pwb_2")
    @render_widget
    def _():
        return plot_from_config(metrics_data, "workbench", "ram")
        
    @output(id="ov_pct_1")
    @render_widget
    def _():
        return plot_from_config(metrics_data, "connect", "cpu")
        
    @output(id="ov_pct_2")
    @render_widget
    def _():
        return plot_from_config(metrics_data, "connect", "ram")
        
    ### logins -------------------------------------------------------

    import ipydatagrid
    @output(id="logins_pwb")
    @render_widget
    def _():
        dat = logs_data.logs.workbench_logins().to_pandas()
        grid = ipydatagrid.DataGrid(
            dat, 
            selection_mode = "row",
            layout = {"height": "16em"}, 
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
            layout = {"height": "16em"}, 
            base_column_size=100,
            # column_widths = {"name": 150, "description": 300}
        )
        register_widget("logins_pct", grid, session = session)
        return grid

    ### metrics explorer -------------------------------------------------------

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
        name = exp_extract_metric()
        service = reactive_read(exp_metrics_grid(), "selected_cell_values")[0]
        title = reactive_read(exp_metrics_grid(), "selected_cell_values")[2]
        return "name:    " + name + "\n" + "service: " + service + "\n" + "title:   " + title

    @output(id="exp_metrics_plot")
    @render_widget
    def _():
        return metrics_data.metrics.plot(exp_extract_metric(), alias=exp_extract_metric())

    ### dynamic -------------------------------------------------------

    @output
    @render.ui
    @reactive.event(input.btn)
    def btn_value():
        return str(input.btn())
