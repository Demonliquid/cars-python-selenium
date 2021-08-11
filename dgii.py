# %%
from io import SEEK_CUR
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd
import time


# %% DRIVER
driver = webdriver.Edge(executable_path=r'F:\Codigo\Selenium\msedgedriver.exe')

# %% LINK
driver.get(r'https://dgii.gob.do/app/WebApps/ConsultasWeb2/ConsultasWeb/consultas/vehiculosLivianos.aspx')
avanzado = driver.find_element_by_xpath(r'//*[@id="details-button"]')
avanzado.click()
aceptaravanzado = driver.find_element_by_xpath(r'//*[@id="proceed-link"]')
aceptaravanzado.click()


# %% A RELLENAR
Fila = pd.DataFrame(columns=[0, 1, 2, 3, 4])
lista = []






# %% PARA TODAS LAS MARCAS
for marca in range(7422, 7606):
    try:
        selectmarcas = Select(driver.find_element_by_xpath(r'//*[@id="cphMain_lstMarcas"]'))
        selectmarcas.select_by_value(f'{marca}')


        for option in range(0,999):
            try:
                selectmodelo = Select(driver.find_element_by_xpath(r'//*[@id="cphMain_lstModelosFiltro"]'))
                selectmodelo.select_by_index(f"{option}")
                time.sleep(5)


                for año in range(0, 68):
                    try:
                        selectaño = Select(driver.find_element_by_xpath(r'//*[@id="cphMain_lstAños"]'))
                        selectaño.select_by_value(f'{año}')
                        time.sleep(5)

                        try:
                            for tr in driver.find_elements_by_xpath('//*[@id="cphMain_dgVehiculosLivianos"]/tbody'):
                                tds = tr.find_elements_by_tag_name('td')
                                filas = pd.DataFrame([td.text for td in tds])
                                filas = filas.transpose()
                                Fila = pd.concat([Fila, filas])
                        except:
                            pass

                    except:
                        pass
            except:
                pass


    except:
        pass






# %%
Fila.to_excel(r"F:\Trabajo\Promotive\robot dgi\Acuraenadelante.xlsx")


















# %% ANDA PARA UNA MARCA
for option in range(0,999):
    try:
        selectmodelo = Select(driver.find_element_by_xpath(r'//*[@id="cphMain_lstModelosFiltro"]'))
        selectmodelo.select_by_index(f"{option}")
        time.sleep(5)


        for año in range(0, 68):
            try:
                selectaño = Select(driver.find_element_by_xpath(r'//*[@id="cphMain_lstAños"]'))
                selectaño.select_by_value(f'{año}')
                time.sleep(5)

                try:
                    for tr in driver.find_elements_by_xpath('//*[@id="cphMain_dgVehiculosLivianos"]/tbody'):
                        tds = tr.find_elements_by_tag_name('td')
                        filas = pd.DataFrame([td.text for td in tds])
                        filas = filas.transpose()
                        Fila = pd.concat([Fila, filas])
                except:
                    pass

            except:
                pass
    except:
        pass
    


# %%
Fila.to_excel(r"F:\Trabajo\Promotive\robot dgi\Acadian.xlsx")





























# %%
for año in range(0, 68):
    try:
        selectaño = Select(driver.find_element_by_xpath(r'//*[@id="cphMain_lstAños"]'))
        selectaño.select_by_value(f'{año}')
        time.sleep(5)

        try:
            for tr in driver.find_elements_by_xpath('//*[@id="cphMain_dgVehiculosLivianos"]/tbody'):
                tds = tr.find_elements_by_tag_name('td')
                filas = pd.DataFrame([td.text for td in tds])
                filas = filas.transpose()
                Fila = pd.concat([Fila, filas])
        except:
            pass

    except:
        pass


# %%
for categoria in range(0,99):
    selectcategoria = Select(driver.find_element_by_xpath(r'//*[@id="cphMain_lstModelos"]'))
    selectcategoria.select_by_index(f"{categoria}")
    time.sleep(5)


# %%


for x in range(1,7):  # TODAS LAS PAGINAS
    numero = driver.find_element_by_xpath(f'//*[@id="cphMain_dgVehiculosLivianos"]/tbody/tr[11]/td/table/tbody/tr/td[{x}]')
    numero.click()
    time.sleep(5)

    for x in range(1,10): # TODAS LAS FILAS
        try:
            filas = driver.find_element_by_xpath(f'//*[@id="cphMain_dgVehiculosLivianos"]/tbody/tr[{x}]')
            lista.append(filas.text)
        except:
            pass




# %%
lista = []





