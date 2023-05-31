
from shiny import ui
import shiny.experimental as x
from shinywidgets import output_widget
from faicons import icon_svg
# from metrics_explorer import metrics_explorer_ui
# import ipydatagrid

from mod_metrics_explorer import metrics_explorer_ui, metrics_explorer_server
from mod_metrics_plot import metrics_plot_ui
from mod_logs_explorer import logs_explorer_ui

# style="border: 1px solid #999 round;"

app_ui = ui.page_fluid(
    ui.panel_title("Chronicle metrics explorer"),
    ui.navset_tab_card(
    
        ### overview -------------------------------------------------------
        ui.nav(
            x.ui.card(
                x.ui.card_header("Overview"),
                "Top level metrics"
            ), 
                x.ui.card(
                    x.ui.card_header("Workbench"),
                    x.ui.layout_column_wrap(1/2,
                        metrics_plot_ui("ov_pwb_1", "CPU"),
                        metrics_plot_ui("ov_pwb_2", "Memory"),
                    )
                ),
                x.ui.card(
                    x.ui.card_header("Connect"),
                    x.ui.layout_column_wrap( 1/2,
                        metrics_plot_ui("ov_pct_1", "CPU"),
                        metrics_plot_ui("ov_pct_2", "Memory"),
                    )
                )
        ),

        ### logins -------------------------------------------------------
        ui.nav(
            x.ui.card(
                x.ui.card_header("Logins"),
                "List the logins for each service"
                # height="250px"
            ),
            ui.row(
                x.ui.layout_column_wrap(
                    1/2,
                    x.ui.card(
                        x.ui.card_header("Workbench logins"),
                        output_widget("logins_pwb"),
                    ),
                    x.ui.card(
                        x.ui.card_header("Connect logins"),
                        output_widget("logins_pct"),
                    ),
                ),
            ),
        ),

        ### metrics explorer -------------------------------------------------------
        ui.nav(
            x.ui.card(
                x.ui.card_header("Metrics explorer"),
                "Click into a metric to view a plot"
                # height="250px"
            ),
            metrics_explorer_ui("metrics_explorer"),
        ),
        
        ### logs explorer -------------------------------------------------------
        ui.nav(
            x.ui.card(
                x.ui.card_header("Logs explorer"),
                "Explore unique log types"
            ),
            logs_explorer_ui("logs_explorer", "Workbench types"),
        ),

    )
)
