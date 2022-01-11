from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\Sakhamuri\\Desktop\\chromedriver\\chromedriver.exe")
driver.get("https://www.myntra.com/")
driver.find_element_by_xpath("//a[text()='Women']").click()