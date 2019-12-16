'''
模块注释
'''
import re
from urllib import request
#爬虫框架BeautifulSoup Scrapy
#爬虫，反爬虫，反反爬虫
#频繁爬取数据，IP被封，使用IP代理
class Spider():
    '''
    类注释
    '''
    url = "http://jewelry.xbiao.com/"  # 源网页
    root_patten = '<div class="main-content">([\s\S]*?)</ul>'  # 第一层剥壳
    li_patten = '<li>([\s\S]*?)</li>'  # 第二层剥壳
    name_patten = '<span>([\s\S]*?)</span>'  # 匹配名称
    price_patten = '<i>([\s\S]*?)</i>'  # 匹配价格
    hot_patten = '<em>([\d]*?)</em>'  # 匹配热度

    # 获取数据
    def __fetch_contents(self):
        '''
        方法注释
        :return:html
        '''
        r = request.urlopen(Spider.url)
        html = r.read()
        html = str(html, encoding='utf-8')
        return html

    # 数据剥壳
    def __analysiy(self, htmls):
        '''

        :param htmls:
        :return: brands
        '''
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

    # 数据精炼
    def __refine(self, brands):
        '''

        :param brands:
        :return: ,str(brand(name)),str(brand(price)),str(brand(hot))
        '''
        ld = lambda brand: {
            'name': brand['name'][0].strip(),
            'price': brand['price'][0],
            'hot': brand['hot'][0]
        }
        return map(ld, brands)


    # 数据排序
    def __sort(self, brands):
        '''

        :param brands:
        :return:brands
        '''
        brands = sorted(brands, key=self.__sort_seed, reverse=True)
        return brands

    # 排序种子
    def __sort_seed(self, brand):
        hot = int(brand['hot'])
        return hot

    # 展示
    # def __show(self, brands):
    #     for brand in brands:
    #         print(brand['name'] + '-----' + brand['price'] + '----' + brand['hot'])
    def __show(self, brands):
        for rank in range(0, len(brands)):
            print('rank ' + str(rank + 1)
                  + ' name:' + brands[rank]['name']
                  + ' price:' + brands[rank]['price']
                  + ' hot:' + brands[rank]['hot'])

    # 入口
    def go(self):
        html = self.__fetch_contents()
        brands = self.__analysiy(html)
        bransds_refile = list(self.__refine(brands))
        brands_sort = self.__sort(bransds_refile)
        self.__show(brands_sort)


result = Spider()

result.go()
