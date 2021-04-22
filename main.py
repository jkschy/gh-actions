import markdown


def convert(md):
    """
    >>> convert("# Header")
    '<h1>Header</h1>'
    """

    return markdown.markdown(md)