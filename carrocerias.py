# %%
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd


# %% DRIVER
#driver = webdriver.Chrome(executable_path=r'E:\chromedriver.exe')
driver = webdriver.Edge(executable_path=r"E:\msedgedriverbueno.exe")


# %% LINK
driver.get(r'https://www.repuestoscoches24.es/')


# %% A RELLENAR
carrocerias = pd.DataFrame(columns=["MARCA", "AÑO"])


# %% TENER LISTA DE MARCAS
buscadormarca = driver.find_element_by_xpath(r'//select')
buscadormarca.click()
dropdownmarca = Select(buscadormarca)
marcas = dropdownmarca.options
listamarcas = []
for marca in marcas:
    listamarcas.append(marca.text)
marcas = None



# %%
dropdownmarca.select_by_visible_text("ABARTH")
dropdownmarca.deselect_all()
buscadoraño = driver.find_element_by_xpath(r'//*[contains(concat( " ", @class, " " ), concat( " ", "js-year", " " ))] | //select')
dropdownaño = Select(buscadoraño)
años = dropdownmarca.options
for año in años:
    print(años.text)





# %% TENER AÑO SEGUN MARCA
for marca in listamarcas:
    dropdownmarca.select_by_visible_text(marca)
    dropdownaño = Select(buscadoraño)
    años = dropdownmarca.options
    listaaños = []
    for año in años:
        listaaños.append(años.text)
    años = None
    for año in listaaños:
        carrocerias = carrocerias.append({"MARCA": marca, "AÑO": años})

# %%
carrocerias.head(25)




# %%
