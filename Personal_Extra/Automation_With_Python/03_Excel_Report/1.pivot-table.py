import pandas as pd

df = pd.read_excel('data/supermarket_sales.xlsx')
print(df.head())
print(df.columns.tolist())
pivot_table = df.pivot_table(index='Gender', columns='Product line', values='Total', aggfunc='sum')
print(pivot_table.head())
pivot_table.to_excel('data/pivot_table.xlsx', startrow=4)