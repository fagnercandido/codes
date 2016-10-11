'''
	Sintese
		Objetivo : Cliente para envio/recebimento de arquivos
		Entrada : Um possivel arquivo
		Saida : Um possivel arquivo
		Autor : f_Candido - fagner7777777@gmail.com
'''

import socket


class Client:

	'''
		Construtor
		host - Servidor para conexoes
		port - Porta para conexao
		tcp - Conexao TCP que sera aberta
		dest - Destino para conexao
	'''
	def __init__(self):	
		print __doc__
		self._host = '127.0.0.1'     # Endereco IP do Servidor
		self._port = 7777            # Porta que o Servidor esta
		self._tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._dest = (self._host, self._port)
		self._tcp.connect(self._dest)
		self._nameFile = 'teste.doc'
	'''
		Fechando a conexao TCP
	'''

	def closeConnection(self):
		self._tcp.close()
		
	'''
		Enviando o arquivo
	'''

	def sendFile(self):
		self._tcp.send (self._texto)

	'''
		Lendo o arquivo do fileSystem
	'''

	def readFile(self):
		self._fileOpen = open(self._nameFile, "r")
		self.mountPackage()
		self._tmp = self._fileOpen.read()
		self._texto = self._texto + self._tmp
		self._fileOpen.close()

	'''	
		E criado uma especie de pacote para envio
		Nele sao enviados o nome do arquivo e seu conteudo
		Tambem e criado uma marcacao para tal : __##
	'''

	def mountPackage(self):
		self._texto = self._nameFile+'__##'
		print self._texto


objClient = Client()
objClient.readFile()
objClient.sendFile()
objClient.closeConnection()
		

