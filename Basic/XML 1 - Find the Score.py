## XML 1 Find the Score
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    num_attrib = len(node.attrib)
    for child in node:
        num_attrib += get_attr_number(child)
    return num_attrib

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))