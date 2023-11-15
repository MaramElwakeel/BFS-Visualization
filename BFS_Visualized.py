import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

pause_time = 1

# Define a function to visualize the steps of BFS on a graph
def bfs_animation(graph, start_node):
  # Create an empty set to store visited nodes
  visited = set()
  # Create a deque and add the start node to it
  queue = deque([(start_node, None)])
  # Create a new graph to store the visited nodes and edges
  bfs_graph = nx.DiGraph()

  # Create a figure and axis object for plotting
  fig, ax = plt.subplots(figsize=(8, 8))
  ax.set_title('BFS on Graph', fontsize=20)
  ax.set_axis_off()

  # Draw the initial graph without any nodes visited
  pos = nx.spring_layout(graph)

  # Draw the edges of the initial graph with their respective colors
  edge_colors = ['black' for edge in graph.edges()]
  nx.draw_networkx_edges(graph, pos, edge_color=edge_colors, arrows=True, ax=ax)

  # Draw the labels (numbers) of the nodes in the graph
  labels = {}
  for node in graph.nodes():
    labels[node] = node
  nx.draw_networkx_labels(graph, pos, labels, font_size=16, font_color='black', ax=ax)

  # Create a dictionary to store the color of each node in the graph
  node_colors = {}
  for node in graph.nodes():
    node_colors[node] = 'white'

  # Set the color of the starting node to yellow
  node_colors[start_node] = 'yellow'

  # Draw the nodes of the initial graph with their respective colors
  nx.draw_networkx_nodes(graph, pos, node_color=list(node_colors.values()), edgecolors='black', node_size=1000, ax=ax)

  # Display the plot and pause for a moment
  plt.show(block=False)
  plt.pause(pause_time)

  # While there are still nodes to visit
  while queue:
    # Remove the leftmost node from the deque
    node, parent = queue.popleft()
    # If the node has not been visited before
    if node not in visited:
      # Add the node to the visited set
      visited.add(node)
      # Add the node to the BFS graph
      bfs_graph.add_node(node)
      # If the parent node is not None
      if parent:
        # Add the edge to the BFS graph
        bfs_graph.add_edge(parent, node)

      # Set the color of the current node to red
      node_colors[node] = 'red'

      # Draw the nodes and edges of the graph with their respective colors
      nx.draw_networkx_nodes(graph, pos, node_color=list(node_colors.values()), edgecolors='black', node_size=1000, ax=ax)
      nx.draw_networkx_edges(bfs_graph, pos, edge_color='blue',ax=ax)

      # # Display the plot and pause for a moment
      plt.pause(pause_time)

      # Get the neighbors of the current node
      neighbors = list(graph.neighbors(node))

      # Sort the neighbors of the current node
      neighbors.sort()

      # Add the neighbors of the current node to the deque
      for neighbor in neighbors:
          queue.append((neighbor, node))
          # Set node color of neighbors to yellow
          node_colors[neighbor] = 'yellow' if node_colors[neighbor] != 'green' else 'green'
          # Draw the nodes of the graph with their respective colors
      nx.draw_networkx_nodes(graph, pos, node_color=list(node_colors.values()), edgecolors='black', node_size=1000, ax=ax)
      plt.pause(pause_time)

      # Set the color of the current node to green, visited and neighbors added
      node_colors[node] = 'green'

      # # Draw the nodes of the graph with their respective colors
      nx.draw_networkx_nodes(graph, pos, node_color=list(node_colors.values()), edgecolors='black', node_size=1000, ax=ax)

      # Display the plot and pause for a moment
      plt.pause(pause_time)

  # Display the final plot
  plt.show()
           



##### TRY EACH CASE SEPERATELY BY COMMENTING AND UNCOMMENTING ######


# Test Case 1: Simple directed graph
graph = nx.DiGraph()
graph.add_edges_from([(1, 2), (2, 3), (3, 4), (3, 5), (4, 5)])
bfs_animation(graph, 1)  
# Expected output: A plot showing the BFS algorithm starting from node 1, visiting nodes in the order 1, 2, 3, 4, 5.


# # Test Case 2: Undirected graph
# graph = nx.Graph()
# graph.add_edges_from([(1, 2), (2, 3), (2, 4), (3, 4), (4, 5), (5, 1)])
# bfs_animation(graph, 1)
# # Expected output: A plot showing the BFS algorithm starting from node 1, visiting nodes in the order 1, 2, 5, 3, 4.


# # Test Case 3: Disconnected graph
# graph = nx.Graph()
# graph.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])
# graph.add_nodes_from([6, 7, 8])
# bfs_animation(graph, 1)
# # Expected output: A plot showing the BFS algorithm starting from node 1, visiting nodes in the order 1, 2, 5, 3, 4. The nodes 6, 7, 8 should be displayed but not visited.

# # Test Case 4: Cyclic graph
# graph = nx.DiGraph()
# graph.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 2)])
# bfs_animation(graph, 1)
# # Expected output: A plot showing the BFS algorithm starting from node 1, visiting nodes in the order 1, 2, 3, 4. The algorithm should terminate without visiting the node 2 again.
