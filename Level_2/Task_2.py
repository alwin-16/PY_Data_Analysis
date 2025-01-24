# %% [markdown]
# ## Task 2
# 
# # Task: Cuisine Combination
#   
# ## Identify the most common combinations of cuisines in the dataset.
# 
# ##  Determine if certain cuisine combinations tend to have higher ratings.

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
from collections import Counter
import seaborn as sns

# Load the data
df = pd.read_csv("D:\Alwin\Intership\Cognifyz\Intership_Resources\Dataset_copy.csv")

df.head()

# %% [markdown]
# ## Identify the most common combinations of cuisines in the dataset.

# %%
common_combination = df.groupby('Cuisines')['Aggregate rating'].count().sort_values(ascending=False).head(10)

print('The Top 10 common combination of Cuisines are:', common_combination, sep='\n')

# %%
# Plot the data

plt.figure(figsize=(10, 5))
common_combination.plot(kind='bar', color='lightcoral')
plt.title('Top 10 common combination of Cuisines', fontsize=15, fontweight='bold')
plt.xlabel('Cuisines', fontsize=12)
plt.ylabel('Number of Restaurants', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.show()

# %% [markdown]
# ##  Determine if certain cuisine combinations tend to have higher ratings.

# %%
# Select only relevant columns
relevant_data = df[['Restaurant Name', 'Cuisines', 'Aggregate rating', 'Votes']]

# Drop rows with missing cuisines and zero ratings
relevant_data = relevant_data.dropna(subset=['Cuisines', 'Aggregate rating'])
relevant_data = relevant_data[relevant_data['Aggregate rating'] > 0]

# %%
# Split cuisines into individual entries
relevant_data['Cuisine List'] = relevant_data['Cuisines'].apply(lambda x: [c.strip() for c in x.split(',')])

# %%
# Generate all cuisine combinations for each restaurant
relevant_data['Cuisine Combinations'] = relevant_data['Cuisine List'].apply(lambda x: list(combinations(x, 2)))

combinations_with_ratings = []
for _, row in relevant_data.iterrows():
    for combo in row['Cuisine Combinations']:
        combinations_with_ratings.append((combo, row['Aggregate rating']))

# %%

# Create a DataFrame for analysis
combos_df = pd.DataFrame(combinations_with_ratings, columns=['Cuisine Combination', 'Rating'])

# Calculate Average Ratings per Combination
average_ratings = combos_df.groupby('Cuisine Combination').agg(
    Average_Rating=('Rating', 'mean'),
    Rating_Count=('Rating', 'size')
).reset_index()

# %%
# Filter for significant combinations (e.g., at least 10 ratings)
significant_combinations = average_ratings[average_ratings['Rating_Count'] >= 10]

# %%
# Sort combinations by average rating
sorted_combinations = significant_combinations.sort_values(by='Average_Rating', ascending=False).head(10)

# Plot the top 10 combinations
plt.figure(figsize=(10, 6))
sns.barplot(
    y=sorted_combinations['Cuisine Combination'].apply(lambda x: ' & '.join(x)),
    x=sorted_combinations['Average_Rating'], 
    hue=sorted_combinations['Rating_Count'],
    palette='viridis'
)
plt.title('Top 10 Cuisine Combinations by Average Rating', fontsize=16, fontweight='bold')
plt.xlabel('Average Rating')
plt.ylabel('Cuisine Combination')
plt.tight_layout()
plt.show()