# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from pandas import DataFrame
from PIL import Image 
import time
import os
# Load the Random Forest CLassifier model  
filename = 'heart-disease-rf.pkl'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
	return render_template('main.php')


@app.route('/result', methods=['GET','POST'])

    
def predict():
    if request.method == 'POST':
        
       path= request.form.get('file')
       img = Image.open(path)
       # save a image using extension
       if os.path.exists('geeks.jpg'):
           os.remove('geeks.jpg')
       if os.path.exists('myfile1.csv'):
           os.remove('myfile1.csv')
       if os.path.exists('myfile11.csv'):
           os.remove('myfile11.csv')
       if os.path.exists('myfile2.csv'):
           os.remove('myfile2.csv')
       if os.path.exists('myfile4.csv'):
           os.remove('myfile4.csv')
       img.save("geeks.jpg")
       import digtization
      
       time.sleep(200)
       import QRdetection1 as p
       
       #heart = pd.read_csv("myfile1.csv",header=None).iloc[1,:187]
       #no= int(request.form.get('text'))
       #heart = pd.read_csv('mitbih_test.csv',header=None).iloc[no,:187]
       heart = pd.read_csv("myfile4.csv",header=None).iloc[1,:187]
       
       data = np.array(heart)
       data1=data.reshape(1,-1)
       '''
       #--------------------------save data--------
       data0=data.reshape(-1,1)
       data2 = DataFrame(data0)
       data2.to_csv('myfile20.csv',header=False, index=False)'''
      
       #---------------------------------------------------
       my_prediction = model.predict(data1)
       print("classification:=",my_prediction)
       #hr=p.bpm ,
       
       return render_template('result.php',hr=p.bpm , prediction=my_prediction)
              

if __name__ == '__main__':
	app.run(debug=True)

