from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
driver.get("https://orteil.dashnet.org/cookieclicker/")
elem = driver.find_element_by_id("bigCookie")
sleep(2)

def product(product_name):
    elem = driver.find_element_by_id(product_name)
    elem.click()

def upgrade(upgrade_name):
    elem = driver.find_element_by_id(upgrade_name)
    elem.click()

def upgrade_cost(cost_name):
    elem = driver.find_element_by_id(cost_name).text
    return elem

def cookie_amount(amount):
    elem = driver.find_element_by_id(amount).text
    return elem

def owning_print(amount):
   elem = driver.find_element_by_id(amount).text
   return elem

upgradestacker = 100

count   = 0
cursor  = 15
grandma = 100
farm    = 1100

for i in range(0, 1000000):
    elem.click()
    #print("Cookie clicks: ", i)
    c = cookie_amount("cookies")
    l = c.split(' ')
    count = int(l[0])
    #print(l[0])

    if count > cursor:
        print("Cursor cost: ", cursor)
        cursor = int(upgrade_cost("productPrice0"))
        count = 0
        product("product0")
        print("Cursor owned: ", owning_print("productOwned0"))
        print("")

    if count > upgradestacker:
        #print("Cursor upgrade cost: ", cursor)
        upgradestacker = upgradestacker + 500
        count = 0
        upgrade("upgrade0")
        print("")

    if count > grandma:
        print("Grandma cost: ", grandma)
        grandma = int(upgrade_cost("productPrice1"))
        count = 0
        product("product1")
        print("Grandma owned: ", owning_print("productOwned1"))
        print("")
        
    if count > farm:
        #print("Farm cost: ", farm)
        farm = int(upgrade_cost("productPrice2"))
        count = 0
        product("product2")
        print("Farm owned: ", owning_print("productOwned2"))
        print("")



print("Hello")
driver.close()