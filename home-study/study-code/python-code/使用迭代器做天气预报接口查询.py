# coding:utf8

import requests
from collections.abc import Iterable, Iterator


# 气温迭代器,
class WeatherIterator(Iterator):
    # 传入城市名字的字符串列表
    def __init__(self, cities):
        self.cities = cities
        # 记录一个index，刻画迭代的位置，初始化为0
        self.index = 0

    # city是城市名字的字符串
    def getWeather(self, city):
        # 用requests库，对一固定网址进行get请求，得到一个json形式数据；
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        # 对json数据解析，得到数据：data

        if r.json()['status'] ==1000:
            data = r.json()['data']['forecast'][0]
            # 返回目标数据：data['low'], data['high']
            return '%s: %s, %s' % (city, data['low'], data['high'])
        else:
            return '%s: %s, %s' % ('错误',city, r.json()['desc'])

    # 迭代器对象实现的方法：next；功能：每次返回一个城市的信息，最终迭代完后抛出一个异常
    def __next__(self):
        # 用if语句刻画最终迭代完后的状况；self.index，刻画迭代的位置
        if self.index == len(self.cities):
            raise StopIteration
        # 正常迭代情况，即每次迭代出一个城市的气温信息；self.cities[self.index]，得到需要的城市名字
        city = self.cities[self.index]
        # 每迭代一次，要对index + 1
        self.index += 1
        # 将目标城市名字传入geWeather方法，得到目标城市的气温信息；
        return self.getWeather(city)


# 实现可迭代对象，继承Iterable，则对WeatherIterable实例化时，需要传入一个可迭代的对象；
class WeatherIterable(Iterable):
    def __init__(self, cities):
        # 先维护cities，为了后面传给构造器WeatherIterator
        self.cities = cities

    # 可迭代接口，在其内部返回WeatherIterator
    def __iter__(self):
        # 报错：Can't instantiate abstract class WeatherIterator with abstract methods __next__，
        # 即：不能用抽象的方法实例化抽象类WeatherIterator ——— 将next方法改为__next__()方法；
        return WeatherIterator(self.cities)


# 演示，只想要4个城市的气温信息；
city100 = [u'北京', u'安徽', u'福建', u'甘肃', u'广东', u'广西', u'贵州', u'海南', u'河北', u'河南', u'黑龙江', u'湖北', u'湖南', u'吉林', u'江苏',
           u'江西', u'辽宁', u'内蒙古', u'宁夏', u'青海', u'山东', u'山西', u'陕西', u'上海', u'四川', u'天津', u'西藏', u'新疆', u'云南', u'浙江',
           u'重庆', u'香港', u'澳门', u'台湾', u'安庆', u'蚌埠', u'巢湖', u'池州', u'滁州', u'阜阳', u'淮北', u'淮南', u'黄山', u'六安', u'马鞍山',
           u'宿州', u'铜陵', u'芜湖', u'宣城', u'亳州', u'北京', u'福州', u'龙岩', u'南平', u'宁德', u'莆田', u'泉州', u'三明', u'厦门', u'漳州',
           u'兰州', u'白银', u'定西', u'甘南', u'嘉峪关', u'金昌', u'酒泉', u'临夏', u'陇南', u'平凉', u'庆阳', u'天水', u'武威', u'张掖', u'广州',
           u'深圳', u'潮州', u'东莞', u'佛山', u'河源', u'惠州', u'江门', u'揭阳', u'茂名', u'梅州', u'清远', u'汕头', u'汕尾', u'韶关', u'阳江',
           u'云浮', u'湛江', u'肇庆', u'中山', u'珠海', u'南宁', u'桂林', u'百色', u'北海', u'崇左']
city1 = [u'黑龙江']
city2 = [u'北京']
for x in WeatherIterable(city100):
    print(x)
