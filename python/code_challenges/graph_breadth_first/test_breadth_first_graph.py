import pytest 
from breadth_first_graph import Graph , Node



def test_one_node_and_one_edge():
    graph = Graph()

    start = graph.add_node('start')
    graph.add_edge(start, start, 10)

    assert graph.size() == 1
    assert graph.get_neighbors(start) == [(start, 10)]


def test_add_edge_start():
    
    graph = Graph()

    start = Node('start')

    end = graph.add_node('end')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)

def test_add_node(): 
    
    graph = Graph()

    expected = 'suzan' 

    actual = graph.add_node('suzan').value

    assert actual == expected