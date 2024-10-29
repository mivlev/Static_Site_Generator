from enum import Enum

from enum import Enum

class NodeType(Enum):
    NORMAL = 0
    BOLD = 1
    ITALIC = 2
    CODE = 3
    LINKS = 4
    IMAGES = 5

class TextNode:
    def __init__(self, text: str, text_type: NodeType, url: str = None):
        self.text = text
        self.text_type = text_type.value
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode(text={self.text}, text_type={self.text_type}, url={self.url})"