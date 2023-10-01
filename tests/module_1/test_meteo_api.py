""" This is a dummy example to show how to import code from src/ for testing"""


import pandas as pd
from src.module_1.module_1_meteo_api import calculate_statistics


def test__calculate_statistics():
    testing = pd.DataFrame(
        data={
            "temperature_2m_mean": [1, 2, 3, 4],
            "precipitation_sum": [5, 6, 7, 8],
            "soil_moisture_0_to_10cm_mean": [9, 10, 11, 12],
        }
    )
    AVG_temp = (1 + 2 + 3 + 4) / 4
    SD_temp = (
        (
            (1 - AVG_temp) ** 2
            + (2 - AVG_temp) ** 2
            + (3 - AVG_temp) ** 2
            + (4 - AVG_temp) ** 2
        )
        / 3
    ) ** 0.5
    AVG_precip = (5 + 6 + 7 + 8) / 4
    SD_precip = (
        (
            (5 - AVG_precip) ** 2
            + (6 - AVG_precip) ** 2
            + (7 - AVG_precip) ** 2
            + (8 - AVG_precip) ** 2
        )
        / 3
    ) ** 0.5
    AVG_soil = (9 + 10 + 11 + 12) / 4
    SD_soil = (
        (
            (9 - AVG_soil) ** 2
            + (10 - AVG_soil) ** 2
            + (11 - AVG_soil) ** 2
            + (12 - AVG_soil) ** 2
        )
        / 3
    ) ** 0.5

    correct = {
        "AVG_temperature_2m_mean": AVG_temp,
        "SD_temperature_2m_mean": SD_temp,
        "AVG_precipitation_sum": AVG_precip,
        "SD_precipitation_sum": SD_precip,
        "AVG_soil_moisture_0_to_10cm_mean": AVG_soil,
        "SD_soil_moisture_0_to_10cm_mean": SD_soil,
    }

    assert correct == calculate_statistics(testing)
