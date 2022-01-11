from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\Sakhamuri\\Desktop\\chromedriver\\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.find_element_by_xpath("//div[@class='_6lux']//child::input[@name='email']").send_keys("9493425744")
driver.save_screenshot("C:\\User\\Sakhamuri\\Desktop\\folder\\Ex-image.JPEG")

