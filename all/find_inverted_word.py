text = 'As abc res obn nbo til tytty tytyytyt sa.'

def find_inverted_word(text):
	text = text.lower()
	all_words = text.split()

	if '.' in all_words[-1]:
		index = all_words[-1].index('.')
		all_words[-1] = all_words[-1][:index]
		print('after replace:', all_words[-1])

	print('all words:', all_words)
	for word in all_words:
		
		one_couple = []
		inverted_word = ''
		counter = len(word)
		while counter > 0:
			inverted_word += word[counter-1]
			counter -= 1

		print(word, '-', inverted_word)
		if inverted_word in all_words:

			one_couple.append(word)
			one_couple.append(inverted_word)

			return one_couple
	return 0

print(find_inverted_word(text))

