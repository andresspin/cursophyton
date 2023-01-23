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
import Encriptado
import pymysql as pymysql

# ------------------ SERVIDOR ----------------------
IPServidor = '41785A3245774C6D41775232446D4C3441784C335A6D7030'
UsuarioServidor = '41775A324577706D41484C325A6D706C4178443D'
ContrasenaServidor = '417770324147706D416D443242474D5441784832416D4C31417848324147706C41775232446D4C6D41784C335A6D414F5A6D566D5A515A6C5A6D4E3D'
BaseDatosServidor = '417744325A77706A41484C325A6D4D51417752335A774D545A6D5A6D41775A6A'

Estado = True
idBot = 1
procesoBot = "Ascard"

#funcuion para abrir pagina#
def iniciarDriver():
    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    try:
        global driver
        driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()), options=options)
        driver.get(
            "https://ascard.claro.com.co:8080/AdminWeb/pages/login/login.jsf")
        # driver.maximize_window()
    except Exception as e:
        mensaje = "Error al abrir " + procesoBot + ", " + str(e)
        controlErrores("null", "", mensaje)


def controlErrores(idGestion, idBotGestion, mensaje):
    try:
        connectionMySQL = pymysql.connect(host=Encriptado.DeCrypt(IPServidor), user=Encriptado.DeCrypt(UsuarioServidor),
                                          password=Encriptado.DeCrypt(ContrasenaServidor), db=Encriptado.DeCrypt(BaseDatosServidor),
                                          charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        connectionMySQL.autocommit(True)

        cerrarSesion()

        with connectionMySQL.cursor() as cursor:

            valuesInsert = (idGestion, idBotGestion, mensaje, procesoBot)
            sql = "INSERT INTO " + Encriptado.DeCrypt(BaseDatosServidor).strip(
            ) + ".tbl_gbl_errores (FK_ID_GESTION, FK_ID_BOT, MENSAJE, PROYECTO) VALUES (%s ,%s ,%s ,%s);"
            print("SQL INSERT: "+sql)
            cursor.execute(sql, valuesInsert)

            cursor.close()
            connectionMySQL.close()
            driver.close()
            ProcesoMain()
            botRespuesta = "PROCESO NO APLICADO"
            botDescRespuesta = "Se presento un error en proceso , vuelva a intentar"
            registrarCasos(idGestion, "", idBot, botRespuesta,
                           botDescRespuesta, idBotGestion)

    except pymysql.InternalError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)
        Comprobar = "Error Consulta SQL2: " + \
            str(code) + ", " + str(message)

    except pymysql.DatabaseError as error3:
        print(">>>>>>>>>>>>>", error3)
        Comprobar = "Error Consulta SQL2: " + str(error3)

    except pymysql.MySQLError as error4:
        print('Got error {!r}, errno is {}'.format(error4, error4.args[0]))
        Comprobar = "Error Consulta SQL2: " + error4


def consultaCasos():

    estadoConsultaCaso = False

    try:
        connectionMySQL = pymysql.connect(host=Encriptado.DeCrypt(IPServidor), user=Encriptado.DeCrypt(UsuarioServidor),
                                          password=Encriptado.DeCrypt(ContrasenaServidor), db=Encriptado.DeCrypt(BaseDatosServidor),
                                          charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        connectionMySQL.autocommit(True)

        with connectionMySQL.cursor() as cursor:

            sql = "SELECT PK_REGISTRO , CEDULA_CLIENTE, FK_REGISTRO , CEDULA_CLIENTE, NOMBRE_CLIENTE FROM " + str(Encriptado.DeCrypt(BaseDatosServidor)).strip(
            ) + ".tbl_gestion_ascard WHERE BOT_ESTADO_GESTION = 'PENDIENTE' AND ESTADO = 'ACTIVO' ;"
            cursor.execute(sql)
            rows = cursor.fetchall()

            if len(rows) == 0:
                print("ESPERANDO CASOS")
                cursor.close()
                connectionMySQL.close()
                time.sleep(10)

            if len(rows) != 0:
                global cedula
                cedula = rows[0]["CEDULA_CLIENTE"]
                global idGestion
                idGestion = rows[0]["PK_REGISTRO"]
                global idGestionForen
                idGestionForen = rows[0]["FK_REGISTRO"]
                global nombreClienteRegistro
                nombreClienteRegistro = rows[0]["NOMBRE_CLIENTE"]
                print(cedula)
                print(idGestion)
                estadoConsultaCaso = True

                sql1 = "UPDATE " + str(Encriptado.DeCrypt(BaseDatosServidor)).strip(
                ) + ".tbl_gestion_ascard SET ID_BOT = '"+str(idBot)+"', BOT_ESTADO_GESTION = 'VALIDANDO' WHERE PK_REGISTRO = '"+str(idGestion)+"' AND ESTADO = 'ACTIVO' ;"
                cursor.execute(sql1)

                cursor.close()
                connectionMySQL.close()

        return estadoConsultaCaso

    except pymysql.InternalError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)
        mensaje = "Error Consulta SQL2: " + \
            str(code) + ", " + str(message)
        controlErrores(idGestion, idBot, mensaje)

    except pymysql.DatabaseError as error3:
        print(">>>>>>>>>>>>>", error3)
        mensaje = "Error Consulta SQL2: " + str(error3)
        controlErrores(idGestion, idBot, mensaje)

    except pymysql.MySQLError as error4:
        print('Got error {!r}, errno is {}'.format(error4, error4.args[0]))
        mensaje = "Error Consulta SQL2: " + error4
        controlErrores(idGestion, idBot, mensaje)


