from selenium import webdriver ###Importamos el driver
from selenium.webdriver.common.keys import Keys ###Permitirá simular entradas de teclado.


busqueda = input("¿Qué deseas buscar? >> ")
browser = webdriver.Firefox()
browser.get("http://www.google.com")
seek_bar = browser.find_element_by_name("q")
seek_bar.send_keys(busqueda)
seek_bar.send_keys(Keys.ENTER)
