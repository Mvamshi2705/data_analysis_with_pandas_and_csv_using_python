import pandas as pd
df=pd.read_csv("india_historical_places.csv")

#---------------------
# SEARCH BY STATE
#______________________
state_name=input("\nEnter state name to search historical places: ")
print(df[df["State"].str.lower()==state_name.lower()])

#--------------------------
# SEARCH BY DYNASTY
#__________________________
dynasty_name=input("\nEnter dynasty name to search historical places: ")
print(df[df["Dynasty"].str.lower()==dynasty_name.lower()])
