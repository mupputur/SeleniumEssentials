"""
syntax = //*[contains(@attribute,'value')]
"""
from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\Sakhamuri\\Desktop\\chromedriver\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_xpath("//*[contains(@type,'sub')]").click()
driver.find_element_by_xpath("//*[contains(@id,'btn')]").click()
driver.find_element_by_xpath("//*[contains(@name,'name')]").send_keys("123")
driver.find_element_by_id("//*[contains(@name,'Pass')]").send_keys("123")
driver.find_element_by_xpath("//*[starts-with(@id,'btnSa')]").click()