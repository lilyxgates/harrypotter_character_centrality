Written by Lily Gates  
March 2025

## Description
This module explores network analysis through the lens of centrality measures using data from the Harry Potter universe. By constructing a graph of character interactions, the project identifies the most central figures using three metrics: degree centrality, eigenvector centrality, and closeness centrality. The objective is to inform marketing or merchandising strategies—such as diversifying character representation in products—by uncovering which characters hold the most influence in the network.

## Usage
To run the module, ensure the dataset `hp_char.csv` is in the same directory as the script. The script constructs a graph using NetworkX, calculates centrality scores, ranks the top 10 characters for each centrality type, displays network graphs, and exports these results to CSV files. These outputs can guide data-driven decisions related to storytelling, branding, or character merchandise emphasis in the Wizarding World franchise.

## Required Dependencies
* pandas
* numpy
* networkx (to generate network and calculate centrality)
* os (to read in CSV file)
* matplotlib (for visualizing networks)