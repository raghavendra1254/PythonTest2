from sys import executable
import time
from selenium import selenium,webdriver

driver=webdriver.Chrome("C:\\Users\\rannasagaram\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("https://www.imdb.com/")
driver.maximize_window()
driver.find_element_by_xpath("//div[contains(text(),'Sign In')]").click()
driver.find_element_by_xpath("//a[contains(text(),'Create a New Account')]").click()
time.sleep(5)
driver.find_element_by_xpath("//input[@id='ap_customer_name']").send_keys('Raghavendra')
driver.find_element_by_xpath("//input[@id='ap_email']").send_keys('raghavendraraoannasagaram@gmail.com')
driver.find_element_by_xpath("//input[@id='ap_password']").send_keys('Raghurao8#')
driver.find_element_by_xpath("//input[@id='ap_password_check']").send_keys('Raghurao8#')
driver.find_element_by_xpath("//input[@id='continue']").click()
driver.find_element_by_xpath("//label[@id='imdbHeader-navDrawerOpen--desktop']").click()
driver.find_element_by_xpath("//span[text()='Movies']").click()
driver.find_element_by_xpath("//span[text()='Top Rated Movies']").click()
time.sleep(5)
sel=select(driver.find_element_by_id('lister-sort-by-options'))
sel.select_by_index(2)





