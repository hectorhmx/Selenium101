from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from loguru import logger

seek = input("¿Qué deseas buscar? >> ")
browser = webdriver.Chrome()
browser.get("http://www.google.com")
seek_bar = browser.find_element_by_name("q")
seek_bar.send_keys(seek)
seek_bar.send_keys(Keys.ENTER)