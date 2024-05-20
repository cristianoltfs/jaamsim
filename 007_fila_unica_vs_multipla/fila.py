#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:42:22 2024
@author: cristianoltfs
"""

import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.renderers.default="browser"

fila = pd.read_csv("fila.csv", sep = ",")
fila.head()

fila = pd.melt(fila, id_vars='Chegada', value_vars=['AverageQueueTimeUnicaMin','AverageQueueTimeMultiplaMin', 'DiferencaTime', 'MaxEntityWaitingUnica', 'MaxEntityWaitingMultipla', 'DiferencaWait'])


gfila = px.bar(fila,
             x = "value",
             y = "Chegada",
             color = "variable",
             barmode = "group"
)

gfila.update_yaxes(title = 'Intervalo entre chegada: "Exponential Distribution"')

gfila.update_xaxes(title = "Valor")


gfila.show()

gfila.write_html("fila.html")