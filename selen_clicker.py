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

def check_for_invalid(string):
    new_string = string.replace(",", "")
    return new_string

upgradestacker = 100

count   = 0
cursor  = 15
grandma = 100
farm    = 1100
mine    = 12000
factory = 130000

for i in range(0, 100000000):
    elem.click()
    #print("Cookie clicks: ", i)
    c = cookie_amount("cookies")
    l = c.split(' ')
    new_cookie = check_for_invalid(l[0])
    count = int(new_cookie)
    #print(count)

    if count > cursor:
        print("Cursor cost: ", cursor)

        cursor_price = check_for_invalid(upgrade_cost("productPrice0"))
        cursor = int(cursor_price)
        count = 0
        
        product("product0")
        
        print("Cursor owned: ", owning_print("productOwned0"))
        print("")

    if count > upgradestacker:
        print("Cursor upgrade cost: ", cursor)
        upgradestacker = upgradestacker + 500
        count = 0
        upgrade("upgrade0")
        print("")

    if count > grandma:
        print("Grandma cost: ", grandma)

        grandma_price = check_for_invalid(upgrade_cost("productPrice1"))
        grandma = int(grandma_price)
        count = 0

        product("product1")

        print("Grandma owned: ", owning_print("productOwned1"))
        print("")
        
    if count > farm:
        print("Farm cost: ", farm)

        farm_price = check_for_invalid(upgrade_cost("productPrice2"))
        farm = int(farm_price)
        count = 0

        product("product2")

        print("Farm owned: ", owning_print("productOwned2"))
        print("")

    if count > mine:
        print("Mine cost: ", mine)

        mine_price = check_for_invalid(upgrade_cost("productPrice3"))
        mine = int(mine_price)
        count = 0

        product("product3")

        print("mine owned: ", owning_print("productOwned3"))
        print("")

    if count > factory:
        print("Factory cost: ", factory)

        factory_price = check_for_invalid(upgrade_cost("productPrice4"))
        factory = int(factory_price)
        count = 0

        product("product4")

        print("factory owned: ", owning_print("productOwned4"))
        print("")


print("Hello")
driver.close()