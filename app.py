import pandas as pd
from flask import Flask, request, render_template
import numpy as np
import pickle

# Load models
dtr = pickle.load(open('dtr.pkl', 'rb'))
preprocessor = pickle.load(open('preprocessor.pkl', 'rb'))

# Load dataset and extract unique area values
df = pd.read_csv("yield_df.csv") 
unique_areas = df["Area"].drop_duplicates().tolist() 

# Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', areas=unique_areas)

@app.route("/predict", methods=['POST'])
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get form data
        Year = request.form['Year']
        average_rain_fall_mm_per_year = request.form['average_rain_fall_mm_per_year']
        pesticides_tonnes = request.form['pesticides_tonnes']
        avg_temp = request.form['avg_temp']
        Area = request.form['Area']
        Item = request.form['Item']

        # Ensure input values exist in preprocessor's categories
        try:
            features = np.array([[Year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp, Area, Item]], dtype=object)
            transformed_features = preprocessor.transform(features)
            prediction = dtr.predict(transformed_features).reshape(1, -1)
            result = round(prediction[0][0], 2)
        except ValueError as e:
            result = f"Error: {str(e)}" 

        return render_template('index.html', areas=unique_areas, prediction=result)


if __name__ == "__main__":
    app.run(debug=True)
