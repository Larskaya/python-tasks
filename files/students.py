file = open('students.txt', 'r')
students = file.readlines()
answer = ''

# ['Артем 3\n', 'Валера 5\n', 'Геннадий 4\n', 'Мария 3\n', 'Алиса 5']
def get_dict_of_students(students):
	students_with_grades = {}
	for student_with_num in students:
		student_with_num = student_with_num.split()

		students_with_grades[student_with_num[0]] = str(student_with_num[1])
	return students_with_grades

dict_of_students = get_dict_of_students(students)
print('get dict of students:', dict_of_students)

def get_names_with_increase_letters(students_with_grades):
	names_of_students = []
	for name in students_with_grades.keys():

		if int(students_with_grades[name]) > 4:
			names_of_students.append(name.upper())
		else:
			names_of_students.append(name)

	return names_of_students

students_without_grades = get_names_with_increase_letters(dict_of_students)
print('after upper', students_without_grades)


def find_need_names(students_without_grades, dict_of_students):
	answer = ''
	for st1 in students_without_grades:
		for st2 in dict_of_students:

			if st1.lower() == str(st2):
				#print(st1, 'ST1')
				answer += st1 + ' ' + dict_of_students[st2] + '\n'
	return answer

need_names = find_need_names(students_without_grades, dict_of_students)

after_program = open('students.txt', 'w')
after_program.writelines(need_names)
after_program.close()

# составить словари учеников и оценок
# перебрать составленный словарь каждое имя которого класть в новый список
# имена учеников с оценкой 5 писать заглавными буквами
