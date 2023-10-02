import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service())

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#HACER CLIC EN RADIO BUTTONS DINAMICOS
#FORMA 1
driver.find_element(By.XPATH,"//label[@for='radio2']/input").click()
time.sleep(2)

#FORMA 2
listaRadioButton = driver.find_elements(By.CLASS_NAME,"radioButton")
for radioButton in listaRadioButton:
    if radioButton.get_attribute("value") == "radio3":
        radioButton.click()
        assert radioButton.is_selected()
        
        break

time.sleep(2)