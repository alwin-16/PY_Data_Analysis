# %% [markdown]
# # Task 3
# 
# ## Task: Geographic Analysis
#   
# ## Plot the locations of restaurants on a map using longitude and latitude coordinates.
# 
# ##  Identify any patterns or clusters of restaurants in specific areas.

# %%
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import numpy as np
from geodatasets import get_path
import folium
from folium.plugins import heat_map

# Load the data
url = "https://drive.google.com/file/d/1dKZxapT3xLzOTOpy1LCyqctL8YEvzp4Y/view?usp=drive_link"
url = "https://drive.google.com/uc?id=" + url.split("/")[-2]
df = pd.read_csv(url)

df = df.fillna({'Cuisines': "unknown"})

df.head()

# %%
print(df[['Latitude', 'Longitude']])

# %%
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# %% [markdown]
# ## Plot the locations of restaurants on a map using longitude and latitude coordinates.

# %%
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude), crs="EPSG:4326")

# %%
print(gdf.head())

# %%
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
ax = world.plot(color='white', edgecolor='black', figsize=(10, 5))
gdf.plot(ax=ax, color='red', markersize=5, marker='o')
plt.title("Restaurants in the World", fontsize=15, fontweight='bold')
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.savefig("restaurants_in_the_world.png", dpi=300)
plt.show()

# %% [markdown]
# ##  Identify any patterns or clusters of restaurants in specific areas.

# %%
import folium
from folium.plugins import HeatMap

# DataFrame containing 'Latitude' and 'Longitude' columns
world_map = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=1)

# %%
# Create the heat marker data
heat_marker = [[row['Latitude'], row['Longitude']] for index, row in df.iterrows()]

# Create a heat map and add it to the world map
HeatMap(heat_marker, radius=10).add_to(world_map)

# Display the map (if you're in a Jupyter Notebook)
world_map