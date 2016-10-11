class Fatorial:
	total = 1
	def calcula(self, valor):
		if valor == 0:
			return 1
		self.total = (valor)*self.total
		self.calcula(valor-1)

	def printTotal(self):
		print self.total



objFatorial = Fatorial()
objFatorial.calcula(0)
objFatorial.printTotal()
