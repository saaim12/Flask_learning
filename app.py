from flask import Flask,render_template,request,abort,redirect,url_for,session
from form import LoginForm,SignUpForm

app=Flask(__name__)

pets = [
            {"id": 1, "name": "Nelly", "age": "5 weeks", "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
            {"id": 2, "name": "Yuki", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
            {"id": 3, "name": "Basker", "age": "1 year", "bio": "I love barking. But, I love my friends more."},
            {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."},
        ]
Users = {
                "Archie":"Amsterdam",
                "Veronica":"London",
                "Betty":"San Francisco",
                "Jughead":"Los Angeles"
            }
users=[
    {'email':'saim@gmail.com','password':'11223344'}
]
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
@app.route('/')
def home():
    print('home page loaded')
    return render_template("home.html",users=Users,pets=pets)
@app.route("/pet/<int:id>")
def detail(id):
    pet = next((pet for pet in pets if pet["id"] == id), None)
    if pet is None:
        abort(404, description="No Pet was Found with the given ID")
    else:
        return render_template("details.html",pet=pet)

# with request method
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method == "POST":
#         email = request.form["email"]
#         password = request.form["password"]
#         print(email, password)
#
#         for user in users:
#             if user['email'] == email and user['password'] == password:
#                 return redirect(url_for('home'))
#
#         return render_template("login_form_with_request.html", message="Incorrect Email or Password")
#
#     return render_template("login_form_with_request.html")

#with crsf wtf

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        user = next((user for user in users if user["email"] == form.email.data and user["password"] == form.password.data),None)
        if user is None:
            return render_template("login.html", form = form, message = "Wrong Credentials. Please Try Again.")
        else:
            session['user'] = user
        print("Submitted and Valid.")
        return redirect(url_for('home'))
    elif form.errors:
        print(form.errors.items())
        print(form.email.errors)
        print(form.password.errors)
    return render_template("login_form_with_wtf.html", form = form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print(f"Registered: {email} with password: {password}")
        return redirect(url_for('login'))  # or home
    return render_template('signup_form.html', form=form)

@app.route('/signout')
def signout():
    if 'user' in session:
        session.pop('user')
        #this will remove all the data froom the server like other users data as well
        #session.clear()

    return redirect(url_for('home', _scheme='http', _external=True))


@app.errorhandler(404)
def handle_404(error):
    return render_template("abort.html", message=error.description), 404

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=3000)