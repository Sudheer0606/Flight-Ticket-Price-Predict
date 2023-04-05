from flask import Flask, request, render_template
from flask_cors import cross_origin
#import sklearn
from sklearn import svm
from sklearn import datasets
import pickle
import pandas as pd
import numpy as N
import requests
import json
app = Flask(__name__)

train_data = pd.read_excel('E:\SUDHEER\Major project\Data_Train.xlsx')

data = pd.DataFrame(train_data,columns=['Source','Destination','Price','Airline'])
source=data['Source'].tolist()
price=data['Price'].tolist()
dest=data['Destination'].tolist()
air=data['Airline'].tolist()
res = N.array(air) 
unique_res = N.unique(res) 

un=N.unique(N.array(source))
dun=N.unique(N.array(dest))
print(un)
price_del=[]
params = {
  'api_key': '02861096-f9da-4c17-888e-71b2af1011eb',
  'country_code':'IN'
  
}
method = 'suggest?q=mum'
api_base = 'http://airlabs.co/api/v9/'
api_result = requests.get(api_base+method, params)
api_response = api_result.json()['response']


City=['Delhi',"Mumbai","Chennai","Kolkata","Banglore"]

@app.route("/")
@cross_origin()
def home():
    
    return render_template("home.html",City=un,Desti=dun)
del_p={}





@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
   
    if request.method == "POST":
        
      
        




        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
        # print("Journey Date : ",Journey_day, Journey_month)

        # Departure
        Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
        # print("Departure : ",Dep_hour, Dep_min)

        # Arrival
        date_arr = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
        # print("Arrival : ", Arrival_hour, Arrival_min)

        # Duration
        dur_hour = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)
        # print("Duration : ", dur_hour, dur_min)

        # Total Stops
       
        # print(Total_stops)

        # Airline
        # AIR ASIA = 0 (not in column)
       
       

      
        Source = request.form["Source"]

    
        Destination = request.form["Destination"]
        
        
        del_p={}
        for i in range(0,len(unique_res)):
            price_del=[]
            for j in range(0,10000):
                if source[j]==Source and air[j]==unique_res[i]:
                    price_del.append(price[j])
            price_del.sort()
            del_p[unique_res[i]]=price_del
        new_dict = {k: v for k, v in del_p.items() if v}
        sorted_dict = {k: v for k, v in sorted(new_dict.items(), key=lambda item: item[1])}

    

       
        return render_template('result.html',City=un,Desti=dun,sorted_dict=sorted_dict,Source=request.form["Source"],Destination=request.form["Destination"],Date=request.form["Dep_Time"])
    


    return render_template("result.html")

@app.route("/search", methods = ["GET", "POST"])
def search():
   
    if request.method == "POST":
        
     
        del_p={}
        for i in range(0,len(unique_res)):
            price_del=[]
            for j in range(0,10000):
                if source[j]==request.form["source_input"] and air[j]==unique_res[i]:
                    price_del.append(price[j])
            price_del.sort()
            del_p[unique_res[i]]=price_del
        new_dict = {k: v for k, v in del_p.items() if v}
        sorted_dict = {k: v for k, v in sorted(new_dict.items(), key=lambda item: item[1])}

    

        
        return render_template('result.html',City=un,Desti=dun,sorted_dict=sorted_dict,Source=request.form["source_input"],Destination=request.form["source_out"],Date=request.form["source_date"])
    


    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)
