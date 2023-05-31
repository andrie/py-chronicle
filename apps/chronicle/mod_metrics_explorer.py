
from shiny import module, reactive, render, ui, req
import shiny.experimental as x
from shinywidgets import output_widget, render_widget, register_widget, reactive_read
from chronicle.plot import *

# ============================================================
# Module: metrics_explorer
# ============================================================

@module.ui
def metrics_explorer_ui(label: str = "Increment counter"):
    # import ipydatagrid
    # from ipydatagrid 
    return ui.row(
        x.ui.layout_column_wrap(
            1/2,
            x.ui.card(
                x.ui.card_header("Filter metric"),
                x.ui.layout_column_wrap(
                    1/2,
                    ui.input_text("exp_filter_service", "Filter on service", placeholder="Enter text"),
                    ui.input_text("exp_filter_names", "Filter on name", placeholder="Enter text"),
                ),
                output_widget("exp_metrics_grid"),
            ),
            x.ui.card(
                x.ui.card_header("Selected metric"),
                output_widget("exp_metrics_plot"),
                ui.output_text_verbatim("exp_selected_metric"),
            )
        )
    )



@module.server
def metrics_explorer_server(input, output, session, metrics_data):
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
            # layout = {"height": "16em"}, 
            # layout = {"height": "100%"}, 
            base_column_size=100,
            column_widths = {"name": 150, "description": 300}
        )
        register_widget("exp_metrics_grid", grid, session = session)
        return grid
    
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

