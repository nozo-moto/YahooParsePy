import urllib.parse, urllib.request
import xml.etree.ElementTree as ET

class YahooParse:
    url = 'https://jlp.yahooapis.jp/MAService/V1/parse'
    def __init__(self, appid: str):
        self.appid = appid

    def getParse(self, text: str) -> str:
        param = [
            ("appid", self.appid),
            ("results", "ma,uniq"),
            ("sentence", text),
        ]
        url = "{0}?{1}".format(self.url, urllib.parse.urlencode(param))
        try:
            result = urllib.request.urlopen(url).read()
        except ValueError:
            print("アクセスに失敗しました。")
        return str(result,'utf-8')

    def parseXML(self, text: str) -> list:
        root = ET.fromstring(text)
        result = [child[1].text for child in root[0][2]]
        return result

    def parse(self, text: str) -> list:
        # print(text)
        return self.parseXML(self.getParse(text))
