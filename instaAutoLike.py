from selenium import webdriver

# for the edge browser
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with

import time
# for beautifulSoup it can only extract the static pages and not dynamic pages...
from bs4 import BeautifulSoup

# pandas for dataframes
import pandas as pd

# This commannd is install the drivers for the required browser.
service = Service(EdgeChromiumDriverManager().install())

# this command initialises the driver
# this also starts the session (1)
driver = webdriver.Edge(service=service)

# take action on the browser (2)
# this command opens this url onto the browser.
driver.get("https://www.instagram.com/")

# Request browser information (3)
# Various browser info like title, cookies, alerts, browser size/position etc can be accessed.
title = driver.title
print(title)

# Waiting Strategy (4)
# This is imp bcoz the browser is not always synced with the test script.
driver.implicitly_wait(10)

# # Finding the element (5)
usernameInput=driver.find_elements(By.NAME,"username")[0].send_keys("")
passwordInput=driver.find_elements(By.NAME,"password")[0]
passwordInput.send_keys("")
print(passwordInput)
# login=driver.find_elements(By.,"username")[0].send_keys("")
loginButton = driver.find_element(locate_with(By.TAG_NAME, "button").near(passwordInput))
print(loginButton)
loginButtonSourceCode=loginButton.get_attribute('innerHTML')
print(loginButtonSourceCode)

if "Log In" not in loginButtonSourceCode:
    print("Log In button not available.")
    time.sleep(2)
    driver.quit()

loginButton.click()
time.sleep(10)

saveInfoButtons=driver.find_elements(By.TAG_NAME,"button")
print(len(saveInfoButtons))
for btn in saveInfoButtons:
    btnSourceCode=btn.get_attribute('innerHTML')
    if "Not Now" in btnSourceCode:
        print("This is a ""Not Now"" button.")
        btn.click()
        break

time.sleep(5)
print("TILL HERE")
notificationButtons=driver.find_elements(By.TAG_NAME,"button")
for btn in notificationButtons:
    btnSourceCode=btn.get_attribute('innerHTML')
    if "Not Now" in btnSourceCode:
        print("This is a ""Not Now"" Notification button.")
        btn.click()

print("Till here")
# images=driver.find_elements(By.)
time.sleep(50)



# Scrolling by some amount so the comments starts loading (6)
# body = driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
# video = 1

# Finding the element (5)


# this ends the session (8)
print("quitting...")
driver.quit()
