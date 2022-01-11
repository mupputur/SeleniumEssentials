from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\Sakhamuri\\Desktop\\chromedriver\\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.find_element_by_xpath("//*[@class='inputtext _55r1 _6luy _9npi']//preceding::input[@class='inputtext _55r1 _6luy']").send_keys("snlns123@gmail.com")