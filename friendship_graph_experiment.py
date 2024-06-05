import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def generate_random_graph(num_nodes, edge_prob):
    G = nx.erdos_renyi_graph(num_nodes, edge_prob)
    return G

def average_number_of_friends(G):
    degrees = np.array([degree for node, degree in G.degree()])
    return np.mean(degrees)

def average_number_of_friends_of_friends(G):
    friends_of_friends = []
    for node in G.nodes():
        friends = list(G.neighbors(node))
        if len(friends) > 0:
            friends_degrees = [G.degree(friend) for friend in friends]
            friends_of_friends.append(np.mean(friends_degrees))
    return np.mean(friends_of_friends)

num_nodes = 100
edge_prob = 0.1
G = generate_random_graph(num_nodes, edge_prob)

avg_friends = average_number_of_friends(G)
avg_friends_of_friends = average_number_of_friends_of_friends(G)

print(f"Average number of friends: {avg_friends:.2f}")
print(f"Average number of friends of friends: {avg_friends_of_friends:.2f}")

chosen_node = list(G.nodes())[0]  # Choose the first node
friends = list(G.neighbors(chosen_node))
friends_of_friends = set()
for friend in friends:
    friends_of_friends.update(G.neighbors(friend))
friends_of_friends -= set(friends)
friends_of_friends -= {chosen_node}

plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G)
nx.draw(G, pos, node_size=50, node_color='blue', with_labels=False, alpha=0.3)
nx.draw_networkx_nodes(G, pos, nodelist=[chosen_node], node_size=100, node_color='green')
nx.draw_networkx_nodes(G, pos, nodelist=friends, node_size=80, node_color='yellow')
nx.draw_networkx_nodes(G, pos, nodelist=friends_of_friends, node_size=80, node_color='red')
nx.draw_networkx_edges(G, pos, edgelist=[(chosen_node, friend) for friend in friends], edge_color='yellow', width=2)
nx.draw_networkx_edges(G, pos, edgelist=[(friend, fof) for friend in friends for fof in G.neighbors(friend) if fof in friends_of_friends], edge_color='red', style='dashed')

plt.title("Node, Friends, and Friends of Friends in the Network")
plt.show()
