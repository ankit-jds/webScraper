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

# This commannd is install the drivers for the required browser.
service = Service(EdgeChromiumDriverManager().install())

# this command initialises the driver
# this also starts the session (1)
driver = webdriver.Edge(service=service)

# take action on the browser (2)
# this command opens this url onto the browser.
driver.get("http://localhost:3000/sg")

# Request browser information (3)
# Various browser info like title, cookies, alerts, browser size/position etc can be accessed.
title = driver.title
print(title)

# Waiting Strategy (4)
# This is imp bcoz the browser is not always synced with the test script.
driver.implicitly_wait(10)

# # Finding the element (5)
mobileInput=driver.find_elements(By.ID,"mobile")[0].send_keys("9427189784")

sendotp = driver.find_element(By.ID, "next0")
print(sendotp)

sendotp.click()
time.sleep(10)

array=["first", "sec", "third", "fourth", "fifth", "sixth"]
otp="133456"
for i in range(len(array)):
    id=array[i]
    otp_digit=otp[i]
    otpInput=driver.find_elements(By.ID,id)[0].send_keys(otp_digit)

time.sleep(100)
# saveInfoButtons=driver.find_elements(By.TAG_NAME,"button")
# print(len(saveInfoButtons))
# for btn in saveInfoButtons:
#     btnSourceCode=btn.get_attribute('innerHTML')
#     if "Not Now" in btnSourceCode:
#         print("This is a ""Not Now"" button.")
#         btn.click()
#         break

# time.sleep(5)
# print("TILL HERE")
# notificationButtons=driver.find_elements(By.TAG_NAME,"button")
# for btn in notificationButtons:
#     btnSourceCode=btn.get_attribute('innerHTML')
#     if "Not Now" in btnSourceCode:
#         print("This is a ""Not Now"" Notification button.")
#         btn.click()

# print("Till here")
# # images=driver.find_elements(By.)
# time.sleep(50)




# this ends the session (8)
print("quitting...")
driver.quit()
