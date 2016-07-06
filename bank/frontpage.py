#!/usr/bin/python
#-*-coding:utf8-*-
from selenium import webdriver
import time


browser = webdriver.Firefox()
url = "http://codingpy.com"
browser.set_window_size(1200, 900)
browser.get(url)
time.sleep(10)

browser.save_screenshot("codingpy.png")
browser.close()