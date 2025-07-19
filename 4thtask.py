# ✅ SkillCraft Task 04 - Accident Data Analysis (Final Working Code)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# Step 1: Load only first 100,000 rows
df = pd.read_csv('US_Accidents_March23.csv', nrows=100000)
print("✅ File loaded successfully (100,000 rows)")
print(df.head())

# Step 2: Basic Exploration
print("\nDataset Info:")
print(df.info())
print("\nMissing Values:\n", df.isnull().sum())

# Step 3: Clean the data
df = df.dropna(subset=['Weather_Condition', 'Start_Time'])
if 'Road_Condition' in df.columns:
    df = df.dropna(subset=['Road_Condition'])

# Step 4: Extract hour from Start_Time
df['Hour'] = pd.to_datetime(df['Start_Time'], errors='coerce').dt.hour
df = df.dropna(subset=['Hour'])

# ✅ Ensure saving in same folder
output_path = os.getcwd()

# Step 5: Accidents by Hour
plt.figure(figsize=(10, 6))
df['Hour'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Accidents by Hour of the Day')
plt.xlabel('Hour')
plt.ylabel('Number of Accidents')
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(output_path, 'accidents_by_hour.png'))
plt.show()

# Step 6: Accidents by Weather Condition
plt.figure(figsize=(10, 6))
df['Weather_Condition'].value_counts().head(10).plot(kind='bar', color='orange')
plt.title('Top 10 Weather Conditions during Accidents')
plt.xlabel('Weather Condition')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(output_path, 'accidents_by_weather.png'))
plt.show()

# Step 7: Accidents by Road Condition (Only if column exists)
if 'Road_Condition' in df.columns:
    plt.figure(figsize=(8, 5))
    df['Road_Condition'].value_counts().plot(kind='bar', color='green')
    plt.title('Accidents by Road Condition')
    plt.xlabel('Road Condition')
    plt.ylabel('Count')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'accidents_by_road.png'))
    plt.show()
else:
    print("Road_Condition column not found. Skipping this graph.")

# Step 8: Map Visualization
if 'Start_Lat' in df.columns and 'Start_Lng' in df.columns:
    fig = px.scatter_mapbox(
        df.head(5000), lat='Start_Lat', lon='Start_Lng',
        zoom=4, mapbox_style="open-street-map",
        title="Accident Hotspots (First 5000 Points)"
    )
    map_file = os.path.join(output_path, "accident_hotspots_map.html")
    fig.write_html(map_file)
    print(f"✅ Map saved: {map_file}")
else:
    print("Latitude and Longitude columns not found. Skipping map.")

# Step 9: Conclusion
print("\n--- Insights Summary ---")
print("Peak accident hour:", df['Hour'].value_counts().idxmax())
print("Most common weather during accidents:", df['Weather_Condition'].value_counts().idxmax())
if 'Road_Condition' in df.columns:
    print("Most common road condition:", df['Road_Condition'].value_counts().idxmax())