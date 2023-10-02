import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(service=Service())
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

dropdown = Select(driver.find_element(By.TAG_NAME, "select"))
dropdown.select_by_index(1)
dropdown.select_by_value("consult")
dropdown.select_by_visible_text("Student")

time.sleep(3)