# %%
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


# %%
#tabla = pd.DataFrame({"Patente":[], "Tipo":[], "Marca":[], "Modelo":[], "RUT":[], "Nro. Motor":[], "Año":[], "Nombre a Rutificador":[]})
tablacompleta = pd.DataFrame()
tablalocalidad = pd.DataFrame()
driver = webdriver.Chrome(executable_path=r'E:\chromedriver.exe')
rut = pd.read_csv(r"E:\RUT CHILE.csv")


# %% PATENTE, SEGMENTO, MARCA, MODELO, RUT, MOTOR, AÑO
for RUT in rut["DATOS PERSONALES"]:
    driver.get(r'https://www.volanteomaleta.com/')
    botonrut = driver.find_element_by_xpath(r'//*[@id="Tabs"]/ul/li[3]/a')
    botonrut.click()
    busquedarut = driver.find_element_by_xpath(r'//*[@id="formato-live"]/div/input')
    busquedarut.send_keys(str(RUT))
    buscar = driver.find_element_by_xpath(r'//*[@id="formato-live"]/div/span/button')
    buscar.click()
    html = driver.page_source
    df = pd.read_html(html)
    tablacompleta = tablacompleta.append(df[0], ignore_index=True)
    print(tablacompleta.info())


# %% AGREGA LOCALIDAD
for RUT in rut["DATOS PERSONALES"]:
    driver.get(r'https://www.nombrerutyfirma.com/')
    botonrut = driver.find_element_by_xpath(r'//*[@id="Tabs"]/ul/li[2]/a')
    botonrut.click()
    busquedarut = driver.find_element_by_xpath(r'//*[@id="formato-live"]/div/input')
    busquedarut.send_keys(str(RUT))
    buscar = driver.find_element_by_xpath(r'//*[@id="formato-live"]/div/span/button')
    buscar.click()
    html = driver.page_source
    df = pd.read_html(html)
    tablalocalidad = tablalocalidad.append(df[0], ignore_index=True)
    print(tablalocalidad.info())

# %%
tablacompleta.to_excel(r'C:\Users\Martin\Desktop\Nueva carpeta\tablacompleta.xlsx')

# %%
tablalocalidad.to_excel(r'C:\Users\Martin\Desktop\Nueva carpeta\tablalocalidad.xlsx')

# %%
# %% VERIFICAR CHASIS
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path=r"D:\Basededatos\chromedriver.exe", options=options)
tablacompleta = pd.DataFrame()


# %% PATENTE, SEGMENTO, MARCA, MODELO, RUT, MOTOR, AÑO
for CHASIS in verificado["NUMERO CHASIS / VIN"]:
    driver.get(r'https://en.vindecoder.pl/,')
    busquedachasis = driver.find_element_by_xpath(r'//*[@id="vin"]')
    busquedachasis.send_keys(str(CHASIS))
    buscar = driver.find_element_by_xpath(r'//*[@id="vindecoder"]/button')
    buscar.click()
    html = driver.page_source
    df = pd.read_html(html)
    fd = df[0].transpose()
    tablacompleta = tablacompleta.append(fd[0], ignore_index=True)

