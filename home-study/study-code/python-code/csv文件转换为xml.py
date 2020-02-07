from xml.etree.ElementTree import ElementTree, Element, tostring,parse
import csv


def csvToxml(fname):
    with open(fname, 'r') as rf:
        reader = csv.reader(rf)
        header = next(reader)
        #创建根节点
        root = Element('RECORDS')

        for record in reader:
            e_record = Element('RECORD')
            root.append(e_record)
            for tag,text in zip(header,record):
                e = Element(tag)
                e.text = text
                e_record.append(e)
    return ElementTree(root)


et = csvToxml('admin_user_20200203.csv')
et.write('admin_user_20200203.xml')

with open('admin_user_20200203.xml','r') as rf:
    root = parse(rf).getroot()
    for record in root:
        print(record.find('user_name').text)


