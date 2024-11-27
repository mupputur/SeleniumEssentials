
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service= Service(executable_path=".\\chromedriver.exe")
driver= webdriver.Chrome(service=service)
driver.get("https://letcode.in/edit")
# enter the full name
driver.find_element(By.ID,"fullName").send_keys("PoojaPadarthi")
# appending the text and press the tab
tb = driver.find_element(By.ID,"join")
tb.send_keys(" one")
tb.send_keys(Keys.TAB)
# reading the text
text= driver.find_element(By.ID,'getMe')
text_box= text.get_attribute("value")
print(text_box)
# clear the text
ele= driver.find_element(By.ID,"clearMe").clear()
# checking the edit field is disabled or not
ef= driver.find_element(By.ID,"noEdit").is_enabled()
print(ef)
# confirming that text field is for only reading purposse
tr= driver.find_element(By.ID,"dontwrite").get_attribute("readonly")
print(tr)
time.sleep(3)
driver.quit()
