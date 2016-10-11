'''
	Sintese :
		Objetivo : Determinar os numeros perfeitos
		Entrada : n valores
		Saida : Numeros que se enquadram na condicao
		Autor :
			f_Candido
			@fagner_candido
			fagner7777777@gmail.com

'''
import time

class NPerfeitos:
	
		
	def __init__(self):
		self.totalSomatorio = 0
		self.valorInicial = 30
		self.contador = 2
		self.listaSomatorio = [1]	
		
	def calcula(self):
		'''
			Metodo que que calcula os numeros perfeitos
		'''
		while(True):
			if self.contador == self.valorInicial:
				self.totalSomatorio = self.somatorio(self.listaSomatorio)
				if self.totalSomatorio == self.valorInicial:
					print self.valorInicial
					time.sleep(2)
					self.alteraAtributos()
				else:
					print self.valorInicial
					self.alteraAtributos()
			if self.isDivisivel(self.valorInicial, self.contador):
				self.listaSomatorio.append(self.contador)
			self.contador = self.contador + 1
	
	def isDivisivel(self, dividendo, divisor):
		'''
			Metodo que compara a divisibilidade
		'''
		if((dividendo%divisor) == 0):
			return True
		else:
			return False

	def somatorio(self, lista):
		'''
			Metodo que realiza o somatorio
		'''
		somatorioTotal = 0
		for auxiliar in lista:
			somatorioTotal = somatorioTotal + auxiliar
		return somatorioTotal

	def alteraAtributos(self):
		'''
			Reinicializa os atributos
		'''
		self.valorInicial = self.valorInicial + 1
		self.contador = 2
		self.listaSomatorio = []
		self.listaSomatorio.append(1)
		self.totalSomatorio = 0

objNPerfeitos = NPerfeitos()
objNPerfeitos.calcula()
