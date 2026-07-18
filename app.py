from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return("Hi Baby")
    
if __name__ == '__main__':
    app.run(host="localhost", port=5000) 