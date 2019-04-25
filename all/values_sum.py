start_values = [0, 2, 3, 4, 5, 0]

odd = []
sum_of_extreme_el = 0
odd = list(filter(lambda x: x % 2 == 1, start_values))
sum_of_extreme_el = start_values[0] + start_values[-1]
num_greater_sum = list(filter(lambda x: x > sum_of_extreme_el, odd))
answer = 0
for el in num_greater_sum:
	answer += el
print('answer:', answer)