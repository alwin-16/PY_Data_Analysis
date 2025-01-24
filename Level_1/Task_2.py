# %% [markdown]
# # Task 2
# 
# # Task: City Analysis
# 
# ## Identify the city with the highest number of restaurants in the dataset.
# 
# ## Calculate the average rating for restaurants in each city.
# 
# ##  Determine the city with the highest average rating.
# 

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("D:\Alwin\Intership\Cognifyz\Intership_Resources\Dataset_copy.csv")

df.head()

# %%
missing_values = df.isnull().sum()

missing_values

# %% [markdown]
# ## Identify the city with the highest number of restaurants in the dataset.

# %%
highest_no_of_restaurant = df['City'].value_counts().head(1)

print('The City with highest number of restaurant is:', highest_no_of_restaurant, sep='\n')

# %% [markdown]
# ## Calculate the average rating for restaurants in each city.

# %%
df['City'].unique()

# %%
average_rating = df.groupby('City')['Aggregate rating'].mean()

print('The average rating of restaurant in each city is:', average_rating, sep='\n')

# %% [markdown]
# ##  Determine the city with the highest average rating.

# %%
average_rating = df.groupby('City')['Aggregate rating'].mean()

highest_avg_rating = average_rating.idxmax()

value = average_rating.max()

print('The city with highest average rating is:', highest_avg_rating, 'with rating:', value)