from flask import Flask, render_template, request, jsonify

from static.scripts import pred_rent

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction', methods = ['POST'])
def prediction():
    pred = pred_rent(request.form['bed'], request.form['bath'], request.form['city'])
    return str(pred)

if __name__ == "__main__":
    app.run(debug=True)