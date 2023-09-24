API_URL = "https://climate-api.open-meteo.com/v1/climate?"
COORDINATES = {
    "Madrid": {"latitude": 40.416775, "longitude": -3.703790},
    "London": {"latitude": 51.507351, "longitude": -0.127758},
    "Rio": {"latitude": -22.906847, "longitude": -43.172896},
}
VARIABLES = "temperature_2m_mean,precipitation_sum,soil_moisture_0_to_10cm_mean"
import requests
import pandas as pd

def main():
    print("Exercise module 1")
    meteo_data_Madrid=get_data_meteo_api(COORDINATES["Madrid"])
    statistics=calculate_statistics(meteo_data_Madrid)
    
    raise NotImplementedError


def get_data_meteo_api(city):
    if ("latitude" not in city or "longitude" not in city):
        print("Please recheck your data, it doesn't match what API needs.")
    elif(type(city.get("latitude")) is not float or type(city.get("longitude")) is not float):
        print("Please recheck your data, it doesn't match what API needs.")
    else:
        API_URL_city=API_URL+"latitude="+str(city.get("latitude"))\
        +"&longitude="+str(city.get("longitude"))+"&start_date=1950-01-01&end_date=2050-12-31"\
        +"&daily="+VARIABLES
        
        json_API=connectAPI(API_URL_city)
        json_df=json_to_df(json_API)
        return json_df

def connectAPI(api_url):
    r = requests.get(api_url)
    if (r.status_code!=200):
        print("There has been an error, please review the code.")
    else: 
        return r.json()

def json_to_df(json_API):
    del json_API["latitude"]
    del json_API["longitude"]
    del json_API["generationtime_ms"]
    del json_API["utc_offset_seconds"]
    del json_API["timezone"]
    del json_API["timezone_abbreviation"]
    del json_API["elevation"]
    del json_API["daily_units"]
    json_API=json_API["daily"]
    json_df=pd.DataFrame.from_dict(json_API)
    return json_df

def calculate_statistics(meteo_data):
    print("indevelopment")
    print(meteo_data.dtypes)
if __name__ == "__main__":
    main()