from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\Sakhamuri\\Desktop\\chromedriver\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_xpath("//*[@id='logInPanelHeading']//following::input[@id='txtUsername']").send_keys("Admin")
driver.find_element_by_xpath("//*[@id='logInPanelHeading']//following::input[2]").send_keys("admin123")
driver.find_element_by_xpath("//*[contains(@type,'sub')]").click()
driver.find_element_by_xpath("//*[contains(text(),'My Info')]").click()
driver.find_element_by_xpath("//*[@type='button' and @id='btnSave']").click()
driver.find_element_by_xpath("//*[@id='personal_cmbNation']").click()
driver.find_element_by_xpath("//option[text(),'Icelander']//following-sibling::option[1]]").click()