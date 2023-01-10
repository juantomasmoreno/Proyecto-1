# -*- coding: utf-8 -*-

import csv
import os
import streamlit as st


class Grado:
    def __init__(self, ide, nombre, uni, uni_a, nota, plazas):
        self.id = int(ide)
        self.nombre = nombre
        self.uni = uni
        self.uni_a = uni_a
        self.nota = float(nota)
        self.plazas = int(plazas)
        
        
class Clase:
    def __init__(self):
        self.carreras = {}
        
    def nueva_carrera(self,ide, nombre,uni, uni_a, nota, plazas):
        self.carreras[ide] = Grado(ide, nombre,uni, uni_a, nota, plazas)
        return True, 'Añadido correctamente'
    
    def cargar_datos(self, fichero):
        try:
            with open(fichero,'r', encoding='utf-8') as csvfile:
                r = csv.reader(csvfile, delimiter=';')
                leidos = 0
                next(r)
                for ide, nombre, uni, uni_a, nota, plazas in r:
                    nota=nota.replace(',','.',1)
                    b, msg = self.nueva_carrera(ide,str(nombre), str(uni), uni_a, nota, plazas)
                    if b:                 
                        leidos += 1
                print(f'{leidos} carreras leídas correctamente')
                return True, 'Carga de datos correcta'
        except Exception as ex:
            print('Error al leer fichero de datos. Excepcion de tipo '+
                    f'{type(ex).__name__}\nArgumentos:{ex.args}. \n'+
                    f'Directorio actual:{os.getcwd()}')

def buscar_uni(clase):
    texto = ''
    st.header('¿Qué quieres estudiar?')
    texto = st.text_input().lower()
    n = 1
    dic = {}
    listainfo = ['Elige un grado']
    if len(texto) < 3:
        st.caption('Mínimo 3 caracteres')
    else:
        for grado in clase.carreras.values():
            if texto in grado.nombre.lower():
                carrera = f'{n} - {grado.nombre} - {grado.uni}'
                st.caption(carrera)
                listainfo.append(carrera)
                dic[n] = grado
                n += 1
        
        if not dic:
            st.subheader('No hemos encontrado ningún grado')
        else:    
            elec = 0
            if elec < 1 or elec > len(dic):
                 st.subheader('¿Quieres más información sobre algún grado?')
                 opcion = st.selectbox('', listainfo)
                 try:
                     opcion = opcion.split('-')
                     grado=dic[int(opcion[0])]
                     st.subheader(f'{grado.nombre} en la {grado.uni}')
                     st.subheader(f'Nota de corte: {grado.nota}')
                     if grado.plazas != 0:
                        st.subheader(f'{grado.plazas} plazas')
                 except:
                     st.subheader('Vuelve a elegir')
                     
                 
        
  
           
if __name__ == '__main__':
    c=Clase()
    c.cargar_datos('termometro_def2.csv')
    # st.image('header.png')
    st.header('Aquí podrás encontrar tu próxima carrera universitaria.')
    uni = buscar_uni(c)
    
