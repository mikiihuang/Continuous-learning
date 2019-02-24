import configparser
import requests
def read_config(filename):
    """

    :param filename: 读取的配置文件
    :return: 词典
    """

    config = configparser.ConfigParser()
    config.read("config.ini")
    section = config.sections()
    conf = config.items(section[0])
    data = {item[0]:item[1] for item in conf}
    # assert data["environment"] == "test"
    if data['environment'] == "test":
        data["url"] = "https://test.alphalawyer.cn/"
    return data


conf = read_config("config.ini")
#
# import xlrd
# workbook = xlrd.open_workbook("interface.xlsx")
# get_sheet = workbook.sheet_by_index(0)
# # print(get_sheet.name)
# rows = get_sheet.nrows
# caseList = []
# for n in range(1,rows):
#     if get_sheet.cell(n,0) == "N":
#         pass
#     else:
#         tempdict = {}
#         tempdict["id"] = n
#         tempdict["path"] = get_sheet.cell(n,2).value
#         tempdict["method"] = get_sheet.cell(n,5).value
#         tempdict['data'] = get_sheet.cell(n, 6).value
#         tempdict['save'] = get_sheet.cell(n, 9).value
#         tempdict['contain'] = get_sheet.cell(n, 8).value
#         tempdict['datapath'] = get_sheet.cell(n, 10).value
#         caseList.append(tempdict)
# # print(caseList)
# #
# headers = {"Content-Type": "application/json;charset=UTF-8"}
# length = len(caseList)
# for i in range(length):
#     if tempdict["method"] == "POST":
#         url = conf["url"]+tempdict["path"]
#         login = requests.post(url,tempdict["data"],headers).json()
#         token = login["jwtTokenDTO"]["token"]
#         headers["token"]=token
#
import xlwt
f = xlwt.Workbook(encoding="utf-8")
sheet1 = f.add_sheet("测试结果")
row0 = [u'业务',u'状态',u'北京',u'上海',u'广州',u'深圳',u'状态小计',u'合计']
for x in range(len(row0)):
    sheet1.write(0, x, row0[x])
sheet1.write(1,0,"好啊")
sheet1.write(1,1,123)
f.save("1.xls")
# for i in range(10):
#     sheet1.write(i, 0, "hahahaha")
#     sheet1.write(i, 1, "北京")
# f.save("after.xlsx")
