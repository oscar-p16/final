# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 19:46:25 2021

@author: oscar perez
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = 'covid_22_noviembre.csv'
data = pd.read_csv(url)

# casos de Contagiados 

num_pais = len(data)
print("P")
print(num_pais)
print() 
num_pais = len(data)
print("P")
print(num_pais)
print()

#////////////////////////////////

# Número de Municipios

num_muni = len(data.groupby('Nombre municipio').size())
print("P")
print(num_muni)
print() 

num_muni = len(data.groupby('Nombre municipio').size())
print("P")
print(num_muni)
print()

num_muni = len(data.groupby('Nombre municipio').size())
print("P")
print(num_muni)
print()

#////////////////////////////////
# municipios afectados

data['Ubicación del caso'].replace('casa','Casa',inplace=True)
data['Ubicación del caso'].replace('CASA','Casa',inplace=True)
num_encasa = len(data[data['Ubicación del caso'] == 'Casa'])
print("Punto 4")
print(num_encasa)
print() 

num_encasa = len(data[data['Ubicación del caso'] == 'Casa'])
print("Punto 4")
print(num_encasa)
print()


#////////////////////////////////
#punto 5
data['Recuperado'].replace('fallecido','Fallecido',inplace=True)
num_recu = len(data[data['Recuperado'] == 'Recuperado'])
print("Punto 5")
print(num_recu)
print()

num_recu = len(data[data['Recuperado'] == 'Recuperado'])
print("Punto 5")
print(num_recu)
print() 
print()

#////////////////////////////////
#punto 6

num_fall = len(data[data['Ubicación del caso'] == 'Fallecido'])
print("Punto 6")
print(num_fall)
print()

data['Estado'].replace('LEVE','Leve',inplace=True)


num_pais = len(data)
print("Punto 1")
print(num_pais)
print()


num_muni = len(data.groupby('Nombre municipio').size())
print("Punto 2")
print(num_muni)
print()



list_muni = data.groupby('Nombre municipio').size().sort_values(ascending = False)
print("Punto 3")
print(list_muni)

print()



num_fall = len(data[data['Ubicación del caso'] == 'Fallecido'])
print("Punto 6")
print(num_fall)
print()

#////////////////////////////////
#punto 7

tipoContagio = data.groupby('Tipo de contagio').size().sort_values(ascending = False)
print("Punto 7")
print(tipoContagio)
print()

print(tipoContagio)
print()

#////////////////////////////////
#punto 8
data['Nombre departamento'].replace('Tolima','TOLIMA',inplace=True)
data['Nombre departamento'].replace('Caldas','CALDAS',inplace=True)
num_dept = len(data.groupby('Nombre departamento').size().sort_values(ascending = False))
print("Punto 8")
print(num_dept)
print()

print(num_dept)
print()

#////////////////////////////////
#punto 9
list_dept= data.groupby('Nombre departamento').size().sort_values(ascending = False)
print("Punto 9")
print(list_dept)
print()

print()

data['Nombre municipio'].replace('puerto colombia','PUERTO COLOMBIA',inplace=True)
data['Nombre municipio'].replace('puerto COLOMBIA','PUERTO COLOMBIA',inplace=True)
data['Nombre municipio'].replace('MEDELLiN','MEDELLIN',inplace=True)
data['Nombre municipio'].replace('Galapa','GALAPA',inplace=True)
data['Nombre municipio'].replace('momil','MOMIL',inplace=True)
data['Nombre municipio'].replace('Guepsa','GUEPSA',inplace=True)
data['Nombre municipio'].replace('barrancabermeja','BARRANCABERMEJA',inplace=True)
data['Nombre municipio'].replace('Pensilvania','PENSILVANIA',inplace=True)
data['Nombre municipio'].replace('Anserma','ANSERMA',inplace=True)
num_muni = len(data.groupby('Nombre municipio').size())
print("Punto 2")
print(num_muni)

print(list_dept)
print()

#////////////////////////////////
#punto 10

tipoAtencion = data.groupby('Ubicación del caso').size().sort_values(ascending = False)
print("Punto 10")
print(tipoAtencion)
print() 
tipoAtencion = data.groupby('Ubicación del caso').size().sort_values(ascending = False)
print("Punto 10")
print(tipoAtencion)
print()tipoAtencion = data.groupby('Ubicación del caso').size().sort_values(ascending = False)
print("Punto 10")
print(tipoAtencion)
print()

#////////////////////////////////
#punto 11
