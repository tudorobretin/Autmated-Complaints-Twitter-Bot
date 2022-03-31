import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from twitter import Twitter


URL = "https://www.speedtest.net/"
driver = webdriver.Chrome(executable_path="C:\\Users\\MAXMEDIA\\Desktop\\Python downloads\\Chromedriver\\chromedriver.exe")
driver.set_window_size(1300, 900)
# driver.get(URL)
# time.sleep(1)
#
# driver.find_element(By.ID, '_evidon-banner-acceptbutton').click()
# time.sleep(1)
#
# driver.execute_script("window.scrollTo(0, 400)")
# time.sleep(1)
#
# driver.find_element(By.CSS_SELECTOR, ".start-button a").click()
#
# time.sleep(40)
#
# down_speed = float(driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
# print(down_speed)
down_speed = 420

twitter = Twitter(driver=driver)

if down_speed < 1000:

    twitter.login()
    twitter.send_tweet_complaint(down_speed=down_speed)

#download-speed