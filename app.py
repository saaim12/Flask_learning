from flask import Flask,render_template

app=Flask(__name__)

# @app.route('/')
# def home():
#     #it will see in the /templates  folder for the html files
#     return render_template("home_with_jinja.html")
#
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
def home():
    return render_template('home_with_jinja.html',users=users)


if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=3000)