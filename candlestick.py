from plotly.tools import FigureFactory as FF
import indicators
import pandas as pd

class Candlestick(dict):
    """ Class for managing a candlestick stock figure. """

    VOLUME_ENABLED = False

    def __init__(self, df, primaryKey="Close"):
        super(Candlestick, self).__init__(
            FF.create_candlestick(df.Open, df.High, df.Low, df.Close, dates=df.index))
        self.df = df
        for subplot in self["data"]:
            subplot["hoverinfo"] = "none"

        self._addMarkers(primaryKey, df[primaryKey])

        self._addMovingAverage(df[primaryKey], 200)
        self._addMovingAverage(df[primaryKey], 50)

        if Candlestick.VOLUME_ENABLED:
            self._addVolumeBars(df["Volume"])

            self["layout"] = {
                "paper_bgcolor": 'rgba(0,0,0,0)',
                "plot_bgcolor": 'rgba(0,0,0,0)',
                "yaxis1": {"domain": [0, 1]},
                "yaxis2": {"domain": [0, 0.2], "anchor": "x1"},
            }

    def _addMarkers(self, name, series):
        markerTexts = [ "{0:.2f} ({1:+.2%})".format(value, perChange)
            for (value, perChange) in zip(series.diff(), series.pct_change())]
        labelScatter = {
            "x": series.index,
            "y": series.values,
            "name": name,
            "mode": 'markers',
            "marker": { "size": 0, "opacity": 0, "color": "#000000" },
            "type": 'scatter',
            "text": markerTexts,
            "showlegend": False,
            "hoverinfo": "all",
            "xaxis": "x1",
            "yaxis": "y1",
        }
        self["data"] += [ labelScatter ]

    def _addMovingAverage(self, series, n):
        window = series.rolling(window=n)
        ma = pd.Series(window.mean())
        maSubplot = {
            "x": ma.index,
            "y": ma.values,
            "name": 'MA_{}'.format(n),
            "mode": 'line',
            "marker": { "size": 1 },
            "type": 'scatter',
            "showlegend": False,
            "hoverinfo": "name+y",
            "xaxis": "x1",
            "yaxis": "y1",
        }
        self["data"] += [ maSubplot ]

    def _addVolumeBars(self, series):
        sp = {
            "x": series.index,
            "y": series.values,
            "name": "Volume",
            "type": "bar",
            "opacity": 0.2,
            "showlegend": False,
            "showgrid": False,
            "showticklabels": False,
            "hoverinfo": "name+y",
            "xaxis": "x1",
            "yaxis": "y2",
        }
        self["data"] = [ sp ] + self["data"]