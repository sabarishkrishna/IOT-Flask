from flask import Flask, render_template, session, request
from src import get_config
from src.User import User


basename = get_config('basename')

app = Flask(__name__, static_folder='assets', static_url_path=basename)
app.secret_key = get_config('secret_key')


# Testing the image viewer file.

@app.route(basename + '/image')
def image():
    return render_template('image.html')

@app.route(basename + '/dashboard')
def dashboard():
    return render_template('dashboard.html', session=session)                  

@app.route(basename + '/auth', methods=['POST'])
def authentication():
    if session.get('authenticated') == True:
        return {
                    "message": "User already authenticated...",
                    "authenticated": True
                }
    else:
        if 'username' in request.form and 'password' in request.form:
            username = request.form['username']    
            password = request.form['password']

            try:
                User.login(username, password)
                session['authenticated'] = True
                session['username'] = username
                print(session.get('username'))
                return {
                    "message": "Successfully Authenticated",
                    "authenticated": True
                }

            except Exception as e:
                return {
                    "message": str(e),
                    "authenticated": False
                }

        else:
            return {
                "message": "Not enough parameters",
                "authenticated": False
            }             


app.run(port=8080, debug=True)