import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(service=Service())
wait = WebDriverWait(driver, 6)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")


driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()

tabs = driver.window_handles
driver.switch_to.window(tabs[1])
email = driver.find_element(By.XPATH, "//p[@class='im-para red']/strong/a").text
driver.switch_to.window(tabs[0])

driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys("learning")
driver.find_element(By.ID, "signInBtn").click()


wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[@class='alert alert-danger col-md-12']")))
response = driver.find_element(By.XPATH, "//div[@class='alert alert-danger col-md-12']").text

assert "Incorrect username/password." == response

print(response)
time.sleep(5)
