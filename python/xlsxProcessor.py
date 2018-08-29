from openpyxl import Workbook
import openpyxl
from openpyxl.compat import range
from openpyxl.utils import get_column_letter
from os import listdir
from os.path import isfile, join

def findList(coluna, colunaAtiva):
	sqlPartial = []
	for iterador in range(len(colunaAtiva)):
		if coluna == "A":
			sqlPartial.append(' STRING '+str(colunaAtiva[iterador].value)+';')
			#print(' WHERE [EST_CD] = '+str(colunaAtiva[iterador].value))
		if coluna == "C":
			sqlPartial.append(', STRING '+str(colunaAtiva[iterador].value))
			#print(' , SET [EST_NU_COTAMAXIMA] = '+str(colunaAtiva[iterador].value))
		if coluna == "D":
			sqlPartial.append(' UPDATE STRING '+str(colunaAtiva[iterador].value))
			#print(' UPDATE [GDHTB].[ESTACAO] SET [EST_NU_COTAMINIMA] = '+str(colunaAtiva[iterador].value))
	return sqlPartial

arquivos = [f for f in listdir('.') if isfile(join('.', f))]
arquivos.remove('xlsxProcessor.py')
arquivos.remove('saida')
file = open("saida", "a+")
for arquivo in arquivos:
	wb = openpyxl.load_workbook(filename=arquivo)
	sheets = wb.get_sheet_names()
	for sheet in sheets:
		sqls = []
		colunas = ['D', 'C', 'A']
		sheetAtiva = wb[sheet]
		for coluna in colunas:
			colunaAtiva = sheetAtiva[coluna]
			sqls.append(findList(coluna, colunaAtiva))
		totalLinhas = len(sqls[0])
		for contador in range(totalLinhas):
			print(sqls[0][contador]+sqls[1][contador]+sqls[2][contador])
			file.write(sqls[0][contador]+sqls[1][contador]+sqls[2][contador]+"\n")
file.close()