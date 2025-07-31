from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "welcome home"

@app.route("/square/<int:number>")
def square(number):
    return "the square of number is"+ str(number*number)+" nnn"

@app.route("/<my_name>")
def myname(my_name):
    return "welcome back" + my_name

if __name__== "__main__":
    print("server is runnnig")
    app.run(debug=True,host="0.0.0.0",port=3000)

