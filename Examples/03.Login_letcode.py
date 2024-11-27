from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service= Service(executable_path=".\\chromedriver.exe")
driver= webdriver.Chrome(service=service)
driver.get("https://letcode.in/")
time.sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT,"Log in").click()
time.sleep(3)
driver.find_element(By.NAME,"email").send_keys("koushik350@gmail.com")
driver.find_element(By.NAME,"password").send_keys("Pass123$")
time.sleep(3)
driver.find_element(By.XPATH,"//*[.='LOGIN']").click()
#Closing the webdriver
driver.quit()