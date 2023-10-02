import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service())
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

acciones = ActionChains(driver)
acciones.scroll_to_element(driver.find_element(By.ID, "mousehover")).perform()
acciones.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
acciones.double_click(driver.find_element(By.LINK_TEXT, "Reload")).perform()
time.sleep(3)

#drag and drop
driver.get("https://selenium08.blogspot.com/2020/01/click-and-hold.html")
acciones.drag_and_drop(driver.find_element(By.XPATH, "//li[@name='A']"), driver.find_element(By.XPATH, "//li[@name='C']")).perform()
time.sleep(3)

#Simula oprimir teclas
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
acciones.key_down(Keys.TAB).send_keys("texto").perform()
time.sleep(3)
