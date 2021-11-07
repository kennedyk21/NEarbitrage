from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
PATH = r"C:\Users\kenne\chromedriver.exe"

f = open("betinfo.txt", "a")

driver = webdriver.Chrome(PATH)
driver.get("https://www.vegasinsider.com/nhl/odds/las-vegas/")
actions = ActionChains(driver)
elements = driver.find_elements_by_class_name("viCellBg1")
for element in elements:
    title = driver.find_element_by_class_name("oddsGameCell")
    f.write(title.text + "\t")
    alements = driver.find_elements_by_class_name("cellTextNorm")
    for alement in alements:
        f.write(alement.text+"\t")
    f.write("pause \n")
f.close() 

