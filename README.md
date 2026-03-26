# AI-Driven-Identity-Risk-Scoring-for-Adaptive-Access-Control
AI-powered web application that analyzes incoming call patterns to detect potential scam or fake calls, providing real-time risk classification (Safe, Suspicious, High Risk) along with explainable insights.
# 📞 AI Fake Call Detection System

An intelligent web-based application that analyzes incoming call parameters and predicts whether a call is **Safe**, **Suspicious**, or **High Risk** using Machine Learning.

---

## 🚀 Features

- 🔍 Real-time call risk analysis
- 🤖 Machine Learning-based prediction
- 📊 Probability-based risk scoring
- 🧠 Explainable AI (XAI) – provides reasons for each prediction
- 🎨 Clean, modern UI with dynamic visualization

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS (custom UI)
- **Machine Learning:** Scikit-learn (model saved using pickle)
- **Libraries:** NumPy

---

## 📂 Project Structure
├── app.py
├── model.pkl
├── templates/
│ └── index.html

---

## ⚙️ How It Works

1. User inputs call details:
   - Call Time (0–23 hours)
   - Duration (in seconds)
   - Frequency (calls per week)
   - Familiarity (0 = Unknown, 1 = Known)

2. The system processes the input through a trained ML model.

3. Output includes:
   - Risk Score (percentage)
   - Classification:
     - 🟢 Safe
     - 🟡 Suspicious
     - 🔴 High Risk

4. Additional rule-based logic explains why a call was flagged.

---

## 🧠 Prediction Logic

- Uses `predict_proba()` to compute risk probability :contentReference[oaicite:0]{index=0}
- Classification thresholds:
  - **< 0.3** → Safe
  - **0.3 – 0.7** → Suspicious
  - **> 0.7** → High Risk :contentReference[oaicite:1]{index=1}

### Explainable Signals:
- Short call duration
- Low interaction frequency
- Unknown contact
- Unusual timing patterns

---

## ▶️ Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/your-username/fake-call-detector.git
cd fake-call-detector
```
2. Install dependencies
```
pip install flask numpy
```
###3. Run the application
```
python app.py
```
### 4. Open in browser
``` 
http://127.0.0.1:5000/
