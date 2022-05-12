# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:23:33 2022

@author: adrir
"""

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.image('header.png')
df=pd.read_csv('Career_Mode_FIFA.csv' , delimiter= ';')
df.head()
liga=input('Que liga?')
fifa=st.slider('¿Qué FIFA quieres comprobar?', 15, 22, 15, 1)
df1=df.loc[(df['league_name'] == liga) & (df['FIFA']==fifa)]

x=df1.groupby('club_name')['overall'].mean()+df1.groupby('club_name')['overall'].median()-135
y = x.sort_values(ascending=True)
plt.figure(figsize=(10,20))
plt.grid(axis='x')
plt.title(f'Valoracion media clubs {liga}  fifa {fifa}')
plt.barh(y.index, y.values)
plt.show()
