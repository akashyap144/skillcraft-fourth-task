# SkillCraft Internship - Task 04  
## Traffic Accident Data Analysis - US Accidents Dataset  

This project is part of my **SkillCraft Data Science Internship**.  
The task focuses on analyzing **US Accidents Data** to identify patterns related to **road conditions, weather, and time of the day** and visualizing accident hotspots.

---

## 🔥 Key Features  
✅ Data cleaning and handling of missing values  
✅ Extracting **hour-wise accident patterns**  
✅ Visualization of accidents by **hour, weather condition, and road condition**  
✅ Map visualization to locate **accident hotspots**  
✅ Summary of key insights  

---

## 🛠 Technologies Used  
- Python  
- Pandas  
- Matplotlib  
- Seaborn  
- Plotly (for interactive maps)  

---

## 📂 Files in this Repository  
- `4thtask.py` → Python script for accident data analysis  
- `US_Accidents_March23.csv` → Dataset used (first 100,000 rows analyzed)  
- Graphs:  
  - `accidents_by_hour.png`  
  - `accidents_by_weather.png`  
  - `accidents_by_road.png`  
  - `accident_hotspots_map.html` (interactive map)  

---

## ✅ Code Snippet  

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Step 1: Load only first 100,000 rows from the large dataset
df = pd.read_csv('US_Accidents_March23.csv', nrows=100000)
print("✅ File loaded successfully (100,000 rows)")
print(df.head())

# Step 2: Clean the data
df = df.dropna(subset=['Weather_Condition', 'Start_Time'])
if 'Road_Condition' in df.columns:
    df = df.dropna(subset=['Road_Condition'])

# Step 3: Extract hour from Start_Time
df['Hour'] = pd.to_datetime(df['Start_Time'], errors='coerce').dt.hour
df = df.dropna(subset=['Hour'])

# Step 4: Visualize Accidents by Hour
plt.figure(figsize=(10, 6))
df['Hour'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Accidents by Hour of the Day')
plt.xlabel('Hour')
plt.ylabel('Number of Accidents')
plt.grid(True)
plt.tight_layout()
plt.savefig('accidents_by_hour.png')
plt.show()

# Step 5: Accidents by Weather Condition
plt.figure(figsize=(10, 6))
df['Weather_Condition'].value_counts().head(10).plot(kind='bar', color='orange')
plt.title('Top 10 Weather Conditions during Accidents')
plt.xlabel('Weather Condition')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('accidents_by_weather.png')
plt.show()

# Step 6: Accidents by Road Condition (if available)
if 'Road_Condition' in df.columns:
    plt.figure(figsize=(8, 5))
    df['Road_Condition'].value_counts().plot(kind='bar', color='green')
    plt.title('Accidents by Road Condition')
    plt.xlabel('Road Condition')
    plt.ylabel('Count')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('accidents_by_road.png')
    plt.show()

# Step 7: Map Visualization (Hotspots)
if 'Start_Lat' in df.columns and 'Start_Lng' in df.columns:
    fig = px.scatter_mapbox(df, lat='Start_Lat', lon='Start_Lng', zoom=4,
                            mapbox_style="open-street-map",
                            title="Accident Hotspots")
    fig.write_html("accident_hotspots_map.html")
    fig.show()

# Step 8: Summary of Insights
print("\n--- Insights Summary ---")
print("Peak accident hour:", df['Hour'].value_counts().idxmax())
print("Most common weather during accidents:", df['Weather_Condition'].value_counts().idxmax())
if 'Road_Condition' in df.columns:
    print("Most common road condition:", df['Road_Condition'].value_counts().idxmax())# skillcraft-fourth-task
Task 04 of SkillCraft Data Science Internship – Accident data analysis using Python (Pandas, Matplotlib, Seaborn, Plotly). Includes data cleaning, EDA, and visualizations of accident patterns and hotspots.

Author
Kumar Akash Deep
Skillcraft Data Science Intern
