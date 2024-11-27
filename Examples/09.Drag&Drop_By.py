from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

service= Service(executable_path=".\\chromedriver.exe")
driver= webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://jqueryui.com/draggable/")
driver.switch_to.frame(0)
source= driver.find_element(By.ID,"draggable")
location= source.location
x= location.get('x')
print('x= ',x)
y= location.get('y')
print('y= ',y)
act= ActionChains(driver)
act.drag_and_drop_by_offset(source,x+40,y+30).perform()
driver.quit()
