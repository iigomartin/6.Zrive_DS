import requests
import pandas as pd
import matplotlib.pyplot as plt

API_URL = "https://climate-api.open-meteo.com/v1/climate?"
COORDINATES = {
    "Madrid": {"latitude": 40.416775, "longitude": -3.703790},
    "London": {"latitude": 51.507351, "longitude": -0.127758},
    "Rio": {"latitude": -22.906847, "longitude": -43.172896},
}
VARIABLES = "temperature_2m_mean,precipitation_sum,soil_moisture_0_to_10cm_mean"

def main():
    print("Exercise module 1")
    meteo_data_Madrid = get_data_meteo_api(COORDINATES["Madrid"])
    statistics_Madrid = calculate_statistics(meteo_data_Madrid)
    print(statistics_Madrid)
    represent_city(meteo_data_Madrid)

    meteo_data_London = get_data_meteo_api(COORDINATES["London"])
    statistics_London = calculate_statistics(meteo_data_London)
    print(statistics_London)
    represent_city(meteo_data_London)

    meteo_data_Rio = get_data_meteo_api(COORDINATES["Rio"])
    statistics_Rio = calculate_statistics(meteo_data_Rio)
    print(statistics_Rio)
    represent_city(meteo_data_Rio)

    raise NotImplementedError


def get_data_meteo_api(city):
    if "latitude" not in city or "longitude" not in city:
        print("Please recheck your data, it doesn't match what API needs.")
    elif (
        type(city.get("latitude")) is not float
        or type(city.get("longitude")) is not float
    ):
        print("Please recheck your data, it doesn't match what API needs.")
    else:
        API_URL_city = (
            API_URL
            + "latitude="
            + str(city.get("latitude"))
            + "&longitude="
            + str(city.get("longitude"))
            + "&start_date=1950-01-01&end_date=2050-12-31"
            + "&daily="
            + VARIABLES
        )
        json_API = connectAPI(API_URL_city)
        return json_to_df(json_API)


def connectAPI(api_url):
    r = requests.get(api_url)
    if r.status_code != 200:
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
    json_API = json_API["daily"]
    return pd.DataFrame.from_dict(json_API)


def calculate_statistics(meteo_data):
    AVG_temp = meteo_data["temperature_2m_mean"].mean()
    SD_temp = meteo_data["temperature_2m_mean"].std()
    AVG_precip = meteo_data["precipitation_sum"].mean()
    SD_precip = meteo_data["precipitation_sum"].std()
    AVG_soil = meteo_data["soil_moisture_0_to_10cm_mean"].mean()
    SD_soil = meteo_data["soil_moisture_0_to_10cm_mean"].std()
    return {
        "AVG_temperature_2m_mean": AVG_temp,
        "SD_temperature_2m_mean": SD_temp,
        "AVG_precipitation_sum": AVG_precip,
        "SD_precipitation_sum": SD_precip,
        "AVG_soil_moisture_0_to_10cm_mean": AVG_soil,
        "SD_soil_moisture_0_to_10cm_mean": SD_soil,
    }


def represent_city(meteo_data):  # sourcery skip: extract-duplicate-method
    meteo_data[["Year", "Month", "Day"]] = meteo_data["time"].str.split(
        "-", expand=True
    )
    meteo_data = meteo_data.drop(columns=["time", "Month", "Day"])
    meteo_grouped = meteo_data.groupby("Year").mean()

    meteo_grouped["temperature_2m_mean"].plot()
    plt.title("Evolution of mean temperature with time - Its rising")
    plt.show()

    meteo_grouped["precipitation_sum"].plot()
    plt.title("Evolution of mean precipitation with time - Its remaining the same")
    plt.show()

    meteo_grouped["soil_moisture_0_to_10cm_mean"].plot()
    plt.title("Evolution of soil moisture with time - Its remaining the same")
    plt.show()


if __name__ == "__main__":
    main()
