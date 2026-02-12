from flask import Flask, render_template
import requests

app = Flask(__name__)

GOLD_API_KEY = "e6aa0755-f0f4-4615-b39f-6100850ef176"
FUEL_API_KEY = "e6aa0755-f0f4-4615-b39f-6100850ef176"

def get_gold_silver():
    url = f"https://api.commoditypriceapi.com/v2/latest?apiKey={GOLD_API_KEY}&symbols=XAU,XAG&quote=INR"
    res = requests.get(url).json()
    gold = res["rates"].get("XAU", {}).get("value", "N/A")
    silver = res["rates"].get("XAG", {}).get("value", "N/A")
    return gold, silver

def get_fuel_prices():
    url = f"https://api.purepriceio.com/v1/india/fuel?apiKey={FUEL_API_KEY}"
    res = requests.get(url).json()
    petrol = res.get("petrol", {}).get("price", "N/A")
    diesel = res.get("diesel", {}).get("price", "N/A")
    return petrol, diesel

@app.route("/")
def index():
    gold, silver = get_gold_silver()
    petrol, diesel = get_fuel_prices()
    return render_template("index.html",
                           gold=gold,
                           silver=silver,
                           petrol=petrol,
                           diesel=diesel)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

