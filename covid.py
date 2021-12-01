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

topDeptCo = data.groupby('Nombre departamento').size().sort_values(ascending = False).head(10)
print("Punto 11")
print(topDeptCo)
print() 

topDeptCo = data.groupby('Nombre departamento').size().sort_values(ascending = False).head(10)
print("Punto 11")
print(topDeptCo)
print()

#////////////////////////////////
#punto 12

topDeptFa = data[data['Ubicación del caso'] == 'Fallecido'].groupby('Nombre departamento').size().sort_values(ascending = False).head(10)
print("Punto 12")
print(topDeptFa)
print() 

topDeptFa = data[data['Ubicación del caso'] == 'Fallecido'].groupby('Nombre departamento').size().sort_values(ascending = False).head(10)
print("Punto 12")
print(topDeptFa)
print()

#////////////////////////////////
#punto 13

topDeptRe = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size().sort_values(ascending = False).head(10)
print("Punto 13")
print(topDeptRe)
print() 

topDeptRe = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size().sort_values(ascending = False).head(10)
print("Punto 13")
print(topDeptRe)
print() 
print()

#////////////////////////////////
#punto 14

topMunCo = data.groupby('Nombre municipio').size().sort_values(ascending = False).head(10)
print("Punto 14")
print(topMunCo)
print()

print(topMunCo)
print()

#////////////////////////////////
#punto 15


topMunFa = data[data['Ubicación del caso'] == 'Fallecido'].groupby('Nombre municipio').size().sort_values(ascending = False).head(10)
print("Punto 15")
print(topMunFa)
print()

topMunFa = data[data['Ubicación del caso'] == 'Fallecido'].groupby('Nombre municipio').size().sort_values(ascending = False).head(10)
print("Punto 15")
print(topMunFa)
print()

#////////////////////////////////
#punto 16

topMunRe = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size().sort_values(ascending = False).head(10)
print("Punto 16")
print(topMunRe)
print()  

topMunRe = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size().sort_values(ascending = False).head(10)
print("Punto 16")
print(topMunRe)
print() 

#////////////////////////////////
#punto 17
ciudadesCont = data.groupby(['Nombre departamento','Nombre municipio']).size().sort_values(ascending = False)
print("Punto 17")
print(ciudadesCont)

ciudadesCont = data.groupby(['Nombre departamento','Nombre municipio']).size().sort_values(ascending = False)
print("Punto 17")
print(ciudadesCont)
print()

#////////////////////////////////
#punto 18

genCiudad = data.groupby(['Nombre departamento','Nombre municipio','Sexo']).size()
print("Punto 18")
print(genCiudad)
print()

genCiudad = data.groupby(['Nombre departamento','Nombre municipio','Sexo']).size()
print("Punto 18")
print(genCiudad)
print()

#////////////////////////////////
#punto 19

promCiudad = data.groupby(['Nombre departamento','Nombre municipio','Sexo']).Edad.mean()
print("Punto 19")
print(promCiudad)
print()

promCiudad = data.groupby(['Nombre departamento','Nombre municipio','Sexo']).Edad.mean()
print("Punto 19")
print(promCiudad)
print()

#////////////////////////////////
#punto 20

data['Nombre del país'].replace('ESTADOS UNIDOS','ESTADOS UNIDOS DE AMÉRICA',inplace=True)
data['Nombre del país'].replace('VENEUELA','VENEZUELA',inplace=True)
data['Nombre del país'].replace('MEXICO','MÉXICO',inplace=True)
paisProc = data.groupby('Nombre del país').size().sort_values(ascending = False)
print("Punto 20")
print(paisProc)

paisProc = data.groupby('Nombre del país').size().sort_values(ascending = False)
print("Punto 20")
print(paisProc)
print()

#////////////////////////////////
#punto 21

fechaContagios = data.groupby('Fecha de diagnóstico').size().sort_values(ascending = False)
print("Punto 21")
print(fechaContagios)
print() 

fechaContagios = data.groupby('Fecha de diagnóstico').size().sort_values(ascending = False)
print("Punto 21")
print(fechaContagios)
print()

#////////////////////////////////
#punto 22

tasaMor = (len(data[data['Ubicación del caso'] == 'Fallecido']) / len(data)) * 100
tasaRec = (len(data[data['Recuperado'] == 'Recuperado']) / len(data)) * 100
print("Punto 22")
print(tasaMor)
print(tasaRec)
print() 

print("Punto 22")
print(tasaMor)
print(tasaRec)
print()

#////////////////////////////////
#punto 23

tasaMorDept = (data[data['Ubicación del caso'] == 'Fallecido'].groupby('Nombre departamento').size().sort_values(ascending = False) / data[data['Ubicación del caso'] == 'Fallecido'].groupby('Nombre departamento').size().sort_values(ascending = False).sum()) * 100
tasaRecDept = (data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size().sort_values(ascending = False) / data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size().sort_values(ascending = False).sum()) * 100
print("Punto 23")
print(tasaMorDept)
print(tasaRecDept)
print() 

print("Punto 23")
print(tasaMorDept)
print(tasaRecDept)
print()

#////////////////////////////////
#punto 24

