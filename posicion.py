# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 08:47:20 2022

@author: adrir
"""
import csv
import os
import matplotlib.pyplot as plt
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
                    
                print ( f'{leidos} jugadores leidos correctamente')
                return True, 'correcto'
        except Exception as ex:
            print ( 'Error al leer fichero de datos. Excepcion de tipo '+
                    f'{type(ex).__name__}\nArgumentos:{ex.args}. \n'+
                    f'Directorio actual:{os.getcwd()}')


        
    def buscar(self):
        texto = ''
        n = 1
        dic = {}
        while len(texto) < 3 or not dic:
            texto = input('¿A quién buscas?: ').lower()
            if len(texto) < 3:
                print('Introduce más carácteres en la búsqueda')
            else:
                for ide,jugador in self.jugadores.items():
                    if texto in jugador.nombre.lower().split(): 
                        print(f'{n} {jugador.nombre}')
                        dic[n] = ide
                        n += 1
                    elif texto in jugador.nCorto.lower().split():
                        print(f'{n} {jugador.nCorto}')
                        dic[n] = ide
                        n += 1
                if not dic:
                    print('No hay ningún jugador con esa búsqueda')
                    texto = ''
        elec = 0
        while elec < 1 or elec > len(dic):
            try:
                elec = int(input('Elige un jugador: '))
            except:
                elec = 0
        return dic[elec]
    def buscar_nac(self):
        texto = ''
        n = 1
        dic = {}
        while len(texto) < 3 or not dic:
            texto = input('¿De que país?: ').lower()
            if len(texto) < 3:
                print('Introduce más carácteres en la búsqueda')
            else:
                for ide,jugador in self.jugadores.items():
                    if texto in jugador.pais.lower() and jugador.pais not in dic.values(): 
                        print(f'{n} {jugador.pais}')
                        dic[n] = jugador.pais
                        n += 1
                if not dic:
                    print('No hay ningún jugador con esa búsqueda')
                    texto = ''
        elec = 0
        while elec < 1 or elec > len(dic):
            try:
                elec = int(input('Elige una nacionalidad: '))
            except:
                elec = 0
        return dic[elec]
    def buscar_pos(self):
        texto = ''
        n = 1
        dic = {}
        while len(texto) < 1 or not dic:
            texto = input('¿En que posicion?: ').lower()
            if len(texto) < 1:
                print('Introduce más carácteres en la búsqueda')
            else:
                for ide,jugador in self.jugadores.items():
                    lista=jugador.posicion.lower().split(',')
                    for i in lista:
                        if texto==i and i not in dic.values(): 
                            print(f'{n} {i}')
                            dic[n] = i
                            n += 1
                if not dic:
                    print('No hay ningún jugador con esa búsqueda')
                    texto = ''
        elec = 0
        while elec < 1 or elec > len(dic):
            try:
                elec = int(input('Elige una posicion: '))
            except:
                elec = 0
        return dic[elec]
    def jugadores_pos_nat(self,nat,pos):
        
        lista=[]
        for ide,jugador in self.jugadores.items():
            if nat==jugador.pais and pos.lower() in jugador.posicion.lower().split(",") and len(lista)<11:
                lista.append((jugador.nombre,jugador.media))
        print(lista)
            



c=Clase()
c.cargar_datos('Fifa22.csv') 
nat=c.buscar_nac()
pos=c.buscar_pos()
c.jugadores_pos_nat(nat,pos)