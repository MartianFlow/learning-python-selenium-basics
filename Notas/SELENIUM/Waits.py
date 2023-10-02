import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(service=Service())
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(3)
wait = WebDriverWait(driver, 6)

driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("ber")
wait.until(expected_conditions.invisibility_of_element((By.XPATH, "//div[@class='products']/div[4]")))
list = driver.find_elements(By.CSS_SELECTOR, ".product-action")
print(f"longitud: {len(list)}")

#Assingment###########################################################################
#Validacion nombre productos esperados y actuales con filtro
nomProductos = driver.find_elements(By.CSS_SELECTOR,".product .product-name")
nomProductosEsperado = ["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]
nomProductosActuales = []
for nombre in nomProductos:
    nomProductosActuales.append(nombre.text)
    assert "ber" in nombre.text
assert nomProductosEsperado == nomProductosActuales
########################################################################################

for option in list:
    option.find_element(By.CSS_SELECTOR, "button").click()

driver.find_element(By.CLASS_NAME, "cart-icon").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
codeText = driver.find_element(By.CLASS_NAME, "promoInfo").text

#Assignment####################################################################
#Comparar valor total y valor con descuento
totalAmount = float(driver.find_element(By.CLASS_NAME,"totAmt").text)
discountAmount = float(driver.find_element(By.CLASS_NAME,"discountAmt").text)
print(totalAmount - (totalAmount*0.1))
print(discountAmount)
assert discountAmount == totalAmount - (totalAmount*0.1)

time.sleep(5)

