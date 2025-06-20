import xml.etree.ElementTree as ET

# XML data provided
xml_string = """
<a>
  <b>X</b>
  <c>
    <d>Y</d>
    <e>Z</e>
  </c>
</a>
"""

# Path to find
path = "/a/c/e"

# Parse the XML string
root = ET.fromstring(xml_string)

# ElementTree's find() method uses a simple path syntax.
# The path "/a/c/e" implies 'a' is the root.
# We need to adapt the path for the find() method.
# If the root of our parsed XML is 'a', we search for 'c/e'.

path_parts = path.strip('/').split('/')

if root.tag == path_parts[0]:
    # The rest of the path to search for
    search_path = './' + '/'.join(path_parts[1:])
    print(search_path)
    element = root.find(search_path)
    if element is not None:
        print(f"Value at path '{path}': {element.text}")
    else:
        print(f"Element at path '{path}' not found.")
else:
    print(f"Root tag mismatch. Expected '{path_parts[0]}', but got '{root.tag}'.")
