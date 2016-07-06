#!/usr/bin/python
#-*-coding:utf8-*-
from selenium import webdriver
import time

#获得一个火狐浏览器对象，会打开火狐
ff = webdriver.Firefox()
#会进入weibo.com
ff.get('http://weibo.com/')
#每步操作留3秒时间
time.sleep(3)
#输入用户名(你的微博账号)
ff.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div[3]/div[2]/div[1]/div/input").send_keys('jinchenyx@sina.com')
time.sleep(3)
#输入密码（你的微博密码）
ff.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div/input").send_keys('jxyzh0512')
time.sleep(3)
#点击登录
ff.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div[3]/div[2]/div[6]/a").click()

#写微博
time.sleep(10)
ff.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[2]/textarea').send_keys('test from selenium')
#发布
time.sleep(3)
ff.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[3]/div[1]/a').click()