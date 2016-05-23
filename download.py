import datetime
import candlestick
import plotly.offline as py
import pandas_datareader.data as web

endtime = datetime.date.today()
starttime = datetime.date.fromordinal(endtime.toordinal() - 365)
df = web.DataReader("scty", 'yahoo', starttime, endtime)
fig = candlestick.Candlestick(df)

# print(fig)
py.plot(fig, filename='aapl-candlestick.html', validate=False)