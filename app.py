from flask import Flask
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/generate_report", methods=['POST'])
def output_calc():
    return "Truck Valuation and Comparison Report"


if __name__ == "__main__":
    app.run()
    