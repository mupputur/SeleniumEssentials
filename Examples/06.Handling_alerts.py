from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

service = Service(executable_path="C:\\Users\\Lenovo\\Downloads\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe")
driver= webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://letcode.in/alert")
# accepting the alert
driver.find_element(By.XPATH,"//*[text()='Simple Alert']").click()
alert= driver.switch_to.alert
alert.accept()
time.sleep(3)
# Dismiss the Alert & print the alert text
driver.find_element(By.XPATH,"//*[text()='Confirm Alert']").click()
dis_alert= driver.switch_to.alert
print(dis_alert.text)
time.sleep(3)
dis_alert.dismiss()
time.sleep(3)
# Type your name & accept in prompt alert
driver.find_element(By.XPATH,"//*[text()='Prompt Alert']").click()
prompt= driver.switch_to.alert
prompt.send_keys("pooja")
time.sleep(3)
prompt.accept()
# sweet alert
driver.find_element(By.XPATH,"//*[text()='Modern Alert']").click()
driver.find_element(By.ID,"modern").click()
time.sleep(1)
driver.quit()
