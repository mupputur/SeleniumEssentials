from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\Sakhamuri\\Desktop\\chromedriver\\chromedriver.exe")
driver.get("https://www.facebook.com/")
"""
ancestor
"""
driver.find_element_by_xpath("//div[@id='passContainer']/ancestor::div//input[@name='email']").send_keys("123")
"""
descendant
"""
driver.find_element_by_xpath("//div[@class='_6lux']//descendant::input[@id='pass']").send_keys("123")