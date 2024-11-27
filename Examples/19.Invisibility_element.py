from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
toast= driver.find_element(By.XPATH,"//div[@role='alertdialog']")
alert_text= WebDriverWait.until(EC.visibility_of(toast))
print(alert_text.text)
WebDriverWait.until(EC.invisibility_of_element(toast))
driver.find_element(By.PARTIAL_LINK_TEXT,"Sign out").click()
driver.quit
