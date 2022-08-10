import xml.etree.ElementTree as ET
handler = ET.parse("Library.xml")
stuff = handler.findall("dict/dict/dict")
print(stuff[0])

