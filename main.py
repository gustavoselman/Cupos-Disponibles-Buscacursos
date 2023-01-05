from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by  import By
from webdriver_manager.chrome import ChromeDriverManager            # para instalar el driver de Chrome automáticamente

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
        
        self.driver.get('https://buscacursos.uc.cl/?cxml_semestre=' + str(self.year) + '-' + str(self.semester) + '&cxml_sigla=' + str(sigla) + '&cxml_nrc=&cxml_nombre=&cxml_categoria=TODOS&cxml_area_fg=TODOS&cxml_formato_cur=TODOS&cxml_profesor=&cxml_campus=TODOS&cxml_unidad_academica=TODOS&cxml_horario_tipo_busqueda=si_tenga&cxml_horario_tipo_busqueda_actividad=TODOS#top')
        if secciones_de_interes == []:      # si no se escribió nada en la secciones_de_interes, toma el valor de secciones         
            for i in range(secciones):       # 3 --> 0,1,2
                nrc         = self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div/div/div[3]/table/tbody/tr[' + str(i+4) + ']/td[1]').text
                sigla       = self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div/div/div[3]/table/tbody/tr[' + str(i+4) + ']/td[2]').text
                nombre      = self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div/div/div[3]/table/tbody/tr[' + str(i+4) + ']/td[10]').text
                
                # TODO: mostrar disponibles para ingeniería (NO el total que considera college, ...)
                # self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div/div/div[3]/table/tbody/tr[4]/td[16]/a/img').click()
                # print()
                # print(self.driver.find_element(By.XPATH, '//*[@id="div1"]/table/tbody/tr[5]/td[1]').text)
                # print()

                disponibles = self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div/div/div[3]/table/tbody/tr[' + str(i+4) + ']/td[15]').text
                
                total       = self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div/div/div[3]/table/tbody/tr[' + str(i+4) + ']/td[14]').text
                print(str(nrc) + str(" -- ") + str(sigla) + str(": ") + str(nombre) + str(" --> ") + str(disponibles) + str("/") + str(total) + str("   sec_") + str(i+1))
        else:
            for i in secciones_de_interes:
                nrc         = self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div/div/div[3]/table/tbody/tr[' + str(i+3) + ']/td[1]').text
                sigla       = self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div/div/div[3]/table/tbody/tr[' + str(i+3) + ']/td[2]').text
                nombre      = self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div/div/div[3]/table/tbody/tr[' + str(i+3) + ']/td[10]').text
                disponibles = self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div/div/div[3]/table/tbody/tr[' + str(i+3) + ']/td[15]').text
                total       = self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div/div/div[3]/table/tbody/tr[' + str(i+3) + ']/td[14]').text
                print(str(nrc) + str(" -- ") + str(sigla) + str(": ") + str(nombre) + str(" --> ") + str(disponibles) + str("/") + str(total) + str("   sec_") + str(i))
        print()

if __name__ == "__main__":
    buscador = BuscaCursos(year=2023, semester=1)         
    
    buscador.info_ramo('FON103', secciones=1)               # Inclusión y Discapacidad: el valor de la diversidad
    buscador.info_ramo('ICS2123', secciones=3)              # Modelos Estocásticosf
    buscador.info_ramo('ICS2813', secciones=3)              # Organización y Comportamiento en la empresa
    buscador.info_ramo('IIC2154', secciones=4)              # Proyecto de Especialidad
    buscador.info_ramo('IIC2613', secciones=1)              # Inteligencia Artificial
    
    """ Si te interesa ver secciones en específico lo pudes hacer de la siguiente forma """
    # buscador.info_ramo('IIC2154', secciones_de_interes=[2, 4])              # Proyecto de Especialidad