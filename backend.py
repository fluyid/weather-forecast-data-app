import requests

API_KEY = "a25a27d0b74b80d2882d41c5eb3ec5e0"

def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url=url)
    data = response.json()
    filtered_data = data["list"]
    # 8 values for 24 hours // 1 value for every 3 hours
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[0:nr_values]
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind="Temperature"))