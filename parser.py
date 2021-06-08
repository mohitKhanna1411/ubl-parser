import pdfkit
import xml.etree.ElementTree as ET
mytree = ET.parse('ubl.xml')

# myroot = mytree.getroot()

char_to_replace = {'{urn:oasis:names:specification:ubl:schema:xsd:Invoice-2': '',
                   '{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2': '',
                   '}': '',
                   '{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2': ''}


def cleaning_tag(tag):
    for key, value in char_to_replace.items():
        tag = tag.replace(key, value)
    return tag


out = ''

for elem in mytree.iter():
    print(cleaning_tag(elem.tag), elem.text)
    out += cleaning_tag(elem.tag) + ': ' + elem.text + '</br>'


text = '''
<html>
    <body>
       ''' + out + '''
    </body>
</html>
'''

file = open("sample.html", "w")
file.write(text)
file.close()

pdfkit.from_file('sample.html', 'out.pdf')
# namespaces = {
#     'cac': 'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2', 'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2'}
# for country in myroot.find('cac:OrderReference', namespaces):
#     rank = country.find('cbc:ID', namespaces).text
#     name = country.get('cbc:ID')
#     print(rank, name)
# for x in myroot:
#     clean_tag = cleaning_tag(x.tag)

#     print(x.tag, x.text)
#     # if x.tag == 'OrderReference':
#     # rank = x.tag.find('cbc:ID', namespaces).text
#     # name = x.tag.get('cbc:ID')
#     # print(rank, name)
#     for country in clean_tag.find('cac:OrderReference', namespaces):
#         rank = country.find('cbc:ID', namespaces).text
#         name = country.get('cbc:ID')
#         print(rank, name)
