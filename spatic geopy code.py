from geopy.distance import distance
from fuzzywuzzy import fuzz
import pandas as pd

# Read in the dataset
df = pd.read_csv('data.csv')

# Define a function to check if two entries are within 200 meters of each other
def is_close(coord1, coord2):
    return distance(coord1, coord2).m < 200

# Define a function to check if two names are similar
def is_similar(name1, name2):
    return fuzz.token_sort_ratio(name1, name2) > 80

# Add a new column to the DataFrame to store the similarity results
df['is_similar'] = False

# Loop through all pairs of entries in the dataset
for i in range(len(df)):
    for j in range(i+1, len(df)):
        # Check if the entries are within 200 meters and have similar names
        if is_close((df.iloc[i]['latitude'], df.iloc[i]['longitude']),
                    (df.iloc[j]['latitude'], df.iloc[j]['longitude'])) and \
           is_similar(df.iloc[i]['name'], df.iloc[j]['name']):
            # Mark the entries as similar in the DataFrame
            df.at[i, 'is_similar'] = True
            df.at[j, 'is_similar'] = True
    print(i)
    if i > 5:
        break
# Write the DataFrame to a new CSV file
df.to_csv('data_out.csv', index=False)
