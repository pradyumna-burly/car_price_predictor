from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model
regmodel = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    columns = ['name', 'company', 'year', 'kms_driven', 'fuel_type']
    new_data = pd.DataFrame([list(data.values())], columns=columns)
    output = regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

if __name__ == '__main__':
    app.run(debug=True)
