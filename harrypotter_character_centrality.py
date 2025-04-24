# Lily Gates
# March 2025

#pip install networkx

import json
import random
import numpy as np
import pandas as pd
import networkx as nx  # Create network graph
import os  # Read file from computer
import matplotlib.pyplot as plt  # Dipslay graph
import matplotlib.lines as mlines


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
########## 1. DEGREE CENTRALITY #########
########## DISPLAY NETWORK GRAPH ########
#########################################

# Get the top 10 nodes by degree centrality
top_10_nodes = sorted(degree_centrality, key=degree_centrality.get, reverse=True)[:10]

# Set node sizes based on centrality
node_sizes = [200 * degree_centrality[node] for node in g.nodes()]

# Node colors (crimson for top 10, light blue for others)
node_colors = ['crimson' if node in top_10_nodes else 'skyblue' for node in g.nodes()]

# Node edge colors (black outline for top 10, none for others)
node_edgecolors = ['black' if node in top_10_nodes else 'none' for node in g.nodes()]

# Position the nodes using spring layout
pos = nx.spring_layout(g, seed=42, k=6)

# Set label positions slightly above nodes to avoid overlap
label_pos = {node: (coords[0], coords[1] + 0.04) for node, coords in pos.items()}

# Create labels for top 10 and other nodes
top_10_labels = {node: node for node in top_10_nodes}
other_labels = {node: node for node in g.nodes() if node not in top_10_nodes}

# Draw the base graph with nodes and edges first
plt.figure(figsize=(15, 10))
nx.draw(g, pos, with_labels=False, node_size=node_sizes, node_color=node_colors, edge_color='gray', alpha=0.7, edgecolors=node_edgecolors)

# Draw the other labels (non-top 10) first
nx.draw_networkx_labels(
    g, label_pos, labels=other_labels, font_size=8, font_weight='bold', font_color='black'
)

# Draw the top 10 labels with the translucent white box (draws them on top of the other labels)
nx.draw_networkx_labels(
    g, label_pos, labels=top_10_labels, font_size=8, font_weight='bold', font_color='black',
    bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.2', alpha=0.8)
)

# Create the legend for the top 10 nodes
legend_labels = {node: f"{node}: {degree_centrality[node]:.3f}" for node in top_10_nodes}
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='crimson', markersize=8) for _ in top_10_nodes]
legend_text = [legend_labels[node] for node in top_10_nodes]
legend = plt.legend(handles=handles, labels=legend_text, title="Top 10 by Degree Centrality", loc="upper right", fontsize=8, title_fontsize=10)

# Make the legend title bold
legend.get_title().set_fontweight('bold')

# Add the title
plt.title("Harry Potter Character Network: Top 10 by Degree Centrality", fontsize=14)

# Save and display the plot
plt.savefig("harrypotter_top10_degree_centr.png", dpi=300, bbox_inches='tight')
plt.show()


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
##### 2. EIGENVECTOR CENTRALITY #########
########## DISPLAY NETWORK GRAPH ########
#########################################

# Get the top 10 nodes by Eigenvector centrality
top_10_nodes = sorted(eigenvector_centrality, key=eigenvector_centrality.get, reverse=True)[:10]

# Set node sizes based on centrality
node_sizes = [200 * eigenvector_centrality[node] for node in g.nodes()]

# Node colors (crimson for top 10, light blue for others)
node_colors = ['crimson' if node in top_10_nodes else 'skyblue' for node in g.nodes()]

# Node edge colors (black outline for top 10, none for others)
node_edgecolors = ['black' if node in top_10_nodes else 'none' for node in g.nodes()]

# Position the nodes using spring layout
pos = nx.spring_layout(g, seed=42, k=6)

# Set label positions slightly above nodes to avoid overlap
label_pos = {node: (coords[0], coords[1] + 0.04) for node, coords in pos.items()}

# Create labels for top 10 and other nodes
top_10_labels = {node: node for node in top_10_nodes}
other_labels = {node: node for node in g.nodes() if node not in top_10_nodes}

