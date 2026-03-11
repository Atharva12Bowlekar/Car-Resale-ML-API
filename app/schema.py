from pydantic import BaseModel

class cars_specs(BaseModel):
    car_name : str
    brand : str
    vehicle_age : int 
    km_driven : int
    seller_type : str	
    fuel_type : str
    transmission_type : str
    mileage	: float
    engine : int	
    max_power : float
    seats : int	 