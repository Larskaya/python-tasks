matrix = [ ['a', 2, 3],
			[1, 'b', 3],
			[1, 2, 'c'] ]

counter_of_lists = 0
counter_of_num_in_list = 0
diagonal_numbers = []

while counter_of_lists < len(matrix):

	diagonal_numbers.append( matrix[counter_of_lists][counter_of_num_in_list] )

	counter_of_num_in_list += 1
	counter_of_lists += 1

print('answer:', diagonal_numbers)