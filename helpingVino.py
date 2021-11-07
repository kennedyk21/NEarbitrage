
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
PATH = r"C:\Users\kenne\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.nj.com/highschoolsports/2021/03/who-was-the-top-senior-hs-hockey-player-for-the-2021-season-vote-now.html")
actions = ActionChains(driver)
#does the same thing as earlier just waits a time instead
driver.implicitly_wait(5)
#actions.click() an action
#actions.perform() performs the actions
#cookie_count = driver.find_element_by_id("cookies")
vino = driver.find_element_by_id("PDI_answer49714813")
vote = driver.find_element_by_id("pd-vote-button10767994")
#items = [driver.find_element_by_id("productOwned"+str(i) for i in ranges(1,-1,-1))] 
actions.click(vino)
actions.click(vote)
for i in range(10):
    driver.implicitly_wait(5)
    actions.perform()
    print("success")
    driver.refresh()
