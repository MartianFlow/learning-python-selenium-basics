import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service())
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.ID, "name").send_keys("Jeff")
driver.find_element(By.ID, "alertbtn").click()
alerta = driver.switch_to.alert
textoAlerta = alerta.text
assert "Jeff" in textoAlerta
alerta.accept()
alerta.dismiss()
time.sleep(2)

# Alerta dos
driver.find_element(By.ID, "confirmbtn").click()
alertaConfirmacion = driver.switch_to.alert
time.sleep(2)
alerta.dismiss()
