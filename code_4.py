import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    year = "2012"
    country_code = "ARG"
    query_text = f"date == @year"
    df_year = df.query(query_text)
    print(round(df_year['dollar_price'].mean(), 2))
    return df_year

def get_big_mac_price_by_country(country_code):
    country_code = "ARG"
    query_text = f"iso_a3 == @country_code"
    df_country = df.query(query_text)
    print(round(df_country['dollar_price'].mean(), 2))
    return df_country

def get_the_cheapest_big_mac_price_by_year(year):
    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    mac_price_year = get_big_mac_price_by_year(year="2012", country_code="ARG")
    

    mac_price_coutry = get_big_mac_price_by_country("ARG")