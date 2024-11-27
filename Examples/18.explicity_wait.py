from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Initiize the driver
service = Service(excutable_path= "..\\chromedriver_win32\\chromedriver.exe")
driver= webdriver.Chrome(service=service)
driver.implicitly_wait(3)
driver.get("https://letcode.in/waits")
# click on simple alert
alert = driver.find_element(By.XPATH,"//*[text()='Simple Alert']").click()
alert_text= WebDriverWait(driver, 10).until(EC.alert_is_present())
print(alert_text.text)
driver.switch_to.alert.accept()
time.sleep(3)
driver.quit()