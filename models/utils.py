import numpy as np 
import pandas as pd 
import pickle
import json

class DiadetesModel():
    def __init__ (self,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
        self.Glucose=Glucose
        self.BloodPressure=BloodPressure
        self.SkinThickness=SkinThickness
        self.Insulin=Insulin
        self.BMI=BMI
        self.DiabetesPedigreeFunction=DiabetesPedigreeFunction
        self.Age=Age

    def Load_model(self):
        with open("models\logistic_model.pkl","rb")as f:
            self.logistic_model=pickle.load(f)

        with open("models\dict.json","r")as f:
            self.dict=json.load(f)  

    def Diabetes_prediction(self):
        self.Load_model()

        array=np.zeros(len(self.dict["columns"]))
        array[0]=self.Glucose
        array[1]=self.BloodPressure
        array[2]=self.SkinThickness
        array[3]=self.Insulin
        array[4]=self.BMI
        array[5]=self.DiabetesPedigreeFunction
        array[6]=np.log(self.Age)

        print(array)
        prediction=self.logistic_model.predict([array])[0]
        print(prediction)
        if prediction==1:
            return "POSITIVE,DONT BE AFRAID JUST TAKE CARE"

        else:
            return "NEGATIVE,THATS VERY GOOD JUST ENJOY LIFE"


if __name__=="__main__" :

     Glucose=150
     BloodPressure=70
     SkinThickness=30
     Insulin=0
     BMI=27
     DiabetesPedigreeFunction=0.45
     Age=40

     diabetes=DiadetesModel(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
     diabetes_pred=diabetes.Diabetes_prediction()

     print("person having diabetes",diabetes_pred)
     



    








        

