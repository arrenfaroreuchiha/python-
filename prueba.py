# -*- coding: utf-8 -*-

# esta es mi primera variable en python
cadena = "Hola mundo"

multiples_lineas = """ Hola
						mundo como estas niño"""

a = True

b = False # use esto para ser falso 

a = 2 ** 3

""" Esto es un comentario de python y
		 no se ve nunca en la aplicación """

b = 27 % 4
numero = 2
numero2 = 3
numero3 = 2
if numero == numero2:
	print "Los numeros son iguales"
elif numero == numero3:
	print "Los numeros son iguales", numero, numero3
else:
	print "Los unumeros son diferentes"

# estos son los ciclos 
anio = 2001
while anio <= 2012:
    print "Informes del Ano", str(anio)
    anio += 1


lista = ['Juan', 'Antonio', 'Pedro', 'Herminio']

for nombre in lista:
    print nombre

for numero in range(1, 1