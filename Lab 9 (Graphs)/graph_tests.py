"""Lab 9 Test File
Author: Parth Ray
"""

import unittest
from my_graph import Vertex, MyGraph

class TestList(unittest.TestCase):

    def test_01(self):
        graph = MyGraph('graph_testinput1.txt')
        self.assertEqual(graph.get_conn_components(), [['1', '2', '3', '4', '5'],
                                                       ['6', '7', '8', '9']])
        self.assertTrue(graph.bicolor())

    def test_02(self):
        graph = MyGraph('graph_testinput2.txt')
        self.assertEqual(graph.get_conn_components(), [['1', '2', '3'],
                                                       ['4', '6', '7', '8']])
        self.assertFalse(graph.bicolor())


    def test_get_vertices1(self):
        graph = MyGraph('graph_testinput1.txt')
        self.assertEqual(graph.get_vertices(),
                         ["1", "2", "3", "4", "5", "6", "7", "8", "9"])

    def test_get_vertices2(self):
        graph = MyGraph('graph_testinput2.txt')
        self.assertEqual(graph.get_vertices(), ["1", "2", "3", "4", "6", "7", "8"])

    def test_get_vertex_none(self):
        graph = MyGraph('graph_testinput1.txt')
        self.assertEqual(None, graph.get_vertex("10"))

    def test_get_vertex(self):
        graph = MyGraph('graph_testinput1.txt')
        self.assertEqual(graph.get_vertex("1").key, "1")
        self.assertEqual(graph.get_vertex("1").adjacent_to, ["2", "3", "4", "5"])

    def test_add_vertex(self):
        graph = MyGraph('graph_testinput2.txt')
        graph.add_vertex("9")
        self.assertEqual(graph.get_vertex("9").key, "9")
        self.assertEqual(graph.get_vertex("9").adjacent_to, [])

    def test_add_edge(self):
        graph = MyGraph('graph_testinput1.txt')
        graph.add_edge("1", "6")

if __name__ == '__main__':
    unittest.main()
