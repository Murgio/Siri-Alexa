import random

answers = ['I did not understand what you just said',
			'It doesn\'t look like anything to me',
			'I don\'t know, whatever']

while True:
	user_input = input(">>> ")
	if user_input.lower() == 'hi':
		print("Hello")
	else:
		print(random.choice(answers))