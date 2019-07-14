import re


with open("data_163", "r") as f:
    # data = ''
    txt = f.read()
    print(txt)

data = re.findall('"title":"(.*?)","priority',txt)
# .*title":"(.*?)",".*
# data = re.findall('.*title":"(.*?)",".*',txt)
print(data)
for i in data:
    info = i.replace("\\", "")
    print(info)