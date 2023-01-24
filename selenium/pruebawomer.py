from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import encript

user3   = "5A6D526D5A515A6A5A6D526D5A775A325A6D786D5A775A6B5A6D783D"
psswrd3 = "41515A3245774D5141784C3245514C6C417778325A475A6C5A6D4E6D5A775A6D5A78443D"
print(encript.DeCrypt(user3))
print(encript.DeCrypt(psswrd3))



def iniciarDriver():
    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    global driver
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    driver.get(
        "https://app.wom.co/womerU/login/index.php")
    time.sleep(3)
    try:           
        userName = driver.find_element(
            By.ID, "username")
        userName.send_keys(encript.DeCrypt(user3))
        time.sleep(3)

        usrPsswrd = driver.find_element(
            By.ID, "password")
        usrPsswrd.send_keys(encript.DeCrypt(psswrd3))
        time.sleep(3)

        submit = driver.find_element(
            By.ID, "loginbtn")
        submit.click()
        time.sleep(3)
    except Exception as error:

         print("Error en la funcion iniciarDriver: "+ str(error))

iniciarDriver()
