from sys import executable

from selenium import selenium, webdriver

driver=webdriver.Chrome("C:\\Users\\rannasagaram\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("http://www.facebook.com")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element_by_id("email").send_keys("raghuannasagaram@gmail.com")
driver.find_element_by_id("pass").send_keys("Raghurao8#")
driver.find_element_by_name("login").click()
driver.get_screenshot_as_file("facebook.png")
driver.quit()


