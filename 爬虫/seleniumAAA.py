
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get('https://zhidao.baidu.com/') #

# 句柄切换
now_handle = driver.current_window_handle
print(now_handle)
driver.implicitly_wait(20)
inputStr = driver.find_element_by_id("kw")
inputStr.send_keys("感冒")
inputStr.send_keys(Keys.RETURN)
time.sleep(1)
all_handles = driver.window_handles
print(all_handles)


f = open("data3.txt","a",encoding="utf-8")
for i in range(5):

    html = driver.page_source

    soup = BeautifulSoup(html,"html.parser")

    # DOM解析，获取需要的元素
    dts = soup.find_all("dt",class_="dt mb-4 line")
    for item in dts:
        f.write(item.text.strip()+"\n")
    time.sleep(1)

    # 点击翻页
    next_page = driver.find_element_by_css_selector(".pager a:nth-last-child(2)").click()
    time.sleep(1)

driver.quit()


