
from shiny import ui
import shiny.experimental as x
from shinywidgets import output_widget
from faicons import icon_svg
# from metrics_explorer import metrics_explorer_ui
# import ipydatagrid

style="border: 1px solid #999;"

app_ui = ui.page_fluid(
    ui.panel_title("Chronicle metrics explorer"),
    ui.navset_tab_card(
    
        ### overview
        ui.nav(
            x.ui.value_box(
                "Overview", "All the things"
            ), 
            ui.row(
                ui.h2("Workbench"),
                ui.column(6, "CPU", style=style),
                ui.column(6, "Memory", style=style),
            ),
            ui.row(
                ui.h2("Connect"),
                ui.column(6, "CPU", style=style),
                ui.column(6, "Memory", style=style),
            ),
        ),

        ### metrics explorer
        ui.nav(
            x.ui.card(
                x.ui.card_header("Metrics explorer")
                # height="250px"
            ),
            # metrics_explorer_ui(),
            # ui.h2("Metrics explorer"),
            ui.row(
                ui.input_text("exp_filter_service", "Filter on service", placeholder="Enter text"),
                ui.input_text("exp_filter_names", "Filter on name", placeholder="Enter text")
            ),
            output_widget("exp_metrics_grid"),
            ui.output_text_verbatim("exp_selected_metric"),
            output_widget("exp_metrics_plot"),
            # metrics_explorer_ui()
        ),

        ### dynamic
        ui.nav(
            x.ui.value_box(
                "Dynamic",
                ui.output_ui("btn_value"),
                showcase=icon_svg("flask", height="60px")
            ),
            ui.h2("To be developed"),
            ui.p("This is a placeholder for a future tab."),
            ui.input_action_button("btn", "Click me"),
        ),
    )
)
