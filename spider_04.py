#!/usr/bin/env python3
# -*- coding:utf-8 -*-
""" 动作链    实现一个节点的拖拽操作，将某个节点从一处拖拽到另外一处，"""

from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()

url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'

browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()




