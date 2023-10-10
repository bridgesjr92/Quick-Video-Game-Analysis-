import pandas as pd
import numpy as np
from plotly import express as px


x = pd.read_csv('Video_Games.csv')
# Convert Year_of_release to a proper date.
# 1. Find out the data type for each column
# Remove Nan before converting data types because you will get error
types = x.dtypes
x.dropna()

# 2. Convert datatype
x['Year_of_Release'] = x['Year_of_Release'].astype(int)

# 3. Only want range from 2000 and higher due to data before 2000 being inconsistent
Year_of_Release = x[x['Year_of_Release'] > 2000]

# Problems to solve:
# Step 1: # Figure out the amount of games produced in a year - # Create a bar chart - using plotly
Release_year = Year_of_Release['Year_of_Release'].value_counts()
Release_year_i = Release_year.reset_index()
Release_year_i = Release_year_i.sort_values(by='Year_of_Release')

# Step 2: Create a stacked bar chart displaying each Genre for each year
genre_count = Year_of_Release.value_counts(subset=['Year_of_Release', 'Genre'])
genre_count_1 = genre_count.reset_index()
fig = px.bar(genre_count_1, x="Year_of_Release", y="count", color="Genre", title="Genre_by_Year")
fig.show()

# Step 3 Create a line chart showing genre over the years
genre_count_1.sort_values(by="Year_of_Release")
genre_count_1_sorted = genre_count_1.sort_values(by="Year_of_Release")
fig = px.line(genre_count_1_sorted, x='Year_of_Release', y='count', color='Genre', title="Genres", markers=True)
fig.show()

# Figure out which platform had the most games - Simple Bar Chart
Console = Year_of_Release['Platform'].value_counts()
console_i = Console.reset_index()
fig = px.bar(console_i, x='Platform', y='count')
fig.show()

# Create a pie chart of only PS2 Games and show the percentage of the genre
Year_of_Release = x[x['Year_of_Release'] > 2000]

ps2_1 = Year_of_Release[Year_of_Release['Platform'] == 'PS2']
ps2_1i = ps2_1.reset_index()
ps2_2 = ps2_1i.value_counts(subset=['Platform', 'Genre'])
ps2_final = ps2_2.reset_index()

fig = px.pie(ps2_final, values='count', names='Genre', title='Genre%')
fig.show()

