import xml.etree.ElementTree as ET

# XML data from the example
xml_data = '''<person>
    <name>Chuck</name>
    <phone type="intl">+1 734 303 4456</phone>
    <email hide="yes" />
</person>'''

print("=== XML Attribute Demonstration ===")
print("XML Structure:")
print(xml_data)
print("\n" + "="*50)

# Parse the XML
root = ET.fromstring(xml_data)

# Find the phone element
phone_element = root.find('phone')

print(f"\nPhone element text content: '{phone_element.text.strip()}'")
print(f"Phone element 'type' attribute: '{phone_element.get('type')}'")

print("\n--- All attributes of phone element ---")
for attr_name, attr_value in phone_element.attrib.items():
    print(f"Attribute: {attr_name} = '{attr_value}'")

# Also demonstrate the email element attributes
email_element = root.find('email')
print(f"\nEmail element 'hide' attribute: '{email_element.get('hide')}'")

print("\n--- Key Concepts ---")
print("• 'type' is an ATTRIBUTE of the <phone> element")
print("• Attributes provide additional information about elements")
print("• Attributes are written as name='value' pairs inside the opening tag")
print("• The phone number itself is the TEXT CONTENT of the element")
print("• The 'type' attribute tells us the phone number format is international")
