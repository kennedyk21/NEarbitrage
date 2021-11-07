import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
divider = str(input("input the divider: "))
word = input("input the words: ")
PATH = r"C:\Users\kenne\chromedriver.exe"
driver = webdriver.Chrome(PATH)

vocabulary = word.split(divider)
print(type(vocabulary))


driver.get("https://www.merriam-webster.com/")


f = open("myfile.txt", "a")
actions = ActionChains(driver)
ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
for vocab in vocabulary:
    print(vocab+"1")
    search = WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions)\
                        .until(EC.presence_of_element_located((By.ID, "s-term")))
    print(vocab+"2")                   
    #print(main.text)
    #spans = main.find_elements_by_tag_name("span")
    #for span in spans:
        #print(span)
    #search = driver.find_element_by_id("s-term")
    search.clear()
    print("clear")
    search.send_keys(vocab)
    print("inserrt")
    search.send_keys(Keys.RETURN)
    print("return")
    #defi = driver.find_element_by_class_name("vg")
    print(vocab+"3")
    defi = WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions)\
                        .until(EC.presence_of_element_located((By.CLASS_NAME, "vg")))
    print(vocab+"4")
    f.write(vocab+": "+defi.text+"\n")

"""
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "vg"))
    )
    #print(main.text)
    #spans = main.find_elements_by_tag_name("span")
    #for span in spans:
        #print(span)

    f.write(vocab+": "+main.text+"/n")
except:
    driver.quit()
    """

f.close()