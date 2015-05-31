from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.maximize_window()
print browser.title
browser.find_element_by_id('kw').send_keys('selenium')
browser.find_element_by_id('su').click()
browser.set_window_size(800, 480)
browser.find_element_by_name('wd').clear()
browser.find_element_by_name('wd').send_keys('python')
browser.find_element_by_id('su').send_keys(Keys.ENTER)
browser.maximize_window()
browser.find_element_by_id('tb_mr').click()
time.sleep(3)
browser.back()
print browser.find_element_by_id('cp').text
browser.quit()
