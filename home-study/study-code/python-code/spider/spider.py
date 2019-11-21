import re
from urllib import request


class Spider():
    url = "http://jewelry.xbiao.com/"
    root_patten = '<div class="main-content">([\s\S]*?)</ul>'
    li_patten = '<li>([\s\S]*?)</li>'
    name_patten = '<span>([\s\S]*?)</span>'
    price_patten = '<i>([\s\S]*?)</i>'
    hot_li_patten = '<span class="dai" data-type="0" data-id="75">([\s\S]*?)</span>'
    hot_patten = '<em>([\d]*?)</em>'

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
            li_htmls = re.findall(Spider.li_patten, html)

        for li in li_htmls:
            name = re.findall(Spider.name_patten, li)
            price = re.findall(Spider.price_patten, li)
            hot = re.findall(Spider.hot_patten, li)
            brand = {'name': name, 'price': price,'hot':hot}
            brands.append(brand)
        return brands

    def __refine(self, brands):
        ld = lambda brand: {
            'name': brand['name'][0].strip(),
            'price': brand['price'][0],
            'hot': brand['hot'][0]
        }
        return map(ld, brands)

    def __sort(self, brands):
        sorted(brands, key=self.__sort_seed,reverse=True)
        return brands

    def __sort_seed(self, brand):
        # r = re.findall('\d*',brand['hot'])
        hot = float(brand['hot'])
        return hot

    def __show(self, brands):
        for brand in brands:
            print(brand['name'] + '-----' + brand['price']+'----'+brand['hot'])

    def go(self):
        html = self.__fetch_contents()
        brands = self.__analysiy(html)
        bransds_refile = list(self.__refine(brands))
        brands_sort = self.__sort(bransds_refile)
        self.__show(brands_sort)


result = Spider()

result.go()
