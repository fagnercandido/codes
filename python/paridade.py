#! /usr/bin/python
#Autor: Fagner Candido
#Objetivo : Verifica paridade de Numeros
#Entrada : Um inteiro
#Saida : A paridade do numero
#Leitura do Valor
numero = int(raw_input("Informe o Valor : "))
#O condicional verifica: Caso o modulo de zero, e par
if ((numero % 2) == 0):
   print 'O numero e par'
#Caso contrario e impar
else:
   print 'O numero e impar'