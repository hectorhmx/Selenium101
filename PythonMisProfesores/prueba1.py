# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
search = "Nombre del profesor"
search.casefold()
mydriver = webdriver.Firefox()
mydriver.get("https://www.misprofesores.com/")
mydriver.implicitly_wait(5)##esperara 5 segundos
barBus = mydriver.find_element_by_name("q")
barBus.clear()
barBus.send_keys(search)
barBus.send_keys(Keys.RETURN)
assert "No results found" not in mydriver.page_source
container = mydriver.find_element_by_id("___gcse_0") ##principal container
resultados = container.find_elements_by_class_name("gs-title")

chosen = ""
for i in resultados:
    if i.tag_name=="a":
        url = i.get_attribute("href")
        if "/profesores/" in url :
            nombre = i.text
            nombre = nombre.split("-")
            nombre = nombre[0].casefold()
            if search in nombre:
               print(nombre)
               print(url)
               chosen = url
mydriver.get(chosen)

mydriver.close()
