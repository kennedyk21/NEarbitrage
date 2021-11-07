from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# above imports selinium the library used here
#Below is a path and a line the combination 
# of the two will tell selenium to run chrome
PATH = r"C:\Users\kenne\chromedriver.exe"

driver = webdriver.Chrome(PATH)
#driver.close() closes the tab
#driver.quit() closes the window
#driver.title() takes the title of the webpage
"""
driver.get("https://www.dictionary.com/")
# this variable finds the search bar using the id
#this creates an object location
search = driver.find_element_by_id("searchbar_input")
#this code below will clear the search bar
search.clear()
#this uses keys to type hello in the search bar
search.send_keys("hello")
#this just hits enter
#driver.page_source <-- gives you all of the html stuff
search.send_keys(Keys.RETURN)

main = driver.find_element_by_class_name("default-content")
#show code inside given div
print(main.text)
#code below makes the code pause while looking for an element
#when the element is found the stuff is saved to text
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "default-content"))
    )
    spans = main.find_element_by_tag_name("span")
    for span in spans:
        print(span)

    print(main.text)
except:
    driver.quit()


#this section below is a link button
driver.get("http://www.freshprinceofstatenisland.org/")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Exciting News: Coronavirus"))
    )
    element.click()
    print("hello")
except:
    print("else")
    driver.quit()
"""
#this text below navigates throught the page with a normal button (a herf)
driver.get("https://www.djangoproject.com/")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cta"))
    )
    element.click()
    #this code will send you back a page
    driver.back()
    #if you go back this will send you forward
    driver.forward()
    print("hello")
except:
    print("else")
    driver.quit()

