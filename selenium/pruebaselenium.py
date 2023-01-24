from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time


def iniciarDriver():
    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    global driver
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    driver.get(
        "https://www.way2automation.com/way2auto_jquery/index.php")

    try:
        WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(
            (By.ID, 'load_box')))
        print("div inicial encontrado")
    except:
        print("NO ENCONTRE")

    nombre = driver.find_element(
        By.NAME, "name")
    nombre.send_keys("Andres Espinosa")

    telefono = driver.find_element(
        By.NAME, "phone")
    telefono.send_keys("55544433")

    correo = driver.find_element(
        By.NAME, "email")
    correo.send_keys("fake123@fakemail.com")

    pais = Select( driver.find_element(
        By.NAME, "country"))
    pais.select_by_visible_text("Colombia")

    ciudad = driver.find_element(
        By.NAME, "city")
    ciudad.send_keys("Bogota")

    usuario = driver.find_element(
        By.NAME, "username")
    usuario.send_keys("andrespi")

    clave = driver.find_element(
        By.NAME, "password")
    clave.send_keys("andrespi210785")

    #enviar = driver.find_element(
    #    By.CLASS_NAME, "button")
    #enviar.click()

    time.sleep(600)
    #driver.close()

iniciarDriver()
