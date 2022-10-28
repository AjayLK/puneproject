

# from distutils.command.config import config
from flask import Flask, jsonify, render_template, request
from predict_pune_model.utils import PuneHouse
import config


app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome to Predict the price of house")
    return render_template("index.html")

@app.route('/predict_price', methods = ["POST","GET"])
def get_home_price():
    if request.method == "GET":
        print("We are using GET method")
        data = request.form
        print("Data-->",data)

        # size = eval(data['size'])
        # bath = eval(data['bath'])
        # balcony = eval(data['balcony'])
        # new_total_sqft = eval(data['new_total_sqft'])
        # area_type = data['area_type']
        # site_location = data['site_location']

        size = eval(request.args.get("size"))
        bath = eval(request.args.get("bath"))
        balcony = eval(request.args.get("balcony"))
        new_total_sqft = eval(request.args.get("new_total_sqft"))
        area_type = request.args.get("area_type")
        site_location = request.args.get("site_location")


        print("size,bath,balcony,new_total_sqft,area_type,site_location\n",size,bath,balcony,new_total_sqft,area_type,site_location)

        house_price = PuneHouse(size,bath,balcony,new_total_sqft,area_type,site_location)
        price = house_price.get_predicted_house_price()
        return render_template("index.html",prediction = price)

        # return jsonify({"Result": f"predicted price of pune house is {price} lac"})

    else:
        print("We are using POST method")

        size = eval(request.form.get("size"))
        bath = eval(request.form.get("bath"))
        balcony = eval(request.form.get("balcony"))
        new_total_sqft = eval(request.form.get("new_total_sqft"))
        area_type = request.form.get("area_type")
        site_location = request.form.get("site_location")

        print("size,bath,balcony,new_total_sqft,area_type,site_location\n",size,bath,balcony,new_total_sqft,area_type,site_location)

        house_price = PuneHouse(size,bath,balcony,new_total_sqft,area_type,site_location)
        price = house_price.get_predicted_house_price()

        return render_template("index.html",prediction = price)


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = config.PORT_NUMBER, debug =True)