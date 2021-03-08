from flask import Flask, render_template, request
from dotenv import dotenv_values
import requests

app = Flask(__name__)
env = dotenv_values(".env")
api_key = env["API_KEY"]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form["city"]
        country = request.form["country"]

        weather_url = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=imperial"
        )

        weather_data = weather_url.json()

        temp = round(weather_data["main"]["temp"])
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        return render_template(
            "result.html",
            city=city,
            temp=temp,
            humidity=humidity,
            wind_speed=wind_speed,
        )

    return render_template("index.html")
