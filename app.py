# import libraries
from flask import Flask, render_template, request
import pickle

# flask instance
app = Flask(__name__)

# Load pre-trained models
with open('Models/LR_diabetes_model.pkl', 'rb') as f:
    logreg_model = pickle.load(f)

with open('Models/knn_diabetes_model.pkl', 'rb') as f:
    knn_model = pickle.load(f)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user input from form
        Preg = int(request.form['Pregnancies'])
        Glucose = int(request.form['Glucose'])
        BP = int(request.form['BP'])
        SkinThick = int(request.form['SkinThickness'])
        Insulin = int(request.form['Insulin'])
        BMI = float(request.form['BMI'])
        DPF = float(request.form['DPF'])
        Age = int(request.form['Age'])
        model_choice = request.form['model']

        input_data = [[Preg, Glucose, BP, SkinThick, Insulin, BMI, DPF, Age]]

        # Make prediction
        if model_choice == 'logreg':
            pred = logreg_model.predict(input_data)
        else:
            pred = knn_model.predict(input_data)

        result_text = "Great, patient is not diabetic." if pred[0] == 0 else "Unfortunately, patient is diabetic."

        return render_template('result.html', result=result_text)

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == '__main__':
    app.run(debug=True)
