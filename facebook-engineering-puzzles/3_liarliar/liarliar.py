#! /usr/bin/env python
import Queue

'''
Liar Liar

prompt: https://www.facebook.com/careers/puzzles.php?puzzle_id=20

Understanding the problem:
- Each person can be considered a node
- A node will be colored red or green (for liar vs. truthful person)
- You can't actually know which group is the lying group and which is the truthful group
- All you have to do is give the size of each group  
- We are a assuming a fully connected graph, for simplicity

'''

class Color():
    """
    Enum: red or green
    """
    RED = 1                
    GREEN = 2
    
    @staticmethod
    def opposite(color):
        """
        Returns the opposite color. If uninitialized, raises an error.
        """        
        if color == Color.RED:
            return Color.GREEN
        elif color == Color.GREEN:
            return Color.RED
        else:
            raise AttributeError("Can't get the opposite Color of: " + color)

class RedGreenNode():
    """
    A named node that has a color {red, green}
    It also knows who all its neighbors are
    """
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __init__(self, name, color=None, neighbors=[]):        
        self.name = str(name)
        self.neighbors = set(neighbors)
        self.color = color #red or green
        return
    
    def add_neighbor(self, node_name):
        """
        Add neighbor if it isn't already in the set of neighbors
        """
        self.neighbors.add(node_name)
        return

class RedGreenGraph():
    """
    An undirected graph of RedGreenNodes
    """
    def __init__(self):
        #key = name of the node
        #value = node object
        self.nodes = {}
        
    def add_edge(self, node_1_name, node_2_name):
        """
        Adds an edge to the graph. Creates nodes as needed.
        """
        
        #if the nodes for this edge don't exist, create them        
        try:
            node_1 = self.nodes[node_1_name]
        except KeyError:
            node_1 = RedGreenNode(node_1_name)
            self.nodes[node_1_name] = node_1        
        try:
            node_2 = self.nodes[node_2_name] 
        except KeyError:
            node_2 = RedGreenNode(node_2_name)
            self.nodes[node_2_name] = node_2
        
        #now add neighbors to both nodes
        self.nodes[node_1_name].add_neighbor(node_2_name)
        self.nodes[node_2_name].add_neighbor(node_1_name)
       
    def color_graph(self):
        """
        Performs Breadth-First Traversal using a Queue
        Aribtrailiy colors the first node red
        Colors subsequent nodes in an alternating cycle of {green,red}
        """        
        first_node = self.nodes.itervalues().next()
        first_node.color = Color.RED
            
        q = Queue.Queue()
        q.put(first_node)
    
        while not q.empty():
            node = q.get()
            for neighbor_name in node.neighbors:
                neighbor = self.nodes[neighbor_name]
                if not neighbor.color:
                    neighbor.color = Color.opposite(node.color)
                    q.put(neighbor)                
                            
    def print_red_green_count(self):
        """
        Prints the red and green counts, outputing whichever value is greater first.
        """
        num_green = 0
        num_red = 0
        for name, _node in self.nodes.iteritems():
            if _node.color == Color.RED:
                num_red += 1
            else:
                num_green += 1
                
        print max(num_red, num_green), min(num_red, num_green)
    
def liarliar():
    
    g = RedGreenGraph()    
    
    #read the file "input" and add edges to the graph as we go
    f = open('input', 'r')
    num_nodes = f.readline()  
    for i in range(0, int(num_nodes)):        
        name, num_edges = f.readline().strip().split()               
        for j in range(0, int(num_edges)):
            neighbor_name = f.readline().strip()
            g.add_edge(name, neighbor_name)
    g.color_graph()
    g.print_red_green_count() 
    return    
            
        
if __name__ == '__main__':
    liarliar()