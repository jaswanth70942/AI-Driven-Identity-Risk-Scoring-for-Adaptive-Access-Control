from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    risk = None
    reasons = []

    if request.method == "POST":
        call_time = int(request.form["call_time"])
        duration = int(request.form["duration"])
        frequency = int(request.form["frequency"])
        familiarity = int(request.form["familiarity"])

        features = np.array([[call_time, duration, frequency, familiarity]])
        prob = model.predict_proba(features)[0][1]

        # Classification
        if prob < 0.3:
            result = "Safe 🟢"
        elif prob < 0.7:
            result = "Suspicious 🟡"
        else:
            result = "High Risk 🔴"

        risk = round(prob * 100, 2)

        # Explainable AI (Reasons)
        
        if duration < 60:
            reasons.append("Unusual late-night short call")

        if duration < 30:
            reasons.append("Very short call duration")

        if frequency < 2:
            reasons.append("Rare interaction pattern")

        if familiarity == 0:
            reasons.append("Unknown contact")

    return render_template("index.html", result=result, risk=risk, reasons=reasons)

if __name__ == "__main__":
    app.run(debug=True)