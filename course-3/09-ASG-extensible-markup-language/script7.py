from lxml import etree
import os

def validate_xml(xml_path, xsd_path):
    """
    Validates an XML file against an XSD file.
    """
    try:
        # Parse the XSD schema
        with open(xsd_path, 'rb') as f:
            xsd_content = f.read()
        schema_root = etree.XML(xsd_content)
        schema = etree.XMLSchema(schema_root)

        # Parse the XML document
        xml_parser = etree.XMLParser(schema=schema)
        with open(xml_path, 'rb') as f:
            etree.fromstring(f.read(), xml_parser)
        
        print(f"Validation successful: '{xml_path}' is valid against '{xsd_path}'.")
        return True

    except etree.XMLSchemaParseError as e:
        print(f"XSD Parse Error: {e}")
        return False
    except etree.XMLSyntaxError as e:
        print(f"XML Syntax Error: '{xml_path}' is not valid against '{xsd_path}'.")
        print(f"Reason: {e}")
        return False

# Create example files
xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
"""
xsd_content = """<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="note">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="to" type="xs:string"/>
        <xs:element name="from" type="xs:string"/>
        <xs:element name="heading" type="xs:string"/>
        <xs:element name="body" type="xs:string"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
"""
invalid_xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<note>
  <to>Tove</to>
  <from>Jani</from>
  <header>Reminder</header> <!-- Invalid element -->
  <body>Don't forget me this weekend!</body>
</note>
"""

with open("example.xml", "w") as f:
    f.write(xml_content)
with open("example.xsd", "w") as f:
    f.write(xsd_content)
with open("invalid_example.xml", "w") as f:
    f.write(invalid_xml_content)

# --- Validation ---
print("--- Running Validation ---")
validate_xml("example.xml", "example.xsd")
print("-" * 20)
validate_xml("invalid_example.xml", "example.xsd")
print("--- Validation Complete ---")

# Clean up the created files
os.remove("example.xml")
os.remove("example.xsd")
os.remove("invalid_example.xml")
