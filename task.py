# coding=utf-8

class Matrix(object):
	def __init__(self, listOfData):
		super(Matrix, self).__init__()
		self.listOfData = [[listOfData[0], listOfData[1]],
											 [listOfData[2], listOfData[3]]]

	def set(self, row, col, value):
		self.listOfData[row][col] = value

	def add(self, toAdd):
		return Matrix([self.listOfData[0][0]+toAdd.listOfData[0][0],
			self.listOfData[0][1]+toAdd.listOfData[0][1],
			self.listOfData[1][0]+toAdd.listOfData[1][0],
			self.listOfData[1][1]+toAdd.listOfData[1][1]])		

	def multiply(self, toMultiply):
		result = Matrix([0,0,0,0])
		for i in range(0,3):
			for j in range(0,3):
				for k in range(0,3):
					result.set(i, j, (self.listOfData[i][k]*toMultiply.listOfData[k][j]))
		return result

