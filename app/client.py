
from app.model import load_model
from app.helper_text import main_clean

def compute_polarity(txt):
	brexitmeter_model = load_model()

	x, x_s = main_clean(txt)

	result = brexitmeter_model.predict([x, x_s])

	return result


if __name__ == "__main__":

	user_text = input("Your Text: ")

	result = compute_polarity(user_text)

	polarity_pro = result[:,1]

	print(f"This text is {polarity_pro} Pro Brexit")

	#breakpoint()
