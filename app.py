from flask import Flask, request, render_template, redirect, url_for
from utils.scoring import calculate_score, get_recommendation, calculate_bmi
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    weight = float(data.get('weight', 0))
    height = float(data.get('height', 0))
    bmi = calculate_bmi(weight, height)
    data = dict(data)
    data['bmi'] = bmi  # Add BMI to the data dictionary for scoring
    score = calculate_score(data)
    recommendation = get_recommendation(score)
    return render_template('result.html', score=score, recommendation=recommendation)

@app.route('/handle_symptom_question', methods=['POST'])
def handle_symptom_question():
    choice = request.form.get('choice')
    if choice == 'yes':
        # If the user selects "yes," call the other Flask application running on port 5001
        #response = requests.get('http://127.0.0.1:5001/')
        #return response.text
        return redirect('http://127.0.0.1:5001/')
    else:
        # If the user selects "no," render a thank you message or redirect to another page
        return "Thank you for using the application!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
