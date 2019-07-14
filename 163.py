import requests
import re
import jsonpath
from lxml import etree


def it_163(s, f):
    url = f"https://3g.163.com/touch/reconstruct/article/list/BA8D4A3Rwangning/{s}-{f}.html"
    r = requests.get(url)
    data = r.text
    # print(html)
    # title_list = re.findall(r':(,*?),"priority', html, re.S)
    # print(title_list)
    # data = jsonpath(html, '$..BA8D4A3Rwangning')
    # print(data)
    # # tree = etree.HTML(html)
    # data = tree.xpath('//@title')
    # print(data)
    with open("data_163.txt", "a")as f:
        f.write(data)
    print(len(data))



it_163(1, 10)
