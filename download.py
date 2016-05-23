import datetime
import candlestick
import plotly.plotly as py
import pandas_datareader.data as web
import plotly.tools as tls

endtime = datetime.date.today()
starttime = datetime.date.fromordinal(endtime.toordinal() - 365)
df = web.DataReader("scty", 'yahoo', starttime, endtime)
fig = candlestick.Candlestick(df)

# print(fig)
url = py.plot(fig, validate=False)
tls.get_embed(url)