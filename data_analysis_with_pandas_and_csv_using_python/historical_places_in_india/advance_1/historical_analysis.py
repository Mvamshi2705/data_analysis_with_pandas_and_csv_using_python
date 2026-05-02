import pandas as pd
import folium
import matplotlib.pyplot as plt

#-------------------------
# READ CSV FILE
#------------------------
df=pd.read_csv("india_historical_places.csv")

print("====== HISTORICAL PLACES OF INDIA ======")
print(df)

#------------------------
# BASIC ANALYSIS
#-----------------------
print("\nTotal Number of Historical Places:", len(df))

print("\nState Wise Historical Places Count:")
print(df["State"].value_counts())

print("\nOldest Historical Place:")
print(df.loc[df["YearBuilt"].idxmin()])

print("\nNewest Historical Place:")
print(df.loc[df["YearBuilt"].idxmax()])


#---------------------------------
# CREATE INDIA MAP
#--------------------------------
india_map=folium.Map(location=[22.9734,78.6569], zoom_start=5)

for index, row in df.iterrows():
    popup_text=f"""
<b>{row['Place']}</b><br>
{row['Description']}<br>
State: {row['State']}<br>
City: {row['City']}<br>
Built: {row['YearBuilt']}<br>
Dynasty: {row['Dynasty']}
"""

    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=popup_text,
    ).add_to(india_map)

india_map.save("india_historical_map.html")
print("\nIndia Historical Map Created Sucessfully.")

#------------------------------
# BAR GRAPH : STATEWISE COUNT
#------------------------------
state_count=df["State"].value_counts()
plt.figure(figsize=(10,5))
state_count.plot(kind="bar")
plt.title("State Wise Historical Places Count")
plt.xlabel("State")
plt.ylabel("Number of Places")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("statewise_graph.png")
plt.show()

#------------------------------------
# PIE CHART : DYNASTY DISTRIBUTION
#-------------------------------------
dynasty_count=df["Dynasty"].value_counts()
plt.figure(figsize=(8,8))
dynasty_count.plot(kind="pie", autopct="%1.1f%%")
plt.title("Dynasty Distribution")
plt.ylabel("")
plt.savefig("dynasty_graph.png")
plt.show()

print("\nDynasty Distribution Created Sucessfully.")