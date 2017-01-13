# -*- coding: utf-8 -*-
import funciones
from nsga2func import Solucion
from nsga2func import NSGA2
import nsga2func
import math
import time, sys, random
from random import randint
#import numpy as np
#import matplotlib.pyplot as plt

global matrixDistancia, matrixFlujoUno, matrixFlujoDos
global numFac
matrixDistancia = []
matrixFlujoUno = []
matrixFlujoDos = []


def main():

	numFac = funciones.distribuirMatrices(funciones.lectura())
	start = time.time()
	nsga2 = NSGA2(2, 0.1, 1.0)
	P = []
	funciones.crearPoblacion(P,50, numFac)
	front = nsga2.fastNonDominatedSort(P)
	P = nsga2.sortRanking(P)
	#for elem in P:
	#	print elem.solution, elem.costoFlujo[0], elem.costoFlujo[1], elem.rank
	#lisa = nsga2.ready(P)
	#for elem in lisa:
	#	print elem[1]
	#	print "hola hola"
	pob = nsga2.runAlgorithm(P,50,25)

	#sol = nsga2.sequentialConstructiveCrossover(P[0], P[1])


	end = time.time()
	print "T =", end-start
	



if __name__ == '__main__':
	main()


