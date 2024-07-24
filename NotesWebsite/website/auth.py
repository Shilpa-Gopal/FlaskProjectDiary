from flask import Blueprint, render_template,request,flash

auth = Blueprint('auth',__name__)


@auth.route('/login', method=['GET','POST'])
def login():
    # data = request.form
    # print(data)
    return render_template("login.html", text='Testing')


@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up',method=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash("Email must be greater than 4 characters",category='error')
        elif len(firstname) < 2:
            flash("Firstname must be greater than 2 characters",category='error')
        elif password1 != password2:
            flash("Passwords don't match",category='error')
        elif len(password1) < 7:
            flash("Password must be at least 7 characters",category='error')
        else:
            flash("Success",category='success')
        
    return  render_template("sign_up.html")