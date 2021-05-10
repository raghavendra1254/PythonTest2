from sys import executable
import time
from selenium.webdriver.support.ui import Select
from selenium import selenium,webdriver

driver=webdriver.Chrome("C:\\Users\\rannasagaram\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("https://www.imdb.com/")
driver.maximize_window()
driver.find_element_by_xpath("//label[@id='imdbHeader-navDrawerOpen--desktop']").click()
time.sleep(5)
driver.find_element_by_link_text('Top Rated Movies').click()
Select= Select(driver.find_element_by_name("Sort"))
time.sleep(5)
Select.select_by_index(2)
time.sleep(5)
ele=driver.find_element_by_xpath("//a[contains(text(),'The Kid')]")
driver.execute_script("arguments[0].scrollIntoView();",ele)
time.sleep(5)
ele.click()

