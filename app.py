from flask import Flask

app = Flask(__name__)

# This is a decorator
@app.route('/') # http://www.google.com/ <- /: Root endpoint
def home():
    return "Hello world"


app.run(port=8080)

