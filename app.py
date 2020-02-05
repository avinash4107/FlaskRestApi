import flask

app = flask.Flask(__name__)
@app.route('/avinash', methods=['GET'])
def home():
    return "Welcome to python Rest API     !!!!!"

app.run()
