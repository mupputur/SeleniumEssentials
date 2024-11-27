from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

service= Service(executable_path=".\\chromedriver.exe")
driver= webdriver.Chrome(service=service)
driver.get("https://letcode.in/buttons")
time.sleep(3)
# printing the location of x&y values
location= driver.find_element(By.XPATH,"//*[@class='button is-link is-outlined']").location
print(location)
x= location['x']
y= location['y']
print("x= ",x ,"y= ",y)
time.sleep(3)
# color of the button
color= driver.find_element(By.XPATH,"//*[text()='What is my color?']").value_of_css_property("border")
print(color)
time.sleep(3)
# button size
h_w= driver.find_element(By.XPATH,"//*[text()='How tall & fat I am?']").size
print(h_w)
time.sleep(3)
# checking the button is enabled or not
button= driver.find_element(By.ID,"isDisabled").is_enabled()
print(button)
time.sleep(3)
driver.quit()