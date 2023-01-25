from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time
import encript
import pymysql

# ------------------ SERVIDOR ----------------------
IPServidor = '41785A3245774C6D41775232446D4C3441784C335A6D7030'
UsuarioServidor = '416D563245774D54416D443D'
ContrasenaServidor = '5A6D526D5A775A6D5A6D446D41443D3D'
BaseDatosServidor = '417756324151706A41484C33416D4D54417844314577706D417752325A6A3D3D'

# ---------------------LOGUEO--------------------------------------------------
psswrd = "4151563245774C3341784C3341514C6B5A6D566D5A515A6C5A6D566C44443D3D"
user = "41774C325A474C6C417778325A474D535A78483341774C31417770325A443D3D"


# print(encript.DeCrypt(psswrd))
# print(encript.DeCrypt(user))

def registrarEstadoLinea(statusline):
    try:
        connectionMySQL = pymysql.connect(host=encript.DeCrypt(IPServidor), user=encript.DeCrypt(UsuarioServidor),
                                          password=encript.DeCrypt(ContrasenaServidor),
                                          db=encript.DeCrypt(BaseDatosServidor),
                                          charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        connectionMySQL.autocommit(True)

        with connectionMySQL.cursor() as cursor:

            valueUpdate = (statusline)
            sql = "UPDATE " + str(encript.DeCrypt(BaseDatosServidor)).strip(
            ) + ".tbl_gestion_sac SET STATUSLINE = %s WHERE PK_ID_GEST = 1 ;"
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
        "https://ekia.wom.co/portal/#Overview")

    try:
        WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(
            (By.CLASS_NAME, 'login')))
        print("Logueo ekia")
    except:
        print("NO ENCONTRE")

    # LOGUEO A EKIA ENVIA USUARIO
    userName = driver.find_element(
        By.ID, "inputUserName")
    userName.send_keys(encript.DeCrypt(user))

    # ENVIA CONTRASEÑA DESENCRIPTADA
    usrPsswrd = driver.find_element(
        By.ID, "inputPasswd")
    usrPsswrd.send_keys(encript.DeCrypt(psswrd))

    # PULSA EL BOTON #LOGUE A SIGN IN   
    submit = driver.find_element(
        By.ID, "btnLogin")
    submit.click()
    time.sleep(5)
    consulta()


# CONSULTA QUE BUSCA EL ESTADO DE LA LINEA
def consulta():
    try:

        WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '/html/body/div/div/div[1]/div/ul[1]/li[1]')))
        indicador = driver.find_element(
            By.XPATH, "/html/body/div/div/div[1]/div/ul[1]/li[1]")
        indicador.click()

        WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(
            (By.CLASS_NAME, 'nav-title')))
        sumary = driver.find_element(
            By.CLASS_NAME, "nav-title")
        sumary.click()

        WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(
            (By.NAME, 'search')))
        numberPhone = driver.find_element(
            By.NAME, "search")
        numberPhone.send_keys("3172483947")
        numberPhone.send_keys(Keys.ENTER)

        WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(
            (By.XPATH,
             '/html/body/div/div/div[4]/div[2]/div/div[3]/div/div/div[1]/div/div[1]/div[2]/div/div/div/ul/li[2]/a/span[2]')))
        subscriber = driver.find_element(
            By.XPATH,
            "/html/body/div/div/div[4]/div[2]/div/div[3]/div/div/div[1]/div/div[1]/div[2]/div/div/div/ul/li[2]/a/span[2]")
        subscriber.click()

        WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(
            (By.XPATH,
             '/html/body/div/div/div[4]/div[2]/div/div[3]/div/div/div[1]/div/div[3]/div[2]/div/div[3]/div/div[1]/ul/li/div/div[3]/div[1]/span')))
        statusline = driver.find_element(
            By.XPATH,
            "/html/body/div/div/div[4]/div[2]/div/div[3]/div/div/div[1]/div/div[3]/div[2]/div/div[3]/div/div[1]/ul/li/div/div[3]/div[1]/span").get_attribute(
            "innerHTML")
        print("estado")
        statusline = statusline.replace('<i class="state-dot state_Completed"></i>', '')
        statusline = statusline.strip()
        print(statusline)
        registrarEstadoLinea(statusline)



    except NoSuchElementException:
        print("Elemento no encontrado")

    time.sleep(200)
    # driver.close()


def ProcesoMain():
    iniciarDriver()
    consulta()


ProcesoMain()
