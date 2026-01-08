import pandas as pd
import joblib
import json
from flask import Flask, request, render_template

# Initialize the Flask application
app = Flask(__name__)

# Load the trained machine learning model and the evaluation results
model = joblib.load('churn_model.joblib')
model_columns = joblib.load('model_columns.joblib')

with open('evaluation_results.json', 'r') as f:
    results = json.load(f)

print("Model and evaluation results loaded successfully.")

# Define the main route for the home page
@app.route('/')
def home():
    """
    Renders the main page, passing the model's evaluation
    results to the HTML template to be displayed.
    """
    # Your current index.html does not display these results, but it's good practice to send them.
    return render_template('index.html', results=results)

# Define the route for making a prediction
@app.route('/predict', methods=['POST'])
def predict():
    """
    Receives user input from the form, processes it,
    makes a prediction, and displays the result.
    """
    # Get all the data from the HTML form
    features = request.form.to_dict()

    # Convert numeric fields from string to float/int
    features['tenure'] = float(features['tenure'])
    features['MonthlyCharges'] = float(features['MonthlyCharges'])
    features['TotalCharges'] = float(features['TotalCharges'])
    features['SeniorCitizen'] = int(features['SeniorCitizen'])

    # Create a pandas DataFrame from the user's input
    # Ensure the columns are in the same order as the training data
    input_df = pd.DataFrame([features])
    input_df = input_df[model_columns]

    # Use the loaded model to make a prediction
    prediction = model.predict(input_df)[0]
    prediction_proba = model.predict_proba(input_df)[0]

    # Initialize variables for the result page
    possible_reasons = [] 
    
    if prediction == 1:
        prediction_status = 'churn'
        result_text = "This customer is LIKELY TO CHURN."
        probability_text = f"Probability of Churn: {prediction_proba[1]*100:.2f}%"

        # Logic to find possible reasons for churn
        if features['Contract'] == 'Month-to-month':
            possible_reasons.append("The customer is on a flexible Month-to-Month contract.")
        if features['tenure'] <= 6:
            possible_reasons.append(f"The customer has a very short tenure ({int(features['tenure'])} months).")
        if features['MonthlyCharges'] >= 90:
            possible_reasons.append(f"The monthly bill of ${features['MonthlyCharges']:.2f} is very high.")
        if features['TechSupport'] == 'No':
            possible_reasons.append("The customer does not have Tech Support.")
        if not possible_reasons:
            possible_reasons.append("The customer's profile matches patterns of previous customers who have churned.")
    else:
        prediction_status = 'no-churn'
        result_text = "This customer is UNLIKELY TO CHURN."
        probability_text = f"Probability of No Churn: {prediction_proba[0]*100:.2f}%"

    # Send all results to the 'result.html' page
    return render_template('result.html', 
                           prediction_text=result_text, 
                           probability_text=probability_text,
                           reasons=possible_reasons,
                           status=prediction_status,
                           results=results)

# This block runs the web application
if __name__ == '__main__':
    app.run(debug=True)

