
from shiny import App, render, ui, req, reactive
import shiny
from shinywidgets import output_widget, render_widget, register_widget, reactive_read
import shiny.experimental as x
from faicons import icon_svg

app_ui = ui.page_fluid(
    ui.panel_title("Chronicle metrics explorer"),
    ui.navset_tab_card(
        # elements ----
        ui.nav(
            x.ui.value_box(
                "Overview", "All the things"
            ), 
            output_widget("metrics_grid"),
            ui.output_text_verbatim("selected_metric"),
            output_widget("metrics_plot")
        ),
        ui.nav(
            x.ui.value_box(
                "I got", 
                "99",
                "problems",
                showcase=icon_svg("flask", height="60px")
            ),
            "To be developed"
        ),
        ui.nav(
            x.ui.value_box(
                "Dynamic",
                ui.output_ui("btn_value")
            ),
            ui.h2("To be developed"),
            ui.p("This is a placeholder for a future tab."),
            ui.input_action_button("btn", "Click me"),
        ),
    )
)
