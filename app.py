from flask import Flask, request
from flask import render_template
app = Flask(__name__)


class Report:
    
    def __init__(self, place, time, description):
        self.place = place
        self.time = time
        self.description = description
        
    def __repr__(self) -> str:
        return self.place + " | "+ self.time + " | "+ self.description
        

reports = []

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/report", methods=['GET', 'POST'])
def report():
    if request.method == 'GET':
        return render_template('report.html')
    else:
        print("POST request received")
        place = request.form.get("place")
        time = request.form.get("time")
        description = request.form.get("description")
        print(place, time, description)
        report = Report(place, time, description)
        reports.append(report)
        return render_template('success.html')
        
        
        
@app.route("/submitted-reports")
def submitted_reports():
    return str(reports)
    


@app.route("/success")
def success():
    return render_template('success.html')