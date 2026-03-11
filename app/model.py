import joblib 
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent

model_path = base_dir / "models" / "car_price_model.pkl"

def load_model():
    return joblib.load(model_path)

xgb_model = load_model()