def registrarCasos(idGestion, idGestionForen, cedula, valorDeuda, nombreCliente,  Imei, tipoEquipo,
                   numeroCliente, refereciaEquipo, botRespuesta, botDescRespuesta, idBotGestion):

    try:
        connectionMySQL = pymysql.connect(host=Encriptado.DeCrypt(IPServidor), user=Encriptado.DeCrypt(UsuarioServidor),
                                          password=Encriptado.DeCrypt(ContrasenaServidor), db=Encriptado.DeCrypt(BaseDatosServidor),
                                          charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        connectionMySQL.autocommit(True)

        with connectionMySQL.cursor() as cursor:

            valueUpdate = (idGestionForen, idBot, cedula, valorDeuda, nombreCliente,  Imei, tipoEquipo,
                           numeroCliente, refereciaEquipo, "VALIDADO",
                           botRespuesta, botDescRespuesta, "ACTIVO")
            sql = "INSERT INTO " + str(Encriptado.DeCrypt(BaseDatosServidor)).strip(
            ) + ".tbl_respuesta_ascard (FK_REGISTRO,ID_BOT,CEDULA_CLIENTE,VALOR_DEUDA,NOMBRE_CLIENTE,IMEI,TIPO_EQUIPO,NUMERO_CLIENTE,REFERENCIA_EQUIPO,BOT_ESTADO_GESTION,BOT_RESPUESTA,BOT_DESC_RESPUESTA,ESTADO) VALUES  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            cursor.execute(sql, valueUpdate)
            cursor.close()
            connectionMySQL.close()

    except pymysql.InternalError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)
        mensaje = "Error Consulta SQL2: " + \
            str(code) + ", " + str(message)
        controlErrores(idGestion, idBotGestion, mensaje)

    except pymysql.DatabaseError as error3:
        print(">>>>>>>>>>>>>", error3)
        mensaje = "Error Consulta SQL2: " + str(error3)
        controlErrores(idGestion, idBotGestion, mensaje)

    except pymysql.MySQLError as error4:
        print('Got error {!r}, errno is {}'.format(error4, error4.args[0]))
        mensaje = "Error Consulta SQL2: " + error4
        controlErrores(idGestion, idBotGestion, mensaje)


