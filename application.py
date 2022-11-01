from flask import Flask
from flask import Flask, render_template, request, redirect, session

application = Flask(__name__)

@application.route("/")
def home():
    return render_template('home.html')

@application.route("/generate_report", methods=['POST'])
def output_calc():
    return "Truck Valuation and Comparison Report"


if __name__ == "__main__":
    application.run()
    