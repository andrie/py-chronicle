from shiny import App

# import polars as pl
# import pyarrow.parquet as pq
# import plotly

# import re

# bucket = "colorado-posit-chronicle"
# logs_path = "v1/logs"
# metrics_path = "v1/metrics"
# date_range = "2023/04/03"
# metrics_dsn = f"s3://{bucket}/{metrics_path}/{date_range}"

# import chronicle.core as chr



from ui import app_ui
from server import server

app = App(app_ui, server)
