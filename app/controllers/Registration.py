
from system.core.controller import *
import flask
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class Registration(Controller):
    def __init__(self, action):
        super(Registration, self).__init__(action)
        self.load_model('Login')
   
    def index(self):
        login_registration = self.models['Login'].get_login_registration()
        return self.load_view('index.html')

    def create(self):
        valid=True
        if len(request.form['email']) < 1:
            valid=False
        elif not EMAIL_REGEX.match(request.form['email']):
            flash("Invalid Email Address!")
        if not str(request.form['first_name']).isalpha():
            valid=False
            flash("Sorry, your first name has numbers!")
        if not str(request.form['last_name']).isalpha():
            valid=False
            flash("Sorry, your last name has numbers!")
        if len(request.form['password']) < 8: 
            valid=False
            flash("Sorry, your password is less than 8 characters")
        if request.form['confirm_password'] != request.form['password']:
            valid=False
            flash('your password does not match!')
        if valid==False:
            return redirect('/')
        info = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'password' : request.form['password'],
        }
        session['first_name'] = request.form['first_name']
        self.models['Login'].create(info)
        # return redirect('success.html')
        return redirect('/success')

    def login(self):
        # pull login data from index view, and put it into a dictionary
        # login_data (dictionary) will be passed into the Model function
        # model
        login_data = {
                    'email': request.form['email'],
                    'password': request.form['password']
        }
        user = self.models['Login'].login(login_data)
        if (user == False):
            flash('incorrect login')
            return redirect('/')
        else:
            session['id'] = user['id']
            session['first_name'] = user['first_name']
            return redirect('/success')

    def success(self):
        return self.load_view('success.html')

    def logout():
        session.clear()
        return('/')
