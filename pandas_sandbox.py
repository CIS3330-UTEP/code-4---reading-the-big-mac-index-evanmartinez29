import pandas as pd

# list_teams = ['49ers', 'Cheifs', 'Cowboys', 'Steelers']

# print(type(list_teams))

# print(list_teams)

# series_teams = pd.Series(list_teams)

# print(series_teams)
# print(type(series_teams))
# print(series_teams.index)


# students = {'Hawai':'Isabella', 'Ohia':"David", 'Iowa':'Justin', 'Colorado':'Robert'}

# print(type(students))
# print(students)

# students_series = pd.Series(index=students.keys(), data=students.values())

# print(type(students_series))
# print(students_series)
# print(students_series.index)

df = pd.read_csv('big-mac-full-index.csv')

# print(df)

# print(type(df))
# print(df.columns)
# print(type(df.columns))

# print(df['iso_a3'])


# print((type(df['iso_a3']))

country_code = 'ARG'
query_text = f"iso_a3 == @country_code" #can also use query_text = f"iso_a3 == 'USA'"
df_arg = df.query(query_text)

print(round(df_arg['dollar_price'].mean(), 2))
print(df_arg['dollar_price'].min())
# print(df_arg['dollar_price'].max())

# idx_dollar_price = df_arg['dollar_price'].idxmax()
# print(idx_dollar_price)

# arg_series = df_arg.loc[idx_dollar_price]   
# print(arg_series)
# print(type(arg_series))

# print(df_arg['local_price'].median())




