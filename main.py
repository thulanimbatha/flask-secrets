from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class LoginForm(FlaskForm):
    email = StringField(label='Email')  # added kwarg
    password = PasswordField(label='Password')    # changed to Password field
    submit = SubmitField(label='Log In')

app = Flask(__name__)
app.secret_key = "IShouldBeAlseepByNow15"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    login_form = LoginForm()
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)