#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:31:39 2024

@author: christo
"""


import matplotlib.pyplot as plt

x_line = [1,2,3,4,5];
y_line = [2,4,6,8,10];

plt.plot(x_line,y_line,'-o')
plt.xlabel("x_line")
plt.ylabel("y_line")

plt.title("Line plot")
plt.show()

import plotly.express as px

x_line = [1,2,3,4,5]
y_line = [2,4,6,8,10]

fig = px.line(x=x_line, y=y_line, labels={'x': 'X-axis', 'y': 'Y-axis'}, title='Line Plot')
fig.write_html("plot.html")

# This is used to automatically open up a browser of your plot
import webbrowser
webbrowser.open("plot.html")


import matplotlib.pyplot as plt

x_bar = ["A", "B", "C", "D"]
y_bar = [1, 2, 3, 4]

plt.bar(x_bar, y_bar)
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Plot Example")
plt.show()

import plotly.express as px

x_bar = ['A', 'B', 'C', 'D']
y_bar = [1, 2, 3, 4]

fig = px.bar(x = x_bar, y = y_bar, labels={'x': 'Categories', 'y': 'Values'}, title = "Bar plot")
fig.write_html("plot.html")


# This is used to automatically open up a browser of your plot
import webbrowser
webbrowser.open("plot.html")


import matplotlib.pyplot as plt

x_scatter = [1, 2, 3, 4, 5]
y_scatter = [2, 4, 6, 8, 10]

plt.scatter(x_scatter, y_scatter)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot Example')
plt.show()

import plotly.express as px

x_scatter = [1, 2, 3, 4, 5]
y_scatter = [2, 4, 6, 8, 10]

fig = px.scatter(x=x_scatter, y=y_scatter, labels={'x': 'X-axis', 'y': 'Y-axis'}, title='Scatter Plot')
fig.write_html("plot.html")

# This is used to automatically open up a browser of your plot
import webbrowser
webbrowser.open("plot.html")


import matplotlib.pyplot as plt

x_histogram = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

plt.hist(x_histogram, bins=range(min(x_histogram), max(x_histogram) + 1), edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram Example')
plt.show()

import plotly.express as px

x_histogram = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

fig = px.histogram(x=x_histogram, labels={'x': 'Values'}, title='Histogram')
fig.write_html("plot.html")

# This is used to automatically open up a browser of your plot
import webbrowser
webbrowser.open("plot.html")

data = px.data.gapminder()

# Create a choropleth world map

fig = px.choropleth(
    data_frame = data,
    locations = "iso_alpha",
    color = "gdpPercap",
    hover_name = "country",
    animation_frame = "year",
    title = "World Map Choropleth",
    color_continuous_scale = px.colors.sequential.Plasma,
    projection = "natural earth"
)
fig.write_html("plot.html")
import webbrowser
webbrowser.open("plot.html")


import plotly.express as px

df = px.data.gapminder().query("continent=='Oceania'")
fig = px.line(df, x="year", y="lifeExp", color='country')
fig.write_html("plot.html")

# This is used to automatically open up a browser of your plot
import webbrowser
webbrowser.open("plot.html")
