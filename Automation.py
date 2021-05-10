from sys import executable

from selenium import selenium,webdriver

driver=webdriver.Chrome("C:\\Users\\rannasagaram\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("http://www.gmail.com")
driver.maximize_window()
driver.find_element_by_id('identifierId').send_keys('raghuannasagaram@gmail.com')
driver.find_element_by_xpath("//div[@id='identifierNext']/div/button").click()
driver.find_element_by_name('password').send_keys('Raghurao8#')
driver.find_element_by_xpath("//div[@id='passwordNext']/div/button").click()
