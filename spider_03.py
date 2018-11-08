#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""节点交互 """

from selenium import webdriver
import time

# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input = browser.find_element_by_id('q')
# input.send_keys('iPhone')
# time.sleep(1)
# input.clear()
# input.send_keys('iPad')
# button = browser.find_element_by_class_name('btn-search')
# button.click()
"""在这里我们首先驱动浏览器打开淘宝，然后用 find_element_by_id() 方法获取输入框，
然后用 send_keys() 方法输入 iPhone 文字，等待一秒之后用 clear() 方法清空输入框，
再次调用 send_keys() 方法输入 iPad 文字，之后再用 find_element_by_class_name() 
方法获取搜索按钮，最后调用 click() 方法完成搜索动作。"""
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('iPone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')
button.click()
