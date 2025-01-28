import xml.etree.ElementTree as etree

maxdepth = 0

def depth(elem, level):
    global maxdepth
    level += 1  # Aumentamos el nivel cada vez que descendemos en la estructura
    maxdepth = max(maxdepth, level)  # Actualizamos maxdepth si encontramos un nivel más profundo
    
    for child in elem:  # Recorremos los hijos del elemento actual
        depth(child, level)  # Llamada recursiva para los hijos

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml += input() + "\n"
    
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)  # Empezamos en -1 porque la raíz cuenta como nivel 0
    print(maxdepth)
