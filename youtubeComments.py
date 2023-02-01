from selenium import webdriver

# for the edge browser
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
# driver.get("https://www.youtube.com/watch?v=4MhpEGqh0b4")

# # Request browser information (3)
# # Various browser info like title, cookies, alerts, browser size/position etc can be accessed.
# title = driver.title
# print(title)

# # Waiting Strategy (4)
# # This is imp bcoz the browser is not always synced with the test script.
# # driver.implicitly_wait(10)

# # # Finding the element (5)
# # comment_elements = driver.find_elements(
# #     by=By.TAG_NAME, value='ytd-comment-thread-renderer')
# # print(len(comment_elements))
# # for comment in comment_elements:
# #     print(comment)
# #     print(comment.text)
# #     pass

# # Scrolling by some amount so the comments starts loading (6)
# body = driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
# video = 1

# # Finding the element (5)
# comment_elements = driver.find_elements(
#     by=By.TAG_NAME, value='ytd-comment-thread-renderer')
# print(len(comment_elements))
# for comment in comment_elements:
#     print(comment)
#     print(comment.text)
#     pass


# # this ends the session (8)
# print("quitting...")
# # driver.quit()

usernames = []
comments = []
likes = []
account_links=[]


data=[]
wait = WebDriverWait(driver,15)


# mobile phones
driver.get("https://www.youtube.com/watch?v=AOAlNK2rmQE")
for item in range(5):
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
    time.sleep(15)

for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content-text"))):
    data.append(comment.text)
    print(data)


# content = driver.page_source
# soup = BeautifulSoup(content)
# for a in soup.findAll('div', href=True, attrs={'id':'body'}):

#     print(a)
#     name = a.find('a', attrs={'id': 'author-text'})
#     comment = a.find('yt-formatted-string', attrs={'id': 'content-text'})
#     like = a.find('span', attrs={'id': 'vote-count-middle'})
#     print(name.text, comment.text,likes.text)
#     if(name and comment and likes):
#         usernames.append(name.text)
#         comments.append(comment.text)
#         likes.append(like.text)
#         print(name.text, comment.text, like.text)

# print(usernames,comments,likes)
# print(len(usernames),len(comments),len(likes))
# df = pd.DataFrame(
#     {'Username': usernames, 'Comment': comments, 'Likes': likes})
# df.to_csv('youtube.csv', index=False, encoding='utf-8')
df = pd.DataFrame(
    {'data': data})
df.to_csv('youtubeComments.csv', index=False, encoding='utf-8')
