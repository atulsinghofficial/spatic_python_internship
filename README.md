# Spatic Python Internship
Code in python using geopy

Python program that will identify entries which are within 200 meters of each other and have similar names i.e. strings that are similar, but not necessarily same

For example:

        Bangalore and Bangaloore

        new delhi and NewDelhi



# Resources used in this Task 

1 - Pandas
https://pypi.org/project/pandas/

2 - Haversine Formula
https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points

3 - Geocoding in Python: A Complete Guide
https://www.natasshaselvaraj.com/a-step-by-step-guide-on-geocoding-in-python/amp/

4 - Geocode with Python
https://towardsdatascience.com/geocode-with-python-161ec1e62b89

5 - Finding Nearest pair of Latitude and Longitude match using Python
https://medium.com/analytics-vidhya/finding-nearest-pair-of-latitude-and-longitude-match-using-python-ce50d62af546


# Explanation 

1 - Two functions is_similar and haversine, and uses them to compare the rows in the Data Sets.

2 - The haversine function takes four arguments, lat1, lon1, lat2, and lon2, which are the latitude and longitude coordinates of two points on the Earth's surface, and calculates the distance between them in meters using the haversine formula.

3 - The is_similar function takes two string arguments, s1 and s2, and returns a boolean indicating whether the two strings are similar or not. In this case, similarity is defined as the Levenshtein distance (the number of single-character edits required to transform one string into the other) between the two strings being less than or equal to 5.

4 - The code then creates a new column in the DataFrame called is_similar and initializes all the values to 0.

5 - It then iterates over all pairs of rows in the DataFrame, calculates the haversine distance between their latitude and longitude coordinates, and if it's less than or equal to 200 meters and their names are similar according to the is_similar function, it sets the is_similar values of both rows to 1.

6 - Lastly, it writes the modified Data to a new CSV file.
