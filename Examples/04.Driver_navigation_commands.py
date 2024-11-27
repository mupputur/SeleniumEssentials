
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

service= Service(executable_path=".\\chromedriver.exe")
driver= webdriver.Chrome(service=service)
driver.get("https://letcode.in/buttons")
B_P=driver.current_url
print("button_page_url: ",B_P)
# Goto Home and come back here using driver command
driver.find_element(By.XPATH,"//*[text()='Goto Home']").click()
H_P=driver.current_url
print("home_page_url: ",H_P)
time.sleep(3)
driver.back()
B_P2=driver.current_url
print("return_to_button_page: ",B_P2)
driver.refresh()
driver.get("https://letcode.in/signin")
driver.quit()
