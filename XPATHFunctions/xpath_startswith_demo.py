"""
Requirement : Here demo-in startswith() function in selenium

"""
from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\Sakhamuri\\Desktop\\chromedriver\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_xpath("//*[starts-with(@id,'txtU')]").send_keys("123")