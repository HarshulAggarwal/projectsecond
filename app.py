import pandas as pd
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

indian_food_df = pd.read_csv('indian_food.csv')
cleaned_data_df = pd.read_csv('cleaned_data.csv')
model_data_df = pd.read_csv('model_data.csv')

with open('model.pickle', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    top_foods = indian_food_df.head(10)
    foods_list = top_foods.to_dict(orient='records')
    return render_template('index.html', foods=foods_list)

@app.route('/predict', methods=['POST'])
def predict():
    ingredient_input = request.form.get('ingredient')
    input_data = model_data_df[model_data_df['ingredient_name'] == ingredient_input]
    prediction = model.predict(input_data)
    return render_template('prediction_result.html', ingredient=ingredient_input, prediction=prediction[0])

if __name__ == "__main__":
    app.run(debug=True)
