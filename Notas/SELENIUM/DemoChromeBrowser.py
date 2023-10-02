from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Si dejamos la clase Service sin parametros, se descargara el chromedriver por defecto para la version actual de chrome que tengamos
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.google.com")

print(driver.title)
print(driver.current_url)

driver.get("https://www.youtube.com")
driver.minimize_window() #minimiza el navegador
driver.maximize_window() #maximiza el navegador
driver.back() #retrocede a la pagina anterior
driver.forward() #avanza a la pagina siguiente
driver.refresh() #refresca la pagina actual
driver.close() #cerrar navegador

# service_obj = Service("driver/chromedriver.exe")
# driver = SELENIUM.Chrome(service=service_obj)
# driver.get("https://www.google.com")