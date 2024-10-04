from flask import Flask, render_template, request, redirect
import requests
import time
from threading import Thread
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/",methods=['GET','POST'])
def prediction():
    if request.method == 'POST':
        Gender = request.form.get('gender')
        Married = request.form.get('married')
        Education = request.form.get('education')
        Self_Employed = request.form.get('employed')  
        ApplicantIncome = request.form.get('app_income')  
        CoapplicantIncome = request.form.get('self_co_income') 
        LoanAmount = request.form.get('loan_amount')   
        Loan_Amount_Term = request.form.get('loan_term')   
        Credit_History = request.form.get('credit_history')   
        Property_Area = request.form.get('property_area')
        final = [Gender,Married,Education,Self_Employed,ApplicantIncome,
                 CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]
        # prediction = model.predict([final])
        # if prediction[0] == 1:
        #     return render_template("index.html",pred="----Your Loan is Approved----")
        # else:
        #     return render_template("index.html",pred="----Your Loan is Not Approved----")
        
        # Check for empty values and handle them
        if not all([Gender, Married, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area]):
            return render_template("index.html", pred="----Please fill in all fields----")

        try:
            # Convert to the correct types
            final = [
                int(Gender), int(Married), int(Education), int(Self_Employed), 
                float(ApplicantIncome), float(CoapplicantIncome), 
                float(LoanAmount), float(Loan_Amount_Term), float(Credit_History), 
                int(Property_Area)
            ]

            # Make the prediction
            prediction = model.predict([final])

            if prediction[0] == 1:
                return render_template("index.html", pred="----Your Loan is Approved----")
            else:
                return render_template("index.html", pred="----Your Loan is Not Approved----")

        except ValueError:
            return render_template("index.html", pred="----Invalid input. Please enter valid numbers----")



url = "https://loan-approval-prediction-jc8r.onrender.com"  # Replace with your Render URL
interval = 30  # Interval in seconds (30 seconds)

def reload_website():
    while True:
        try:
            response = requests.get(url)
            print(f"Reloaded at {time.strftime('%Y-%m-%d %H:%M:%S')}: Status Code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error reloading at {time.strftime('%Y-%m-%d %H:%M:%S')}: {str(e)}")
        time.sleep(interval)

# Start the reload function in a separate thread
def start_reloading():
    thread = Thread(target=reload_website)
    thread.daemon = True
    thread.start()

# Run the thread when the app context is created
with app.app_context():
    start_reloading()



if __name__ == '__main__':
    app.run(debug=True)