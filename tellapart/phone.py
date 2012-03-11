'''
Input: a phone number, of variable length
Output: all possible combinations of letters you could make with that phone number, 
by pressing the letters on the phone keypad
'''

class Phone():

	def __init__(self):
		self.words = []
		self.english_words = []					
			
	def get_combos(self, phone_num, seq):
		if not phone_num:
			self.words.append(seq)
			return
		letters = Phone.get_letters(phone_num[0]) 
		if not letters:
			self.get_combos(phone_num[1:], seq)
		else:
			for l in letters:
				self.get_combos(phone_num[1:], l + seq)

	@staticmethod
	def get_letters(num):
		keypad = [
		[], #0
		[], #1
		['a','b','c'],
		['d','e','f'],
		['g','h','i'],
		['j','k','l'],
		['m','n','o'],
		['p','q','r','s'], #7
		['t','u','v'],
		['w','x','y','z'] #9
		]    
		return keypad[int(num)]
    
if __name__ == '__main__':
	p = Phone()
	p.get_combos('2902', '')
	print p.words
