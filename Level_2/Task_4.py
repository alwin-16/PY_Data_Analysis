# %% [markdown]
# # Task 4
# 
# ## Task: Restaurant Chains
# 
# ## Identify if there are any restaurant chains present in the dataset.
#  
# ## Analyze the ratings and popularity of different restaurant chains.

# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
url = "https://drive.google.com/file/d/1dKZxapT3xLzOTOpy1LCyqctL8YEvzp4Y/view?usp=drive_link"
url = "https://drive.google.com/uc?id=" + url.split("/")[-2]
df = pd.read_csv(url)

df = df.fillna({'Cuisines': "unknown"})

df.head()

# %% [markdown]
# ## Identify if there are any restaurant chains present in the dataset.

# %%
restaurant_chain = df.groupby('Restaurant Name').size().reset_index(name='Outlet Count')
new = restaurant_chain[restaurant_chain['Outlet Count'] > 1]
restaurant_chain = new.sort_values('Outlet Count', ascending=False)

restaurant_chain.head(10)

# %%
# Plot the top 10 restaurant chains with the most outlets

plt.figure(figsize=(10, 6))
plt.barh(restaurant_chain['Restaurant Name'].head(10), restaurant_chain['Outlet Count'].head(10), color='coral', edgecolor='black')
plt.ylabel('Restaurant Chain')
plt.xlabel('Outlet Count')
plt.title('Top 10 Restaurant Chains', fontsize=15, fontweight='bold')
plt.savefig('top_10_restaurant_chains.png')
plt.gca().invert_yaxis()
plt.show()

# %% [markdown]
# ## Analyze the ratings and popularity of different restaurant chains.

# %%
ratings = df.groupby('Restaurant Name')['Aggregate rating'].mean().reset_index(
    name='Average Rating').sort_values('Average Rating', ascending=False)

ratings.head(10)

# %%
votes = df.groupby('Restaurant Name')['Votes'].sum().reset_index(
    name='Total Votes').sort_values('Total Votes', ascending=False)

votes.head(10)

# %%
# Plot the top 5 restaurants with the highest average rating

plt.figure(figsize=(11, 6))
plt.bar(votes['Restaurant Name'].head(5), votes['Total Votes'].head(5), color='coral', edgecolor='black')
plt.ylabel('Average Rating', fontsize=12)
plt.xlabel('Restaurant Chain', fontsize=12)
plt.title('Top 5 Restaurants with the Highest Average Rating', fontsize=15, fontweight='bold')
plt.savefig('top_5_restaurants_highest_average_rating.png')
plt.show()