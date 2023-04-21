import pandas as pd

ride_sharing = pd.DataFrame

"""A- Drop complete duplicates from ride_sharing"""
ride_dup = ride_sharing.drop_duplicates()

"""
B- but if there is a typo of the duplication like the user_birth_year of the same person is entered in a different way: 
"""
# accept one of them or mean
statistics = {'user_birth_year': 'min', 'duration': 'mean'}

# Group by ride_id and compute new statistics
ride_unique = ride_dup.groupby('ride_id').agg(statistics).reset_index()

# Find duplicated values again
duplicates = ride_unique.duplicated(subset='ride_id', keep=False)
duplicated_rides = ride_unique[duplicates == True]

# Assert duplicates are processed
assert duplicated_rides.shape[0] == 0

# if more than column is common:
height_weight = pd.DataFrame
column_names = ['first_name', 'last_name', 'address']
summaries = {'height': 'max', 'weight': 'mean'}
height_weight = height_weight.groupby(by=column_names).agg(summaries).reset_index()
# Make sure aggregation is done
duplicates = height_weight.duplicated(subset=column_names, keep=False)
height_weight[duplicates].sort_values(by='first_name')

"""
C- if we has upper, small case problem 
"""
# Lowercase
marriage_status = pd.DataFrame
marriage_status['marriage_status'] = marriage_status['marriage_status'].str.lower()
marriage_status['marriage_status'].value_counts()
# unmarried 528
# married 472

"""
D-  Value consistency
'married ' , 'married' , 'unmarried' , ' unmarried'
"""
# Strip all spaces
demographics = pd.DataFrame
demographics = demographics['marriage_status'].str.strip()
demographics['marriage_status'].value_counts()
