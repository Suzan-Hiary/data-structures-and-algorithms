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