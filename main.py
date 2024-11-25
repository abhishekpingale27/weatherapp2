import streamlit as st
import requests


def get_weather(city_name, api_key):
    """Fetches weather data for a given city using WeatherAPI."""
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {"key": api_key, "q": city_name, "aqi": "no"}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None


# Streamlit app
def main():
    st.title("🌤️ Weather Information App")
    st.write("Enter a city name to get the current weather details.")

    # Input for city name
    city_name = st.text_input("City Name", placeholder="e.g., London, Tokyo")

    # Fetch Weather API key from secrets
    #try:

        #api_key = st.secrets["WEATHER_API_KEY"]  # Use the correct key name
    #except KeyError:
        #st.error("API key not found! Please ensure it is correctly set in `secrets.toml` or the Streamlit Cloud settings.")
        #return

    api_key = st.secrets["weather"]["WEATHER_API_KEY"]

    if st.button("Get Weather"):
        if city_name.strip():
            # Fetch weather data
            weather_data = get_weather(city_name, api_key)
            if weather_data:
                st.subheader(f"Weather in {weather_data['location']['name']}, {weather_data['location']['country']}:")
                st.write(f"**Temperature:** {weather_data['current']['temp_c']}°C")
                st.write(f"**Weather Condition:** {weather_data['current']['condition']['text']}")
                st.write(f"**Humidity:** {weather_data['current']['humidity']}%")
                st.write(f"**Wind Speed:** {weather_data['current']['wind_kph']} km/h")
            else:
                st.error("Unable to fetch weather data. Please try again later.")
        else:
            st.warning("Please enter a city name!")


if __name__ == "__main__":
    main()
