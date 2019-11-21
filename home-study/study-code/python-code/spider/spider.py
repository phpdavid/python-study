import re
from urllib import request


class Spider():
    url = "http://jewelry.xbiao.com/"
    root_patten = '<div class="main-content">([\s\S]*?)</ul>'
    li_patten = '<li>([\s\S]*?)</li>'
    name_patten = '<span>([\s\S]*?)</span>'
    price_patten = '<i>([\s\S]*?)</i>'

    def __fetch_contents(self):
        r = request.urlopen(Spider.url)
        html = r.read()
        html = str(html, encoding='utf-8')
        return html


    def __analysiy(self, htmls):
        root_html = re.findall(Spider.root_patten, htmls)
        li_htmls = []
        brands = []
        for html in root_html:
            li_htmls = re.findall(Spider.li_patten,html)


        for li in li_htmls:
            name = re.findall(Spider.name_patten,li)
            price = re.findall(Spider.price_patten,li)
            brand = {'name':name,'price':price}
            brands.append(brand)
        print(brands)






    def go(self):
        html = self.__fetch_contents()
        self.__analysiy(html)


result = Spider()

result.go()
