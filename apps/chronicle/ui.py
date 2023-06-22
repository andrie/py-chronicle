
from shiny import ui
import shiny.experimental as x
from shinywidgets import output_widget
from faicons import icon_svg
# from metrics_explorer import metrics_explorer_ui
# import ipydatagrid

from mod_metrics_explorer import metrics_explorer_ui
from mod_metrics_plot import metrics_plot_ui
from mod_logs_explorer import logs_explorer_ui

# style="border: 1px solid #999 round;"

def col3(x):
    return ui.column(3, x)

def col4(x):
    return ui.column(4, x)

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
                    x.ui.layout_column_wrap(
                        1/3,
                        metrics_plot_ui("ov_pwb_1", "System CPU"),
                        metrics_plot_ui("ov_pwb_2", "User CPU"),
                        metrics_plot_ui("ov_pwb_3", "Memory"),
                    ),
                ),
                x.ui.card(
                    x.ui.card_header("Connect"),
                    x.ui.layout_column_wrap(
                        1/4,
                        metrics_plot_ui("ov_pct_1", "System CPU"),
                        metrics_plot_ui("ov_pct_2", "User CPU"),
                        metrics_plot_ui("ov_pct_3", "Memory"),
                        metrics_plot_ui("ov_pct_4",  "Licensed user count (365 days)"),
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
                # ui.column
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

