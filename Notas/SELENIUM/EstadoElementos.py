from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service())

#is_selected
elemento = driver.find_element(By.ID, "casilla_verificacion")
esta_seleccionado = elemento.is_selected()
if esta_seleccionado:
    print("La casilla de verificación está seleccionada.")
else:
    print("La casilla de verificación no está seleccionada.")

#is_enabled
elemento = driver.find_element(By.ID, "boton_habilitado")
esta_habilitado = elemento.is_enabled()
if esta_habilitado:
    print("El botón está habilitado y se puede hacer clic en él.")
else:
    print("El botón está deshabilitado y no se puede interactuar con él.")


#is_displayed
elemento = driver.find_element(By.ID, "elemento_visible")
esta_visible = elemento.is_displayed()
if esta_visible:
    print("El elemento es visible en la página.")
else:
    print("El elemento está oculto o fuera de la vista.")