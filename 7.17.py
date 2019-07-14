# n = [1,2,3]
# s = 5
# for i in range(len(n)):
#     for j in range(i+1, len(n)):
#         if n[i] + n[j] == s:
#             print(s)
#         else:
#             continue
#
# def sum(n, s):
#     for i in range(len(n)):
#         for j in range(i+1, len(n)):
#             if n[i] + n[j] == s:
#                 return True
#             else:
#                 continue
#     return False
#
# print(sum([1,2,3], 6))
#
# 12579
# 9
import requests
from lxml import etree


url = "https://tech.163.com/"
r = requests.get(url)
r.encoding = r.apparent_encoding
# print(r.text)
tree = etree.HTML(r.text)
tittle_list = tree.xpath('//div[@class="newest-lists"]/ul/li/a/p/text()')
for i in tittle_list:
    i = i.replace(' ', '')
    i = i.replace('\n', '')
    print(i)

# print(tittle_list)
