import imp
from selenium import webdriver
import selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

import time

service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

driver.get("")
# driver.maximize_window()

time.sleep(20)
# # getting page source is not useful because we get an empty page like this:
# # <html><head></head><body></body></html>
# html=driver.page_source
# print(html)
print("Started...")
# print(driver.page_source)
elements=driver.find_elements(By.TAG_NAME,"I")
print(elements,"elements")
for element in elements:
    if element.get_attribute("class")=="fa fa-external-link faa-shake animated-hover":
        print("element clicked")
        element.click()
i=0
while True:
    i+=1
    # break

driver.quit()