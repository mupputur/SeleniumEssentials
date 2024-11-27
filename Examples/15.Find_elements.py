from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service= Service(executable_path= ".\\chromedriver.exe")
driver= webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://letcode.in/edit")
labels= driver.find_elements(By.TAG_NAME,"label")
last_element= labels[-1]
print("last_element= "+last_element.text)
size= len(labels)
if size==6:
    print("test case passed")
for label in labels:
    print(label.text)
driver.quit()