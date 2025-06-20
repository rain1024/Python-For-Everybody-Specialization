import xml.etree.ElementTree as ET

data = '''<a>
  <b>X</b>
  <c>
    <d>Y</d>
    <e>Z</e>
  </c>
</a>'''

root = ET.fromstring(data)
parent_map = {c: p for p in root.iter() for c in p}

e_element = root.find('.//e')
if e_element is not None:
    parent = parent_map[e_element]
    print(f"The parent of 'e' is '{parent.tag}'")
else:
    print("Element 'e' not found.")
