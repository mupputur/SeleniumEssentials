from selenium import webdriver
import time
driver=webdriver.Chrome("C:\\Users\\Sakhamuri\\Desktop\\chromedriver\\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.find_element_by_xpath("//*[@class='_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy']").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@class='_52lr fsm fwn fcg']//following::input[@class='inputtext _58mg _5dba _2ph-']").send_keys("Naga")
driver.find_element_by_xpath("//input[@name='lastname']").send_keys("Nethi")
driver.find_element_by_xpath("//*[@name='reg_passwd__']//preceding::input[@name='reg_email__']").send_keys("snlns123@gmail.com")
time.sleep(5)
driver.find_element_by_xpath("//input[@name='reg_email_confirmation__']").send_keys("snlns123@gmail.com")
driver.find_element_by_xpath("//*[@name='reg_passwd__']").send_keys("Naga@123")
driver.find_element_by_xpath("//*[@name='birthday_day']").click()
driver.find_element_by_xpath("//option[text()='5']//following-sibling::option[1]").click()
driver.find_element_by_xpath("//*[@name='birthday_month']").click()
driver.find_element_by_xpath("//option[text()='May']//preceding-sibling::option[1]").click()
driver.find_element_by_xpath("//*[@name='birthday_year']").click()
driver.find_element_by_xpath("//option[text()='1997']//following-sibling::option[1]").click()
driver.find_element_by_xpath("//*[text()='Female']").click()