# Car Resale Price Prediction API

## Overview

This project provides a **Machine Learning powered REST API** that predicts the resale price of a used car based on vehicle specifications. The model is trained using the **Cardekho used car dataset** and is deployed using **FastAPI**, containerized with **Docker**, and orchestrated with **Kubernetes**.

The goal of this project is to demonstrate a **production-ready ML deployment pipeline**, covering:

* Data preprocessing and feature engineering
* Machine learning model training
* Model packaging and serialization
* REST API deployment with FastAPI
* Containerization using Docker
* Deployment using Kubernetes

---

## Project Architecture

```
Client Request
      |
      v
   FastAPI
      |
      v
 ML Pipeline (Preprocessing + Model)
      |
      v
 Predicted Car Price
```

The FastAPI application receives car specifications as input, processes the data through a trained machine learning pipeline, and returns the predicted resale price.

---

## Project Structure

```
CAR_RESALE
│
├── app
│   ├── main.py        # FastAPI application
│   ├── model.py       # Model loading and prediction logic
│   └── schema.py      # Pydantic request schema
│
├── datasets
│   └── cardekho_dataset.csv
│
├── models
│
├── k8s
│   ├── deployment.yaml
│   └── service.yaml
│
├── car_price_model.pkl     # Serialized trained model
├── Dockerfile              # Docker container configuration
├── requirements.txt        # Project dependencies
├── eda_resale_cars.ipynb   # Exploratory data analysis
├── eda_resale_cars_pipeline.ipynb
└── README.md
```

---

## Dataset

The model is trained using the **Cardekho Used Car Dataset**, which contains information about used vehicles such as:

* Brand
* Vehicle age
* Kilometers driven
* Fuel type
* Transmission type
* Engine capacity
* Mileage
* Maximum power
* Seating capacity

These features are used to predict the **resale price of the car**.

---

## Machine Learning Pipeline

The preprocessing pipeline includes:

* Feature selection
* Encoding of categorical variables
* Scaling of numerical features
* Model training using regression algorithms

The pipeline is serialized using **pickle** and loaded inside the API for prediction.

---

## Input Features

The API expects the following input parameters:

```
car_name
brand
vehicle_age
km_driven
seller_type
fuel_type
transmission_type
mileage
engine
max_power
seats
```

---

## Example Request

Example JSON request:

```json
{
  "car_name": "Volkswagen Vento",
  "brand": "Volkswagen",
  "vehicle_age": 8,
  "km_driven": 100000,
  "seller_type": "Dealer",
  "fuel_type": "Petrol",
  "transmission_type": "Manual",
  "mileage": 18.19,
  "engine": 1598,
  "max_power": 103.5,
  "seats": 5
}
```

---

## Example Response

```
{
  "predicted_price": 8.5 (in lakhs)
}
```

---

## Running the Project Locally

### 1 Install Dependencies

```
pip install -r requirements.txt
```

### 2 Run FastAPI Server

```
uvicorn app.main:app --reload
```

The API will run on:

```
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

You can test the prediction endpoint directly from the browser.

---

## Running with Docker

### Build Docker Image

```
docker build -t car-resale-api .
```

### Run Container

```
docker run -p 8000:8000 car-resale-api
```

The API will be available at:

```
http://localhost:8000
```

---

## Kubernetes Deployment

The project includes Kubernetes configuration files.

### Apply Deployment

```
kubectl apply -f k8s/deployment.yaml
```

### Apply Service

```
kubectl apply -f k8s/service.yaml
```

### Check Pods

```
kubectl get pods
```

### Check Services

```
kubectl get services
```

---

## Technology Stack

* Python
* FastAPI
* Scikit-learn
* Pandas
