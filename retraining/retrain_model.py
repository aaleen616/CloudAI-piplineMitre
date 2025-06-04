import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Dummy retrain function
def retrain_model():
    data = pd.read_csv('cleaned_data.csv')
    model = LinearRegression().fit(data[['feature']], data['label'])
    joblib.dump(model, 'model.pkl')
    print("Model retrained and saved")

if __name__ == "__main__":
    retrain_model()