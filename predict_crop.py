import pickle

model = pickle.load(open("crop_model.pkl", "rb"))

N = float(input("Enter Nitrogen value: "))
P = float(input("Enter Phosphorus value: "))
K = float(input("Enter Potassium value: "))
temperature = float(input("Enter Temperature: "))
humidity = float(input("Enter Humidity: "))
ph = float(input("Enter pH value: "))
rainfall = float(input("Enter Rainfall: "))

prediction = model.predict([[N, P, K, temperature,
                             humidity, ph, rainfall]])

print("Recommended Crop:", prediction[0])