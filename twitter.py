import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


class Twitter:
    def __init__(self, driver):
        self.driver = driver
        self.PASSWORD = os.environ['password']

    def login(self):

        self.driver.get("https://twitter.com/home")
        time.sleep(3)

        email_form = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
        email_form.send_keys("tudorobre@gmail.com")
        time.sleep(1)

        press_next = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div')
        press_next.click()
        time.sleep(1)

        try:
            password = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(self.PASSWORD)
            self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div').click()

        except:
            username = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            username.send_keys("tudorobre")
            time.sleep(1)

            next_button = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')
            next_button.click()
            time.sleep(1)

            password = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(self.PASSWORD)
            time.sleep(1)

            login_button = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div')
            login_button.click()

    def send_tweet_complaint(self, down_speed):

        time.sleep(1)
        accept_cookies = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/div[1]/div')
        accept_cookies.click()

        tweet_input_field = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div')
        tweet_input_field.send_keys(f"This is an automated tweet.\n"
                        f"@DigiRomania, current internet speed: {down_speed}Mbs\n"
                        f"What I'm paying for: 1000Mbs")
        time.sleep(1)

        tweet_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        #tweet_button.click()
