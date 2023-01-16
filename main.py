from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager            # para instalar el driver de Chrome automáticamente
import winsound                 # para el sonido BIP

class BuscaCursos:

    def __init__(self, year, semester):
        self.year = year
        self.semester = semester
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)        # para instalar el driver de Chrome automáticamente
        print()

    def info_ramo(self, sigla, secciones = 1, secciones_de_interes = []):
        
        if secciones_de_interes == []:      # si no se escribió nada en la secciones_de_interes, toma el valor de secciones     
            big_ofrecidas = 0
            big_disponibles = 0    
            self.driver.get('https://buscacursos.uc.cl/?cxml_semestre=' + str(self.year) + '-' + str(self.semester) + '&cxml_sigla=' + str(sigla) + '&cxml_nrc=&cxml_nombre=&cxml_categoria=TODOS&cxml_area_fg=TODOS&cxml_formato_cur=TODOS&cxml_profesor=&cxml_campus=TODOS&cxml_unidad_academica=TODOS&cxml_horario_tipo_busqueda=si_tenga&cxml_horario_tipo_busqueda_actividad=TODOS#top')
            for i in range(secciones):       # 3 --> 0,1,2
                nrc         = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/div/div/div[3]/table/tbody/tr[' + str(i+4) + ']/td[1]'))).text
                sigla       = self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div/div/div[3]/table/tbody/tr[' + str(i+4) + ']/td[2]').text
                nombre      = self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div/div/div[3]/table/tbody/tr[' + str(i+4) + ']/td[10]').text
                ofrecidas = 0
                disponibles = 0
                j = 0
                WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/div/div/div[3]/table/tbody/tr[' + str(i+4) + ']/td[16]/a'))).click()    # click en lupa para revisar detalle de disponibilidad de cupos
                sleep(1)
                search = True
                while search:
                    escuela = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div1"]/table/tbody/tr[' + str(j+5) + ']/td[1]'))).text
                    try:
                        nivel = self.driver.find_element(By.XPATH, '//*[@id="div1"]/table/tbody/tr[' + str(j+5) + ']/td[2]').text
                        extra = self.driver.find_element(By.XPATH, '//*[@id="div1"]/table/tbody/tr[' + str(j+5) + ']/td[4]').text
                    except:
                        search = False
                    if ((escuela == "Vacantes libres" or "Ingeniería" in escuela or nivel == "Pregrado") and nivel != "Magister") and search and extra == "":
                        disponibles += int(self.driver.find_element(By.XPATH, '//*[@id="div1"]/table/tbody/tr[' + str(j+5) + ']/td[9]').text)
                        ofrecidas += int(self.driver.find_element(By.XPATH, '//*[@id="div1"]/table/tbody/tr[' + str(j+5) + ']/td[7]').text)
                    j += 1
                print(str(nrc) + str(" -- ") + str(sigla) + str(": ") + str(nombre) + str(" --> ") + str(disponibles) + str("/") + str(ofrecidas) + str("   sec_") + str(i+1))
                big_ofrecidas += ofrecidas
                big_disponibles += disponibles
                final = str(sigla) + str(": ") + str(nombre) + str(" --> ") + str(disponibles) + str("/") + str(ofrecidas)
                ofrecidas = 0
                disponibles = 0
                WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnClose"]'))).click()        # close
            if secciones > 1:
                final = str(sigla) + str(": ") + str(nombre) + str(" --> ") + str(big_disponibles) + str("/") + str(big_ofrecidas)
        else:
            big_ofrecidas = 0
            big_disponibles = 0
            self.driver.get('https://buscacursos.uc.cl/?cxml_semestre=' + str(self.year) + '-' + str(self.semester) + '&cxml_sigla=' + str(sigla) + '&cxml_nrc=&cxml_nombre=&cxml_categoria=TODOS&cxml_area_fg=TODOS&cxml_formato_cur=TODOS&cxml_profesor=&cxml_campus=TODOS&cxml_unidad_academica=TODOS&cxml_horario_tipo_busqueda=si_tenga&cxml_horario_tipo_busqueda_actividad=TODOS#top')
            for i in secciones_de_interes:
                nrc         = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/div/div/div[3]/table/tbody/tr[' + str(i+3) + ']/td[1]'))).text
                sigla       = self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div/div/div[3]/table/tbody/tr[' + str(i+3) + ']/td[2]').text
                nombre      = self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div/div/div[3]/table/tbody/tr[' + str(i+3) + ']/td[10]').text
                ofrecidas = 0
                disponibles = 0
                j = 0
                WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/div/div/div[3]/table/tbody/tr[' + str(i+3) + ']/td[16]/a'))).click()    # click en lupa para revisar detalle de disponibilidad de cupos
                search = True
                while search:
                    escuela = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div1"]/table/tbody/tr[' + str(j+5) + ']/td[1]'))).text
                    try:
                        nivel = self.driver.find_element(By.XPATH, '//*[@id="div1"]/table/tbody/tr[' + str(j+5) + ']/td[2]').text
                        extra = self.driver.find_element(By.XPATH, '//*[@id="div1"]/table/tbody/tr[' + str(j+5) + ']/td[4]').text
                    except:
                        search = False
                    if (escuela == "Vacantes libres" or "Ingeniería" in escuela or nivel == "Pregrado") and search and extra == "":
                        disponibles += int(self.driver.find_element(By.XPATH, '//*[@id="div1"]/table/tbody/tr[' + str(j+5) + ']/td[9]').text)
                        ofrecidas += int(self.driver.find_element(By.XPATH, '//*[@id="div1"]/table/tbody/tr[' + str(j+5) + ']/td[7]').text)
                    j += 1
                print(str(nrc) + str(" -- ") + str(sigla) + str(": ") + str(nombre) + str(" --> ") + str(disponibles) + str("/") + str(ofrecidas) + str("   sec_") + str(i))
                big_ofrecidas += ofrecidas
                big_disponibles += disponibles
                final = str(sigla) + str(": ") + str(nombre) + str(" --> ") + str(disponibles) + str("/") + str(ofrecidas)
                ofrecidas = 0
                disponibles = 0
                WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnClose"]'))).click()        # close
            if len(secciones_de_interes) > 1:
                final = str(sigla) + str(": ") + str(nombre) + str(" --> ") + str(big_disponibles) + str("/") + str(big_ofrecidas)
        print()
        return final

    def bip(self):
        frequency = 400  # Set Frequency To 400 Hertz
        duration = 50  # Set Duration To 50 ms (1000 ms == 1 s)
        winsound.Beep(frequency, duration)

    def detectar_liberacion_cupo(self, sigla, secciones_de_interes):
            self.driver.get('https://buscacursos.uc.cl/?cxml_semestre=' + str(self.year) + '-' + str(self.semester) + '&cxml_sigla=' + str(sigla) + '&cxml_nrc=&cxml_nombre=&cxml_categoria=TODOS&cxml_area_fg=TODOS&cxml_formato_cur=TODOS&cxml_profesor=&cxml_campus=TODOS&cxml_unidad_academica=TODOS&cxml_horario_tipo_busqueda=si_tenga&cxml_horario_tipo_busqueda_actividad=TODOS#top')
            for i in secciones_de_interes:
                nrc         = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/div/div/div[3]/table/tbody/tr[' + str(i+3) + ']/td[1]'))).text
                sigla       = self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div/div/div[3]/table/tbody/tr[' + str(i+3) + ']/td[2]').text
                nombre      = self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div/div/div[3]/table/tbody/tr[' + str(i+3) + ']/td[10]').text
                ofrecidas = 0
                disponibles = 0
                j = 0
                WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/div/div/div[3]/table/tbody/tr[' + str(i+3) + ']/td[16]/a'))).click()    # click en lupa para revisar detalle de disponibilidad de cupos
                search = True
                sleep(1)
                while search:
                    escuela = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div1"]/table/tbody/tr[' + str(j+5) + ']/td[1]'))).text
                    try:
                        nivel = self.driver.find_element(By.XPATH, '//*[@id="div1"]/table/tbody/tr[' + str(j+5) + ']/td[2]').text
                        extra = self.driver.find_element(By.XPATH, '//*[@id="div1"]/table/tbody/tr[' + str(j+5) + ']/td[4]').text
                    except:
                        search = False
                    if (escuela == "Vacantes libres" or "Ingeniería" in escuela or nivel == "Pregrado") and search and extra == "":
                        disponibles += int(self.driver.find_element(By.XPATH, '//*[@id="div1"]/table/tbody/tr[' + str(j+5) + ']/td[9]').text)
                        ofrecidas += int(self.driver.find_element(By.XPATH, '//*[@id="div1"]/table/tbody/tr[' + str(j+5) + ']/td[7]').text)
                    j += 1
                print(str(nrc) + str(" -- ") + str(sigla) + str(": ") + str(nombre) + str(" --> ") + str(disponibles) + str("/") + str(ofrecidas) + str("   sec_") + str(i))
                WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnClose"]'))).click()        # close
                
                if (disponibles > 0):
                    print("Hay cupos")
                else:
                    print("No hay cupos")
                    self.bip()

