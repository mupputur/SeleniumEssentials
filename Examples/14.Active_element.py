from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service= Service(executable_path=".\\chromedriver.exe")
driver= webdriver.Chrome(service=service)
driver.get("https://www.facebook.com/")
time.sleep(3)
A_E= driver.switch_to.active_element
A_E.send_keys("abc@gmail.com",Keys.TAB,
              "P@d123",Keys.ENTER)
driver.quit()