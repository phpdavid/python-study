import re
from urllib import request


class Spider():
    url = "http://jewelry.xbiao.com/"
    root_patten = '<div class="main-content">([\s\S]*?)</ul>'
    name_patten = '<span>([\s\S]*?)</span>'
    price_patten = '<i>([\s\S]*?)</i>'

    def __fetch_contents(self):
        r = request.urlopen(Spider.url)
        html = r.read()
        html = str(html, encoding='utf-8')
        return html


    def __analysiy(self, htmls):
        root_html = re.findall(Spider.root_patten, htmls)
        brands = []
        for html in root_html:
            name = re.findall(Spider.name_patten, html)
            price = re.findall(Spider.price_patten, html)
            brand = {'name': name,'price': price}
            brands.append(brand)
        print(brands)

    def go(self):
        html = self.__fetch_contents()
        sec_html = self.__analysiy(html)


result = Spider()

result.go()
