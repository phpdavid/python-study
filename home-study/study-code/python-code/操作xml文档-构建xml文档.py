from xml.etree.ElementTree import ElementTree, Element, tostring

e = Element('Data')  # 声明元素
e.set('name', 'abc')  # 声明元素的属性
e.text = '123'  # 元素的文本
e2 = Element('Row')
e3 = Element('Open')
e3.text = '8.80'
e2.append(e3)  # 添加子元素
e.text = None  # 去掉e的text
e.append(e2)
# print(tostring(e))  # 查看xml效果
#写入到文件
et = ElementTree(e)
et.write('demo.xml')