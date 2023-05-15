import numpy as np
from flask import Flask,request,jsonify
import pickle
import numpy

model=pickle.load(open('pikl1.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world"
@app.route('/predict',methods=['POST'])
def predict():
    EQ =request.form.get('EQ')
    IQ=request.form.get('IQ')
    Technical_Skills =request.form.get('Technical_Skills')
    Soft_Skills =request.form.get('Soft_Skills')
    Extra_Activities =request.form.get('Extra_Activities')
    Hackathons =request.form.get('Hackathons')
    Projects =request.form.get('Projects')
    CGPA =request.form.get('CGPA')
    Internships =request.form.get('Internships')
    Gender_n =request.form.get('Gender_n')
    Stream_m =request.form.get('Stream_m')

    input_query = np.array([[float(EQ), float(IQ), float(Technical_Skills), float(Soft_Skills), float(Extra_Activities),
                             float(Hackathons), float(Projects), float(CGPA), float(Internships), float(Gender_n),
                             float(Stream_m)]])

    result = model.predict(input_query)[0]

    return jsonify({'placement':str(result)})
if __name__=='__main__':
    app.run(debug=True)