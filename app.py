from flask import Flask,render_template,request
from form import LoginForm
app=Flask(__name__)
Users = {
                "Archie":"Amsterdam",
                "Veronica":"London",
                "Betty":"San Francisco",
                "Jughead":"Los Angeles"
            }
@app.route('/')
def home():
    print('home page loaded')
    return render_template("index.html",users=Users)

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=3000)