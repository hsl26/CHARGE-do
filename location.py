from flask import Flask, render_template, jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('location.html')

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
