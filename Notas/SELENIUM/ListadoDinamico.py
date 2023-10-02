import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service())
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

# driver.find_element(By.ID,"autosuggest").send_keys("bo")
# time.sleep(2)
# driver.find_element(By.XPATH,"//a[text()='Bolivia']").click()

driver.find_element(By.ID,"autosuggest").send_keys("bo")
time.sleep(2)
listadoElementos = driver.find_elements(By.CSS_SELECTOR, ".ui-corner-all")
for elemento in listadoElementos:
    if elemento.text == "Cambodia":
        elemento.click()

#get_attribue value nos sirve para validar textos que se mapean dinamicamente en inputs de texto
texto = driver.find_element(By.ID,"autosuggest").get_attribute("value")
print(texto)
assert texto == "Cambodia"
