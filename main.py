import markdown

def convert(md):
  """
  >>> convert("# header")
  '<h1>header</h1>'
  """
  
  return markdown.markdown(md)
