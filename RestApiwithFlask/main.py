from flask import Flask,jsonify
from flask import Flask


app=Flask(__name__)   
    
@app.route('/')
def hello_world():
    return "Hello  World!"

    
@app.route('/oddcheck/<int: n>')
def oddcheck(n):
    k=str(n%2 != 0)
    result ={
        "Number":n,
        "isOdd": k,
    }
    return k

if __name__ == '__main__':
    app.run(debug=True)