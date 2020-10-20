# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 14:46:07 2020

@author: mbejan
"""

from math import pi

import pandas as pd

from bokeh.plotting import figure, output_file, show

df = pd.read_csv("adbe.csv")
df["Date"] = pd.to_datetime(df["Date"])

da = df["Date"]
hi = df["High"]
lo = df["Low"]
op = df["Open"]
cl = df["Close"]

inc = df["Close"] > df["Open"]
dec = df["Open"] > df["Close"]

w = 12*60*60*1000 # half day in ms

TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title = "Nasdaq Candlestick")
p.xaxis.major_label_orientation = pi/4
p.grid.grid_line_alpha=0.3

p.segment(da, hi, da, lo, color="black")
p.vbar(da[inc], w, op[inc], cl[inc], fill_color="#D5E1DD", line_color="black")
p.vbar(da[dec], w, op[dec], cl[dec], fill_color="#F2583E", line_color="black")

output_file("candlestick.html", title="candlestick.py example")

show(p)  # open a browser