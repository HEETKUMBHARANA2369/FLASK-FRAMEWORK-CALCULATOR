from flask import Flask,request,render_template
app = Flask(__name__)
@app.route("/")
def calculator():
    return render_template("index.html")
@app.route("/calculate",methods=['POST'])
def calculate():
    num1 = float(request.form["n1"])
    num2 = float(request.form["n2"])
    # print(num1)
    operation = request.form['operation']
    if operation == "Addition":
        print("Addition is selected")
        res = num1+num2
    elif operation == "Subtraction":
        print("Subtraction is selected")
        res = num1-num2
    elif operation == "Multiplication":
        print("Multiplication is selected")
        res = num1*num2
    elif operation == "Division":
        print("Division is selected")
        if num2 == 0:
            return "Zero Division Error"
        res = num1/num2
    else:
        return "Operation not available"
    
    return f"{int(num1)} and {int(num2)}'s {operation} is {int(res)}"

if __name__ == "__main__":
    app.run(debug=True)