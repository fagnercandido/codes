# Sintese :
#	Objetivo : Demonstrar o uso do modulo pdb
#	Entrada : ?
#	Saida : ?
#	Autor : fagner candido - f_Candido - fagner7777777@gmail.com
#Obs : para ir para proximoa linha analizada tecle e "n" e de enter
#      para listar, "l" e enter

#Aqui chamamos o modulo
import pdb

#Chamamos o metodo para analisar o programa
pdb.set_trace()

#Atributos
nome = ""
idade = 0

#Leitura dos dados
print "Informe seu nome : "
nome = raw_input()
print "Informe sua idade"
idade = raw_input()

#Apresentado os resultados
print "Seu nome e :", nome
print " e sua idade : ", idade
