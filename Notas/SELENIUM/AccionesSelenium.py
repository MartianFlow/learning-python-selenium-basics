

#Hacer clic en un elemento
elemento = driver.find_element(By.ID, "boton")
elemento.click()

#Enviar texto a un campo de entrada
elemento = driver.find_element(By.NAME, "nombre_usuario")
elemento.send_keys("mi_usuario")

#Borrar un campo de entrada:
elemento = driver.find_element(By.ID, "campo")
elemento.clear()

#Obtener el texto de un elemento
elemento = driver.find_element(By.CLASS_NAME, "texto")
texto = elemento.text

#Seleccionar una opción de una lista desplegable (select)
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element(By.NAME, "selector"))
select.select_by_value("opcion_valor")

#Realizar acciones de arrastrar y soltar
elemento_fuente = driver.find_element(By.ID, "fuente")
elemento_destino = driver.find_element(By.ID, "destino")

from selenium.webdriver import ActionChains
acciones = ActionChains(driver)
acciones.drag_and_drop(elemento_fuente, elemento_destino).perform()