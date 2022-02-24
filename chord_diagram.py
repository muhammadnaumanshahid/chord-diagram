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
names = ["contract","smart","block","chain","bitcoin","data","devic","suppli","plural","receiv","configur","privaci","applic","include","transact","financi","energi","busi","develop","network","secur","protocol","attack","user","method","hash"]


from plotapi import Chord
import json

# Enter license information
# Visit https://plotapi.com/my-account to buy a new license.
# Chord.set_license("your username", "your license key")

Chord.set_license("nauman555@gmail.com", "PLOTAPI-P-db6afc71-692f-47d3-834d-8b843cd874ca")

Chord(matrix, names, arc_numbers=True, data_table_show_indices=False,opacity=0.8).to_html()
