#!/usr/bin/env python3
# -*- coding:utf-8 -*-
""" 查找节点 例：淘宝"""

"""
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
"""
from selenium import webdriver

# 首先初始化启动浏览器
browser = webdriver.Chrome()

# 打开网页
browser.get('https://www.taobao.com')

# 查找节点可以通过ID, css selector, xpath, name来查找
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
input_fouth = browser.find_element_by_name('q')

# 输出查找
print(input_first, '\n', input_second,'\n', input_third,'\n', input_fouth)

browser.close()








# Selenium 还提供了通用的 find_element() 方法，它需要传入两个参数，一个是查找的方式
# By，另一个就是值，实际上它就是 find_element_by_id() 这种方法的通用函数版本
# 比如 find_element_by_id(id) 就等价于 find_element(By.ID, id)，二者得到的结果完全一致。

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input_first = browser.find_element(By.ID, 'q')
# print(input_first)
# browser.close()













