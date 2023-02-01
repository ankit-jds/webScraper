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

loginButton = driver.find_element(By.CSS_SELECTOR, ".sqdOP.L3NKy.y3zKF")
print(loginButton)

loginButton.click()
time.sleep(3)

saveinfoNotNowButton=driver.find_element(By.CSS_SELECTOR,"._acan._acao._acas")
print(saveinfoNotNowButton)
saveinfoNotNowButton.click()

time.sleep(2)
print("TILL HERE")

notifyNotNowButton=driver.find_element(By.CSS_SELECTOR,"._a9--._a9_1")
print(notifyNotNowButton)
notifyNotNowButton.click()

time.sleep(2)
print("TILL HERE Heading to account Page.")

driver.get("")

# for i in range(100): 
#     body = driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
#     time.sleep(1)
#     print("Till here",i)
count=0
reel=driver.find_element(By.CLASS_NAME,"_abq3")
reel.click()
while True:
    time.sleep(0)
    likeButton=driver.find_element(By.CSS_SELECTOR,'._aamw').click()
    nextButton=driver.find_elements(By.CSS_SELECTOR,'._aaqg._aaqh')
    if nextButton:
       nextButton[0].click()
    else:
        closeBtn=driver.find_element(By.CSS_SELECTOR,'.x1n2onr6.x1lliihq').click()
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(4)
        reel=driver.find_elements(By.CLASS_NAME,"_abq3")[count+1]
        reel.click()
    
    count+=1

    
# print("No of Reels: ",len(reels))
# for reel in reels:
#     reel.click()
#     time.sleep(30)
#     if driver.current_url != "":
#         closeBtn=driver.find_element(By.CSS_SELECTOR,'.x1n2onr6.x1lliihq').click()
    
# this ends the session (8)
time.sleep(100)
print("quitting...")
driver.quit()
