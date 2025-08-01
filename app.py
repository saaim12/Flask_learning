from flask import Flask,render_template,request
from form import LoginForm
app=Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
@app.route('/home')
def home():
    #it will see in the /templates  folder for the html files
    return render_template("home.html")

#
#Jinja is a template engine that lets us serve dynamic data to the template files.
# Delimiters#
# Let’s explore some delimiters used in Jinja Syntax.
#
# {% ... %} is used for statements.
# {{ ... }} is used for variables.
# {# ... #} is used for comments.
# # ... ## is used for line statements.
# this is how we pass variables
users={
                "Archie":"Amsterdam",
                "Veronica":"London",
                "Betty":"San Francisco",
                "Jughead":"Los Angeles"
            }
@app.route('/')
def main():
    return render_template('home_with_jinja.html',users=users)

# this is form handling through request in flask
# @app.route('/login',methods=['GET','POST'])
# def login():
#     if request.method == 'POST':
#         # Access form data sent with POST
#         username = request.form['username']
#         password = request.form['password']
#         print(username,password)
#         # return f"Welcome, {username}! password{password}"
#     return render_template('login_page.html')

# this is form handling through wtf library

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    print(form.email.data)
    print(form.password.data)
    # some imp methods
    if form.validate_on_submit():
        print("Submitted and Valid.")
    elif form.errors:
        print(form.errors.items())
        print(form.email.errors)
        print(form.password.errors)
    return render_template("login_with_wtf.html", form = form)

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=3000)