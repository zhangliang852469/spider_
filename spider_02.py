#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""多个节点的查找 find_elements()
find_elements_by_id
find_elements_by_name
find_elements_by_xpath
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector
"""

from selenium import webdriver
from selenium.webdriver.common.by import  By

browser = webdriver.Chrome()

browser.get('https://www.taobao.com')

# lis = browser.find_elements_by_css_selector('.service-bd li')
# lis = browser.find_elements_by_class_name('service-bd')
lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')

print(lis)
browser.close()
