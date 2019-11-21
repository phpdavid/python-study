import re
from urllib import request


class Spider():
    url = "http://jewelry.xbiao.com/"  # 源网页
    root_patten = '<div class="main-content">([\s\S]*?)</ul>'  # 第一层剥壳
    li_patten = '<li>([\s\S]*?)</li>'  # 第二层剥壳
    name_patten = '<span>([\s\S]*?)</span>'  # 匹配名称
    price_patten = '<i>([\s\S]*?)</i>'  # 匹配价格
    hot_patten = '<em>([\d]*?)</em>'  # 匹配热度

    # 获取网页内容
    def __fetch_contents(self):
        r = request.urlopen(Spider.url)
        html = r.read()
        html = str(html, encoding='utf-8')
        return html

    # 网页内容剥壳
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
            brand = {'name': name, 'price': price, 'hot': hot}
            brands.append(brand)
        return brands

    # 网页内容精简
    def __refine(self, brands):
        ld = lambda brand: {
            'name': brand['name'][0].strip(),
            'price': brand['price'][0],
            'hot': brand['hot'][0]
        }
        return map(ld, brands)

    # 排序
    def __sort(self, brands):
        brands = sorted(brands, key=self.__sort_seed, reverse=True)
        return brands

    # 排序种子
    def __sort_seed(self, brand):
        hot = int(brand['hot'])
        return hot

    # 展示
    def __show(self, brands):
        for brand in brands:
            print(brand['name'] + '-----' + brand['price'] + '----' + brand['hot'])

    # 入口
    def go(self):
        html = self.__fetch_contents()
        brands = self.__analysiy(html)
        bransds_refile = list(self.__refine(brands))
        brands_sort = self.__sort(bransds_refile)
        self.__show(brands_sort)


result = Spider()

result.go()
