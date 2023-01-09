# -*- coding: utf-8 -*-

import csv
import os


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
    texto = input('Elige que grado quieres buscar:').lower()
    n = 1
    dic = {}
    if len(texto) < 3:
        print('Introduce más carácteres en la búsqueda')
    else:
        for grado in clase.carreras.values():
            if texto in grado.nombre.lower():
                print(f'{n} {grado.nombre} ({grado.uni})')
                dic[n] = grado
                n += 1
        
        if not dic:
            print('No hay ningún alumno con esa búsqueda')
        else:    
            elec = 0
            if elec < 1 or elec > len(dic):
                 try:
                     elec = int(input('Elige una universidad: '))
                     grado=dic[elec]
                     print(f'{grado.nombre},{grado.uni},{grado.uni_a},{grado.nota},{grado.plazas}')
                     
                 except:
                     print('Vuelve a elegir')
                     
                 
        
  
           
if __name__ == '__main__':
    c=Clase()
    c.cargar_datos('tprueba.csv')
    # st.image('header.png')
    print('Aquí podrás encontrar tu próxima carrera universitaria.')
    uni = buscar_uni(c)
    
