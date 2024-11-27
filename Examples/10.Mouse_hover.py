from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

service= Service(executable_path=".\\chromedriver.exe")
driver= webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.flipkart.com/")
driver.implicitly_wait(15)
#driver.find_element(By.PARTIAL_LINK_TEXT,"✕").click()
ele= driver.find_element(By.PARTIAL_LINK_TEXT,"Electronics")
time.sleep(3)
act= ActionChains(driver)
act.move_to_element(ele).perform()
time.sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT,"Apple").click()
driver.quit()
