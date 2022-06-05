from flask import Flask, request
from flask import render_template
app = Flask(__name__)


class Report:

    def __init__(self, place, time, description):
        self.place = place
        self.time = time
        self.description = description

    def __repr__(self):
        return self.place + " | " + self.time + " | " + self.description


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/report", methods=['GET', 'POST'])
def report():
    if request.method == 'GET':
        return render_template('report.html')
    else:
        place = request.form.get("place")
        time = request.form.get("time")
        description = request.form.get("description")
        report = Report(place, time, description)
        save_report(report)
        return render_template('success.html')


@app.route("/success")
def success():
    return render_template('success.html')


def save_report(report):
    file = open('reports.txt', 'a')
    file.write(str(report) + "\n")
    file.close()
