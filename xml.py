from xml.dom import minidom


xmldoc = minidom.parse('kropa.xml')
itemlist = xmldoc.getElementsByTagName('name')[0]
print(itemlist.firstChild.data)
itemlist.firstChild.data = "Changed XML"
file = open("newXMMMML.xml", "w")
xml = xmldoc.toxml()
file.write(xml)