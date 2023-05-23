
from shiny import ui
import shiny.experimental as x
from shinywidgets import output_widget
from faicons import icon_svg
# from metrics_explorer import metrics_explorer_ui
# import ipydatagrid

style="border: 1px solid #999 round;"

app_ui = ui.page_fluid(
    ui.panel_title("Chronicle metrics explorer"),
    ui.navset_tab_card(
    
        ### overview
        ui.nav(
            x.ui.card(
                x.ui.card_header("Overview"),
                "Top level metrics"
            ), 
            ui.row(
                ui.h2("Workbench"),
                x.ui.layout_column_wrap(
                    1/2,
                    x.ui.card(
                        x.ui.card_header("CPU"),
                        x.ui.card_body(
                            output_widget("ov_pwb_1"),
                        ),
                        height = 400,
                        max_height= 400,
                        # fill = True
                    ),
                    x.ui.card(
                        x.ui.card_header("Memory"),
                        output_widget("ov_pwb_2"),
                    ),
                )
            ),
            ui.row(
                ui.h2("Connect"),
                ui.column(6, output_widget("ov_pct_1"), style=style),
                ui.column(6, output_widget("ov_pct_2"), style=style),
            ),
        ),

        ### logins
        ui.nav(
            x.ui.card(
                x.ui.card_header("Logins"),
                "List the logins for each service"
                # height="250px"
            ),
            ui.row(
                x.ui.card(
                    x.ui.card_header("Workbench logins"),
                    output_widget("logins_pwb"),
                )
            ),
            ui.row(
                x.ui.card(
                    x.ui.card_header("Connect logins"),
                    output_widget("logins_pct"),
                )
            ),
        ),

        ### metrics explorer
        ui.nav(
            x.ui.card(
                x.ui.card_header("Metrics explorer"),
                "Click into a metric to view a plot"
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
        # ui.nav(
        #     x.ui.value_box(
        #         "Dynamic",
        #         ui.output_ui("btn_value"),
        #         showcase=icon_svg("flask", height="60px")
        #     ),
        #     ui.h2("To be developed"),
        #     ui.p("This is a placeholder for a future tab."),
        #     ui.input_action_button("btn", "Click me"),
        # ),
    )
)
