import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file.lower())

def get_big_mac_price_by_year(year,country_code):
    df['year'] = pd.to_datetime(df["date"]).dt.year
    df_year = df.query("year == @year and iso_a3 == @country_code")
    mean_price = round(df_year['dollar_price'].mean(), 2)
    print(mean_price)
    return mean_price

def get_big_mac_price_by_country(country_code):
    country_code = "MEX"
    query_text = f"iso_a3 == @country_code"
    df_country = df.query(query_text)
    print(round(df_country['dollar_price'].mean(), 2))
    return df_country

def get_the_cheapest_big_mac_price_by_year(year):
    df['year'] = pd.to_datetime(df["date"]).dt.year
    df_low_price = df.query("year == @year")
    low_price = df_low_price['dollar_price'].min()
    low_price_f = round(low_price, 2)
    country_name = df_low_price.loc[df_low_price['dollar_price'].idxmin(), 'name']
    country_code = df_low_price.loc[df_low_price['dollar_price'].idxmin(), 'iso_a3']
    print(f"{country_name}({country_code}): ${low_price_f}")
    return low_price_f

def get_the_most_expensive_big_mac_price_by_year(year):
    df['year'] = pd.to_datetime(df["date"]).dt.year
    df_high_price = df.query("year == @year")
    high_price = df_high_price['dollar_price'].max()
    high_price_f = round(high_price, 2)
    country_name = df_high_price.loc[df_high_price['dollar_price'].idxmax(), 'name']
    country_code = df_high_price.loc[df_high_price['dollar_price'].idxmax(), 'iso_a3']
    print(f"{country_name}({country_code}): ${high_price_f}")
    return high_price_f

if __name__ == "__main__":
    mac_price_year = get_big_mac_price_by_year(2010,"ARG")
    
    mac_price_coutry = get_big_mac_price_by_country("MEX")

    mac_low_price_year = get_the_cheapest_big_mac_price_by_year(2008)

    mac_high_price_year = get_the_most_expensive_big_mac_price_by_year(2003)