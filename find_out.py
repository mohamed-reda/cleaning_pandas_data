import pandas as pd

"""
find how many marriage_status count and unique
"""
df = pd.DataFram
df["marriage_status"] = df["marriage_status"].astype('category')
df.describe()
# count 241
# unique 4
# top 1
# freq 120

"""
know the unknown duplication to use B- solution
"""
height_weight = df
# Column names to check for duplication
column_names = ['first_name', 'last_name', 'address']
duplicates = height_weight.duplicated(subset=column_names, keep=False)
# Output duplicate values
height_weight[duplicates].sort_values(by='first_name')
# 22 Cole Palmer 8366 At, Street 177 91
# 102 Cole Palmer 8366 At, Street 178 92


"""
find typo
"""
marriage_status = pd.DataFram

marriage_status.groupby('marriage_status').count()

# or
# Get marriage status column
demographics = pd.DataFram
marriage_status = demographics['marriage_status']
marriage_status.value_counts()
