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
import re
import time
import encript
import pymysql

# ------------------ SERVIDOR ----------------------
IPServidor = '41785A3245774C6D41775232446D4C3441784C335A6D7030'
UsuarioServidor = '416D563245774D54416D443D'
ContrasenaServidor = '5A6D526D5A775A6D5A6D446D41443D3D'
BaseDatosServidor = '417756324151706A41484C33416D4D54417844314577706D417752325A6A3D3D'

#---------------------LOGUEO--------------------------------------------------
user2   = "41774C325A474C6C417778325A474D535A78483341774C31417770325A443D3D"
psswrd2 = "4147703245774D52417748335A775A335A6D786D41775A6A5A78523D"
#print(encript.DeCrypt(user2))
#print(encript.DeCrypt(psswrd2))


def registrarImei(imei):

    try:
        connectionMySQL = pymysql.connect(host=encript.DeCrypt(IPServidor), user=encript.DeCrypt(UsuarioServidor),
                                          password=encript.DeCrypt(ContrasenaServidor), db=encript.DeCrypt(BaseDatosServidor),
                                          charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        connectionMySQL.autocommit(True)

        with connectionMySQL.cursor() as cursor:

            valueUpdate = (imei)
            sql = "UPDATE " + str(encript.DeCrypt(BaseDatosServidor)).strip(
            ) + ".tbl_gestion_sac SET IMEI = %s WHERE PK_ID_GEST = 1 ;"
            cursor.execute(sql, valueUpdate)
            cursor.close()
            connectionMySQL.close()



    except pymysql.InternalError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)
        
    except pymysql.DatabaseError as error3:
        print(">>>>>>>>>>>>>", error3)
        
    except pymysql.MySQLError as error4:
        print('Got error {!r}, errno is {}'.format(error4, error4.args[0]))

def registrarEstadoImei(imeiStatus):

    try:
        connectionMySQL = pymysql.connect(host=encript.DeCrypt(IPServidor), user=encript.DeCrypt(UsuarioServidor),
                                          password=encript.DeCrypt(ContrasenaServidor), db=encript.DeCrypt(BaseDatosServidor),
                                          charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        connectionMySQL.autocommit(True)

        with connectionMySQL.cursor() as cursor:

            valueUpdate = (imeiStatus)
            sql = "UPDATE " + str(encript.DeCrypt(BaseDatosServidor)).strip(
            ) + ".tbl_gestion_sac SET IMEISTATUS = %s WHERE PK_ID_GEST = 1 ;"
            cursor.execute(sql, valueUpdate)
            cursor.close()
            connectionMySQL.close()

            

    except pymysql.InternalError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)
        
    except pymysql.DatabaseError as error3:
        print(">>>>>>>>>>>>>", error3)
        
    except pymysql.MySQLError as error4:
        print('Got error {!r}, errno is {}'.format(error4, error4.args[0]))


def iniciarDriver():
    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    global driver
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    driver.get(
        "https://app.wom.co/funcionalidadCore/core/login/index.jsp")

    try:
        WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(
            (By.ID, 'cajaLogin')))
        print("Logueo Gecko")
    except:
        print("NO ENCONTRE")

    #LOGUEO A GECKO ENVIA USUARIO
    userName = driver.find_element(
        By.ID, "account_user")
    userName.send_keys(encript.DeCrypt(user2))

    # ENVIA CONTRASEÑA DESENCRIPTADA
    usrPsswrd = driver.find_element(
        By.ID, "account_password")
    usrPsswrd.send_keys(encript.DeCrypt(psswrd2))

    # PULSA EL BOTON PARA INGRESO
    submit = driver.find_element(
         By.XPATH,'//button[text()="Ingresar"]')
    submit.click()
    consulta2()


def consulta2():  
    try:

        WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//span[text()="CONSULTAS CORE"]')))
        concore = driver.find_element(
            By.XPATH, '//span[text()="CONSULTAS CORE"]')
        concore.click()
        concore.click()
        print('ok')

        
        #select HSS ESTATICA
        WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(
             (By.ID, 'select_query')))

        toSelect = Select(driver.find_element(By.ID,'select_query'))
        toSelect.select_by_value('4')
        print("HSS ESTATICA")   
        
        #ingresar el numero de telefono
        WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(
            (By.ID, 'phoneNumber')))
        phoneQ = driver.find_element(
            By.ID, 'phoneNumber')
        phoneQ.send_keys("3172483947")   
        
        #pulsa boton consultar
        buttonQ = driver.find_element(
            By.XPATH, '//button[text()="Consultar"]')
        buttonQ.click()
        
        #captura imei
        WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(
            (By.ID, 'IMEI_REAL_0')))
        imei = driver.find_element(
            By.ID , "IMEI_REAL_0").get_attribute("value")
        print(imei)    
        registrarImei(imei)    
               
        # consulta el imei capturado
        toSelect.select_by_value('1')
        WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(
            (By.ID, 'imeiNumber')))
        imeiQ = driver.find_element(
            By.ID, 'imeiNumber')
        imeiQ.send_keys(imei)
        buttonQ.click()

        #captura estado de Imei
        WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(
            (By.ID, 'IMEI_STATUS_0')))
        imeiStatus = driver.find_element(
            By.ID , "IMEI_STATUS_0").get_attribute("value")
        print(imeiStatus)
        registrarEstadoImei(imeiStatus)


        print("ESCOGE IMEI")
    
    except NoSuchElementException:
        print("SE CONSIGUE EL IMEI")


    time.sleep(200)




iniciarDriver()
