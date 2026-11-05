class HTMLNode:
    def __init__(
            self, 
            tag: str | None = None, 
            value: str | None = None, 
            children: list[HTMLNode] | None = None, 
            props: dict[str, str] | None = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Method not implemented")

    def props_to_html(self):
        if not self.props:
            return ''
        props: list[str] = []
        for k in self.props:
            props.append(f'{k}="{self.props[k]}"')

        return ' '.join(props)

    def __repr__(self):
        return f'HTMLNode({self.tag, self.value, self.children, self.props})'

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict[str, str] | None = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError('A leaf node must have a value')
        if not self.tag:
            return self.value

        return f'<{self.tag}{'' if not self.props else ' ' + super().props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f'HTMLNode({self.tag} {self.value} {self.props})'

class ParentNode(HTMLNode):
    def __init__(
            self, 
            tag: str, 
            children: list[LeafNode], 
            props: dict[str, str] = None
        ):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("A parent node must have a tag")
        if not self.children:
            raise ValueError("A parent node must have a children at least")

        result: str = ''
        for c in self.children:
            result += c.to_html()

        return f'<{self.tag}>{result}</{self.tag}>'
    