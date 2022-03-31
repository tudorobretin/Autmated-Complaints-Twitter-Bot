from selenium import webdriver
from twitter import Twitter
from ookla import Ookla

CONTRACT_SPEED = 1000
driver = webdriver.Chrome(executable_path="C:\\Users\\MAXMEDIA\\Desktop\\Python downloads\\Chromedriver\\chromedriver.exe")
driver.set_window_size(1300, 900)

ookla = Ookla(driver=driver)
twitter = Twitter(driver=driver)

down_speed = ookla.test_speed()

if down_speed < CONTRACT_SPEED:

    twitter.login()
    twitter.send_tweet_complaint(down_speed=down_speed, contract_speed=CONTRACT_SPEED)

#download-speed