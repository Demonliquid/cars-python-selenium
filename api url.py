# %%
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd

# %% DRIVER
driver = webdriver.Edge(executable_path=r'E:\Codigo\Selenium\msedgedriver.exe')


# %% LINK
driver.get(r'https://ebroker.icwi.com:8086/quote/getModels/1')


# %% A RELLENAR
Modelos = pd.DataFrame(columns=["ID", "MODELOS"])


# %% LISTA DE MODELOS
modelos = driver.find_element_by_xpath(r'/html/body/model/model_detail[2]/model_name')


# %%
modelos.text

# %%
Modelos = Modelos.append({"ID":1, "MODELOS": f"{modelos.text}"}, ignore_index=True)



# %% LOOP
Modelos = pd.DataFrame(columns=["ID", "MODELOS"])

for marcaid in range(1,702):
    driver.get(f'https://ebroker.icwi.com:8086/quote/getModels/{marcaid}')
    
    for x in range(1, 100):
        try:
            modelos = driver.find_element_by_xpath(f'/html/body/model/model_detail[{x}]/model_name')
            Modelos = Modelos.append({"ID":f"{marcaid}", "MODELOS": f"{modelos.text}"}, ignore_index=True)
        except:
            pass




# %%
Modelos
# %%
Modelos.to_csv(r"F:\Trabajo\Promotive\Saint Kitts\st.csv", index=False)
# %%
Marcas = pd.read_excel(r"F:\Trabajo\Promotive\Saint Kitts\index.xlsx", engine="openpyxl")
# %%
Completo = pd.merge(Modelos, Marcas, left_on="ID", right_on="ID", how="left")


# %%
Marcas["ID"] = Marcas["ID"].astype(int)
Modelos["ID"] = Modelos["ID"].astype(int)

# %%
Completo.to_excel(r"F:\Trabajo\Promotive\Saint Kitts\Saint_Kitts_Insurance.xlsx")
# %%
