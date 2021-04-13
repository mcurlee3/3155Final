import pandas as pd

df_main = pd.read_csv("Data - General Data.csv")
df_locations = pd.read_csv("Data - Locations.csv")
df_locations = pd.read_csv("Data - Locations.csv")
df_cost = pd.read_csv("Cost of Living.csv")

df_main = df_main.sort_values('Country name')

df_main.head()

df_locations.drop(["country"],axis=1,inplace=True)

df_locations = df_locations.rename(columns={'name':'Country name'})

df_merge = pd.merge(df_main,df_locations, on='Country name')

df_merge_v2 = pd.merge(df_merge, df_cost, on='Country name')

file = open('Merged.csv', 'w')
file.write(df_merge.to_csv())
file.close()
file = open('Merged_v2.csv', 'w')
file.write(df_merge.to_csv())
file.close()