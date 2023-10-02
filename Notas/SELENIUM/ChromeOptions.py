from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Podremos configurar opciones extras al navegador mediante las chromeOptions
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")


#Se deben pasar las opciones al driver
driver = webdriver.Chrome(service=Service(),options=chrome_options)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

#Tomar screenshots
driver.get_screenshot_as_file("screenTest.png")

