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