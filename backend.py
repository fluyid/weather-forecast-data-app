import requests

API_KEY = "a25a27d0b74b80d2882d41c5eb3ec5e0"

def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url=url)
    data = response.json()
    filtered_data = data["list"]
    # print(filtered_data)
    # 8 values for 24 hours // 1 value for every 3 hours
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[0:nr_values]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))