class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list["HTMLNode"] = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html is not implemented for this class")

    def props_to_html(self):
        if not self.props:
            return ""
        html = " "  # Start with one leading space
        for key, value in self.props.items():
            html += f'{key}="{value}" '
        return html[:-1]  # Remove trailing space
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag 
            and self.value == other.value 
            and self.children == other.children 
            and self.props == self.props
        )
    
class LeafNode(HTMLNode):
    def __init__(self, value: str, tag: str = None, props: dict = None):
        super().__init__(tag, value, [], props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode value cannot be None")
        if self.tag is None:
            return self.value
        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"