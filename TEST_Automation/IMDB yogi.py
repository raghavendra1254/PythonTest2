import time
from selenium.webdriver.support.ui import Select
from selenium import selenium,webdriver

driver=webdriver.Chrome("C:\\Users\\rannasagaram\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("https://www.imdb.com/")
driver.maximize_window()

driver.get("http://www.imdb.com")
driver.maximize_window()
time.sleep(5)
driver.find_element_by_xpath("//div[contains(text(),'Menu')]").click()
time.sleep(4)
driver.find_element_by_link_text("Top Rated Movies").click()

Select = Select(driver.find_element_by_name("sort"))
time.sleep(2)
Select.select_by_index(2)
time.sleep(5)
ele = driver.find_element_by_xpath("//a[contains(text(),'The Kid')]")
driver.execute_script("arguments[0].scrollIntoView();",ele)
time.sleep(5)
ele.click()

d = driver.find_element_by_link_text("6 February 1921 (USA)")
print(d.text)