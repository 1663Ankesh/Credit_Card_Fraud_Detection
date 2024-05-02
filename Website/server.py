from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load your scikit-learn model
model_path1 = "../XGBoost/xgboost_upsampling_model.joblib"


try:
    model1 = joblib.load(model_path1)
except Exception as e:
    print(f'Error loading the model: {e}')
    model = None


@app.route('/predict', methods=['POST'])
def predict():
    if request.is_json:
        data = request.json.get('data')
        
        if data is not None:
            
            columns = ['V1', 'V2', 'V3','V4','V5','V6','V7','V8','V9','V10','V11','V12','V13','V14','V15','V16','V17','V18','V19','V20','V21','V22','V23','V24','V25','V26','V27','V28', 'Amount']  # Add all your column names here
            input_data = pd.DataFrame([data], columns=columns)

            prediction1 = model1.predict(input_data)
            prediction=[prediction1[0]]

            
            if(prediction[0]==0):
                prediction[0]='Not Fraud';
            else:
                prediction[0]='Fraud';

            
            str="XGBoost Prediction : "+prediction[0]
            
            return str;
        else:
            return jsonify({'error': 'No data key in JSON payload'}), 400
    else:
        return jsonify({'error': 'Request is not in JSON format'}), 400


if __name__ == '__main__':
    app.run(port=5000)
