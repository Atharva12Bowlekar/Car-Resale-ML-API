import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from fastapi import FastAPI

from app.schema import cars_specs
from app.model import xgb_model


import warnings
warnings.filterwarnings(action="ignore")


app = FastAPI()

@app.get("/")
def root():
    return {"message": "XGBoost Car Resale Regressor API is properly running"}

@app.post("/predict")
def predict(data: cars_specs):
    # test_data = [[ data.car_name, data.brand, data.vehicle_age, data.km_driven, data.seller_type, data.fuel_type,
    #                data.transmission_type, data.mileage, data.engine, data.max_power, data.seats ]]

    # columns = ["car_name", "brand", "vehicle_age", "km_driven", "seller_type", "fuel_type", "transmission_type",
    #            "mileage", "engine", "max_power", "seats"]

    # test_df = pd.DataFrame(test_data, columns=columns)

    data_dict = data.model_dump()
    test_df = pd.DataFrame([data_dict])

    test_df["km_driven_per_year"] = round(test_df["km_driven"] / test_df["vehicle_age"], 0)
    test_df["power_to_engine_ratio"] = round(test_df["max_power"] * 1000 / test_df["engine"], 2) 

    test_df["seats"] = test_df["seats"].astype(str)

    log_cols = ["km_driven", "engine", "max_power", "km_driven_per_year"]
    for col in log_cols:
        test_df[col] = np.log1p(test_df[col]).round(4)

    prediction_log = xgb_model.predict(test_df)

    prediction = np.expm1(prediction_log)

    return {"prediction": round(float(prediction[0]), 2)}



    # categorical_columns = ['car_name', 'brand', 'seller_type', 'fuel_type', 'transmission_type', 'seats']

    # test_encoded = encoder.transform(test_df[categorical_columns])
    
    # one_hot_df = pd.DataFrame(
    #     test_encoded,
    #     columns = encoder.get_feature_names_out(categorical_columns),
    #     index = test_df.index
    # )

    # test_df_encoded = pd.concat([test_df.drop(columns=categorical_columns), one_hot_df], axis=1)
    # test_df_encoded = test_df_encoded.reindex(columns=model_columns, fill_value=0)

    # prediction_log = xgb_model.predict(test_df_encoded)

    # prediction = np.expm1(prediction_log)

    # return {"prediction": round(float(prediction[0]), 2)}


