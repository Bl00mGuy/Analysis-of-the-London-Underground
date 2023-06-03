import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

url = "https://graphia.app/datasets/Simple_pairwise-London_tube_map.txt"
df = pd.read_csv(url, header=None, delimiter="\t")

G = nx.from_pandas_edgelist(df, source=0, target=1)

num_components = nx.number_connected_components(G)
print("Количество компонент связности:", num_components)

print("\n")

transfers = [node for node, degree in G.degree() if degree > 2]
print("Пересадочные станции:")
for station in transfers:
    print(station)

print("\n")

def longest_path(G):
    PathLength = 0
    for start in G: 
        PathLengths = nx.single_source_shortest_path_length(G, start)
        MaxPath = max(PathLengths.values())
        if MaxPath > PathLength:
            PathLength = MaxPath
    return PathLength
print("Cколько станций мы можем максимально проехать по Лондонскому метро, ни разу не проехав одну и ту же станцию несколько раз:", longest_path(G))

plt.figure(figsize=(150, 75))
pos = nx.kamada_kawai_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=30, node_color="green", alpha=0.9)
nx.draw_networkx_edges(G, pos, edge_color="gray", width=1.5, alpha=0.8)
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif', font_weight='bold', alpha=0.9)
plt.axis("off")
plt.title("London Subway Map", fontweight='bold', fontsize=20)
plt.show()
