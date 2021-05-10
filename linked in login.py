from sys import executable

from selenium import selenium,webdriver

driver=webdriver.Chrome("C:\\Users\\rannasagaram\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("https://in.linkedin.com/")
driver.maximize_window()
driver.find_element_by_name('session_key').send_keys('raghuannasagaram@gmail.com')
driver.find_element_by_id('session_password').send_keys('Indrani@123')
driver.find_element_by_id('session_password').submit()
driver.implicitly_wait(60)
driver.title()




