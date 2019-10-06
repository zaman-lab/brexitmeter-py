from model import load_model
from helper_text import main_clean

if __name__ == "__main__":

	brexitmeter_model = load_model()

	twt = input("Tweet Text: ")

	x, x_s = main_clean(twt)

	result = brexitmeter_model.predict([x, x_s])

	polarity_pro = result[:,1]
	print(f"This tweet is {polarity_pro} Pro Brexit")

	#breakpoint()
