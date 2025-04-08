# Lily Gates
# March 2025

#pip install networkx

import json
import random
import numpy as np
import pandas as pd
import networkx as nx
import os

#########################################
### GET FULL PATH FOR IMDB .JSON FILE ###
#########################################

# Get the current working directory
current_directory = os.path.dirname(os.path.realpath(__file__))

# File name
file_name = "hp_char.csv"

# Construct the full file path
file_path = os.path.join(current_directory, file_name)

# Confirm Paths
print(f"CURRENT DIRECTORY: {current_directory}")
print(f"FILE PATH: {file_path}")

print("###########################################################")
print("###########################################################")

df = pd.read_csv(file_name)

# Build the graph from the dataset (source, target, weight)
g = nx.Graph()

# Adding edges to the graph using the source, target, and weight from the dataset
for _, row in df.iterrows():
    g.add_edge(row['source'], row['target'], weight=row['weight'])

# Ensure the graph has nodes and edges
print(f"Graph has {g.number_of_nodes()} nodes and {g.number_of_edges()} edges.")

#########################################
########## 1. DEGREE CENTRALITY #########
############ List Top 10 ################
#########################################

degree_centrality = nx.degree_centrality(g)

top_k = 10
top_k_list = []

for i, u in enumerate(sorted(degree_centrality, key=degree_centrality.get, reverse=True)[:top_k], start=1):
    top_k_centrality = (i, u, degree_centrality[u])
    top_k_centrality_list = list(top_k_centrality)  # Convert to list
    top_k_list.append(top_k_centrality_list)  # Store in list  

df_degree = pd.DataFrame(top_k_list, columns=["Rank", "Character Name", "Degree Centrality Score"])
print(f"DEGREE CENTRALITY OF TOP {top_k} CHARACTERS:")
print(df_degree)

print("###########################################################")
print("###########################################################")

#########################################
##### 2. EIGENVECTOR CENTRALITY #########
############ List Top 10 ################
#########################################

eigenvector_centrality = nx.eigenvector_centrality(g)

top_k = 10
top_k_list = []

for i, u in enumerate(sorted(eigenvector_centrality, key=eigenvector_centrality.get, reverse=True)[:top_k], start=1):
    top_k_centrality = (i, u, eigenvector_centrality[u])
    top_k_centrality_list = list(top_k_centrality)  # Convert to list
    top_k_list.append(top_k_centrality_list)  # Store in list  

# Create Eigenvector Centrality DataFrame
df_eigenvector = pd.DataFrame(top_k_list, columns=["Rank", "Character Name", "Eigenvector Centrality Score"])
print(f"EIGENVECTOR CENTRALITY OF TOP {top_k} CHARACTERS:")
print(df_eigenvector)

print("###########################################################")
print("###########################################################")

#########################################
##### 3. CLOSENESS CENTRALITY #########
############ List Top 10 ################
#########################################

closeness_centrality = nx.closeness_centrality(g)

top_k = 10
top_k_list = []

for i, u in enumerate(sorted(closeness_centrality, key=closeness_centrality.get, reverse=True)[:top_k], start=1):
    top_k_centrality = (i, u, closeness_centrality[u])
    top_k_centrality_list = list(top_k_centrality)  # Convert to list
    top_k_list.append(top_k_centrality_list)  # Store in list  

# Create Closeness Centrality DataFrame
df_closeness = pd.DataFrame(top_k_list, columns=["Rank", "Character Name", "Closeness Centrality Score"])
print(f"CLOSENESS CENTRALITY OF TOP {top_k} CHARACTERS:")
print(df_closeness)

print("###########################################################")
print("###########################################################")


########################
##### GRAPHING #########
########################


# Assume g is your graph object already created
degree_centrality = nx.degree_centrality(g)
eigenvector_centrality = nx.eigenvector_centrality(g)
closeness_centrality = nx.closeness_centrality(g)

# Create a DataFrame for each centrality measure
centralities = {
    "Degree Centrality": degree_centrality,
    "Eigenvector Centrality": eigenvector_centrality,
    "Closeness Centrality": closeness_centrality
}

# Convert each centrality dictionary to a DataFrame and merge them
df_list = []
for centrality_name, centrality_dict in centralities.items():
    df = pd.DataFrame(list(centrality_dict.items()), columns=["Character Name", centrality_name])
    df_list.append(df)

# Merge all DataFrames on the "Character Name" column
df_merged = df_list[0]
for df in df_list[1:]:
    df_merged = pd.merge(df_merged, df, on="Character Name", how="outer")

# Sort the DataFrame by the 'Degree Centrality' for top characters
df_merged = df_merged.sort_values(by="Degree Centrality", ascending=False).reset_index(drop=True)

# Show the merged DataFrame
print(df_merged[0:10])

#################################
##### Save and Read CSV #########
#################################

# SAVING DataFrames to CSV

# Merge the top 10 centrality results into a single DataFrame
merged_top_10_df = pd.DataFrame({
    "Rank": range(1, 11),
    "Character Name": df_degree["Character Name"],
    "Degree Centrality": df_degree["Degree Centrality Score"],
    "Eigenvector Centrality": df_eigenvector["Eigenvector Centrality Score"],
    "Closeness Centrality": df_closeness["Closeness Centrality Score"]
})

# Save the merged DataFrame to a CSV
merged_filename = "merged_top_10_centrality_hp.csv"
merged_top_10_df.to_csv(merged_filename, index=False)


# Save the top 10 for Degree Centrality to CSV
degree_centrality_filename = "top_10_degree_centrality_hp.csv"
degree_centrality_top_10 = df_degree[["Rank", "Character Name", "Degree Centrality Score"]]
degree_centrality_top_10.to_csv(degree_centrality_filename, index=False)

# Save the top 10 for Eigenvector Centrality to CSV
eigenvector_centrality_filename = "top_10_eigenvector_centrality_hp.csv"
eigenvector_centrality_top_10 = df_eigenvector[["Rank", "Character Name", "Eigenvector Centrality Score"]]
eigenvector_centrality_top_10.to_csv(eigenvector_centrality_filename, index=False)

# Save the top 10 for Closeness Centrality to CSV
closeness_centrality_filename = "top_10_closeness_centrality_hp.csv"
closeness_centrality_top_10 = df_closeness[["Rank", "Character Name", "Closeness Centrality Score"]]
closeness_centrality_top_10.to_csv(closeness_centrality_filename, index=False)


#######################################################

# READING each CSV back into a DataFrame

# Reading the merged CSV back into a DataFrame
merged_centrality_read = pd.read_csv(merged_filename)
print("Merged Top 10 Centrality for Characters:")
print(merged_centrality_read)

# Read the Degree Centrality CSV
degree_centrality_read = pd.read_csv(degree_centrality_filename)
print("Degree Centrality Top 10:")
print(degree_centrality_read)

# Read the Eigenvector Centrality CSV
eigenvector_centrality_read = pd.read_csv(eigenvector_centrality_filename)
print("Eigenvector Centrality Top 10:")
print(eigenvector_centrality_read)

# Read the Closeness Centrality CSV
closeness_centrality_read = pd.read_csv(closeness_centrality_filename)
print("Closeness Centrality Top 10:")
print(closeness_centrality_read)
