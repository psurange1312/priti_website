from flask import Flask

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello PureSoul'

if __name__ == '__main__':
    print("hello Priti")
    app.run(host= '0.0.0.0', debug=True)
