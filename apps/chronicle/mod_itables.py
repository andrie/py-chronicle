from shiny import Inputs, Outputs, Session, App, module, reactive, render, ui

# ============================================================
# Module: itables
# ============================================================

@module.ui
def itables_ui():
    return ui.output_ui("out")


@module.server
def itables_server( input, output, session, df):

    from itables.javascript import _datatables_repr_ as DT

    @output(id="out")
    @render.ui
    def out():
        return ui.HTML(DT(df))