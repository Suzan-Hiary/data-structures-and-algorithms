from graph_business_trip import Node , Graph
import pytest 


def test_graph_trip():
    graph = Graph()
    pandora = graph.add_node('Pandora')
    metroville = graph.add_node('Metroville')
    Arendelle = graph.add_node('Arendelle')
    graph.add_edge(pandora, metroville, 82)
    graph.add_edge(metroville, Arendelle, 99)
    expected = (True, '$181')
    actual = Graph.business_trip(graph, [pandora, metroville, Arendelle])
    assert expected == actual


def test_graph_trip_two():
    graph = Graph()
    pandora = graph.add_node('Pandora')
    metroville = graph.add_node('Metroville')
    graph.add_edge(pandora, metroville, 82)
    expected = (True, '$82')
    actual = Graph.business_trip(graph, [pandora, metroville])
    assert expected == actual


def test_graph_trip_three():
    graph = Graph()
    Narnia = graph.add_node('Narnia ')
    Arendelle= graph.add_node('Arendelle')
    Naboo=graph.add_node('Naboo')
    expected = (False, '$0')
    actual = Graph.business_trip(graph, [Narnia, Arendelle, Naboo]	)
    assert expected == actual

def test_graph_depth_first():
  graph = Graph()
  v1 = graph.add_node('a')
  v2 = graph.add_node('b')
  v3 = graph.add_node('c')
  v4 = graph.add_node('d')
  v5 = graph.add_node('e')
  v6 = graph.add_node('f')
  v7 = graph.add_node('g')
  v8 = graph.add_node('h')
  graph.add_edge(v1, v2)
  graph.add_edge(v1, v4)
  graph.add_edge(v2,v1)
  graph.add_edge(v2,v3)
  graph.add_edge(v2,v4)
  graph.add_edge(v3,v2)
  graph.add_edge(v3,v7)
  graph.add_edge(v4,v1)
  graph.add_edge(v4,v2)
  graph.add_edge(v4,v5)
  graph.add_edge(v4,v8)
  graph.add_edge(v4,v6)
  graph.add_edge(v6,v4)
  graph.add_edge(v6,v8)
  graph.add_edge(v8,v6)
  graph.add_edge(v8,v4)
  graph.add_edge(v5,v4)
  assert  ['a', 'b', 'c', 'g', 'd', 'e', 'h', 'f'] == ['a', 'b', 'c', 'g', 'd', 'e', 'h', 'f']