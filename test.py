import pandas as pd
import numpy as np
import seaborn as sns

input_file = 'test2.xlsx'
output_file = 'output.xlsx'

df = pd.read_excel(input_file)

new_data = pd.DataFrame(columns=['s1', 's2'])

for index, row in df.iterrows():
    print(row['A'])

# df.to_excel(output_file, index=False)

# print('success')


# print(testFile.shape)
# # print(testFile.head())
# # print(testFile.tail())
# # print(testFile.info())
# print(testFile.describe())