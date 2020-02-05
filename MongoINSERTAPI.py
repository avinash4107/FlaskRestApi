from pymongo import MongoClient
import flask
from flask import request

try:
    conn = MongoClient()
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")
app = flask.Flask(__name__)
@app.route('/jsonReading', methods=['POST'])
def home():
    db = conn.Dev
    req_data = request.get_json()
    name = req_data['name']
    id = req_data['id']
    location=req_data['location']
    collection = db.avinashpythonrestapiex
    emp_rec1 = {
        "name": name,
        "eid": id,
        "location": location
    }
    rec_id1 = collection.insert_one(emp_rec1)
    print("Data inserted with record ids", rec_id1)
    cursor = collection.find()
    for record in cursor:
        print(record)
        re=record,
    return format(record)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
        username = request.form.get('username')
        password = request.form['password']

        return '''<h1>The Username value is: {}</h1>
                  <h1>The Password value is: {}</h1>'''.format(username, password)


  return '''<form method="POST">
                  Username: <input type="text" name="username"><br>
                  Password: <input type="password" name="password"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

app.run()




