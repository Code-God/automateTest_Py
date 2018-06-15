import time
from datetime import datetime
from telnetlib import EC

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#为了防止乱码问题，以及方便的在程序中添加中文注释，把编码统一成 UTF-8
#coding=utf-8

#导入 selenium 的 webdriver 包，只有导入 webdriver 包我们才能使用 webdriver API 进行自动化脚本的开发
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def showbaidu(request):
    #将控制的 webdriver 的Chrome赋值给 driver
    driver = webdriver.Chrome()
    #浏览器窗口最大化
    driver.maximize_window()
    # 隐性等待 这里设置智能等待10s
    driver.implicitly_wait(10)
    try:
        #把百度的地址定义为一个字符串
        first_url = 'http://www.baidu.com'
        #通过 get()方法，向浏览器发送网址
        driver.get(first_url)
        #打印百度地址，通过%s引用字符串变量
        print("access to %s " % (first_url))
        #通过 id=kw 定位到百度的输入框，并通过键盘方法send_keys()向输入框里输入 hello world
        driver.find_element_by_id("kw").send_keys("hello world")
        #通过 id=su 定位的搜索按钮，并向按钮发送单击事件click()
        driver.find_element_by_id("su").click()
        #清空搜索框中的内容
        driver.find_element_by_id("kw").clear()
        # 通过 id=kw 定位到百度的输入框，并通过键盘方法send_keys()向输入框里输入 程序员
        driver.find_element_by_id("kw").send_keys("程序员")
        # 通过 id=su 定位的搜索按钮，并向按钮发送单击事件click()
        driver.find_element_by_id("su").click()
        # 设置等待时间5s
        time.sleep(5)
        # 获取网页的html数据
        html = driver.page_source
        # 截图
        driver.get_screenshot_as_file("D:\\baidu_img.jpg")
    finally:
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        # 退出并关闭窗口的每一个相关的驱动程序
        driver.quit()
    return HttpResponse("测试完成："+html)
    # try:
    #     # 为了更好的对比效果，首先我们设置了一个存在的元素，然后在去找一个不存在的元素，同样设置了10s的等待时间
    #     # kw元素存在时
    #     print(datetime.now())  #
    #     element = WebDriverWait(driver, 10).until(  # until 也属于WebDriverWait,代表一直等待,直到某元素可见，until_not与其相反，判断某个元素直到不存在
    #         EC.presence_of_element_located((By.ID, "kw"))  # presence_of_element_located主要判断页面元素kw在页面中存在。
    #     )
    #     # kw111元素不存在时
    #     print(datetime.now())
    #     element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.ID, "kw111"))
    #     )
    # finally:
    #     print(datetime.now())
    #     driver.quit()