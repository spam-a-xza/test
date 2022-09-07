
##  API based on Flask

##  necessary libraries and functions
from flask import Flask, jsonify, request

##  create a Flask app
app = Flask(__name__)

##  returns hello world when we use GET.
##  returns the data that we send when we use POST.
@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):

        data = "hello world"
        return jsonify({'data': data})


##  GET http://127.0.0.1:5000/home/10
##  returns 100 (square of 10)
@app.route('/home/<int:num>', methods = ['GET'])
def disp(num):

    return jsonify({'data': num**2})


# driver function
if __name__ == '__main__':

    app.run(debug = True)
