# app.py
from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model/house_price_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        final_input = [np.array(features)]
        prediction = model.predict(final_input)[0]
        return render_template('index.html', prediction_text=f"Predicted House Price: ${prediction:.2f}")
    except:
        return render_template('index.html', prediction_text="Invalid input. Try again.")

if __name__ == "__main__":
    app.run(debug=True)
