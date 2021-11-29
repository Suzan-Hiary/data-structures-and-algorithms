
from collections import deque


class Node:
    """
        Instance of a node object
        """

    def __init__(self, value):
        self.value = value


class Queue():
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value) # O(1)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)
class Graph:

    """
    the Common (graph ) data structure.
    """
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        """adds a node to the graph
        
        Arguments:
            value {[value]} -- [description]
        
        input:
            value() : new node value
        output: 
            (node) :new node added to graph
        
        Returns:
            node
        """
        node = Node(value)
        self._adjacency_list[node] = []
        return node



    def add_edge(self, start_node, end_node, weight=0):

        """
        Adding edge between two nodes in the graph.
        Input:
        start_node : First node to start edge from
        end_node : Second node to point edge to
        weight: Adds a weight to the edge (default 0).
        """
        if start_node not in self._adjacency_list:
            raise KeyError('Start node is not exist in Graph')

        if end_node not in self._adjacency_list:
            raise KeyError('End node is not exist in Graph')

        adjacencies = self._adjacency_list[start_node]

        adjacencies.append((end_node,weight))

    def get_nodes(self):
        """
        Get collection of all nodes in graph.
        Output:
        (list): Collection of all nodes in graph.
        """
        return self._adjacency_list.keys()

    def get_neighbors(self, node):

        """
        Get collection of neighbors for a node in graph.
        Input:
        node (Node): Get neighbors of the node.
        Output:
        (list): Neighbors of the node.
        """
        return self._adjacency_list[node]


    def size(self):
        """
         Returns: Total number of nodes in the graph
        """
        return len(self._adjacency_list)


    def breadth_first(self , node):

        try:
            if node not in self._adjacency_list:
                    raise KeyError('the Nodes arent in graph !!!')

            q = Queue()
            q.enqueue(node)
            visited_nodes = {}
            visited_nodes[node] = True
            output = []

            while len(q):
                cur = q.dequeue()
                output.append(cur)
                neighbors = self._adjacency_list[cur]
                for i in neighbors:
                    if i[0] not in visited_nodes:
                        q.enqueue(i[0]) 
                    visited_nodes[i[0]] = True
            return output
        except Exception as error:
            print("something went wrong!!!")

    def business_trip(graph, cities:list ):
        cost = 0
        flight = False
        for i in range(len(cities)-1):
            items = graph._adjacency_list[cities[i]]
            print(items)
            for item in items:
                if cities[i+1] == item[0]:
                    cost += item[1]
                    flight = True
                    break
                else:
                    cost += 0
                    flight = False
        if not flight:
            return False,'$0'     
        return True,'$'+ str(cost)



