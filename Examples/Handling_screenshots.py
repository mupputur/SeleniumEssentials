import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PIL import Image

service= Service(executable_path=".\\chromedriver.exe")
driver= webdriver.Chrome(service=service)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.find_element(By.PARTIAL_LINK_TEXT,"New Releases").click()
# Loading the image
driver.save_screenshot("amazon_newreleases.png")
# Showing the imagess
image = Image.open("amazon_newreleases.png")
image.show()
time.sleep(4)
driver.close()

