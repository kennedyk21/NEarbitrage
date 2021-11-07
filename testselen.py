from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# above imports selinium the library used here
#Below is a path and a line the combination 
# of the two will tell selenium to run chrome
PATH = r'C:\Users\kenne\chromedriver.exe'
print(PATH)
driver = webdriver.Chrome(PATH)
driver.get("https://www.dictionary.com/")