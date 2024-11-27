
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

service = Service(excutable_path= "C:\\Users\\Lenovo\\Downloads\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe")
driver= webdriver.Chrome(service=service)
driver.get("https://letcode.in/frame")
driver.maximize_window()
# switching to the first frame
driver.switch_to.frame("firstFr")
# entering th first name
first_name= driver.find_element(By.NAME,"fname")
first_name.send_keys("pooja")
# entering the lat name
last_name= driver.find_element(By.NAME,"lname")
last_name.send_keys("padarthi")
time.sleep(3)
# switching to the inner frame
driver.switch_to.frame(0)
time.sleep(3)
# entering the email
mail= driver.find_element(By.XPATH,"//*[@name='email']")
mail.send_keys("abc@gmail.com")
time.sleep(3)
driver.quit()


