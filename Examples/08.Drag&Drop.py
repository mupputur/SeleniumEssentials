from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initiize the driver
service= Service(executable_path=".\\chromedriver.exe")
driver= webdriver.Chrome(service=service)
driver.get("https://letcode.in/dropable")
driver.maximize_window()
time.sleep(5)
# source element
source_ele=driver.find_element(By.ID,"draggable")
# target element
target_ele=driver.find_element(By.ID,"droppable")
# drag and drop the source element into target element
act=ActionChains(driver)
act.drag_and_drop(source_ele,target_ele).perform()
time.sleep(3)
driver.quit()
