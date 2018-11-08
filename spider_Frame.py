#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
在网页中有这样一种节点叫做 iframe，也就是子Frame，相当于页面的子页面，
它的结构和外部网页的结构是完全一致的。Selenium 打开页面后，它默认是在父级Frame
里面操作，而此时如果页面中还有子 Frame，它是不能获取到子 Frame 里面的节点的。
所以这时候我们就需要使用 switch_to.frame() 方法来切换 Frame。

"""
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.switch_to.frame('iframeResult')
# # try:
# # #     logo = browser.find_element_by_class_name('logo')
# # # except NoSuchElementException:
# # #     print('NO LOGO')
# # # browser.switch_to.parent_frame()
# # # logo = browser.find_element_by_class_name('logo')
# # # print(logo)
# # # print(logo.text)

browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser,10)
input = wait.until(EC.presence_of_all_elements_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input, button)










