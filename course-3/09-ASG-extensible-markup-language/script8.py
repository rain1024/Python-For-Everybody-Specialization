import os
from lxml import etree

# This script demonstrates XML validation based on an XSD schema.
# It requires the 'lxml' library. If not installed, run: pip install lxml

# --- File Definitions ---

# The path for the file is relative to the current directory
# The current directory is course-3/09-ASG-extensible-markup-language/
XSD_FILE = "person.xsd"
XML_FILE_INVALID = "person_invalid.xml"
XML_FILE_VALID = "person_valid.xml"

# XSD content defining the structure of a 'person' element.
# Note that the 'age' element is expected to be in lowercase.
XSD_CONTENT = """
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
    <xs:complexType name="personType">
        <xs:sequence>
            <xs:element name="lastname" type="xs:string"/>
            <xs:element name="age" type="xs:integer"/>
            <xs:element name="dateborn" type="xs:date"/>
        </xs:sequence>
    </xs:complexType>
    <xs:element name="person" type="personType"/>
</xs:schema>
"""

# This XML is invalid because the 'Age' tag is capitalized,
# but the XSD expects it to be in lowercase 'age'.
XML_CONTENT_INVALID = """
<person>
    <lastname>Severance</lastname>
    <Age>17</Age>
    <dateborn>2001-04-17</dateborn>
</person>
"""

# This is the corrected version of the XML, with the 'age' tag in lowercase.
XML_CONTENT_VALID = """
<person>
    <lastname>Severance</lastname>
    <age>17</age>
    <dateborn>2001-04-17</dateborn>
</person>
"""

def setup_files():
    """Create the XML and XSD files for the demo."""
    with open(XSD_FILE, "w") as f:
        f.write(XSD_CONTENT)
    with open(XML_FILE_INVALID, "w") as f:
        f.write(XML_CONTENT_INVALID)
    with open(XML_FILE_VALID, "w") as f:
        f.write(XML_CONTENT_VALID)
    print("Created XSD and XML files for demonstration.")

def validate_xml(xml_path, xsd_path):
    """
    Validates an XML file against an XSD schema and prints the result.
    """
    print(f"--- Validating {xml_path} against {xsd_path} ---")
    try:
        xml_doc = etree.parse(xml_path)
        xsd_doc = etree.parse(xsd_path)
        xml_schema = etree.XMLSchema(xsd_doc)

        xml_schema.assertValid(xml_doc)
        print(f"SUCCESS: {xml_path} is valid.")
        return True
    except etree.DocumentInvalid as err:
        print(f"ERROR: {xml_path} is invalid.")
        print("Validation error message:")
        print(err)
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def cleanup_files():
    """Remove the created files."""
    for f in [XSD_FILE, XML_FILE_INVALID, XML_FILE_VALID]:
        if os.path.exists(f):
            os.remove(f)
    print("\nCleaned up demonstration files.")

if __name__ == "__main__":
    try:
        setup_files()
        print("-" * 50)
        # 1. Validate the incorrect XML file
        validate_xml(XML_FILE_INVALID, XSD_FILE)
        print("-" * 50)
        # 2. Validate the correct XML file
        validate_xml(XML_FILE_VALID, XSD_FILE)
        print("-" * 50)
    finally:
        # 3. Clean up the created files
        cleanup_files()
