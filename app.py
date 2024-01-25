from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)


@app.route('/')
def test_page():  # put application's code here
    return render_template('index.html')


@app.route('/sendInput', methods= ['POST'])
def sendInput():
    try:
        #Get the data from the request body which is sent as a JSON
        #data is a python dictionary
        data = request.get_json()
        #we have stored the json object from the request in the data variable above.
        firstName = data['firstName']
        return jsonify({'firstName': firstName, 'success':True})


    except Exception as e:
        return jsonify({'success': False})




@app.route('/hello/<name>')
def hello_name(name):
   return '<h1>Hello %s!<h1>' % name

if __name__ == '__main__':
    app.run()