# Draw the base graph with nodes and edges first
plt.figure(figsize=(15, 10))
nx.draw(g, pos, with_labels=False, node_size=node_sizes, node_color=node_colors, edge_color='gray', alpha=0.7, edgecolors=node_edgecolors)

# Draw the other labels (non-top 10) first
nx.draw_networkx_labels(
    g, label_pos, labels=other_labels, font_size=8, font_weight='bold', font_color='black'
)

# Draw the top 10 labels with the translucent white box (draws them on top of the other labels)
nx.draw_networkx_labels(
    g, label_pos, labels=top_10_labels, font_size=8, font_weight='bold', font_color='black',
    bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.2', alpha=0.8)
)

# Create the legend for the top 10 nodes
legend_labels = {node: f"{node}: {eigenvector_centrality[node]:.3f}" for node in top_10_nodes}
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='crimson', markersize=8) for _ in top_10_nodes]
legend_text = [legend_labels[node] for node in top_10_nodes]
legend = plt.legend(handles=handles, labels=legend_text, title="Top 10 by Eigenvector Centrality", loc="upper right", fontsize=8, title_fontsize=10)

# Make the legend title bold
legend.get_title().set_fontweight('bold')

# Add the title
plt.title("Harry Potter Character Network: Top 10 by Eigenvector Centrality", fontsize=14)

# Save and display the plot
plt.savefig("harrypotter_top10_eigenvector_centr.png", dpi=300, bbox_inches='tight')
plt.show()

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

#########################################
##### 3. CLOSENESS CENTRALITY #########
########## DISPLAY NETWORK GRAPH ########
#########################################

# Get the top 10 nodes by closeness centrality
top_10_nodes = sorted(closeness_centrality, key=closeness_centrality.get, reverse=True)[:10]

# Set node sizes based on centrality
node_sizes = [100 * closeness_centrality[node] for node in g.nodes()]

# Node colors (crimson for top 10, light blue for others)
node_colors = ['crimson' if node in top_10_nodes else 'skyblue' for node in g.nodes()]

# Node edge colors (black outline for top 10, none for others)
node_edgecolors = ['black' if node in top_10_nodes else 'none' for node in g.nodes()]

# Position the nodes using spring layout
pos = nx.spring_layout(g, seed=42, k=6)

# Set label positions slightly above nodes to avoid overlap
label_pos = {node: (coords[0], coords[1] + 0.04) for node, coords in pos.items()}

# Create labels for top 10 and other nodes
top_10_labels = {node: node for node in top_10_nodes}
other_labels = {node: node for node in g.nodes() if node not in top_10_nodes}

# Draw the base graph with nodes and edges first
plt.figure(figsize=(15, 10))
nx.draw(g, pos, with_labels=False, node_size=node_sizes, node_color=node_colors, edge_color='gray', alpha=0.7, edgecolors=node_edgecolors)

# Draw the other labels (non-top 10) first
nx.draw_networkx_labels(
    g, label_pos, labels=other_labels, font_size=8, font_weight='bold', font_color='black'
)

# Draw the top 10 labels with the translucent white box (draws them on top of the other labels)
nx.draw_networkx_labels(
    g, label_pos, labels=top_10_labels, font_size=8, font_weight='bold', font_color='black',
    bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.2', alpha=0.8)
)

# Create the legend for the top 10 nodes
legend_labels = {node: f"{node}: {closeness_centrality[node]:.3f}" for node in top_10_nodes}
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='crimson', markersize=8) for _ in top_10_nodes]
legend_text = [legend_labels[node] for node in top_10_nodes]
legend = plt.legend(handles=handles, labels=legend_text, title="Top 10 by Closeness Centrality", loc="upper right", fontsize=8, title_fontsize=10)

# Make the legend title bold
legend.get_title().set_fontweight('bold')

# Add the title
plt.title("Harry Potter Character Network: Top 10 by Closeness Centrality", fontsize=14)

# Save and display the plot
plt.savefig("harrypotter_top10_closeness_centr.png", dpi=300, bbox_inches='tight')
plt.show()

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
