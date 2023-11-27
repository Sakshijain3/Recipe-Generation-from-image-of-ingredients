# from flask import Flask, render_template, request
# from transformers import pipeline
# import torch

# app = Flask(__name__)

# model_name_or_path = "flax-community/t5-recipe-generation"
# recipe_generator = pipeline(
#     "text2text-generation",
#     model=model_name_or_path,
#     tokenizer=model_name_or_path,
#     device=0 if torch.cuda.is_available() else -1
# )

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/generate', methods=['POST'])
# def generate_recipe():
#     prompt = request.form['prompt']
#     recipe = recipe_generator(prompt, max_length=100)
#     return render_template('index.html', recipe=recipe[0]['generated_text'])

# if __name__ == '__main__':
#     app.run(debug=True)

# let the above lines be commented or you can delete the above lines

## start from here
# from flask import Flask, render_template, request
# from transformers import pipeline
# import torch

# app = Flask(__name__)

# model_name_or_path = "flax-community/t5-recipe-generation"
# recipe_generator = pipeline(
#     "text2text-generation",
#     model=model_name_or_path,
#     tokenizer=model_name_or_path,
#     device=0 if torch.cuda.is_available() else -1
# )

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         prompt = request.form['input']
#         recipe = recipe_generator(prompt, max_length=100)
#         return render_template('index.html', output=recipe[0]['generated_text'])
#     else:
#         return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)


#  flask app with recipe generation and TTS

from flask import Flask, render_template, request
from transformers import pipeline
import pyttsx3
import torch

app = Flask(__name__)

model_name_or_path = "flax-community/t5-recipe-generation"
recipe_generator = pipeline(
    "text2text-generation",
    model=model_name_or_path,
    tokenizer=model_name_or_path,
    device=0 if torch.cuda.is_available() else -1
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def generate_recipe():
    if request.method == 'POST':
        prompt = request.form['prompt']
        recipe = recipe_generator(prompt, max_length=100)
        return render_template('index.html', recipe=recipe[0]['generated_text'])
    else:
        return render_template('index.html')

# @app.route('/', methods=['POST'])
# def text_to_speech():
#     if request.method == 'POST':
#         recipe = request.form['recipe']
#         engine = pyttsx3.init()
#         engine.say(recipe)
#         engine.runAndWait()
#         return render_template('index.html', recipe=recipe, tts=True)
#     else:
#         return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
