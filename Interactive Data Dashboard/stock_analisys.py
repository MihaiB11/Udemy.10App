#!/usr/bin/env python
# coding: utf-8

# In[53]:


from pandas_datareader import data
from datetime import datetime
from bokeh.plotting import figure, show, output_file

start = datetime(2020, 1, 1)
end = datetime(2020, 10, 20)

df = data.DataReader(name = "AAPL", data_source = "yahoo", start = start, end = end)

def inc_dec(c, o):
    if c > o:
        value = "Increase"
    elif c < o:
        value = "Decrease"
    else:
        value = Equal
    return value
df["Status"] = [inc_dec(c, o) for c, o in zip(df.Close, df.Open)]

#inc = df.index[df.Close > df.Open]
#dec = df.index[df.Open > df.Close]

df["Middle"] = (df.Open+df.Close)/2
df["Height"] = abs(df.Close - df.Open)

p = figure(x_axis_type = 'datetime', width = 1000, height = 300, sizing_mode = "scale_width")
p.title.text = "Candlestick Chart"
p.grid.grid_line_alpha = 0.3

hours_12 = 12*60*60*1000

p.segment(df.index , df.High , df.index, df.Low, color = "black")
p.rect(x = df.index[df.Status == "Increase"], y = df.Middle[df.Status == "Increase"], width = hours_12, height = df.Height[df.Status == "Increase"], fill_color = "green", line_color = "black")

p.rect(x = df.index[df.Status == "Decrease"], y = df.Middle[df.Status == "Decrease"], width = hours_12, height = df.Height[df.Status == "Decrease"], fill_color = "red", line_color = "black")

output_file("CS.html")
show(p)


# In[ ]:




