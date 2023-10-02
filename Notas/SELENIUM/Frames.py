import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service())
driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr")

driver.find_element(By.XPATH,"//body[@class='mce-content-body ']/p").clear()
driver.find_element(By.XPATH,"//body[@class='mce-content-body ']/p").send_keys("Manipulando Iframe")

driver.switch_to.default_content()
print(driver.find_element(By.XPATH,"//div[@class='example']/h3").text)

time.sleep(3)


