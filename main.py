from distutils.command.config import config
from flask import Flask,jsonify,render_template,request
from models.utils import DiadetesModel
import config 

app = Flask(__name__)

@app.route("/")
def hello_Flask():
    return render_template("index.html")

@app.route("/predict_diabetes",methods=["POST","GET"])
def get_diabetes_patient():

    if request.method=="GET":

        Glucose=int(request.args.get("Glucose"))
        BloodPressure=int(request.args.get("BloodPressure"))
        SkinThickness=int(request.args.get("SkinThickness"))
        Insulin=int(request.args.get("Insulin"))
        BMI=int(request.args.get("BMI"))
        DiabetesPedigreeFunction=int(request.args.get("DiabetesPedigreeFunction"))
        Age=int(request.args.get("Age"))


        diabetes=DiadetesModel(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
        
        diabetes_pred=diabetes.Diabetes_prediction()
         

        print("person having diabetes")

        return render_template("index.html",prediction=diabetes_pred)

    else:

        Glucose=int(request.form.get("Glucose"))
        BloodPressure=int(request.form.get("BloodPressure"))
        SkinThickness=int(request.form.get("SkinThickness"))
        Insulin=int(request.form.get("Insulin"))
        BMI=int(request.form.get("BMI"))
        DiabetesPedigreeFunction=int(request.form.get("DiabetesPedigreeFunction"))
        Age=int(request.form.get("Age"))

        diabetes=DiadetesModel(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
        diabetes_pred=diabetes.Diabetes_prediction()

        return render_template("index.html",prediction=diabetes_pred)

        


if __name__ == "__main__":
    app.run(host='0.0.0.0' , port= config.PORT_NUMBER, debug=True)
     


