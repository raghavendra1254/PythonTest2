from sys import executable

from selenium import selenium, webdriver

driver=webdriver.Chrome("C:\\Users\\rannasagaram\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(20)
