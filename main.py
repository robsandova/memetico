# -*- coding: utf-8 -*-
import funciones
from nsga2func import Solucion
from nsga2func import NSGA2
import nsga2func
import math
import time, sys, random, datetime
from random import randint
from itertools import cycle
#from PyGMO import *

#import numpy as np
import matplotlib.pyplot as plt

global matrixDistancia, matrixFlujoUno, matrixFlujoDos
global numFac
matrixDistancia = []
matrixFlujoUno = []
matrixFlujoDos = []


def main():

	numFac = funciones.distribuirMatrices(funciones.lectura())
	start = datetime.datetime.now()
	nsga2 = NSGA2(2, 0.1, 1.0)
	P = []
	funciones.crearPoblacion(P,75, numFac)

	#for elem in P:
	#	print elem.solution, elem.costoFlujo, elem.rank
	#print len(P)	
	#print "+++++++++++++++++++++++++++++++++++++++++"
	
	#for elemento in P:
	#	elemento.costoAsignacion()
	fronteras= nsga2.fastNonDominatedSort(P)
	P = nsga2.ordenPostBusqueda(P, fronteras,75)

	#print P[0].solution, P[0].costoFlujo

	#archive = []
	#print len(P)
	
	#vecino = nsga2.buscarDominante(P[0])

	#for elem in P:
	#	print elem.solution, elem.costoFlujo, elem.rank
	#	if elem.rank == 1:
	#		archive.append(elem)

	#print "Archive: "
	#for elemento in archive:
	#	print elemento.solution, elemento.costoFlujo, elemento.rank

#	print vecino.solution, vecino.costoFlujo

#	question = nsga2.checkArchive(vecino, archive)
#	if question is True:
#		archive = nsga2.updateArchive(vecino, archive)

#	for elemento in archive:
#		print elemento.solution, elemento.costoFlujo		




	#print "Trabajo escrito de tesis"

	#nsga2.createNewPob(P, 1, 2, 0.2)
	#print "Solucion : ", P[0].solution, P[0].costoFlujo[0], P[0].costoFlujo[1]
	#print "y su vecindario, con alpha = 0.3"
	#nsga2.generarAlphaVecinos(P[0], 0.6)
	#Cada parametro es: 
	#tamanio Pob, GENERACIONES, ALPHA(VECINOS A GENERAR), indiceCX (1=Seq, 2=Onepoint), indiceMUT (1=2opt, 2=3opt)
	
	#print P[0].solution
	#print P[1].solution
	#childs =nsga2.cycleCrossover(P[0], P[1])
	#for child in childs:
	#	print child.solution
	
	nsga2.runAlgorithm(P,75, 35, 1, start)

	#a = [i for i in range(numFac)]





if __name__ == '__main__':
	main()


