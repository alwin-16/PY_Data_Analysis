# %% [markdown]
# # Task 3
# 
# #  Task: Price Range Distribution
# 
# ## Create a histogram or bar chart to visualize the distribution of price ranges among the restaurants.
#  
# ## Calculate the percentage of restaurants in each price range category.

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("D:\Alwin\Intership\Cognifyz\Intership_Resources\Dataset_copy.csv")

df.head()

# %% [markdown]
# ## Create a histogram or bar chart to visualize the distribution of price ranges among the restaurants.

# %%
df.info()

# %%
df['Price range'].unique()

# %%
price_counts = df['Price range'].value_counts()

price_counts

# %%
df['Price range'].hist(color='lightgreen',edgecolor='black', align='left',bins=4)
plt.title('Distribution of Price Ranges Among Restaurants', fontsize=16, fontweight='bold')
plt.xlabel('Price Range', fontsize=14)
plt.ylabel('Number of Restaurants', fontsize=14)
plt.grid(False)
plt.savefig('Price_Range_Distribution.png')
plt.show()

# %% [markdown]
# ## Calculate the percentage of restaurants in each price range category.

# %%
percentage_price_range = df['Price range'].value_counts()

total = percentage_price_range.sum()

percentage_price_range = percentage_price_range.apply(lambda x: (x/total)*100)

# %%
percentage_price_range

formatted_prices = percentage_price_range.apply(lambda x: f"{x:.2f}%")

formatted_prices

# %%
plt.figure(figsize=(8, 6))
plt.pie(percentage_price_range, autopct='%1.1f%%', startangle=90, colors=['green','orange','red','blue','purple'],
       textprops={'fontsize': 14}, wedgeprops={'edgecolor': 'black'}, labels=formatted_prices.index)
plt.title('Distribution of Price Ranges Among Restaurants', fontsize=16, fontweight='bold')
plt.axis('equal')
plt.savefig('Price_Range_Pie_Chart.png')
plt.show()