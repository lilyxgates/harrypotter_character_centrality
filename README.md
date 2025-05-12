# Harry Potter Network Analysis
*Written by Lily Gates*  
*March 2025*

## Description
This module uses network analysis techniques to explore centrality measures within the Harry Potter universe. By constructing a character interaction graph, the project identifies key figures based on three centrality metrics: degree centrality, eigenvector centrality, and closeness centrality. The insights gathered aim to assist in marketing or merchandising decisions, such as highlighting the most influential characters in products or promotional campaigns.

## Usage
To run the module, ensure the dataset `hp_char.csv` is placed in the same directory as the script. The script performs the following steps:

1. Builds a graph of character interactions using NetworkX.
2. Calculates centrality scores for each character based on degree, eigenvector, and closeness centrality.
3. Ranks the top 10 characters for each centrality measure.
4. Visualizes the network graph and exports the results to CSV files for further analysis.

These outputs can be used to inform decisions on character merchandise emphasis, storytelling strategies, or even targeted branding in the Wizarding World franchise.

## Required Dependencies
- **pandas**: For data handling.
- **numpy**: For numerical operations.
- **networkx**: To generate the network graph and calculate centrality.
- **os**: For reading the CSV file.
- **matplotlib**: For visualizing the network graph.
