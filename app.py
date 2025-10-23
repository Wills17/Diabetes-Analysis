# import libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
import os


# flask instance
app = Flask(__name__)


# load models
logreg_path = os.path.join(app.root_path, 'Models', 'LR_diabetes_model.pkl')
knn_path = os.path.join(app.root_path, 'Models', 'KNN_diabetes_model.pkl')

with open(logreg_path, 'rb') as f:
    logreg_model = pickle.load(f)

with open(knn_path, 'rb') as f:
    knn_model = pickle.load(f)


# flask routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_page')
def predict_page():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user input
        preg = float(request.form['pregnancies'])
        glucose = float(request.form['glucose'])
        bp = float(request.form['bloodpressure'])
        skin = float(request.form['skinthickness'])
        insulin = float(request.form['insulin'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])
        age = float(request.form['age'])
        model_choice = request.form['model']

        features = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])

        # Choose model
        if model_choice == 'logreg':
            prediction = logreg_model.predict(features)[0]
        else:
            prediction = knn_model.predict(features)[0]

        # Interpret prediction
        result_text = "Diabetes Risk Detected" if prediction == 1 else "No Diabetes Detected"
        risk = bool(prediction)

        return render_template(
            'result.html',
            result=result_text,
            model=model_choice,
            risk=risk
        )

    except Exception as e:
        return render_template('result.html', result=f"Error: {e}", model="N/A", risk=False)

if __name__ == '__main__':
    app.run(debug=True)
