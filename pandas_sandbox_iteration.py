import pandas as pd

df = pd.read_csv("big-mac-full-index.csv")

# print(df)
# print(df.columns)
# print(type(df.columns))
# print(len(df.columns))

# print(len(df))
# print(df.index)
# print(len(df.index))
# print(type(df.index)

# for i in df.index:
#     # print(df["iso_a3"][i])
#     # print(df.loc[i]['name'])
#     # print(df.iloc[i]['name'])
#     print(df.loc[i])
#     print(type(df.loc[i]))


df_mex = df.query('iso_a3 == "MEX"')
# print(df_mex)


# for i in range(len(df_mex)):
#     print(df_mex.loc[df_mex.index[i]])


# for index, row in df.iterrows():
#     print(df['name'][index])


def get_new_name(row):
    # print(row)
    new_colum_value = f"{row['name']} ({row['iso_a3']})"
    # print(new_colum_value)
    return new_colum_value

df['new_name'] = df.apply(get_new_name, axis=1)
print(df)