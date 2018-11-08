#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" 获取节点信息"""

# 获取属性
from selenium import webdriver
from selenium.webdriver import ActionChains


browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)

# 使用 get_attribute() 方法来获取节点的属性
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))

# 获取文本值 直接调用 .text
inpu = browser.find_element_by_class_name('zu-top-add-question')
print(inpu.text)

# 获取ID 位置 标签名 大小
print(inpu.id)
print(inpu.location)
print(inpu.tag_name)
print(inpu.size)
