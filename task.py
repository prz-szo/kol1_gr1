from math import sqrt


class Matrix:
	def __init__(self, *numbers):
		matrix_size = sqrt(len(numbers))
		if matrix_size.is_integer():
			self.list_of_data = list(numbers)
			self.matrix_size = int(matrix_size)
		else:
			raise ValueError('Cannot create Matrix from those arguments!')

	@staticmethod
	def construct(*numbers):
		matrix_size = sqrt(len(numbers))
		if matrix_size.is_integer():
			return Matrix(*numbers)
		else:
			raise ValueError('Cannot create Matrix from those arguments!')

	def add(self, to_add):
		if (self == to_add):
			return Matrix(*[self[x]+to_add[x] for x in range(self.matrix_size**2)])
		else:
			raise ValueError('Cannot add diffrent size matrices!')

	def __add__(self, to_add):
		if type(to_add) == Matrix:
			return self.add(to_add)
		elif type(to_add) == str:
			raise ValueError('Cannot adding string to the Matrix!')
		else:
			matrix_of_value = Matrix(*(to_add for x in range(self.matrix_size**2)))
			return self.add(matrix_of_value)

	def __radd__(self, to_add):
		return self + to_add

	def multiply_by(self, to_multiply):
		if (self == to_multiply):
			size = self.matrix_size
			result_matrix = Matrix(*(0 for x in range(size**2)))
			for row in range(size):
				for col in range(size):
					value_of_result_matrix = 0
					for k in range(size):
						value_of_result_matrix += self[row*size + k] * to_multiply[k*size + col]
					result_matrix[row*size + col] = value_of_result_matrix
			return result_matrix
		else:
			raise ValueError("Cannot multiplying diffrent size matrices")

	def __mul__(self, to_multiply):
		if type(to_multiply) == Matrix:
			return self.multiply_by(to_multiply)
		elif type(to_multiply) == str:
			raise ValueError('Cannot multiplying Matrix with the Matrix!')
		else:
			matrix_of_value = Matrix(*(to_multiply for x in range(self.matrix_size**2)))
			return self.multiply_by(matrix_of_value)

	def __rmul__(self, to_multiply):
		return self * to_multiply

	def __str__(self):
		size = self.matrix_size
		return "\n".join([" ".join(
			["{}".format(self[row*size + col]) for col in range(size)]) for row in range(size)])

	def __getitem__(self, index):
		return self.list_of_data[index]

	def __setitem__(self, index, value):
		self.list_of_data[index] = value

	def __eq__(self, another_matrix):
		return self.matrix_size == another_matrix.matrix_size

if __name__ == "__main__":
	import main
