def paretoLocalSearch(self, poblacion, tamPob, alphaVec):
		archive, solutionArchive, vecindad, soluciones, listaVecinos, solucionAux = [], [], [], [], [], []
		numFac = poblacion[0].numFacilities
		#print "largo pob: ", len(poblacion)
		#Para cada solucion de la poblacion, si la solucion tiene rank 1 la agrego a mi archive
		#Ademas seteo su bit de visita en 0.
		for solucion in poblacion:
			#print solucion.solution
			if solucion.rank == 1:
				archive.append(solucion)
				solucion.visitado = 0
				#print solucion.solution
		#Mientras no esten todos los elementos del archive visitados
		while self.contadorVisitados(archive):
			#Para cada elemento en el archivo, agrego sus vectores solucion a un vector para 
			#.verificar que si se agregan elementos repetidos sea con el bit de visitado en 1.
			for elemento in archive:
				solutionArchive.append(elemento.solution)
			#Selecciono una solucion cuyo bit de visita sea 0.	
			#print "seleccionando y  obteniendo vecinos"
			solSeleccionada = self.seleccionar(archive)
			#Genero la vecindad TOTAL de la solucion seleccionada
			if alphaVec >= 0.9:
				vecindad = self.generoVecinos(solSeleccionada, numFac)
			else:
				vecindad = self.generarAlphaVecinos(solSeleccionada, alphaVec)
			#Agrego el elemento a la vecindad para analizarla con respecto a ND-Sort y Crowding
			vecindad.append(solSeleccionada)
			#Agrego para comprobar que este
			solucionAux.append(solSeleccionada.solution)
			#Realizo el proceso de FND Sort y luego ordeno por crowding distance de los vecinos
			#. con el fin de obtener solo los mejores vecinos, los cuales seran agregados al archive
			fronteras = self.fastNonDominatedSort(vecindad)
			vecindad = self.ordenPostBusqueda(vecindad, fronteras, tamPob)
			#Para cada vecino en la vecindad, selecciono solo los con ranking 1, los agrego tanto
			#. a la lista de listas con soluciones y a la lista de vecinos a agregar al archive.
			
			for vecino in vecindad:
				#print vecino.solution, vecino.costoFlujo[0], vecino.costoFlujo[1], vecino.rank, vecino.crowdedDistance
				
				if vecino.rank == 1:
					soluciones.append(vecino.solution)
					listaVecinos.append(vecino)
					#print "vecino a agregar: "
					#print vecino.solution, vecino.rank
			#print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
			#Si la solSeleccionada esta en las mejores soluciones, la agrego y su bit de visita en 1.
			#print "Se agregaran ", len(listaVecinos), "elementos"
			#print "agregando nuevas soluciones"
			if solSeleccionada.solution in soluciones:
				#print "esta!!!!!"
				solSeleccionada.visitado = 1
				#Ahora todos los elementos del vecindario deben ser agregados excepto la solucion 
				for elementoVecino in listaVecinos:
					#Si es la solSeleccionada, continuo
					if elementoVecino.solution in solucionAux:
						continue
					#Si no
					else:
						#Si el elementoVecino ya esta en el archive, lo agrego pero con bit de visitado en 1
						if elementoVecino.solution in solutionArchive:
							elementoVecino.visitado = 1
							#archive.append(elementoVecino)
							#Aqui tengo una duda... siempre que la solucion ya esta en el archive, hare un ordenamiento no dominada?
							#Deberia solo setear su bit de visita en 0, en otra parte debería ordenarlo, solo cuando se agregan...
							#REVISAR!!!!
							#self.fastNonDominatedSort(archive)
							#archive = self.actualizarArchive(archive)

						#Si no esta, simplemente lo agrego
						else:
							#Aca se justifica por que lo estoy agregando.... bien, 
							archive.append(elementoVecino)
							self.fastNonDominatedSort(archive)
							archive = self.actualizarArchive(archive)
				
				del listaVecinos[:]			
			
			elif solSeleccionada.solution not in soluciones:
				#print "NO esta !!"
				archive.remove(solSeleccionada)
				for elementoVecino in listaVecinos:
					if elementoVecino.solution in solutionArchive:
						elementoVecino.visitado = 1
						#archive.append(elementoVecino)
						#self.fastNonDominatedSort(archive)
						#archive = self.actualizarArchive(archive)
					else:
						archive.append(elementoVecino)
						self.fastNonDominatedSort(archive)
						archive = self.actualizarArchive(archive)					
				del listaVecinos[:]
			tamanoPonderar = tamPob*0.1
			if len(archive)	>= tamanoPonderar*tamPob:
				print "Population size bigger than setted: ", len(archive),
				print "Reducing Size. . ."
				fronteras = self.fastNonDominatedSort(archive)
				archive = self.ordenPostBusqueda(archive, fronteras, tamPob)
				for elem in archive:
					print elem.visitado,
			else:
				self.fastNonDominatedSort(archive)
				archive = self.actualizarArchive(archive)



			#print "elementos del archive: "
			#contador = 0
			#for elemento in archive:
			#	print elemento.solution, contador, elemento.visitado
			#	contador +=1
			#print "len Archive: ", len(archive)
				
			del solutionArchive[:]			
		#Debo chequear si el archive resultante es menor al tamanio de la poblacion,
		#. si esto se cumple es necesario generar mutaciones dentro de los mejores elementos 
		#. de la poblacion para llenar con mutaciones de buenas soluciones
		#. REVISARRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR!!!
		return archive			

