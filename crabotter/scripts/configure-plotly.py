import plotly
import os

plotly.tools.set_credentials_file(
    username=os.environ["PLOTLY_USERNAME"],
    api_key=os.environ["PLOTLY_API_KEY"])