from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service())

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

#Ejecutar script de JS
driver.execute_script("window.scrollTo(0,2000);")
#Tomar screenshots
driver.get_screenshot_as_file("screenTest.png")