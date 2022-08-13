from turtle import title
import praw
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import boto3

def connect_to_reddit():
    reddit = praw.Reddit(
        client_id="V0fNmBNycUyDAq2-WTSybQ",
        client_secret="GdwSr-4_TC_Q0QKZA-m0-tOoC9UA-Q",
        user_agent="my reddit bot",
    )
    return reddit


def select_a_subreddit(reddit):
    post_list = []
    print("\n")
    subreddit = reddit.subreddit("askreddit")
    print("\n")
    i = 0
    for post in subreddit.hot(limit=10):
        print("----------------------")
        print(i)
        print(post.title)
        i += 1
        post_list.append(post)

    picked_post = reddit.submission(
        id=post_list[int(input("Which post would you like to use? \n"))])

    return picked_post


def get_screenshots(picked_post, num_of_comments):
    files = []
    post_id = picked_post.id
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://reddit.com/r/AskReddit/comments/" + post_id)
    time.sleep(1)
    try:
        print(driver.find_element(By.CLASS_NAME, "_1jefpljVGT-eHObg40F8Dm").is_displayed())
        if(driver.find_element(By.CLASS_NAME, "_1jefpljVGT-eHObg40F8Dm").is_displayed()):
            nsfw = driver.find_element(By.CLASS_NAME, "_3-bzOoWOXVn2xJ3cljz9oC")
            nsfw_yes_button = nsfw.find_element(By.CLASS_NAME, "i2sTp1duDdXdwoKi1l8ED")
            nsfw_yes_button.screenshot("button.png")
            nsfw_yes_button.click()
            nsfw_post_button = nsfw = driver.find_element(By.CLASS_NAME, "gCpM4Pkvf_Xth42z4uIrQ")
            nsfw_post_button.click()
        time.sleep(3)
    except NoSuchElementException:

        time.sleep(1)
    title = driver.find_element(By.ID, "t3_"+picked_post.id)
    title.screenshot("redditscreenshots/title.png")
    for x in range(num_of_comments):
        comment = picked_post.comments[x]
        test = driver.find_element(By.ID, "t1_"+comment.id)
        test.screenshot("redditscreenshots/comment" + str(x) + ".png")
        files.append("redditscreenshots/comment" + str(x) + ".png")
    driver.quit()
    return files
