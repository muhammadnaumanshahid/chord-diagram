# importing Pandas libary
import pandas as pd
# reading data from csv
df = pd.read_excel("heatmap.xlsx")
# Now, matrix contains a 26x26 matrix of the values.
matrix = df.corr()
# Replacing negative values with 0’s, as features can be negatively correlated.
matrix[matrix < 0] = 0
# Multiplying all values by 100 for clarity, since correlation values lie b/w 0 and 1.
matrix = matrix.multiply(100).astype(int)
# Converting the DataFrame to a 2D List, as it is the required input format.
matrix = matrix.values.tolist()

# Names of the features.
names = ["T1-contrac","T1-smart","T1-bitcoin","T1-suppli","T1-applic","T1-chain","T1-financi","T1-energi","T1-busi","T1-develop","T3-data","T3-network","T3-secur","T3-proto","T3-attack","T3-devic","T3-transact","T3-privaci","T3-user","T6-method","T6-block","T6-includ","T6-hash","T6-plural","T6-receiv","T6-config"]


from plotapi import Chord
import json

# Enter license information
# Visit https://plotapi.com/my-account to buy a new license.
# Chord.set_license("your username", "your license key")

Chord.set_license("nauman555@gmail.com", "PLOTAPI-P-db6afc71-692f-47d3-834d-8b843cd874ca")

Chord(matrix, names, colors="monsters", arc_numbers=True, data_table_show_indices=False,opacity=0.8).to_html()
