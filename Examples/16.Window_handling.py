from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

service= Service(executable_path="C:\\Users\\Lenovo\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver= webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://letcode.in/windows")

# clicking on home button
driver.find_element(By.ID,"home").click()
time.sleep(3)
window_handels= driver.window_handles
print(window_handels)
child=driver.window_handles[1]
print(child)
print(driver.current_url)
# switching to child window
driver.switch_to.window(child)
# printing the title of the page
get_title=driver.title
print(get_title)
# switching to parent window
parent=driver.window_handles[0]
driver.switch_to.window(parent)
# closing the parent window
driver.close()
time.sleep(3)
print(driver.window_handles)
driver.switch_to.window(child)
driver.find_element(By.XPATH,"//*[text()='Tabs']").click()
# clicking on multiple windows tab
driver.find_element(By.ID,"multi").click()
win=driver.window_handles
print(win)
# closing the child window
driver.switch_to.window(child)
driver.close()
time.sleep(3)
driver.switch_to.window(win[1])
time.sleep(3)
# printing all windows titles
get_title3=driver.title
print(get_title3)
driver.switch_to.window(win[2])
time.sleep(3)
get_title4=driver.title
print(get_title4)
time.sleep(3)
# closing all the windows
driver.quit()


