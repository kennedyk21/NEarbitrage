
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
PATH = r"C:\Users\kenne\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")
actions = ActionChains(driver)
#does the same thing as earlier just waits a time instead
driver.implicitly_wait(5)
#actions.click() an action
#actions.perform() performs the actions
cookie_count = driver.find_element_by_id("cookies")
cookie = driver.find_element_by_id("bigCookie")
#items = [driver.find_element_by_id("productOwned"+str(i) for i in ranges(1,-1,-1))] 
actions.click(cookie)
for i in range(5000):
    actions.perform()
    value = int(cookie_count.text.split(" ")[0])
    for i in range(1,-1,-1):
        item =  driver.find_element_by_id("productPrice"+str(i))
        num = int(item.text)

        
        if (num< value):
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
    #split turns the sentance into an array at any given value
    #the value in this one is the space
    #the 0 takes the first given in the array
    """
    count = int(cookies.text.split(" ")[0])
    
    for item in items:
        value = int(item.text)
        if value<=count:
            upgrade_actions = actionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
"""
