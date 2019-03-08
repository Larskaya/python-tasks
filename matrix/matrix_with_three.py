# [ [3, 2, 2, 2, 2]
#	[1, 3, 2, 2, 2]
#	[1, 1, 3, 2, 2]
#	[1, 1, 1, 3, 2]
#	[1, 1, 1, 1, 3] ]

rows = 5
columns = 5

def add_nulls(rows, columns):
	matrix = []

	counter_columns = 0
	counter_rows = 0
	while counter_rows < rows:

		one_str = []
		while counter_columns < columns:
			one_str.append(1)
			counter_columns += 1

		print(one_str)
		counter_columns = 0
		matrix.append(one_str)
		counter_rows += 1

	print('first:', matrix)
	return matrix

def change_diagonal(matrix):

	counter_for_diagonal = 0
	while counter_for_diagonal < len(matrix):
		matrix[counter_for_diagonal][counter_for_diagonal] = 3
		counter_for_diagonal += 1

	return matrix

def change_for_two(matrix):
	for list_ in matrix:
		main_counter = 0
		index_of_three = list_.index(3)
		print('index of three:', index_of_three)

		counter = index_of_three
		while counter < len(list_):
			print('counter', counter)
			if counter > index_of_three:
				print('true')
				list_[counter] = 2
			counter += 1
		main_counter += 1
	print(matrix)
	return matrix

def get_matrix(rows, columns):
	with_nulls = add_nulls(rows, columns)
	matrix_with_change_diagonal = change_diagonal(with_nulls)

	answer = change_for_two(matrix_with_change_diagonal)
	return answer

print(get_matrix(rows, columns))

matrix_filter = lambda a, b: 3 if a == b else 1 if a > b else 2
m = [[matrix_filter(r, c) for c in range(0, columns)] for r in range (0, rows)]
print('m:')
print(m)





