# Calculator
from flask import (Flask, jsonify, request, abort, render_template, logging)
from flask import render_template
from flask import request

application = app = Flask(__name__)
@app.route("/")
def home():
    """Serve homepage template."""
    return render_template("index.html")

# BMI_Calculator
@app.route("/bmi", methods = ['POST', 'GET'])
def Calculate():
    BMI = ''
    if request.method == 'POST' and 'weight_p' in request.form and 'height_f' in request.form and 'height_in' in request.form:
    
        #Declare all variables.
        weight_p = int(request.form.get("weight_p"))   
        height_f = int(request.form.get("height_f")) 
        height_in = int(request.form.get("height_in")) 
        #Formular that convert the height in Inches
        height_sq = ((height_f*12) + height_in)**2 

        BMI = round((weight_p/height_sq)*703, 2) #Formular that calculate the BMI.

    return render_template("calc.html", BMI = BMI)

# Simple Calculator
@app.route("/operation", methods = ['POST', 'GET'])
def calculate():
    num1 = request.form['number1']
    op = request.form['operator']
    num2 = request.form['number2']
    
    result = 1
    if op == '+':
          result = float(num1) + float(num2);
   
    if op == '-':
          result = float(num1) - float(num2);

    if op == '*':
          result = float(num1) * float(num2);

    if op == '/':
          result = float(num1) / float(num2);

    return jsonify(result=result)

@app.route("/calculator", methods = ['POST', 'GET'])
def index1():
    return render_template("app.html")


# Units Converter
@app.route("/converter", methods = ['POST', 'GET'])
def converter():
    return ("Under Construction!!!")

if __name__ == "__main__":
    # Use 'debug=True' to avoid resarting vs code 
    # everytime there is an update in the code.
    app.run(debug=True)
