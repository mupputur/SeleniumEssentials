from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(excutable_path="..\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://letcode.in/table")
table= driver.find_element(By.ID,"simpletable")
headers= table.find_elements(By.TAG_NAME,"th")
for header in headers:
    print(header.text)

all_rows= driver.find_elements(By.XPATH,"//*[@id='simpletable']/tbody/tr")
length= len(all_rows)
print("row_size: ",length)
if (length==3):
    print("pass")
else:
    print("fail")
"""
for row in all_rows:
    col= row.find_elements(By.TAG_NAME,"td")
    first_col= col[0]
    print(first_col.text)
"""
for i in range(length) :
    rows= all_rows[i].find_elements(By.TAG_NAME,"td")
    last_name= rows[1]
    print(last_name.text)
    if last_name == "Raj":
        rows[3].find_element(By.TAG_NAME,"input").click()
        time.sleep(5)
        break;

driver.quit()  

