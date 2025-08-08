from flask import Flask, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def main():
    return "Hello World"

@app.route('/cpuinfo')
def cpuinfo():
    if whoami() == "root":
        return "<pre>"+os.popen('sysctl -a | grep machdep.cpu').read()+"</pre>"
    else:
        return "you are not a root user!!"

@app.route('/whoami')
def whoami():
    return os.popen('whoami').read().strip()

    

@app.route('/guest/<guest>')
def guest(guest):
    return 'hello {} user!!!!'.format(guest)

@app.route('/isroot')
def isroot():
    if whoami() == 'root':
        return 'Hello root user!!!!!!!'
    else:
        return redirect(url_for('guest', guest=whoami().strip()))

if __name__ == '__main__':
    app.run(debug=True)