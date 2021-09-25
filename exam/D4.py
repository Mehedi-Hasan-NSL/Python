class Traslator:
	def predict(self, text):
		pass

translator = Traslator()

def predict_bangla_text_to_english_text(bangla_text):
	english_text = translator.predict(bangla_text)
	return english_text

"""
If we want improve this API for frequent search we 
can use Memoization, means we can create a memory of 
previous search 

"""
memory = dict()

def predict_bangla_text_to_english_text_efficient(bangla_text):
	if bangla_text not in memory:
		memory[bangla_text] = translator.predict(bangla_text)
	return memory[bangla_text]

"""

it wil create a dictionary of translated words 
for frequent search it will be efficient

"""