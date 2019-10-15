
from app import APP_ENV
from app.model import load_model
from app.helper_text import main_clean

def classify(txt, model):
	"""
	Params:
		txt is the text to classify
		model is the model used to perform the classification
	"""
	x, x_s = main_clean(txt)
	results = model.predict([x, x_s]) #> array([[0.57155126, 0.42844874]], dtype=float32)
	results = results[0] #> array([0.57155126, 0.42844874], dtype=float32)
	response = {"text": txt, "pro_brexit": results[1]}
	return response

if __name__ == "__main__":

	model = load_model()

	if APP_ENV=="production":
		example_texts = [
			"I want the UK to stay EU #remain #remain #remain",
			"I want the UK to leave EU #BrexitNow",
		]
		for txt in example_texts:
			results = classify(user_text, model)
			print(results)
	else:
		while True:
			user_text = input("Your Text (press ENTER at any time to quit): ")
			if user_text in ["", "exit", "exit()"]: break
			results = classify(user_text, model)
			print(results)
