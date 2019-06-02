from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


convert = input("convert to:")




yturl='https://document.online-convert.com/convert-to-'

searchurl = yturl+convert
browser = webdriver.Chrome()
browser.get(searchurl)
time.sleep(4)
classname = browser.find_element_by_class_name('uploadButton')
classname.click() 
time.sleep(10)

clickbutton = browser.find_element_by_id("multifile-submit-button-main")
clickbutton.click()
time.sleep(5)