def finalizarGestion(idGestionForen, idBotGestion):
    try:
        connectionMySQL = pymysql.connect(host=Encriptado.DeCrypt(IPServidor), user=Encriptado.DeCrypt(UsuarioServidor),
                                          password=Encriptado.DeCrypt(ContrasenaServidor), db=Encriptado.DeCrypt(BaseDatosServidor),
                                          charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        connectionMySQL.autocommit(True)

        with connectionMySQL.cursor() as cursor:

            valueUpdate = ("FINALIZADO", "INACTIVO", idGestionForen)
            sql = "UPDATE " + str(Encriptado.DeCrypt(BaseDatosServidor)).strip(
            ) + ".tbl_respuesta_ascard SET BOT_ESTADO_GESTION = %s , ESTADO= %s WHERE FK_REGISTRO = %s ;"
            cursor.execute(sql, valueUpdate)

            sql1 = "UPDATE " + str(Encriptado.DeCrypt(BaseDatosServidor)).strip(
            ) + ".tbl_gbl_bots SET SESION = '', ESTADO_FUNCIONAMIENTO = 'Disponible' WHERE ID_BOT = '"+str(idBotGestion)+"' AND ESTADO_GENERAL = 'Activo' AND PROYECTO = '" + str(procesoBot) + "' ;"
            cursor.execute(sql1)

            sql2 = "UPDATE " + str(Encriptado.DeCrypt(BaseDatosServidor)).strip(
            ) + ".tbl_gestion_ascard SET BOT_ESTADO_GESTION = 'VALIDADO' , ESTADO = 'INACTIVO' WHERE PK_REGISTRO = '"+str(idGestion)+"';"
            cursor.execute(sql2)

            cursor.close()
            connectionMySQL.close()

    except pymysql.InternalError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)
        mensaje = "Error Consulta SQL2: " + \
            str(code) + ", " + str(message)
        controlErrores(idGestion, idBotGestion, mensaje)

    except pymysql.DatabaseError as error3:
        print(">>>>>>>>>>>>>", error3)
        mensaje = "Error Consulta SQL2: " + str(error3)
        controlErrores(idGestion, idBotGestion, mensaje)

    except pymysql.MySQLError as error4:
        print('Got error {!r}, errno is {}'.format(error4, error4.args[0]))
        mensaje = "Error Consulta SQL2: " + error4
        controlErrores(idGestion, idBotGestion, mensaje)


def consultaUsuario():

    estadConsultaUsuario = False

    try:
        connectionMySQL = pymysql.connect(host=Encriptado.DeCrypt(IPServidor), user=Encriptado.DeCrypt(UsuarioServidor),
                                          password=Encriptado.DeCrypt(ContrasenaServidor), db=Encriptado.DeCrypt(BaseDatosServidor),
                                          charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        connectionMySQL.autocommit(True)

        with connectionMySQL.cursor() as cursor:

            sql = "SELECT ID_BOT , USUARIO , CONTRASENA FROM " + str(Encriptado.DeCrypt(BaseDatosServidor)).strip(
            ) + ".tbl_gbl_bots WHERE ESTADO_FUNCIONAMIENTO = 'Disponible' AND ESTADO_GENERAL = 'Activo' AND PROYECTO = '" + str(procesoBot) + "';"
            cursor.execute(sql)
            rows = cursor.fetchall()

            if len(rows) == 0:
                sql = "UPDATE " + str(Encriptado.DeCrypt(BaseDatosServidor)).strip(
                ) + ".tbl_gestion_ascard SET BOT_ESTADO_GESTION = 'PENDIENTE' , ESTADO = 'ACTIVO' WHERE PK_REGISTRO = '"+str(idGestion)+"';"
                cursor.execute(sql)
                cursor.close()
                connectionMySQL.close()
                print("ESPERANDO USUARIOS")
                time.sleep(10)

            if len(rows) != 0:
                global idBotGestion
                idBotGestion = rows[0]["ID_BOT"]
                global usuarioIngresar
                usuarioIngresar = rows[0]["USUARIO"]
                global contraseñaIngrear
                contraseñaIngrear = rows[0]["CONTRASENA"]
                print(idBotGestion)
                print(usuarioIngresar)
                print(contraseñaIngrear)
                estadConsultaUsuario = True

                sql = "UPDATE " + str(Encriptado.DeCrypt(BaseDatosServidor)).strip(
                ) + ".tbl_gbl_bots SET SESION = '"+str(idBot)+"', ESTADO_FUNCIONAMIENTO = 'Ocupado' WHERE ID_BOT = '"+str(idBotGestion)+"' AND ESTADO_GENERAL = 'Activo' AND PROYECTO = '" + str(procesoBot) + "' ;"
                cursor.execute(sql)
                cursor.fetchall()

                cursor.close()
                connectionMySQL.close()

        return estadConsultaUsuario

    except pymysql.InternalError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)
        mensaje = "Error Consulta SQL2: " + \
            str(code) + ", " + str(message)
        controlErrores("", idBotGestion, mensaje)

    except pymysql.DatabaseError as error3:
        print(">>>>>>>>>>>>>", error3)
        mensaje = "Error Consulta SQL2: " + str(error3)
        controlErrores("", idBotGestion, mensaje)

    except pymysql.MySQLError as error4:
        print('Got error {!r}, errno is {}'.format(error4, error4.args[0]))
        mensaje = "Error Consulta SQL2: " + error4
        controlErrores("", idBotGestion, mensaje)

