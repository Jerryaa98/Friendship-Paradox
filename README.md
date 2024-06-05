# Friendship Paradox Experiment

This repository contains a Python script that demonstrates the friendship paradox using a random graph. The friendship paradox is the phenomenon where, on average, your friends have more friends than you do. This paradox is illustrated by generating a random social network and comparing the average number of friends each person has with the average number of friends that their friends have.

### Features
- Generates a random graph using the Erdős-Rényi model.
- Calculates the average number of friends each person has.
- Calculates the average number of friends that each person's friends have.
- Visualizes the graph highlighting a specific node, its friends, and the friends of its friends.

### Requirements

- Python 3.x
- NetworkX
- NumPy
- Matplotlib

### Installation
1) Clone the repository

```bash
git clone https://github.com/Jerryaa98/Friendship-Paradox.git

cd friendship-paradox-experiment
```
2) Install Requirements

```
pip install -r requirements.txt
```

3) Run the Scripts

- For the experiment

```
 python3 friendship_numbers_experiment.py
```
This will generate a graph with 100-500 nodes and a 0.1 probability of edge creation between any two nodes. 

The script will print the average number of friends and the average number of friends of friends.

the experiment will repeat 10 times.

- For visualization

```
python3 friendship_graph_experiment.py
```
This will generate a graph with 100 nodes and a 0.1 probability of edge creation between any two nodes. 

The script will print the average number of friends and the average number of friends of friends, and display a visual representation of the network highlighting the chosen node, its friends, and the friends of its friends.

### Contributing
Contributions are welcome! If you have any suggestions or improvements, please create an issue or submit a pull request.