tasaMorCiu = (data[data['Ubicación del caso'] == 'Fallecido'].groupby('Nombre municipio').size().sort_values(ascending = False) / data[data['Ubicación del caso'] == 'Fallecido'].groupby('Nombre municipio').size().sort_values(ascending = False).sum()) * 100
tasaRecCiu = (data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size().sort_values(ascending = False) / data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size().sort_values(ascending = False).sum()) * 100
print("Punto 24")
print(tasaMorCiu)
print(tasaRecCiu)
print() 

print("Punto 24")
print(tasaMorCiu)
print(tasaRecCiu)
print()

#////////////////////////////////
#punto 25
atenCiu = data.groupby(['Nombre municipio','Ubicación del caso']).size()
print("Punto 25")
print(atenCiu)
print() 
atenCiu = data.groupby(['Nombre municipio','Ubicación del caso']).size()
print("Punto 25")
print(atenCiu)
print() 
print()


#////////////////////////////////
#punto 26

promEdadCiu = data.groupby(['Nombre municipio','Sexo']).Edad.mean()
print("Punto 26")
print(promEdadCiu)
print()

print("Punto 26")
print(promEdadCiu)
print()

#////////////////////////////////
#punto 27

data.groupby('Fecha de diagnóstico').size().cumsum().plot(label = "Contagios",figsize=(25,10))
Fallecidos = data[data['Ubicación del caso'] == 'Fallecido']
Fallecidos.groupby('Fecha de diagnóstico').size().cumsum().plot(label = "Fallecidos ",figsize=(25,10))
Recuperado = data[data['Recuperado'] == 'Recuperado']
Recuperado.groupby('Fecha de diagnóstico').size().cumsum().plot(label = "Recuperados",figsize=(25,10))
plt.legend()
plt.show() 

data.groupby('Fecha de diagnóstico').size().cumsum().plot(label = "Contagios",figsize=(25,10))
Fallecidos = data[data['Ubicación del caso'] == 'Fallecido']
Fallecidos.groupby('Fecha de diagnóstico').size().cumsum().plot(label = "Fallecidos ",figsize=(25,10))
Fallecidos.groupby('Fecha de diagnóstico').size().cumsum().plot(label = "Fallecidos",figsize=(25,10))
Recuperado = data[data['Recuperado'] == 'Recuperado']
Recuperado.groupby('Fecha de diagnóstico').size().cumsum().plot(label = "Recuperados",figsize=(25,10))
plt.legend()
plt.show()

#////////////////////////////////
#punto 28

data.groupby('Nombre departamento').size().sort_values(ascending=False).head(10).plot(label = "Contagios",figsize=(20,10))
Fallecidos = data[data['Ubicación del caso'] == 'Fallecido']
Fallecidos.groupby('Nombre departamento').size().sort_values(ascending=False).head(10).plot(label = "Fallecidos",figsize=(20,10))
Recuperado = data[data['Recuperado'] == 'Recuperado']
Recuperado.groupby('Nombre departamento').size().sort_values(ascending=False).head(10).plot(label = "Recuperados",figsize=(20,10))
plt.legend()
plt.show() 

Recuperado = data[data['Recuperado'] == 'Recuperado']
Recuperado.groupby('Nombre departamento').size().sort_values(ascending=False).head(10).plot(label = "Recuperados",figsize=(20,10))
plt.legend()
plt.show()

#////////////////////////////////
#punto 29

data.groupby('Nombre municipio').size().sort_values(ascending=False).head(10).plot(label = "Contagios",figsize=(20,10))
Fallecidos = data[data['Ubicación del caso'] == 'Fallecido']
Fallecidos.groupby('Nombre municipio').size().sort_values(ascending=False).head(10).plot(label = "Fallecidos",figsize=(20,10))
Recuperado = data[data['Recuperado'] == 'Recuperado']
Recuperado.groupby('Nombre municipio').size().sort_values(ascending=False).head(10).plot(label = "Recuperados",figsize=(20,10))
plt.legend()
plt.show() 

Recuperado = data[data['Recuperado'] == 'Recuperado']
Recuperado.groupby('Nombre municipio').size().sort_values(ascending=False).head(10).plot(label = "Recuperados",figsize=(20,10))
plt.legend()
plt.show() 
plt.show()

#////////////////////////////////
#punto 30

falleEdad = data[data['Ubicación del caso'] == 'Fallecido'].groupby('Edad').size().sort_values(ascending = False)
print("Punto 30")
print(falleEdad)
print() 

falleEdad = data[data['Ubicación del caso'] == 'Fallecido'].groupby('Edad').size().sort_values(ascending = False)
print("Punto 30")
print(falleEdad)
print()

#////////////////////////////////
#punto 31

porcAten = ((data.groupby('Ubicación del caso').size().sort_values(ascending = False)) / ((data.groupby('Ubicación del caso').size().sort_values(ascending = False)).sum())) * 100
print("Punto 31")
print(porcAten)
print() 

porcAten = ((data.groupby('Ubicación del caso').size().sort_values(ascending = False)) / ((data.groupby('Ubicación del caso').size().sort_values(ascending = False)).sum())) * 100
print("Punto 31")
print(porcAten)
print() 
print()

#////////////////////////////////
#punto 32
