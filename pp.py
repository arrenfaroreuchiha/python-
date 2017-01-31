# *-* coding: utf:-8 -*-

print "suma, resta, multiplicacion y divicion"

class itachi():
	def naruto(self):
		cantidad = int(raw_input("cantidad de numeros:"))
		return cantidad

	def hinata(self, cantidad):
		contador = 0
		divicion = 0
		contador1 = 1
		vector = []
		print "elija si es suma=1, resta=2, multiplicacion=3, divicion=4"
		eleccion = int(raw_input("que opccion elijes:"))
		while eleccion == 0 or eleccion > 4:
			print "elija con los numeros que le indique"

		if eleccion == 1:
			for i in range(cantidad):
				numero = int(raw_input("cual es el numero:"))
				contador = contador + numero
				vector.insert(i, numero)
				vector.sort()
			print "la suma es:", contador
			print "este es el vector", vector
		
		if eleccion == 2:
			for i in range(cantidad):
				numero = int(raw_input("cual es el numero:"))
				contador = contador - numero
			print "esta es la resta:", contador


		elif eleccion == 3:
			for i in range(cantidad):
				numero = int(raw_input("cual es el numero:"))
				contador1 = contador1 * numero
			print "esta es la multiplicacion:", contador1

		elif eleccion == 4:
			for i in range(cantidad):
				numero = int(raw_input("cual es el numero:"))
				contador = contador + numero
				divicion = contador / cantidad
			print "esta es la divicion:", divicion



sasuke = itachi()
lee = sasuke.naruto()
lista = sasuke.hinata(lee)
