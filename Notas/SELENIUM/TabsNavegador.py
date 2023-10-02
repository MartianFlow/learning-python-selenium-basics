import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service())

driver.get("http://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
tabs = driver.window_handles #almacenar los tabs abiertos en el navegador en un listado
driver.switch_to.window(tabs[-1]) #indicamos que deseamos movernos al ultimo tab
time.sleep(2)
textNewTab = driver.find_element(By.TAG_NAME,"h3").text
assert "New Window" in textNewTab
driver.close() #cierra el tab en el que estamos posicionados

driver.switch_to.window(tabs[0]) #nos movemos al tab original
textActualTab = driver.find_element(By.TAG_NAME,"h3").text
assert "Opening a new window" in textActualTab
time.sleep(2)