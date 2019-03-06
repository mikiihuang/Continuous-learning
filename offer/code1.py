# https://toutiao.com/index.html转成html.index/com.toutiao://https
#
# def rever(str):
#     all_list = str.split("/")
#     l1= []
#     str = ""
#     for i in all_list:
#         l1.insert(0,list(item for item in i.split("."))[::-1])
#     length = len(l1)
#     for i in range(length-3):
#         str = str+ ".".join(x for x in l1[i])
#         str = str+"/"
#
#     str = str+".".join(l1[-3])+"://"+"".join(l1[-1]).replace(":","")
#
#     # str = str+"//".join(l1[length-1]).replace(":","")
#     print(str)
def rever(str):
    all_list = str.split("://")
    item = all_list[1]
    gang_split = item.split("/")
    l1=[]
    l1.append(list( ))

rever("https://toutiao.com/index.html/123.com")