if __name__ == "__main__":
    buscador = BuscaCursos(year=2023, semester=1)
    
    final_print = []        
    # final_print.append(buscador.info_ramo('ICH1104', secciones=3))                                  # Mecánica de Fluidos
    # final_print.append(buscador.info_ramo('ICS3213', secciones=4))                                  # Gestión de Operaciones
    # final_print.append(buscador.info_ramo('IIC2173', secciones=2))                                  # Arquitectura de Sistemas de Software

    # final_print.append(buscador.info_ramo('ICS3313', secciones=3, secciones_de_interes=[1,2]))      # Marketing
    final_print.append(buscador.info_ramo('IIC2343', secciones=2))                                  # Arquitectura de Computadores

    final_print.append(buscador.info_ramo('IIC2113', secciones=1))                                  # Diseño Detallado de Software
    # final_print.append(buscador.info_ramo('IIC3143', secciones=1))                                  # Desarrollo de Software
    final_print.append(buscador.info_ramo('IIC3757', secciones=1))                                  # Minería de Procesos
    final_print.append(buscador.info_ramo('IIC3745', secciones=1))                                  # Testing
    

    # TODO en vez de default 1 sección, mejor que retorne la búsqueda para todas las secciones disponibles

    print("-------------------------RECUENTO FINAL-------------------------")
    for x in final_print:
        print(x)

    # buscador.detectar_liberacion_cupo('IIC2343', secciones_de_interes=[1,2])

    # TODO ver como poner color rojo/verde/amarillo a print output
    # TODO recorrer todas las secciones (por ejemplo no usar secciones=3 porque si hay 2 secciones falla)