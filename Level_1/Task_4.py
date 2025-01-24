# %% [markdown]
# # Task 4
# 
# ## Task: Online Delivery
# 
# ## Determine the percentage of restaurants that offer online delivery.
#  
# ## Compare the average ratings of restaurants with and without online delivery.
# 

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("D:\Alwin\Intership\Cognifyz\Intership_Resources\Dataset_copy.csv")

df.head()

# %% [markdown]
# ## Determine the percentage of restaurants that offer online delivery.

# %%
value_count = df['Has Online delivery'].value_counts()

offer_online = df['Has Online delivery'].value_counts().get('Yes')

print('The Total restaurant which provides online delivery is:',offer_online)

# %%
# Convert to percentage
percentage = (value_count / value_count.sum()) * 100

# Format the output
formatted_percentage = percentage.map('{:.2f}%'.format)

# Display the formatted percentages
print(formatted_percentage)

# %%
# Plot Pie chart

plt.figure(figsize=(6, 6))
plt.pie(percentage, labels=percentage.index, autopct='%1.1f%%', startangle=90, colors=['green', 'lightgreen'], 
        explode=(0, 0.1), textprops={'fontsize': 14}, wedgeprops={'edgecolor': 'black'})
plt.title('Number of restaurants with online delivery', fontsize=15, fontweight='bold')
plt.savefig('online_delivery.png')
plt.show()

# %% [markdown]
# ## Compare the average ratings of restaurants with and without online delivery.

# %%
avg_rating_with = df.groupby('Has Online delivery')['Aggregate rating'].mean().get('Yes')
avg_rating_without = df.groupby('Has Online delivery')['Aggregate rating'].mean().get('No')

# format the output
avg_rating_with = round(avg_rating_with, 2)
avg_rating_without = round(avg_rating_without, 2)

# Display the average ratings

print('The average rating of restaurants with online delivery is:',avg_rating_with)
print('The average rating of restaurants without online delivery is:',avg_rating_without)

# %%
plt.figure(figsize=(6, 6))
plt.barh(['With Online delivery', 'Without Online delivery'], [avg_rating_with, avg_rating_without], color=['green', 'lightgreen'],
         edgecolor='black', label=['Average rating', 'Average rating'])
plt.title('Average rating of restaurants with and without online delivery', fontsize=15, fontweight='bold')
plt.xlabel('Average rating', fontsize=14)
plt.show()