# %%
for categoria in range(0,99):
    try:
        selectcategoria = Select(driver.find_element_by_xpath(r'//*[@id="cphMain_lstModelos"]'))
        selectcategoria.select_by_index(f"{categoria}")
        time.sleep(5)
        categoriaseleccionada = selectcategoria.first_selected_option.text


        for pagina in range(1,7):  # TODAS LAS PAGINAS
            numero = driver.find_element_by_xpath(f'//*[@id="cphMain_dgVehiculosLivianos"]/tbody/tr[11]/td/table/tbody/tr/td[{pagina}]')
            numero.click()
            time.sleep(5)

            for fila in range(1,10): # TODAS LAS FILAS
                try:
                    filas = driver.find_element_by_xpath(f'//*[@id="cphMain_dgVehiculosLivianos"]/tbody/tr[{fila}]')
                    lista.append(filas.text + " | " + categoriaseleccionada)
                except:
                    pass


    except:
        pass


# %%
for pagina in range(1,7):  # TODAS LAS PAGINAS
    try:
        numero = driver.find_element_by_xpath(f'//*[@id="cphMain_dgVehiculosLivianos"]/tbody/tr[11]/td/table/tbody/tr/td[{pagina}]')
        numero.click()
        time.sleep(5)





        for categoria in range(0,99):
            try:
                selectcategoria = Select(driver.find_element_by_xpath(r'//*[@id="cphMain_lstModelos"]'))
                selectcategoria.select_by_index(f"{categoria}")
                time.sleep(5)
                categoriaseleccionada = selectcategoria.first_selected_option.text


                for fila in range(1,10): # TODAS LAS FILAS
                    try:
                        filas = driver.find_element_by_xpath(f'//*[@id="cphMain_dgVehiculosLivianos"]/tbody/tr[{fila}]')
                        lista.append(filas.text + " | " + categoriaseleccionada)
                    except:
                        pass



            except:
                pass


    except:
        pass


# %%
lista = []


# %%
for pagina in range(1,7):  # TODAS LAS PAGINAS
    try:
        numero = driver.find_element_by_xpath(f'//*[@id="cphMain_dgVehiculosLivianos"]/tbody/tr[11]/td/table/tbody/tr/td[{pagina}]')
        numero.click()
        time.sleep(5)




        for fila in range(1,10): # TODAS LAS FILAS
            try:
                filas = driver.find_element_by_xpath(f'//*[@id="cphMain_dgVehiculosLivianos"]/tbody/tr[{fila}]')
                selectcategoria = Select(driver.find_element_by_xpath(r'//*[@id="cphMain_lstModelos"]'))
                lista.append(filas.text + " | " + categoriaseleccionada)
            except:
                pass






    except:
        pass
    



# %%
selectcategoria = Select(driver.find_element_by_xpath(r'//*[@id="cphMain_lstModelos"]'))
for categoria in range(len(selectcategoria.options)):
    selectcategoria.select_by_index(f"{categoria}")
    time.sleep(10)
    categoriaseleccionada = selectcategoria.first_selected_option.text
    print(categoriaseleccionada)




num_rows = len(driver.find_elements_by_xpath(r'//*[@id="cphMain_dgVehiculosLivianos"]/tbody/tr'))-1
for fila in range(num_rows): # TODAS LAS FILAS
    try:
        filas = driver.find_element_by_xpath(f'//*[@id="cphMain_dgVehiculosLivianos"]/tbody/tr[{fila}]')
        selectcategoria = Select(driver.find_element_by_xpath(r'//*[@id="cphMain_lstModelos"]'))
        lista.append(filas.text + " | " + categoriaseleccionada)
    except:
        pass


for pagina in range(1,7):  # TODAS LAS PAGINAS
    try:
        numero = driver.find_element_by_xpath(f'//*[@id="cphMain_dgVehiculosLivianos"]/tbody/tr[11]/td/table/tbody/tr/td[{pagina}]')
        numero.click()
        time.sleep(5)
    except:
        pass




# %%
for pagina in range(1,7):  # TODAS LAS PAGINAS
    numero = driver.find_element_by_xpath(f'//*[@id="cphMain_dgVehiculosLivianos"]/tbody/tr[11]/td/table/tbody/tr/td[{pagina}]/a')
    numero.click()
    time.sleep(5)





# %%
for pagina in range(1,7):  # TODAS LAS PAGINAS
    numero = driver.find_element_by_xpath(f'//*[@id="cphMain_dgVehiculosLivianos"]/tbody/tr[3]/td/table/tbody/tr/td[{pagina}]/a')
    numero.click()
    time.sleep(5)

# %%
lista = []




# %%
lista

# %%

//*[@id="cphMain_dgVehiculosLivianos"]/tbody/tr[11]/td/table/tbody/tr/td[2]/a