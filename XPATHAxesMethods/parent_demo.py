from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\Sakhamuri\\Desktop\\chromedriver\\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.find_element_by_xpath("//*[@name='email']//parent::div//following-sibling::div//input[@id='pass']").send_keys("123")
