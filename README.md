# Customer Churn Prediction Web Application

## Project Overview

This project is a Customer Churn Prediction system built using Machine Learning and Flask.
The objective is to predict whether a customer is likely to churn or not based on customer-related features.

The trained machine learning model is deployed as a web application so users can easily input customer data and get predictions.

---

## Machine Learning Model

* Algorithm: Logistic Regression
* Problem Type: Binary Classification (Churn / No Churn)
* Evaluation Metrics:

  * Accuracy
  * Precision
  * Recall
  * F1-Score
  * Confusion Matrix

---

## Project Structure

```
LR_Project/
│
├── app.py
├── Churn.ipynb
├── churn_model.joblib
├── model_columns.joblib
├── evaluation_results.json
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── .gitignore
```

---

## Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* Flask
* Joblib
* HTML (Jinja Templates)
* Git & GitHub

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/KhantZaySoe/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv .venv
```

Activate (Windows):

```bash
.venv\Scripts\activate
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Flask Application

```bash
python app.py
```

### 5. Open in Browser

Go to:

```
http://127.0.0.1:5000/
```

Enter customer details and click **Predict** to view the result.

---

## Output

* Churn / No Churn prediction
* Prediction probability
* Possible reasons for churn
* Model evaluation summary

---

## Author

Khant Zay Soe

Machine Learning developer



---

## Note

This project is created for learning and academic purposes.
