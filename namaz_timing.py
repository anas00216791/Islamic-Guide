import requests

def get_prayer_times(city, country):
    url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2"
    response = requests.get(url)
    data = response.json()

    if data["code"] == 200:
        timings = data["data"]["timings"]
        print(f"\n🕌 Namaz Timings for {city.title()}, {country.title()}:\n")
        print(f"Fajr     : {timings['Fajr']}")
        print(f"Dhuhr    : {timings['Dhuhr']}")
        print(f"Asr      : {timings['Asr']}")
        print(f"Maghrib  : {timings['Maghrib']}")
        print(f"Isha     : {timings['Isha']}")
    else:
        print("Error fetching prayer times. Please check city/country name.")

# ---- MAIN ----
if __name__ == "__main__":
    print("📍 Get Today's Namaz Timings\n")
    city = input("Enter your city: ")
    country = input("Enter your country: ")
    get_prayer_times(city, country)
