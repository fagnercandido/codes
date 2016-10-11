'''
	Sintese
		Objetivo : Servidor para envio/recebimento de arquivos
		Entrada : Um possivel arquivo
		Saida : Um possivel arquivo
		Autor : f_Candido - fagner7777777@gmail.com
'''

import socket

class Server():

	'''
		Construtor
		hostServer - Servidor para conexoes
		portServer - Porta para conexao
		tcp - Conexao TCP que sera aberta
		orig - Origem da conexao
	'''
	
	def __init__(self):
		self._hostServer = '127.0.0.1'        # Endereco IP do Servidor
		self._portServer = 7777            # Porta que o Servidor esta
		self._tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._orig = (self._hostServer, self._portServer)
		self._tcp.bind(self._orig)
		self._tcp.listen(999999)	
		self._nameFile = ''
		print __doc__
	'''
		Recebido o pacote, ele retira o cabecalho e retorna o real conteudo
	'''
	def breakPackage(self):

		self._tmp = self._msg.split('__##')
		self._nameFile = self._tmp[0]
		self._msg = self._tmp[1]
		
	'''
		Recebe o arquivo
	'''
	def receiveFile(self):
		self._connection, self._client = self._tcp.accept()
		print 'Conectado por', self._client
		while True:
		        self._msg = self._connection.recv(4096)
			if not self._msg: break
			self.breakPackage()
			self.writeFile()			
			

	'''
		Escreve o arquivo em disco
	'''
	def writeFile(self):
		self._fileOpen = open(self._nameFile, "w")
		self._fileOpen.write(self._msg)
		self._fileOpen.close()	


	'''
		Fecha a conexao
	'''
	def closeConnection(self):
    		self._connection.close()


objServer = Server()
objServer.receiveFile()
objServer.closeConnection()
