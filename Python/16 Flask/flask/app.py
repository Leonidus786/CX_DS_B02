from flask import Flask

"""
It creates an instance of the Flask class,
Which will be your  WSGI(Web Server Gateway Interface)
"""

app=Flask(__name__)

@app.route('/')
def welcome():
    return "<html><H1>Welcome to this Flask Course.</H1></html>"

@app.route('/index')
def index():
    return "<html><B>phunch gye index pe ek nayi jagah same area me</B></html>"


if __name__=="__main__":
    app.run(debug=True)