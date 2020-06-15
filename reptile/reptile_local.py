#!python3
# coding=utf-8
from urllib import request
import ssl


class novel_reptile(object):
    path = "https://m.69shu.com/txt/8894/22698724"
    context = ssl._create_unverified_context()

    def reptile_novel(self, path):
        resp = request.urlopen(path, context=self.context)
        novel = resp.read().decode("utf8")
        print(novel)


if __name__ == '__main__':
    nreptile = novel_reptile()
    nreptile.reptile_novel(path=nreptile.path)
