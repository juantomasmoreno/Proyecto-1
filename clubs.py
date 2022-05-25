# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:23:33 2022

@author: adrir
"""

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def seleccionar(x, df):
  for index, row in df.iterrows():
    club = row['club_name']
    media = row['overall']
    y = dict(x)
    for i, j in y.items():
      clu, cuar = i
      if club == clu and media<j:
        df = df.drop(index)
  return df

st.set_option('deprecation.showPyplotGlobalUse', False)
st.image('header.png')
df = pd.read_csv('Career_Mode_FIFA.csv' , delimiter= ';')
liga = st.selectbox('¿Qué liga quieres comprobar?',
                   ('English Premier League', 'Spain Primera Division', 'Italian Serie A', 'German 1. Bundesliga', 'French Ligue 1'))
fifa = st.slider('¿Qué FIFA quieres comprobar?', 15, 22, 15, 1)

df1 = df.loc[(df['league_name'] == liga) & (df['FIFA']==fifa)]
x = df1.groupby('club_name')['overall'].quantile([.4])
df2 = seleccionar(x, df1)
c = df2.groupby('club_name')['overall'].mean()-65
y = c.sort_values(ascending=True)
plt.figure(figsize=(10,20))
plt.grid(axis='x')
plt.title(f'Valoracion media clubs {liga}  fifa {fifa}')
plt.barh(y.index, y.values)
fig = plt.show()
st.pyplot(fig)
