
from app.model import load_model
from app.helper_text import main_clean

def compute_polarity(txt, model=load_model()):
	"""
	Params:
		txt is the text to classify
		model is the model used to perform the classification
	"""
	x, x_s = main_clean(txt)

	result = model.predict([x, x_s])

	return result


if __name__ == "__main__":

	model = load_model()

	while True:

		user_text = input("Your Text (press ENTER at any time to quit): ")
		if user_text == "": break

		result = compute_polarity(user_text, model)

		polarity_pro = result[:,1]

		print(f"This text is {polarity_pro} Pro Brexit")

	#breakpoint()
