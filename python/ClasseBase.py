#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

# Síntese
   # Objetivo : Demonstrar o uso de Herança
   # Entrada : 
   # Saída : 
   # Autor : f_Candido - fagner7777777@gmail.com

# Classe-Base
class ClasseBase:
	# Definição de alguns metódos
	def soma(self, valorA, valorB):
		print "A soma e : \n", valorA + valorB
	def mostrar(self, nome):
		print nome

# Classe que especializa ClasseBase
# em Python, se dá atráves desta notação
# classeQueIraEspecializar(ClasseGenerica)
class ClasseEspecifica(ClasseBase):
	# Sobrescrita do metódo - Polimorfismo
	def soma(self, valorA, valorB):
		print "A soma e : \n", valorA*valorB

#Execução Exemplo
objEspecifico = ClasseEspecifica()
objEspecifico.soma(3, 5)
objBase = ClasseBase()
objBase.soma(3, 5)
