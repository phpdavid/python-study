from xml.etree.ElementTree import parse, tostring

with open('admin_user_20200203.xml', 'rb') as rf:
    root = parse(rf).getroot()
    # print(parse(rf).getroot().getchildren())  # tag 标签，attrib 属性，text 文本,text.strip() 过滤
    # print(list(parse(rf).getroot()))  # tag 标签，attrib 属性，text 文本,text.strip() 过滤
    # for rec in parse(rf).iterfind('RECORD'):  # 得到生成器对象
    #     print(rec.find('user_name'))  # find 搜索tag名称
    # print(rec.get('name'))  # get 属性
    # exit()
    # print(list(root.iter()))  # iter 递归查找，不传参数，遍历全部
    # print(root.findall('RECORD/user_id'))  # 高级用法，'*'代表所有
    # print(root.findall('.//user_id'))  # 高级用法，'.//' 代表遍历查找
    # print(root.findall('.//user_id/..'))  # 高级用法，'..'父级
    # print(root.findall('RECORD[@name]'))  # 用属性作为条件查找，只能查找子级
    # print(root.findall('RECORD[@name="second"]'))  # 用属性作为条件查找，只能查找子级,查找特定属性名称
    # print(root.findall('RECORD[user_id]'))  #包含指定tag
    # print(root.findall('RECORD[user_id="22"]'))  # 包含指定tag的文本
    # print(root.findall('RECORD[2]'))  # 根据查找出列表的序号,last()最后一个，倒数第二个last()-1
    #
    # exit()
    a = 0
    for li in root:
        print(li.find('user_id').text)
