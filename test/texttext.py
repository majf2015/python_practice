#coding=utf-8
from selenium import webdriver
import time
import selenium

browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
browser.find_element_by_id('kw').send_keys('selenium')
browser.find_element_by_id('su').click()
main_window = browser.current_window_handle

time.sleep(1)
for i in range(1, 11):
    try:
        browser.find_element_by_xpath("//div[@id=%d]/h3/a" % i).click()
        print browser.title
        time.sleep(1)
        browser.switch_to_window(main_window)
    except selenium.common.exceptions.NoSuchElementException:
        print "NoSuchElementException://div[@id=%d]/h3/a" % i
        continue
#browser.quit()