def ready(self, archive):
		contador = 0
		contadorVisita = 0
		listaSolVis = []
		for elemento in archive:
			listaAux = []
			listaAux.append(elemento.solution)
			listaAux.append(elemento.visitado)
			listaSolVis.append(listaAux)
		#print len(listaSolVis)
		i = 0
		largo = len(listaSolVis)	
		while contador != largo:
			#print len(listaSolVis)
			if len(listaSolVis) == 0:
				contador +=1
				break
			else:
				elemSolVis = random.choice(listaSolVis)
			#print "soy elemSolVis: ",
			#print elemSolVis
			if elemSolVis[1] == 1:
				contadorVisita += 1
				listaSolVis.remove(elemSolVis)
				#print "soy listaSolVis: ", listaSolVis
			elif elemSolVis[0] == 0:
				listaSolVis.remove(elemSolVis)
			contador += 1
		if contadorVisita == len(archive):
			#print "True"
			return False
		else:
			return True	



def addAndUpdate(self, solucion, archive):
		#print "comienzo addAndUpdate"
		archiveActualizado = []
		archiveActualizado.append(solucion)
		#print "solucion a analizar: ", solucion.solution
		#print "costo de la solucion obj 1: ", solucion.costoFlujo[0],
		#print "costo solucion obj 2: ",  solucion.costoFlujo[1]
		for elemento in archive:
			#print "solucion a comparar: ", elemento.solution
			#print "costo sol obj 1: ", elemento.costoFlujo[0],
			#print "costo sol obj 2: ",  elemento.costoFlujo[1] 
			#Si encuentro una solucion vecina dominada por mi solucion inicial, continuo
			if funciones.dominance(solucion, elemento):
				#print "la solucion a analizar domina a la solucion a comparar"
				continue
			elif funciones.dominance(elemento, solucion):
				#print "la solucion a comparar domina a la solucion a analizar"
				continue
			#Si encuentro una solucion que es no-dominada por esta nueva solucion ND agregada:
			else:
				#print "ninguna se domina!" 
				archiveActualizado.append(elemento)
				#print "se agrega al archive"
		archiveActualizado = np.array(archiveActualizado)
		archiveActualizado = np.unique(archiveActualizado)
		archiveActualizado = archiveActualizado.tolist()		
		#print "el archive esta compuesto por: "
		#for elem in archiveActualizado:
		#	print elem.solution,
		#print "termino addAndUpdate"
		return archiveActualizado


		#tamArchive = int(round(tamPob*0.2))
		#print tamArchive
		
		#En caso que sea mayor a un 20% del tamanio de la poblacion es necesario reducir!
		#TRASPASAR A FUNCION! IGUAL QUE LA PARTE DE REPETIDAS!
		
		#if len(archive) > tamArchive:
		#	print "MAYOR! A REDUCIR"
			#Si es mayor, elijo los miembros random (CAMBIAR Y PREGUNTAR SI HACERLO POR crowding distance)
		#	aux, aux_solution = [], []
		#	for i in range(tamArchive):
		#		elem = random.choice(archive)
		#		while elem.solution in aux_solution:
		#			elem = random.choice(archive)
		#		aux.append(elem)
		#		aux_solution.append(elem.solution)
		#		elem.visitado = 0
		#	del archive[:]
		#	archive = aux[:]
		#	del aux[:]
		#for elemento in archive:
		#	print elemento.solution, elemento.costoFlujo[0], elemento.costoFlujo[1], elemento.rank, elemento.crowdedDistance, elemento.visitado 

	
	def normalizarValores(self, poblacion, tamPob):
		maxMin = []
		for n_obj in range(0,self.numObjectives):
			objValues = []
			poblacion = self.sortCostoAssignacion(poblacion, n_obj)
			#for elem in poblacion:
			#	print elem.solution, elem.costoFlujo
			minValue = poblacion[0].costoFlujo[n_obj]
			maxValue = poblacion[tamPob-1].costoFlujo[n_obj]
			objValues.append(minValue)
			objValues.append(maxValue)
			maxMin.append(objValues)
			#print "obj2"
		minObj1 = maxMin[0][0]
		maxObj1 = maxMin[0][1]
		minObj2 = maxMin[1][0]
		maxObj2 = maxMin[1][1]
		difObj1 = maxObj1 - minObj1
		difObj2 = maxObj2 - minObj2
		poblacion_SR = []
		soluciones = []
		for elemento in poblacion:
			if elemento.solution not in soluciones:
				poblacion_SR.append(elemento)
				soluciones.append(elemento.solution)
		del soluciones[:]
		#print "pob sin repetidos"
		#for elem in poblacion_SR:
		#	print elem.solution, elem.costoFlujo

		#print minObj1, maxObj1, minObj2, maxObj2 
		
		normValues = []
		for elemento in poblacion_SR:
			values = []
			cost1 = elemento.costoFlujo[0]
			cost2 = elemento.costoFlujo[1]
			valueObj1 = (cost1 - minObj1 )/difObj1
			valueObj2 = (cost2 - minObj2)/difObj2
			values.append(valueObj1)
			values.append(valueObj2)
			normValues.append(values)
		print "valores normalizados"
		#for value in normValues:
		#	print value
		return normValues		




	def generarAlphaVecinos(self, sol, alpha):
		numFac = sol.numFacilities
		tamVecindario = (numFac*(numFac-1))/2
		cantVecinos = tamVecindario*alpha
		cantVecinos = int(round(cantVecinos))
		vecindad, posiciones = [], []
		for i in range(cantVecinos):
			posAux = []
			posRandom1 = random.randint(0, numFac-1)
			posRandom2 = random.randint(0, numFac-1)
			while posRandom1 == posRandom2:
				posRandom2 = random.randint(0, numFac-1)
			posAux.append(posRandom1), posAux.append(posRandom2)
			while ((posAux in posiciones) or posAux.reverse() in posiciones):
				posRandom1 = random.randint(0, numFac-1)
				posRandom2 = random.randint(0, numFac-1)
				while posRandom1 == posRandom2:
					posRandom2 = random.randint(0, numFac-1)
				posAux.append(posRandom1), posAux.append(posRandom2)
			posiciones.append(posAux)
			vecino = Solucion(numFac)
			vecino = self.swap(sol, posRandom1, posRandom2, numFac)
			costos = sol.costoAsignacionMovida(posRandom1, posRandom2)
			vecino.costoFlujo[0] = sol.costoFlujo[0] - costos[0]
			vecino.costoFlujo[1] = sol.costoFlujo[1] - costos[1]
			vecindad.append(vecino)

		#print len(vecindad)	
		#for elem in vecindad:
		#	print elem.solution, elem.costoFlujo[0], elem.costoFlujo[1]
		return vecindad	

	def generoVecinos(self, sol, numFac):
		vecindad, soluciones = [], []
		for i in range(numFac):
			for j in range(numFac):
				if i != j:
					vecino = Solucion(numFac)
					vecino = self.swap(sol, i, j, numFac)
					if vecino.solution not in soluciones:
						soluciones.append(vecino.solution)
						costos = sol.costoAsignacionMovida(i,j)
						vecino.costoFlujo[0] = sol.costoFlujo[0] - costos[0]
						vecino.costoFlujo[1] = sol.costoFlujo[1] - costos[1]
						vecindad.append(vecino)
						#print vecino.solution
		del soluciones[:]
		#print len(vecindad)
		return vecindad


	def binaryTournament(self,poblacion):
		participantes = random.sample(poblacion, 2)
		best = None
		for solParticipante in participantes:
			if (best is None) or self.crowdedComparisonOperator(solParticipante, best) == 1:
				best = solParticipante
		return best

	def sequentialConstructiveCrossover(self, sol, other):
		numFac = sol.numFacilities
		child = Solucion(numFac)
		soluciones = []
		soluciones.append(sol), soluciones.append(other)
		#print soluciones[0].solution, soluciones[1].solution
		sol.costoAsignacion(), other.costoAsignacion()
		#print "Costos iniciales de sol : ", sol.costoFlujo[0], sol.costoFlujo[1]
		#print "Costos iniciales de other: ", other.costoFlujo[0], other.costoFlujo[1]
		aux = random.choice(soluciones)
		locationP = aux.solution[0]
		#print aux.solution
		
		child.solution.insert(0, locationP)
		childAux1 = Solucion(numFac)
		childAux2 = Solucion(numFac)

		while len(child.solution) != len(sol.solution):

			nextElem = self.findNextLoc(soluciones[0], child, locationP, numFac)
			nextElem2 = self.findNextLoc(soluciones[1], child, locationP, numFac)

			childAux1.solution = child.solution[:]
			childAux2.solution = child.solution[:]


			childAux1.solution.append(nextElem)
			childAux2.solution.append(nextElem2)

			#print childAux1.solution, childAux2.solution
			childAux1.costoAsignacionParcial(nextElem)
			childAux2.costoAsignacionParcial(nextElem2)

			if funciones.dominance(childAux1, childAux2):
				
				child.solution = childAux2.solution[:]
				locationP = nextElem2
				del childAux1.solution[:]
				del childAux2.solution[:]

			elif funciones.dominance(childAux2, childAux1):
				child.solution = childAux1.solution[:]
				locationP = nextElem
				del childAux1.solution[:]
				del childAux2.solution[:]

			else:
				child.solution = childAux1.solution[:]
				locationP = nextElem
				del childAux1.solution[:]
				del childAux2.solution[:]

		child.costoAsignacion()		
		return child

	def findNextLoc(self, sol, child, locationP, numFac):
		index = sol.solution.index(locationP)
		#print "indice de location P: ", index
		for x in range(index+1, index+len(sol.solution)):
			elemento = sol.solution[x%numFac]
			if elemento in child.solution:
				continue
			else:
				return elemento


	def createNewPob(self, poblacion, indiceCX, indiceMut):
	
		print "Creating a new Population. . . "
		numFac = poblacion[0].numFacilities
		new_pob, rankedPop, restPop = [], [], []
		for elemento in poblacion:
			if elemento.rank == 1:
				rankedPop.append(elemento)
				new_pob.append(elemento)
			else:
				restPop.append(elemento)
		#AQUI SETEO EL % DE RANDOM
		indiceRand = 0.2
		indiceCruz = 1 - indiceRand
		largoRestante = len(poblacion)-len(new_pob)
		cantidadCX = int(round(largoRestante * indiceCruz))
		cantidadRand = int(round(largoRestante*indiceRand))
		for i in range(1, cantidadCX+1):
			child = Solucion(numFac)
			solSeleccionadas = [None, None]
			for i in range(2):
				sol1 = random.choice(rankedPop)
				sol2 = random.choice(restPop)
				if crowdedComparisonOperator(sol1, sol2) > 0:
					solSeleccionadas[i] = sol1
				else: 
					solSeleccionadas[i] = sol2
			if indiceCX == 1:
				if random.random() < self.crossoverRate:
					child = self.sequentialConstructiveCrossover(solSeleccionadas[0], solSeleccionadas[1])
			elif indiceCX == 2:
				if random.random() < self.crossoverRate:
					child = self.onePointCrossover(solSeleccionadas[0], solSeleccionadas[1])
			if indiceMut == 1:
				if random.random() < self.mutationRate:
					child = self.twOptSearch(child)
			elif indiceMut == 2:
				if random.random() < self.mutationRate:
					child = self.threExchangeMutation(child)
			new_pob.append(child)
		for i in range(1, cantidadRand+1):
			randomChild = Solucion(numFac)
			randomChild = funciones.generarSolucionRandom(randomChild, numFac)
			randomChild.costoAsignacion()
			new_pob.append(randomChild)
		del rankedPop[:]
		del restPop[:]

		return new_pob






	#pobRef = []
	#for elem in pobReferencia:
	#	pobRef.append(elem.costoFlujo)
	#refAux = []
	#refAux = pobRef[:]	
	#for elem in pobEvaluada:
	#	if elem in refAux:
	#		refAux.remove(elem)
	#for elem in pobEvaluada:
	#	sol = Solucion(numFac)
	#	sol.costoFlujo = elem[:]
	#	pobEv.append(sol)
	#for elem in refAux:
	#	sol = Solucion(numFac)
	#	sol.costoFlujo = elem[:]
	#	pobRef2.append(sol)
	#counter = 0
	#for solP in pobEv:
	#	for solQ in pobRef2:
	#		if funciones.weaklyDominance(solQ,solP):
	#			#print solQ.costoFlujo, solP.costoFlujo
	#			counter += 1.0
	#			break
	#		else:
	#			#print solP.costoFlujo, solQ.costoFlujo
	#			continue
	#largo = float(len(pobEv))
	#if largo == 0:
	#	result = 1.0
	#else:
	#	result = counter/largo
	#print "Cobertura: ",result
	#return result