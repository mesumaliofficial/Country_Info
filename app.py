import requests
import streamlit as st

st.set_page_config(page_title='Country Information App', page_icon='🌍', layout="wide")

def fetch_country_info(country_name):
    url = f'https://restcountries.com/v3.1/name/{country_name}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        country_data = data[0]
        name = country_data['name']['common']
        capital = country_data.get('capital', ['No capital found'])[0]
        population = country_data.get('population', 'No population data')
        area = country_data.get('area', 'No area data')
        currencies = country_data.get('currencies', 'No currency data')
        region = country_data.get('region', 'No region data')
        return {
            'name': name,
            'capital': capital,
            'population': population,
            'area': area,
            'currencies': currencies,
            'region': region
        }
    else:
        return None
    
def main():
    st.title("Country Information App 🌍")
    st.write("Enter a country name to get its information.")
    country_name = st.text_input("Country Name", placeholder="e.g., France, Japan, Brazil")

    if country_name:
        country_info = fetch_country_info(country_name)
        if country_info:
            st.subheader(f"Information for {country_info['name']}")
            st.write(f"**Capital:** {country_info['capital']}")
            st.write(f"**Population:** {country_info['population']}")
            st.write(f"**Area:** {country_info['area']} km²")
            st.write(f"**Currencies:** {', '.join(country_info['currencies'].keys()) if isinstance(country_info['currencies'], dict) else country_info['currencies']}")
            st.write(f"**Region:** {country_info['region']}")
        else:
            st.error("Country not found. Please try another name.")

if __name__ == "__main__":
    main()