import unittest

from textnode import TextNode, NodeType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", NodeType.BOLD)
        node2 = TextNode("This is a text node", NodeType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", NodeType.BOLD)
        node2 = TextNode("This is also a text node", NodeType.NORMAL)
        self.assertNotEqual(node, node2)
    
    def test_eq_with_url(self):
        node = TextNode("This is a text node", NodeType.BOLD, "https://www.google.com")
        node2 = TextNode("This is a text node", NodeType.BOLD, "https://www.google.com")
        self.assertEqual(node, node2)

    def test_not_eq_with_url(self):
        node = TextNode("This is a text node", NodeType.BOLD, "https://www.google.com")
        node2 = TextNode("This is a text node", NodeType.BOLD, "https://www.youtube.com")
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", NodeType.BOLD, "https://www.google.com")
        self.assertEqual(repr(node), "TextNode(text=This is a text node, text_type=1, url=https://www.google.com)")

    


if __name__ == "__main__":
    unittest.main()
