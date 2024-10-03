from flask import Flask, render_template, request, redirect
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
        prediction = model.predict([final])
        if prediction[0] == 1:
            return render_template("index.html",pred="----Your Loan is Approved----")
        else:
            return render_template("index.html",pred="----Your Loan is Not Approved----")



if __name__ == '__main__':
    app.run()