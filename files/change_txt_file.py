f = open('text.txt', 'r')
lines = f.readlines()
no_even_nums = ''
print('lines:', lines)
data = ''
data += lines[0]
data = data.split()
for num in data:
	print(num)
	if int(num) % 2 != 0:
		no_even_nums += num + ' '
f.close()

file_without_even_numbers = open('text.txt', 'w')
file_without_even_numbers.writelines(no_even_nums)
file_without_even_numbers.close()