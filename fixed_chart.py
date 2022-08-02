# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 12:36:06 2022

@author: ruben
"""

import plotly.graph_objects as go
import pandas as pd
import plotly.io as pio

pio.renderers.default="browser"

df = pd.read_excel("Instrument data.xlsx")

df2 = pd.read_csv("Orders.csv")

df["Date_time"] = pd.to_datetime(df["Date_time"], format = '%d/%m/%Y %H:%M')
df2["Time"] = pd.to_datetime(df2["Time"], format = '%m/%d/%Y %H:%M')

fig = go.Figure(data=[go.Candlestick(x=df["Date_time"],
                                    open=df["Open"],
                                    high=df["High"],
                                    low=df["Low"],
                                    close=df["Close"],
                                    )])

for i in df2.index:
    fig.add_annotation(
            x=df2["Time"][i],
            y=37450,
            xref="x",
            yref="y",
            text=df2["Type"][i],
            showarrow=True,
            font=dict(
                family="Courier New, monospace",
                size=16,
                color="#000000"
                ),
            align="center",
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor="#636363",
            ax=0,
            ay=-30,
            bordercolor="#c7c7c7",
            borderwidth=2,
            borderpad=4,
            bgcolor="#a2d5f5",
            opacity=0.8
            )

fig.update_layout(showlegend=False)

                
fig.show()


