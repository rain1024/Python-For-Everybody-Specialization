import xml.etree.ElementTree as ET

input_data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(input_data)
print('Name:', tree.find('name').text)
print('Email Hide Attribute:', tree.find('email').get('hide'))
print('Phone Type Attribute:', tree.find('phone').get('type'))
print('Phone Number:', tree.find('phone').text.strip())
