from flask import Flask

app=Flask(__name__)
print(app)

@app.route('/')
def hello():
    return "hello world"

@app.route('/submit')
def submit():
    return "sumit"


if __name__ == "__main__":
    print("running development server")
    app.run(debug = True, host = "0.0.0.0", port = 3000)