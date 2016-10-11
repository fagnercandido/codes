'''
	Sintese:
 		Objetivo: Manipular arquivos csv
		Entrada: Um arquivo csv
		Saida: Um arquivo csv
		Autor: Fagner Candido - f_Candido - fagner7777777@gmail.com
'''
# Importacao do CSV
import csv

class WorkCSV:
	
	fileCSV = ''

	# Imprime a docString associada
	def printDocString(self):
		print __doc__
	# Le o arquivo especificado
	def openCSV(self, nameFile, delimitador):
		self.fileCSV = csv.reader(open(nameFile), delimiter=delimitador)
	# Escrevee no arquivo especificado
	def writeCSV(self, nameFile, row):
		self.fileCSV = csv.writer(open(nameFile, "a"))
		self.fileCSV.writerow(row)
	# Percorre o Arquivo
	def listCSV(self):
		for [fNome, mNome, lNome] in self.fileCSV:
			print 'Primeiro Nome = %s - Nome do Meio = %s - Ultimo Nome = %s' % (fNome, mNome, lNome)
	


obj = WorkCSV()
obj.printDocString()
obj.openCSV('files', ',')
obj.listCSV()
row = ['ronaldo','ronaldo','ronaldo']
obj.writeCSV('files', row)
