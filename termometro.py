# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 08:47:20 2022

@author: adrir
"""
import csv
import os
import streamlit as st

class Grado:
    def __init__(self, id, nombre, uni, uni_a, nota, plazas):
        self.id = int(id)
        self.nombre = nombre
        self.uni = uni
        self.uni_a = uni_a
        self.nota = int(nota)
        self.plazas = int(plazas)
        
class Clase:
    def __init__(self):
        self.carreras = {}
        
    def nueva_carrera(self, nombre, uni_a, nota, plazas):
        self.carreras[id] = Grado(id, nombre, uni_a, nota, plazas)
        return True, 'Añadido correctamente'
    
    def cargar_datos(self, fichero):
        try:
            with open(fichero,'r', encoding='utf-8') as csvfile:
                r = csv.reader(csvfile, delimiter=';')
                leidos = 0
                next(r)
                for id, nombre, uni, uni_a, nota, plazas in r:
                    b, msg = self.nueva_carrera(nombre, uni, uni_a, nota, plazas)
                    if b:                 
                        leidos += 1
                print(f'{leidos} carreras leídas correctamente')
                return True, 'Carga de datos correcta'
        except Exception as ex:
            print('Error al leer fichero de datos. Excepcion de tipo '+
                    f'{type(ex).__name__}\nArgumentos:{ex.args}. \n'+
                    f'Directorio actual:{os.getcwd()}')

    
        
    def buscar_uni(self):
        texto = ''
        texto = st.text_input('Elige en qué universidad quieres buscar','', key=2).lower()
        n = 1
        dic = {}      
        return texto
    
    
    
            
if __name__ == '__main__':
    c=Clase()
    c.cargar_datos('tprueba.csv')
    # st.image('header.png')
    st.header('Aquí podrás filtrar los mejores jugadores por liga, nacionalidad o posición.')
    uni = c.buscar_uni()
    st.caption(uni)
