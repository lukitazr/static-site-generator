import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
            "a",
            "This is a link",
            None,
            {"href": "https://nigger.com", "target": "_blank"},
        )
        self.assertEqual(node.props_to_html(), 'href="https://nigger.com" target="_blank"')

        node = HTMLNode(
            "a",
            "This is a link",
            None,
            {"target": "_blank"},
        )
        self.assertEqual(node.props_to_html(), 'target="_blank"')

        node = HTMLNode(
            "a",
            "This is a link",
            None,
        )
        self.assertEqual(node.props_to_html(), '')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

        node = LeafNode("a", "linkardo nashe", {"href": "https://x.com/", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://x.com/" target="_blank">linkardo nashe</a>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()

