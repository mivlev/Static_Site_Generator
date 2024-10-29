from textnode import TextNode, NodeType

def main():
    dummy = TextNode("dummy", NodeType.NORMAL, url="dummy_url")
    print(dummy)
if __name__ == "__main__":
    main()
