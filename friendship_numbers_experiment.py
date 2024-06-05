import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random as rd

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

for i in range(10):
    num_nodes = rd.randint(100, 500)
    edge_prob = 0.1
    G = generate_random_graph(num_nodes, edge_prob)

    avg_friends = average_number_of_friends(G)
    avg_friends_of_friends = average_number_of_friends_of_friends(G)

    print("--------------------")
    print(f"Graph {i+1}")
    print(f"Number of nodes: {num_nodes}")
    print(f"Average number of friends: {avg_friends:.2f}")
    print(f"Average number of friends of friends: {avg_friends_of_friends:.2f}")

