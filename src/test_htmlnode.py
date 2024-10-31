import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="div", value="This is a div", children=[], props={"class": "container"})
        node2 = HTMLNode(tag="div", value="This is a div", children=[], props={"class": "container"})
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = HTMLNode(tag="div", value="This is a div", children=[], props={"class": "container"})
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=This is a div, children=[], props={'class': 'container'})")
    
    def test_props_to_html(self):
        node = HTMLNode(tag="div", value="This is a div", children=[], props={"class": "container"})
        self.assertEqual(node.props_to_html(), ' class="container"')

    def test_props_to_html_no_props(self):
        node = HTMLNode(tag="div", value="This is a div", children=[])
        self.assertEqual(node.props_to_html(), "")

    def test_to_html(self):
        node = HTMLNode(tag="div", value="This is a div", children=[], props={"class": "container"})
        with self.assertRaises(NotImplementedError):
            node.to_html()
    

if __name__ == "__main__":
    unittest.main()