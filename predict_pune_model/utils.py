import pickle
import json
import pandas as pd
import numpy as np
import config


class PuneHouse():
    def __init__(self,size,bath,balcony,new_total_sqft,area_type,site_location):
        self.size = size
        self.bath = bath
        self.balcony = balcony
        self.new_total_sqft = new_total_sqft
        self.area_type = "area_type_" + area_type
        self.site_location = "site_location_" + site_location



    def load_file(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)


    def get_predicted_house_price(self):
        self.load_file()  # calling load_file method to get

        area_type_index = self.json_data['column_names'].index(self.area_type)
        site_location_index = self.json_data['column_names'].index(self.site_location)

        array = np.zeros(len(self.json_data['column_names']))
        array[0]=self.size
        array[1]=self.bath
        array[2]=self.balcony
        array[7]=self.new_total_sqft

        array[area_type_index] = 1
        array[site_location_index] = 1

        print("Test Array -->\n",array)
        predicted_house_price = self.model.predict([array])[0]
        print("predicted price",predicted_house_price)
        return np.around(predicted_house_price, 2)





if __name__ == "__main__":

    size = 20.0
    bath = 3.0
    balcony = 2.0
    new_total_sqft = 1600.0
    area_type="Carpet  Area"
    site_location="Yerawada"

    house_price = PuneHouse(size,bath,balcony,new_total_sqft,area_type,site_location)
    price = house_price.get_predicted_house_price()
    print()
    print(f"predicted price of pune house is {price} lac")

