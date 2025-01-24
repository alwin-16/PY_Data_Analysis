# %% [markdown]
# # Level 2: Task 1
# 
# # Task: Restaurant Ratings
#  
# ## Analyze the distribution of aggregate ratings and determine the most common rating range.
# 
# ## Calculate the average number of votes received by restaurants.

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("D:\Alwin\Intership\Cognifyz\Intership_Resources\Dataset_copy.csv")

df.head()

# %% [markdown]
# ## Analyze the distribution of aggregate ratings and determine the most common rating range.

# %%
agg_rating = df['Aggregate rating'].value_counts().sort_values(ascending=False).head(10)

agg_rating

# %%
# Plotting the data using histogram

plt.figure(figsize=(10,6))
plt.hist(df['Aggregate rating'], color='lightgreen', edgecolor='black')
plt.xlabel('Aggregate rating', size=12, weight='bold')
plt.ylabel('Frequency', size=12, weight='bold')
plt.title('Distribution of Aggregate rating', size=15, weight='bold')
plt.savefig('Aggregate_rating_distribution.png')
plt.show()

# %% [markdown]
# ## Calculate the average number of votes received by restaurants.

# %%
average_votes = round(df['Votes'].mean(), 2)

print("The average number of votes recieved by restaurants is",average_votes)