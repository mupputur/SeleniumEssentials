from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service= Service(executable_path= ".\\chromedriver.exe")
driver= webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://letcode.in/")
login_btn= driver.find_element(By.PARTIAL_LINK_TEXT,"Log in")
displayed= login_btn.is_displayed()
print("login_btn:",displayed)
#is_enabled
driver.get("https://letcode.in/edit")
edit_btn= driver.find_element(By.ID,"noEdit")
enabled= edit_btn.is_enabled()
print("edit_btn: ",enabled)
driver.get("https://letcode.in/buttons")
disable_btn= driver.find_element(By.ID,"isDisabled")
disabled= print("disable_btn: ",disable_btn)
# is selected
driver.get("https://letcode.in/radio")
time.sleep(3)
selected_btn= driver.find_element(By.XPATH,"//*[.=' Remember me ']")
time.sleep(3)
remember= selected_btn.is_selected()
print("selected: ", remember)
driver.quit()