def usuarioBloqueado():

    try:
        connectionMySQL = pymysql.connect(host=Encriptado.DeCrypt(IPServidor), user=Encriptado.DeCrypt(UsuarioServidor),
                                          password=Encriptado.DeCrypt(ContrasenaServidor), db=Encriptado.DeCrypt(BaseDatosServidor),
                                          charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        connectionMySQL.autocommit(True)

        with connectionMySQL.cursor() as cursor:

            sql1 = "UPDATE " + str(Encriptado.DeCrypt(BaseDatosServidor)).strip(
            ) + ".tbl_gbl_bots SET SESION = '', ESTADO_FUNCIONAMIENTO = 'Bloqueado' WHERE ID_BOT = '"+str(idBotGestion)+"' AND ESTADO_GENERAL = 'Activo' AND PROYECTO = '" + str(procesoBot) + "' ;"
            cursor.execute(sql1)

            sql2 = "UPDATE " + str(Encriptado.DeCrypt(BaseDatosServidor)).strip(
            ) + ".tbl_gestion_ascard SET BOT_ESTADO_GESTION = 'PENDIENTE' , ESTADO = 'ACTIVO' WHERE PK_REGISTRO = '"+str(idGestion)+"';"
            cursor.execute(sql2)

            cursor.close()
            connectionMySQL.close()

    except pymysql.InternalError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)
        mensaje = "Error Consulta SQL2: " + \
            str(code) + ", " + str(message)
        controlErrores(idGestion, idBotGestion, mensaje)

    except pymysql.DatabaseError as error3:
        print(">>>>>>>>>>>>>", error3)
        mensaje = "Error Consulta SQL2: " + str(error3)
        controlErrores(idGestion, idBotGestion, mensaje)

    except pymysql.MySQLError as error4:
        print('Got error {!r}, errno is {}'.format(error4, error4.args[0]))
        mensaje = "Error Consulta SQL2: " + error4
        controlErrores(idGestion, idBotGestion, mensaje)

def cerrarSesion():

    try:
        profile = driver.find_element(By.ID, 'salirForm:botonSalir')
        profile.click()
    except Exception as e:
        mensaje = "Error al entrar en el perfil " + str(e)
        controlErrores("", "", mensaje)

    ProcesoAscard()


def compararNombres(nombreCliente, nombreClienteRegistro):
    try:
        puntaje = 0

        nombreCliente = str((nombreCliente).upper()).strip()
        nombreClienteRegistro = str((nombreClienteRegistro).upper()).strip()

        nombreClienteSplit = nombreCliente.split()
        nombreClienteRegistroSplit = nombreClienteRegistro.split()

        for i in nombreClienteRegistroSplit:
            for x in nombreClienteSplit:
                try:
                    if i == x:
                        puntaje += 1
                except:
                    pass
        if puntaje >= 2:
            return True
        else:
            return False
    except Exception as e:
        mensaje = "Error al validar titularidad nombre " + str(e)
        controlErrores(idGestion, idBot, mensaje)


