from urllib import request


class Spider():
    url = "http://clot-test-erp.cqjlt.net/jlt-org.roles"

    def __fetch_contents(self):
        r = request.urlopen(Spider.url)
        html = r.read()
        a = 1


    def go(self):
        r = self.__fetch_contents()



result = Spider()

result.go()
