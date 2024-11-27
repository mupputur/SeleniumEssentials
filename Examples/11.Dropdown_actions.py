from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service= Service(executable_path= ".\\chromedriver.exe")
driver= webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://letcode.in/dropdowns")

# selecting the apple from select field
fruits= Select(driver.find_element(By.ID,"fruits"))
fruits.select_by_visible_text("Apple")
# selecting the superhero's from that field
s= Select(driver.find_element(By.ID,'superheros'))
s.select_by_visible_text("Batman")
s= Select(driver.find_element(By.ID,'superheros'))
s.select_by_visible_text("Iron Man")
time.sleep(5)
# selecting the last language from languages field and print all languages
languages= Select(driver.find_element(By.ID,"lang"))
languages.select_by_value("sharp")
all_languages= languages.options
for a in all_languages:
    print("languages are: ", a.text)
# selecting the india from country field and print the country field
country=Select(driver.find_element(By.ID,"country"))
country.select_by_value("India")
selected_country= country.first_selected_option.text
print("selected country is: ",selected_country)

driver.quit()