def ProcesoAscard():

    while Estado == True:

        estadoConsultaCaso = consultaCasos()

        if estadoConsultaCaso == True:

            estadConsultaUsuario = consultaUsuario()

            if estadConsultaUsuario == True:
                
                driver.refresh()

                try:
                    WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(
                        (By.ID, 'login-page')))
                except TimeoutException as e:
                    mensaje = "Error al espera Login " + str(e)
                    controlErrores(idGestion, idBot, mensaje)

                try:
                    usuario = driver.find_element(
                        By.ID, 'form-logeo:login-username')
                    usuario.send_keys(usuarioIngresar)
                except Exception as e:
                    mensaje = "Error al enviar usuario Login " + str(e)
                    controlErrores(idGestion, idBot, mensaje)
                try:
                    password = driver.find_element(
                        By.ID, "form-logeo:login-password")
                    password.send_keys(contraseñaIngrear)
                except Exception as e:
                    mensaje = "Error al enviar contraseña Login " + str(e)
                    controlErrores(idGestion, idBot, mensaje)
                try:
                    ingresar = driver.find_element(By.ID, "form-logeo:login")
                    ingresar.click()
                except Exception as e:
                    mensaje = "Error al dar click Login " + str(e)
                    controlErrores(idGestion, idBot, mensaje)

                try:
                    prueba = WebDriverWait(driver, 2).until(EC.visibility_of_all_elements_located(
                        (By.CLASS_NAME, 'ui-growl-item')))
                    if prueba:
                        print("Ya se encuentra una cuenta activa con ese usuario")
                        usuarioBloqueado()

                except:
                    print("NO ENCONTRE PRUEBA")

                try:
                    menuCredito = WebDriverWait(driver, 20).until(
                        EC.visibility_of_element_located((By.XPATH, '//span[text()="CREDITO"]')))
                    menuCredito.click()
                except Exception as e:
                    mensaje = "Error al dar click CREDITO " + str(e)
                    controlErrores(idGestion, idBot, mensaje)

                try:
                    menuModulo = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                        (By.XPATH, '//span[text()="MODULO DE CONSULTAS"]')))
                    menuModulo.click()
                except Exception as e:
                    mensaje = "Error al dar click MODULO DE CONSULTAS " + \
                        str(e)
                    controlErrores(idGestion, idBot, mensaje)

                try:
                    menuConsulta = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                        (By.XPATH, '//span[text()="20. CONSULTA GENERAL DE CREDITOS"]')))
                    menuConsulta.click()
                except Exception as e:
                    mensaje = "Error al dar click CONSULTA GENERAL DE CREDITOS " + \
                        str(e)
                    controlErrores(idGestion, idBot, mensaje)

                try:
                    cedulaCliente = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                        (By.ID, "crmaeConsultaIdentificacion:idIdentificacion")))
                    cedulaCliente.send_keys(cedula)
                    cedulaCliente.send_keys(Keys.ENTER)
                except Exception as e:
                    mensaje = "Error al ingresar cedula cliente " + str(e)
                    controlErrores(idGestion, idBot, mensaje)

                try:
                    noExisteUsuario = WebDriverWait(driver, 4).until(EC.visibility_of_element_located(
                        (By.XPATH, '//span[text()="No se encontraron registros"]')))
                    if noExisteUsuario:
                        botRespuesta = "PROCESO NO APLICADO"
                        botDescRespuesta = "No se encontro el usuario registrado"
                        print(str(idGestion) + " " + str(idGestionForen) + " " +
                              str(botRespuesta) + " " + str(botDescRespuesta) + " " + str(idBotGestion))
                        registrarCasos(idGestion, idGestionForen, cedula, None, None,  None, None,
                                       None, None, botRespuesta, botDescRespuesta, idBotGestion)
                        finalizarGestion(idGestionForen, idBotGestion)
                        cerrarSesion()
                except:
                    noExisteUsuario = False

                if noExisteUsuario == False:

                    try:
                        dataClienteEquipos = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                            (By.ID, "crmaeConsultaIdentificacion:idTablaIdentificacion_data")))
                        cantidadEquipos = dataClienteEquipos.find_elements(
                            By.XPATH, ".//tr")
                        print(len(cantidadEquipos))
                    except Exception as e:
                        mensaje = "Error al contar cantidad equipos " + str(e)
                        controlErrores(idGestion, idBot, mensaje)

                    for x in range(len(cantidadEquipos)):

                        print(x)

                        try:
                            WebDriverWait(driver, 20).until(
                                EC.visibility_of_element_located((By.ID, 'crmaeConsultaIdentificacion:idTablaIdentificacion:' + str(x) + ':idDlVisualizar'))).click()
                        except Exception as e:
                            mensaje = "Error al seleccionar equipo cliente " + \
                                str(e)
                            controlErrores(idGestion, idBot, mensaje)

                        try:

                            WebDriverWait(driver, 20).until(
                                EC.visibility_of_element_located((By.XPATH, '//span[text()="Estructura del pago mínimo"]')))

                            menuCredito = driver.find_element(
                                By.XPATH, '//span[text()="Estructura del pago mínimo"]')

                            menuCredito_Parent = menuCredito.find_element(
                                By.XPATH, ".//parent::div/parent::div")

                            menuCreditoFinal = menuCredito_Parent.find_element(
                                By.XPATH, './/label[contains(text(),"Pago mínimo")]')

                            menuCreditoFinal1 = menuCreditoFinal.find_element(
                                By.XPATH, ".//parent::td")

                            menuCreditoFinal2 = menuCreditoFinal1.find_element(
                                By.XPATH, ".//following-sibling::td")

                            # -----------------VALOR DEUDA-----------------
                            valorDeuda = menuCreditoFinal2.find_element(
                                By.TAG_NAME, "span").get_attribute('innerHTML')
                            valorDeuda = valorDeuda.replace(",", "")
                            valorDeuda = valorDeuda.replace(".", "").strip()

                            # print(valorDeuda)

                        except Exception as e:
                            mensaje = "Error al obtener valor deuda " + str(e)
                            controlErrores(idGestion, idBot, mensaje)

                        try:

                            # ------- NOMBRE CLIENTE --------
                            nombreCliente = WebDriverWait(driver, 20).until(
                                EC.visibility_of_element_located((By.ID, 'tarjetaId'))).get_attribute('innerHTML')
                            nombreCliente = nombreCliente[41:].strip()
                            # print(nombreCliente)

                        except Exception as e:
                            mensaje = "Error al obtener nombre cliente " + \
                                str(e)
                            controlErrores(idGestion, idBot, mensaje)

                        try:

                            # ------- NUMERO CLIENTE --------
                            numeroCliente = WebDriverWait(driver, 20).until(
                                EC.visibility_of_element_located((By.ID, 'tele'))).get_attribute('innerHTML')
                            numeroCliente = numeroCliente[0:6].strip()
                            numeroCliente = numeroCliente + "****"
                            # print(numeroCliente)

                        except Exception as e:
                            mensaje = "Error al obtener numero cliente " + \
                                str(e)
                            controlErrores(idGestion, idBot, mensaje)

                        try:

                            WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                                (By.XPATH, './/a[contains(text(),"Datos generales")]'))).click()

                        except Exception as e:
                            mensaje = "Error al ingresar datos generales " + \
                                str(e)
                            controlErrores(idGestion, idBot, mensaje)

                        try:

                            WebDriverWait(driver, 20).until(
                                EC.visibility_of_element_located(
                                    (By.XPATH, './/a[contains(text(),"Más datos")]'))).click()

                        except Exception as e:
                            mensaje = "Error al ingresar Mas datos " + str(e)
                            controlErrores(idGestion, idBot, mensaje)

                        try:

                            # ------- REFERENCIA EQUIPO CLIENTE --------
                            referenciaGeneral = WebDriverWait(driver, 20).until(
                                EC.visibility_of_element_located(
                                    (By.XPATH, './/td[contains(text(),"Referencia del equipo")]')))

                            refereciaEquipo = referenciaGeneral.find_element(
                                By.XPATH, ".//following-sibling::td").get_attribute('innerHTML')

                            refereciaEquipo = refereciaEquipo.replace(
                                "&nbsp;", " ")
                            # print(refereciaEquipo)

                        except Exception as e:
                            mensaje = "Error al obtener referencia equipo " + \
                                str(e)
                            controlErrores(idGestion, idBot, mensaje)

                        try:

                            # ------- IMEI EQUIPO CLIENTE --------
                            referenciaGeneral1 = WebDriverWait(driver, 20).until(
                                EC.visibility_of_element_located(
                                    (By.XPATH, './/td[contains(text(),"Referencia del equipo")]')))

                            referenciaGeneral2 = referenciaGeneral1.find_element(
                                By.XPATH, ".//parent::tr")

                            referenciaGeneral3 = referenciaGeneral2.find_element(
                                By.XPATH, ".//following-sibling::tr")

                            referenciaGeneral4 = referenciaGeneral3.find_element(
                                By.XPATH, './/td[contains(text(),"IMEI")]')

                            Imei = referenciaGeneral4.find_element(
                                By.XPATH, ".//following-sibling::td").get_attribute("innerHTML")

                            # print(Imei)

                        except Exception as e:
                            mensaje = "Error al obtener IMEI equipo " + str(e)
                            controlErrores(idGestion, idBot, mensaje)

                        try:

                            # ------- TIPO EQUIPO --------
                            tipoEquipoGeneral = WebDriverWait(driver, 20).until(
                                EC.visibility_of_element_located(
                                    (By.XPATH, './/td[contains(text(),"Tipo de Proceso")]')))

                            tipoEquipo = tipoEquipoGeneral.find_element(
                                By.XPATH, ".//following-sibling::td").get_attribute('innerHTML')

                            # print(tipoEquipo)

                        except Exception as e:
                            mensaje = "Error al obtener tipo de equipo " + \
                                str(e)
                            controlErrores(idGestion, idBot, mensaje)

                        # ---- Validacion nombre titular ----
                        validacionTitular = compararNombres(
                            nombreCliente, nombreClienteRegistro)

                        if validacionTitular:
                            pass
                        else:

                            botRespuesta = "PROCESO NO APLICADO"
                            botDescRespuesta = "Lo sentimos los datos brindados no coinciden con los registrados, por favor verifica de nuevo y vuelte a intentar"
                            print(str(idGestion) + " " + str(idGestionForen) + " " + str(valorDeuda) + " " + str(nombreCliente) + " " + str(Imei) + " " + str(tipoEquipo) + " " +
                                  str(numeroCliente) + " " + str(refereciaEquipo) + " " + str(botRespuesta) + " " + str(botDescRespuesta) + " " + str(idBotGestion))
                            registrarCasos(idGestion, idGestionForen, cedula, valorDeuda, nombreCliente,  Imei, tipoEquipo,
                                           numeroCliente, refereciaEquipo, botRespuesta, botDescRespuesta, idBotGestion)
                            break

                        botRespuesta = "PROCESO APLICADO"
                        botDescRespuesta = "Termino con extio"
                        print(str(idGestion) + " " + str(idGestionForen) + " " + str(valorDeuda) + " " + str(nombreCliente) + " " + str(Imei) + " " + str(tipoEquipo) + " " +
                              str(numeroCliente) + " " + str(refereciaEquipo) + " " + str(botRespuesta) + " " + str(botDescRespuesta) + " " + str(idBotGestion))
                        registrarCasos(idGestion, idGestionForen, cedula, valorDeuda, nombreCliente,  Imei, tipoEquipo,
                                       numeroCliente, refereciaEquipo, botRespuesta, botDescRespuesta, idBotGestion)

                        if len(cantidadEquipos) > 1:

                            try:
                                menuCredito = WebDriverWait(driver, 20).until(
                                    EC.visibility_of_element_located((By.XPATH, '//span[text()="CREDITO"]')))
                                menuCredito.click()
                            except Exception as e:
                                mensaje = "Error al dar click CREDITO " + \
                                    str(e)
                                controlErrores(idGestion, idBot, mensaje)

                            try:
                                menuModulo = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                                    (By.XPATH, '//span[text()="MODULO DE CONSULTAS"]')))
                                menuModulo.click()
                            except Exception as e:
                                mensaje = "Error al dar click MODULO DE CONSULTAS " + \
                                    str(e)
                                controlErrores(idGestion, idBot, mensaje)

                            try:
                                menuConsulta = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                                    (By.XPATH, '//span[text()="20. CONSULTA GENERAL DE CREDITOS"]')))
                                menuConsulta.click()
                            except Exception as e:
                                mensaje = "Error al dar click CONSULTA GENERAL DE CREDITOS " + \
                                    str(e)
                                controlErrores(idGestion, idBot, mensaje)

                            try:
                                cedulaCliente = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                                    (By.ID, "crmaeConsultaIdentificacion:idIdentificacion")))
                                cedulaCliente.send_keys(cedula)
                                cedulaCliente.send_keys(Keys.ENTER)
                            except Exception as e:
                                mensaje = "Error al ingresar cedula cliente " + \
                                    str(e)
                                controlErrores(idGestion, idBot, mensaje)

                    finalizarGestion(idGestionForen, idBotGestion)
                    cerrarSesion()


def ProcesoMain():

    iniciarDriver()

    ProcesoAscard()


ProcesoMain()
