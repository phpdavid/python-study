import re
from urllib import request


class Spider():
    url = "https://music.douban.com/"
    root_patten = '<div class="player-round-btn-bg">[\s\S]*?</div>'

    def __fetch_contents(self):
        r = request.urlopen(Spider.url)
        html = r.read()
        html = str(html, encoding='utf-8')
        return html
        # a=1

    def __analysiy(self, html):
        root_html = re.findall(Spider.root_patten, html)
        print(root_html[0])

    def go(self):
        html = self.__fetch_contents()
        self.__analysiy(html)


result = Spider()

result.go()
