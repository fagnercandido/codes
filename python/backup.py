#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

# Síntese 
	# Objetivo : Criar backups de diretórios
	# Entrada : Diretórios - origem/destinho
	# Saída : Mensagem de confirmação
	# Autor : f_Candido - fagner7777777@gmail.com

import sys
import os

class Backup:
   # Lista que receberá os argumentos
   listaArgumentos = []
   contador = 0
   #Recebendo os argumentos
   for contaArgumentos in sys.argv:
      listaArgumentos.append(contaArgumentos)
      contador = contador + 1
   #Valida a entrada
   if contador != 3:
      print "Argumentos invalidos"
      sys.exit()
   #Faz a cópia
   os.system("cp -R "+listaArgumentos[1]+" "+listaArgumentos[2])
