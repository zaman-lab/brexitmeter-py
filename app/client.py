
from app.storage_service import BOT_ENV
from app.model import load_model
from app.helper_text import main_clean

def compute_polarity(txt, model):
	"""
	Params:
		txt is the text to classify
		model is the model used to perform the classification
	"""
	x, x_s = main_clean(txt)

	result = model.predict([x, x_s])

	return result

def classify(txt, model):
	#result = compute_polarity(user_text, model)
	x, x_s = main_clean(txt)
	result = model.predict([x, x_s])
	polarity_pro = result[:,1] # or result[0][1]
	#polarity_pro = result[0][1]
	print(f"This text is {polarity_pro} Pro Brexit")
	return polarity_pro

if __name__ == "__main__":

	model = load_model()
	print("MODEL", type(model))

	if BOT_ENV=="production":
		user_text = "Example: I want the UK to stay EU #remain #remain #remain"
		polarity = classify(user_text, model)
		print("RESULT:", polarity)
	else:
		while True:
			user_text = input("Your Text (press ENTER at any time to quit): ")
			if user_text == "": break
			polarity = classify(user_text, model)
			print("RESULT:", polarity)

	#breakpoint()
