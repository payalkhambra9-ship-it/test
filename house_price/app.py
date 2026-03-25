from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [float(x) for x in request.form.values()]
        
        # Debug
        print("Input:", data)
        print("Length:", len(data))

        prediction = model.predict([data])

        return render_template("index.html", prediction_text=f"House Price: {prediction[0]}")

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)