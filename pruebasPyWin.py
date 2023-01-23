from pruebaselenium import webdriver
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
#FUNCION PARA ABRIR PAGINA#


def iniciarDriver():
    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    global driver
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    driver.get(
        "https://www.google.com/?hl=es")
    # driver.maximize_window()
    #ESPERA A ENCONTRAR ELEMENTO POR XPATH#
    try:
        WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')))
        print("ENCONTRE")
    except:
        print("NO ENCONTRE")

    try:
        #ENVIO YOUTUBE A EL INPUT#
        password = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        password.send_keys("Youtube")
        #PRECIONO TECLA ENTER#
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        #PBUSCRA TEXRTO QUE CONTENGA RELACION#
        textoYoutube = driver.find_element(
            By.XPATH, './/span[contains(text(),"Presenta una variedad de clips de películas")]').get_attribute('innerHTML')

        print(textoYoutube)
    except Exception as e:
        print(e)


iniciarDriver()
