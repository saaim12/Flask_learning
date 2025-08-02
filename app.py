from flask import Flask,render_template,request,abort
from form import LoginForm
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


@app.errorhandler(404)
def handle_404(error):
    return render_template("abort.html", message=error.description), 404

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=3000)