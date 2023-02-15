import pandas as pd
from math import radians, sin, cos, sqrt, asin
import Levenshtein


# Read in the dataset
df = pd.read_csv('data.csv')


# haversine formula determines the great-circle distance between two points on a sphere given their longitudes and latitudes.
def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)2 + cos(lat1) * cos(lat2) * sin(dlon/2)2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r * 1000


# Define a function to check if two names are similar
def is_similar(s1, s2):
    distance = Levenshtein.distance(s1.lower(), s2.lower())
    return distance <= 5


# Add a new column to the DataFrame to store the similarity results
df['is_similar'] = 0


# Loop through all pairs of entries in the dataset
for i, row1 in df.iterrows():
    for j, row2 in df.iterrows():
        if i != j:
            if haversine(row1['latitude'], row1['longitude'], row2['latitude'], row2['longitude']) <= 200:
                if is_similar(row1['name'], row2['name']):
                    df.loc[i, 'is_similar'] = 1
                    df.loc[j, 'is_similar'] = 1



        # Write the DataFrame to a new CSV file
df.to_csv('data_out.csv', index=False)
