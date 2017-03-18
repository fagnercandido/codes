#!/usr/bin/python
# -*- coding: utf-8 -*-
# Sintese
#	Objetivo :  Implementar uma lista encadeada simples
#	Entrada : Um valor qualquer
#	Saida: ...
#	Autor: Fagner Candido - f_Candido
#	Contato: fagner7777777@gmail.com
class ListaEncadeada:
	# Declaracao dos atributos desta Classe
	valorOrbital = None
	proximo = None
	# Fim declaracao


	# Nesta secao encontram-se os metodos para acesso
	# dos respectivos atributos
	def getValorOrbital(self):
		return(self.valorOrbital)
	def getProximo(self):
		return(self.proximo)
	def setValorOrbital(self, valorOrbital):
		self.valorOrbital = valorOrbital
	def setProximo(self, proximo):
		self.proximo = proximo
	# Fim declaracao Metodos Get e Set	


	# Metodo para Insercao 
	def insereInicio(self, raiz, valorOrbital):
		temporario = ListaEncadeada()
		# o atributo proximo aponta para o atributo
		# proximo da raiz	
		temporario.setProximo(raiz.getProximo())
		temporario.setValorOrbital(valorOrbital)
		# o atributo proximo da raiz, aponta para temporario
		raiz.setProximo(temporario)
	# Fim insercao


	# Metodo para percorrer lista
	def percorreListaEncadeada(self, raiz):
		temporario = ListaEncadeada()	
		temporario = raiz.getProximo()
		while(temporario != None):
			print temporario.getValorOrbital()
			# incremento do temporario
			temporario = temporario.getProximo()
	# Fim percorrimento


	# Metodo para remocao
	def removeInicio(self, raiz):
		temporario = ListaEncadeada()
		temporario = raiz.getProximo()
		print temporario.getValorOrbital()
		raiz.setProximo(temporario.getProximo())
		temporario = None
	# Fim remocao
