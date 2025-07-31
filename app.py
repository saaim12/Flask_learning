from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
    #it will see in the /templates  folder for the html files
    return render_template("home_with_jinja.html")




if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=3000)