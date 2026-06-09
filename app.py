from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open("crop_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    values = [float(x) for x in request.form.values()]
    prediction = model.predict([values])

    return render_template(
        'index.html',
        prediction_text=f"Recommended Crop: {prediction[0]}"
    )

if __name__ == "__main__":
    app.run(debug=True)