# -*- coding: utf-8 -*-
from nsga2func import Solucion
from nsga2func import NSGA2
import random
import numpy as np
import matplotlib.pyplot as plt
import sys

global matrixDistancia, matrixFlujoUno, matrixFlujoDos
global numFac
matrixDistancia = []
matrixFlujoUno = []
matrixFlujoDos = []


#IMPLEMENTO BUSQUEDA LOCAL:
# PARAMETROS A CONSIDERAR:
# 1.- DECIDIR RELACION DOMINANCIA
# 2.- DECIDIR UNA ESTRATEGIA DE SELECCION DE ELEMENTOS DEL ARCHIVO
# 3.- DECIDIR UNA ESTRATEGIA DE EXPLORACION DE VECINOS
# 4.- DECIDIR UNA ESTRATEGIA DE MANEJO DEL ARCHIVO
# 5.- DECIRIDE UN CRITERIO TERMINO



def lectura():
	archivo = sys.argv[1]
	instancias = open(archivo, 'r')
	arreglo = []
	tamano = instancias.readline()
	arreglo.append(tamano)
	for line in instancias:
		for caract in line.split(' '):
			if caract == "":
				pass
			elif caract == "\n":
				pass
			else:
				num = caract
				arreglo.append(int(num))
	return arreglo

#DISTRIBUCION EN MATRICES DE FLUJO Y DISTANCIA, UTILES	
def distribuirMatrices(arreglo):
	numFac = int(arreglo[0])
	largoArray = len(arreglo)
	distribucion = numFac*numFac
	rangoMatrizD = distribucion
	rangoMatrizFU = distribucion*2
	rangoMatrizFD = distribucion*3
	for i in range(1,largoArray):
		if (0 < i and i <= rangoMatrizD):
			matrixDistancia.append(arreglo[i])
		elif (rangoMatrizD < i and i <= rangoMatrizFU):
			matrixFlujoUno.append(arreglo[i])
		elif (rangoMatrizFU < i and i <= rangoMatrizFD):
			matrixFlujoDos.append(arreglo[i])
		else:
			pass
	return numFac
#UTILES
def imprimeMatriz(arreglo):
	largo = len(arreglo)
	ancho = int(math.sqrt(largo))
	for i in range(ancho):
		for j in range(ancho):
			print arreglo[i*ancho+j],
			print " ",
		print "\n"

#ALGORITMO		
def generarSolucionRandom(sol, numFac):
	vectorObjetos = []
	vectorLocalidades = []
	for x in range(numFac):
		vectorObjetos.append(x)
		vectorLocalidades.append(x)
	while len(vectorObjetos) > 0:
		obj = random.choice(vectorObjetos)
		loc = random.choice(vectorLocalidades)
		sol.solution.insert(obj, loc)
		vectorObjetos.pop(vectorObjetos.index(obj)), vectorLocalidades.pop(vectorLocalidades.index(loc))
	return sol

#ALGORITMO
def crearPoblacion(poblacion, tamPoblacion, numFac):
	print "Creando poblacion inicial . . ."
	for x in range(tamPoblacion):
		if(x==0):
			solux = Solucion(numFac)
			generarSolucionRandom(solux, numFac)
			poblacion.append(solux)
		else:
			solux = Solucion(numFac)
			generarSolucionRandom(solux, numFac)
			while (solux in poblacion):
				generarSolucionRandom(solux, numFac)
			poblacion.append(solux)
	return poblacion
#ALGORITMO
def dominance(sol, otherSol):
	sF1 = sol.costoFlujo[0]
	sF2 = sol.costoFlujo[1]
	oF1 = otherSol.costoFlujo[0]
	oF2 = otherSol.costoFlujo[1]
	a,b = sF1 < oF1, sF2 < oF2
	c,d = sF1 <= oF1, sF2 <= oF2
	if (c and d) and (a or b):
		#print True
		return True
	else:
		#print False
		return False
#ALGORITMO
def noDominance(sol, archive):
	sF1 = sol.costoFlujo[0]
	sF2 = sol.costoFlujo[1]
	contadorDominancia = 0
	tamArchive = len(archive)
	for elemento in archive:
		oF1 = elemento.costoFlujo[0]
		oF2 = elemento.costoFlujo[1]
		a,b = sF1 <= oF1, sF2 <= oF2
		c,d = oF1 <= sF1, oF2 <= sF2
		if (a and d) or (c and b):
			contadorDominancia += 1
			if contadorDominancia == tamArchive:
				return True
		elif dominance(sol, elemento) or dominance(elemento, sol):
			return False
def graficarPob(poblacion):
	listaSolC1, listaSolC2 = [], []
	for elem in poblacion:
		if elem.rank == 1:
			#elem.costoAsignacion()
			listaSolC1.append(elem.costoFlujo[0])
			listaSolC2.append(elem.costoFlujo[1])
	plt.plot(listaSolC1, listaSolC2, 'ro')
	plt.ylabel('Costo Flujo 2')
	plt.xlabel('Costo Flujo 1')
	plt.show()
	return 1




