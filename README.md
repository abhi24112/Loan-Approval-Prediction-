# Home Loan Approval Prediction Web Application

This is a web application built to predict whether a home loan application will be approved or not based on certain criteria such as gender, marital status, income, and loan amount, among others. It uses a machine learning model for predictions and provides a simple, user-friendly interface for users to input their details and receive instant predictions.

### if your want see the Model Preparation consider reading this: https://github.com/abhi24112/Loan-Approval-Prediction-/blob/master/static/Loan%20Prediction.ipynb



## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [How It Works](#how-it-works)
- [Model Information](#model-information)

## Features

- Simple and responsive user interface using Tailwind CSS.
- Prediction of home loan approval based on user inputs.
- Real-time predictions using __Decision Tree__ machine learning models.

## Technologies Used

- **Backend:** Flask
- **Frontend:** HTML5, Tailwind CSS
- **Machine Learning:** Scikit-learn, Joblib, scipy
- **Deployment:** Render

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/abhi24112/Loan-Approval-Prediction-.git
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv .env
   .env/Scripts/activate (Window)
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

   ```bash
   loan-approval-prediction/
│
├── static/
│   ├── favicon.png
│   ├── logo.png
│   ├── Designer.png
│   └── styles.css
│
├── templates/
│   └── index.html          # The index.html is used for Website representation.
│
├── app.py                 # Main Flask app to handle routes and prediction
├── model.pkl              # Serialized ML model (pre-trained)
└──requirements.txt       # Python dependencies
```

## Screenshots

![image](https://github.com/user-attachments/assets/656290df-7c56-400f-a05b-393bc32a678c)


## How It Works

1. __Form Submission__: Users enter their personal and financial information (gender, marital status, income, loan amount, etc.) in the form.

2. __Data Processing__: When the user submits the form, the app sends the data to the backend using POST requests.

3. __Prediction__: The Flask app processes the data and runs it through a pre-trained machine learning model to predict whether the loan will be approved (Yes) or not (No).

4. __Result Display__: The prediction result is dynamically displayed on the same page (right below the submit button).

## Model Information

- The machine learning model is trained using a dataset of loan applications 
   which is created from __Kaggle__.

- The model uses features like __income, loan amount, credit history, and other personal information__ to make predictions.

- We used the __DecisionTreeClassification__ model which is well optimized for the Classification problems 

- The model is provides us **77.8% accuracy**.

- The model is saved as __model.pkl__ and loaded by the Flask app during runtime to make predictions.
