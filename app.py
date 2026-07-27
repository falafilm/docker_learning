from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return("<h1>Welcome to the Home Page</h1>")

@app.route('/about')

def about():
    return("<h1>About Mr: Nong'Sudarat 2026</h1>")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000) 