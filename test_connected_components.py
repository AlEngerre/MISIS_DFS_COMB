
import unittest
from connected_components import find_connected_components

class TestConnectedComponents(unittest.TestCase):

    def test_connected_graph(self):
        graph = {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1, 3],
            3: [2, 4],
            4: [3, 5],
            5: [4]
        }
        result = find_connected_components(graph)
        expected = [[0, 1, 2, 3, 4, 5]]
        self.assertEqual(result, expected)

    def test_disconnected_graph(self):
        graph = {
            0: [1],
            1: [0],
            2: [3],
            3: [2],
            4: [],
            5: [6],
            6: [5]
        }
        result = find_connected_components(graph)
        expected = [[0, 1], [2, 3], [4], [5, 6]]
        self.assertEqual(result, expected)

    def test_isolated_vertices(self):
        graph = {
            0: [],
            1: [],
            2: [],
            3: []
        }
        result = find_connected_components(graph)
        expected = [[0], [1], [2], [3]]
        self.assertEqual(result, expected)

    def test_empty_graph(self):
        graph = {}
        result = find_connected_components(graph)
        expected = []
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
