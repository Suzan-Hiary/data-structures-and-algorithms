import pytest
from graph import Graph , Node


def test_add_to_graph():
    graph = Graph()
    expected = 'Suzan'
    actual = graph.add_node('Suzan').data
    assert  actual== expected


def test_add_edge_other_case():
    
    graph = Graph()

    node1 = graph.add_node('end')

    node2 = graph.add_node('start')

    graph.add_edge(node1, node2)    


def test_get_nodes():
    graph = Graph()
    meat = graph.add_node('meat')

    chicken = graph.add_node('chicken')

    tomato = Node('tomato')

    expected = 2
    actual =len( graph.get_node())
    assert actual == expected

def test_get_neighbors():
    graph =Graph()
    meat = graph.add_node('meat')
    chicken = graph.add_node('chicken')

    graph.add_edge(meat, chicken)

    expected= [(chicken , 0)]
    actual = graph.get_neighbors(meat)
    assert actual == expected

def test_get_weight():
    graph = Graph()
    start = graph.add_node('start')
    end = graph.add_node('end')
    mid = graph.add_node('middle')
    other = graph.add_node('other')

    graph.add_edge(start, end, 1)
    graph.add_edge(start, mid, 2)
    graph.add_edge(start, other, 3)

    assert graph.get_neighbors(start) == [(end, 1), (mid, 2), (other, 3)]

def test_size():
    graph = Graph()

    graph.add_node('ASAC')
    graph.add_node('suzan')
    graph.add_node('software')

    expected = 3
    actual = graph.size()
    assert actual == expected 

def test_one_edge_one_node():
    graph=Graph()

    start = graph.add_node('start')
    graph.add_edge(start ,start, 10)

    assert graph.size() == 1
    expexted = [(start , 10)]
    actual = graph.get_neighbors(start)
    assert actual == expexted

def test_empty_graph():
    graph = Graph()

    expected = 0
    actual = graph.size()
    assert actual == expected