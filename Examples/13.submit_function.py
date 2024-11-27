from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service= Service(executable_path=".\\chromedriver.exe")
driver= webdriver.Chrome(service=service)
driver.get("https://letcode.in/signin")
time.sleep(3)
driver.find_element(By.NAME,"email").send_keys("koushik350@gmail.com")
driver.find_element(By.NAME,"password").send_keys("Pass123$")
time.sleep(3)
driver.find_element(By.XPATH,"//*[.='LOGIN']").submit()
time.sleep(3)
driver.get("https://letcode.in/buttons")
driver.find_element(By.ID,"home").submit()
time.sleep(3)
driver.quit
# submit only can use in forms only