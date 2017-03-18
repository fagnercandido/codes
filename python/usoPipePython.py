#! /usr/bin/python
#	Autor: fagner candido - f_Candido - fagner7777777@gmail.com
#	Objetivo : Demonstra o uso de IPC em Python
#	Entrada : ?
#	Saida : os comandos

#importa o modulo necessario
import popen2

#Arquivos necessarios
saidaPs, entradaPs = popen2.popen2('ps aux')
saidaHead, entradaHead = popen2.popen2('head')


#Entrada do ps nao e necessario
entradaPs.close()
#Saida do ps vai para a variavel saida
saida = saidaPs.readlines()
#Fechamos o processo correspondente ao ps
saidaPs.close()
#Grep espera uma entrada
entradaHead.writelines(saida)
#Fechando a entrado do grep
entradaHead.close()
# saida do head
print str().join(saidaHead.readlines())
#Finalizamos head
saidaHead.close()








