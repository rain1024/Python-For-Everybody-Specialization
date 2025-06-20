import xml.etree.ElementTree as ET

data = '''
<people>
    <person>
       <name>Chuck</name>
       <phone>303 4456</phone>
    </person>
    <person>
       <name>Noah</name>
       <phone>622 7421</phone>
    </person>
</people>'''

tree = ET.fromstring(data)
persons = tree.findall('person')

for person in persons:
    name = person.find('name').text
    phone = person.find('phone').text
    print('Name:', name)
    print('Phone:', phone)
