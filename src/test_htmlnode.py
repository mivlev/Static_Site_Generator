import unittest

from htmlnode import HTMLNode, LeafNode

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
    

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode(tag="div", value="This is a div", props={"class": "container"})
        node2 = LeafNode(tag="div", value="This is a div", props={"class": "container"})
        self.assertEqual(node, node2)
    
    def test_to_html(self):
        node = LeafNode(tag="div", value="This is a div", props={"class": "container"})
        self.assertEqual(node.to_html(), "<div class=\"container\">This is a div</div>")
    
    def test_to_html_no_value(self):
        node = LeafNode(tag="div", value=None, props={"class": "container"})
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_to_html_no_tag(self):
        node = LeafNode(tag=None, value="This is a div", props={"class": "container"})
        self.assertEqual(node.to_html(), "This is a div")
    
    def test_to_html_no_props(self):
        node = LeafNode(tag="div", value="This is a div", props=None)
        self.assertEqual(node.to_html(), "<div>This is a div</div>")
    
if __name__ == "__main__":
    unittest.main()