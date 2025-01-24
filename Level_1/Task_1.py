# %% [markdown]
# # Level 1: Task 1
# 
# # Task: Top Cuisines
# 
# ## Determine the top three most common cuisines in the dataset.
# 
# ## Calculate the percentage of restaurants that serve each of the top cuisines.

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

# %%
df['Cuisines']

# %%
(df['Cuisines'].unique()).tolist()

# %%
df.fillna('Unknown', inplace=True)

# %% [markdown]
# ## Determine the top three most common cuisines in the dataset.

# %%
cuisine_count = df['Cuisines'].str.split(', ').explode('Cuisines').value_counts()

top_cuisines = cuisine_count.head(3)

print(f'Top 3 Cuisines are: ', top_cuisines, sep='\n')

# %%
# Plotting the top 3 cuisines

import matplotlib.pyplot as plt


top_cuisines.plot(kind='bar', color=['green', 'orange', 'red'], figsize=(8, 6), edgecolor='black')
plt.title('Top 3 Cuisines', fontsize=15, fontweight='bold')
plt.xlabel('Cuisines')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=0, ha='center')
plt.savefig('top_cuisines.png')
plt.show()

# %% [markdown]
# ## Calculate the percentage of restaurants that serve each of the top cuisines.

# %%
total_restaurants = len(df)
cuisine_percentage = (top_cuisines / total_restaurants) * 100

top_cusinine_percentage = cuisine_percentage.head(3)
top_cuisine_labels = top_cuisines.head(3).index

print(f'Top 3 Cuisines Percentage: ', cuisine_percentage, sep='\n')

# %%
cuisine_count = df['Cuisines'].str.split(', ').explode('Cuisines').value_counts()

top_cuisines = cuisine_count.head()

# %%
total_restaurants = len(df)
cuisine_percentage = (top_cuisines / total_restaurants) * 100

top_cuisnine_percentage = cuisine_percentage.head()
top_cuisine_labels = top_cuisines.head().index

plt.figure(figsize=(7, 6))
plt.pie(top_cuisnine_percentage, labels= top_cuisine_labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 14}, 
        wedgeprops={'edgecolor': 'black'}, colors=['green','orange','red','blue','purple'])
plt.title('Percentage of Restaurants by Cuisine', fontsize=15, fontweight='bold')
plt.axis('equal')
plt.savefig('cuisine_percentage.png')
plt.show()