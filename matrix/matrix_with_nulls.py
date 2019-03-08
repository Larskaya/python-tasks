row = 7
column = 7

def make_matrix(row, column):

	matrix = []
	counter_row = 0
	while counter_row < row:

		one_str = []
		counter_column = 0
		while counter_column < column:

			if counter_column == 0 or counter_column == column-1:
				one_str.append(1)

			elif counter_row == 0 or counter_row == row-1:
				one_str.append(1)

			else:
				one_str.append(0)

			counter_column += 1
		matrix.append(one_str)
		counter_row += 1

	return matrix

#print(make_matrix(row, column))

matrixFilter = lambda counter_row, counter_column: int(counter_column == 0 or counter_column == column-1 or counter_row == 0 or counter_row == row-1)
d = [[matrixFilter(i, k) for k in range(0, column)] for i in range (0, row)]

print('d:')
print(d)



