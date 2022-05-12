# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 08:47:20 2022

@author: adrir
"""
import csv
import os
import streamlit as st

class Jugador22:
    def __init__(self,ide, nombre,posicion,media,potencial,edad,altura,club,liga,nivelLiga,pais,pDom,nCorto):      
        self.ide = ide
        self.nombre = nombre
        self.posicion = posicion
        self.media= media
        self.potencial =potencial
        self.edad = edad
        self.altura = altura
        self.club=club
        self.liga=liga
        self.nivelLiga=nivelLiga
        self.pais= pais
        self.pDom=pDom
        self.nCorto=nCorto
        
class Clase:
    def __init__(self):
        self.jugadores = {}
        
    def nuevo_jugador(self,ide,nombre ,posicion,media,potencial,edad,altura,club,liga,nivelLiga,pais,pDom,nCorto):
        if liga=='':
            liga='Sin liga'
            self.jugadores[ide] = Jugador22(ide,nombre ,posicion,media,potencial,edad,altura,club,liga,nivelLiga,pais,pDom,nCorto)
            return True, 'Añadido correctamente'
        else:
            self.jugadores[ide] = Jugador22(ide,nombre ,posicion,media,potencial,edad,altura,club,liga,nivelLiga,pais,pDom,nCorto)
            return True, 'Añadido correctamente'
    
    def cargar_datos(self, fichero):
        try:
            with open(fichero,'r', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                leidos = 0
                next(reader)
                for sofifa_id,long_name,player_positions,overall,potential,age,height_cm,club_name,league_name,league_level,nationality_name,preferred_foot,short_name in reader:
                    b, msg = self.nuevo_jugador(sofifa_id,long_name,player_positions,int(overall),potential,age,height_cm,club_name,league_name,league_level,nationality_name,preferred_foot,short_name)
                    if b:                 
                        leidos += 1
                print(f'{leidos} jugadores leidos correctamente')
                return True, 'correcto'
        except Exception as ex:
            print('Error al leer fichero de datos. Excepcion de tipo '+
                    f'{type(ex).__name__}\nArgumentos:{ex.args}. \n'+
                    f'Directorio actual:{os.getcwd()}')

    def buscar_nac(self):
        texto = ''
        n = 1
        dic = {}   
        for ide,jugador in self.jugadores.items():
            if texto in jugador.pais.lower() and jugador.pais not in dic.values(): 
                # st.caption(f'{n} {jugador.pais}')
                dic[n] = jugador.pais
                n += 1
        if len(dic)>0:    
            elec = 0
            try:
                elec = int(st.text_input('Elige una nacionalidad (escribe el número)',0, key=1))
            except:
                elec = 0
            if elec==0:    
                return texto        
            return dic[elec]
        return texto
        
    def buscar_pos(self):
        texto = ''
        texto = st.text_input('Elige una posición (escribe la abreviatura inglesa: por ejemplo, portero es GK)','', key=2).lower()
        n = 1
        dic = {}      
        return texto
    
    def buscar_liga(self):
        texto = ''
        n = 1
        dic = {}
        for ide,jugador in self.jugadores.items():
            if texto in jugador.liga.lower() and jugador.liga not in dic.values(): 
                # st.caption(f'{n} {jugador.liga}')
                dic[n] = jugador.liga
                n += 1
        if len(dic)>0:        
            elec = 0
            try:
                elec = int(st.text_input('Elige una liga (escribe el número)',0, key=3))
            except:
                elec = 0
            if elec==0:    
                return texto        
            return dic[elec]
        return texto
    
    def jugadores_pos_nat(self,nat,pos,liga):
        lista=[]
        for ide,jugador in self.jugadores.items():
            if nat==jugador.pais and liga==jugador.liga and pos.lower() == jugador.posicion.lower().split(",")[0] and len(lista)<11:
                lista.append((jugador.nombre, jugador.club, jugador.media))
            elif nat==jugador.pais and liga==jugador.liga and pos == '' and len(lista)<11:
                lista.append((jugador.nombre, jugador.club, jugador.media))
            elif nat=='' and liga==jugador.liga and pos.lower() == jugador.posicion.lower().split(",")[0] and len(lista)<11:
                lista.append((jugador.nombre, jugador.club, jugador.media)) 
            elif nat=='' and liga=='' and pos.lower() == jugador.posicion.lower().split(",")[0] and len(lista)<11:
                lista.append((jugador.nombre, jugador.club, jugador.media))
            elif nat==jugador.pais and liga=='' and pos.lower() == jugador.posicion.lower().split(",")[0] and len(lista)<11:
                lista.append((jugador.nombre, jugador.club, jugador.media))
            elif nat==jugador.pais and liga=='' and pos=='' and len(lista)<11:
                lista.append((jugador.nombre, jugador.club, jugador.media))
            elif nat=='' and liga==jugador.liga and pos=='' and len(lista)<11:
                lista.append((jugador.nombre, jugador.club, jugador.media))
        st.write('Estos son los mejores jugadores que cumplen tus requisitos:')
        for i in lista:
            cadena = f'{i[0]} ({i[1]}): Media {i[2]}'
            st.subheader(cadena)
            st.subheader(media)
            
if __name__ == '__main__':
    c=Clase()
    c.cargar_datos('Fifa22.csv')
    st.image('header.png')
    st.header('Aquí podrás filtrar los mejores jugadores por liga, nacionalidad o posición.')
    nat=c.buscar_nac()
    pos=c.buscar_pos()
    liga=c.buscar_liga()
    c.jugadores_pos_nat(nat,pos,liga)
