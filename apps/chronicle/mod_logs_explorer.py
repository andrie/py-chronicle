
from shiny import module, reactive, render, ui, req
import shiny.experimental as x
from shinywidgets import output_widget, render_widget, register_widget, reactive_read
from chronicle.plot import *

# ============================================================
# Module: logs_explorer
# ============================================================

@module.ui
def logs_explorer_ui(label: str = "Workbench types"):
    return ui.row(
        x.ui.layout_column_wrap(
            1/2,
            x.ui.card(
                x.ui.card_header(label),
                # output_widget("exp_logs_grid"),
                ui.input_radio_buttons("service", "Service", ["workbench", "connect"]),
                ui.input_select("log_type", "Log type",
                                ["auth_login", "auth_login_failed", "auth_logout"],
                                size = 10,
                ),
                ui.output_text_verbatim("exp_selected_log_type")
            ),
            x.ui.card(
                x.ui.card_header("Selected"),
                # output_widget("exp_logs_out")
                ui.output_ui("exp_logs_out"),
            )
        )
    )


@module.server
def logs_explorer_server(input, output, session, logs_data, service):
    import ipydatagrid


    # @reactive.Calc
    @reactive.Effect
    def get_types():
        # print("debug get_types()")
        if input.service() == "workbench":
            df = logs_data.logs.unique_workbench_types()
            types = df["type"].tolist()
        elif input.service() == "connect":
            df = logs_data.logs.unique_connect_actions()
            types = df["action"].tolist()
            # print(types)
        else:
            raise ValueError("service must be 'workbench' or 'connect'")

        ui.update_select("log_type", choices = types)
        return df
        


    @output(id="exp_selected_log_type")
    @render.text
    def _():
        req(input.log_type())
        type = input.log_type()
        if input.service() == "workbench":
            out =  "service: " + service + "\n" + "type:   " + type
        elif input.service() == "connect":
            out = "service: " + service + "\n" + "action: " + type
        return out

    @output(id="exp_logs_out")
    @render.ui
    def _():
        from itables.javascript import _datatables_repr_ as DT
        type = input.log_type()
        # print(f"type: {type}")
        if input.service() == "workbench":
            grid_data = logs_data.logs.extract_workbench_audit_logs(type).to_pandas()
            grid_data = grid_data.drop("attributes", axis = 1)
        elif input.service() == "connect":
            grid_data = logs_data.logs.extract_connect_audit_logs(type).to_pandas()
            grid_data = grid_data.drop("attributes", axis = 1)
        return ui.HTML(DT(grid_data))

